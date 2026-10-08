
from pathlib import Path
import json, struct, zipfile, hashlib, collections, statistics

P20=Path("/tmp/p20"); P22=Path("/tmp/p22"); OUT=Path("/tmp/p23"); OUT.mkdir(exist_ok=True)
ROM_SHA="cd7a419797e9a45c3060771769b8f028592416e9381fc8e88b5da4c2c640dfa2"
SECONDARY_BASE=0x200; UNRES=0xFFFF
cands=json.load(open(P22/"phase22_semantic_candidates.json"))
maps_root=P20/"maps"
map_validation=json.load(open(P20/"phase20_map_validation.json"))
thresholds={"0":0.65,"7":0.60,"12":0.60}
confidence_by_role=collections.defaultdict(list); global_counts=collections.Counter(); records=[]

def primary_for_secondary(sid): return 16 if sid>=17 else 0

for d in sorted([p for p in maps_root.iterdir() if p.is_dir()]):
    man=json.load(open(d/"manifest.json")); map_id,name,w,h=man["map_id"],man["name"],man["width"],man["height"]
    raw=(d/"visual_metatile_map.bin").read_bytes()
    vals=list(struct.unpack("<"+"H"*(len(raw)//2),raw))
    if len(vals)!=w*h: raise ValueError(f"{name}: bad input size")
    mv=next((x for x in json.load(open(P22/"phase22_map_candidates.json"))["maps"] if x["map_id"]==map_id and x["name"]==name),None)
    if mv is None: raise ValueError(f"{name}: missing Phase22 map")
    sid=int(mv["secondary_tileset_id"]); primary=primary_for_secondary(sid)
    by_role=cands["candidates"][str(sid)]
    best={}
    for role in ("0","7","12"):
        eligible=[x for x in by_role.get(role,[]) if x["confidence"]>=thresholds[role]]
        best[role]=sorted(eligible,key=lambda x:(-x["confidence"],x["score"],x["metatile_id"]))[0] if eligible else None
    out=[UNRES]*len(vals); confs=[]; resolved=0; reasons=collections.Counter()
    for i,sem in enumerate(vals):
        role=str(sem)
        if role not in ("0","7","12"):
            reasons["source_unresolved" if sem==UNRES else "unsupported_semantic"]+=1; continue
        cand=best[role]
        if cand is None: reasons["below_confidence_threshold"]+=1; continue
        out[i]=SECONDARY_BASE+int(cand["metatile_id"]); resolved+=1; confs.append(float(cand["confidence"]))
        confidence_by_role[role].append(float(cand["confidence"]))
    # Neighborhood consistency: repeated regions use the local majority candidate.
    for i,sem in enumerate(vals):
        role=str(sem)
        if role not in ("0","7","12") or out[i]==UNRES: continue
        x,y=i%w,i//w; ns=[]
        for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=nx<w and 0<=ny<h:
                j=ny*w+nx
                if vals[j]==sem and out[j]!=UNRES: ns.append(out[j])
        if ns:
            majority,_=collections.Counter(ns).most_common(1)[0]
            allowed={SECONDARY_BASE+int(c["metatile_id"]) for c in by_role.get(role,[])[:8] if c["confidence"]>=thresholds[role]}
            if majority in allowed: out[i]=majority
    od=OUT/"visual_blockdata"/f"{map_id:03d}_{name}"; od.mkdir(parents=True,exist_ok=True)
    (od/"visual_metatile_map.bin").write_bytes(struct.pack("<"+"H"*len(out),*out))
    unresolved=[ [i%w,i//w,vals[i]] for i,v in enumerate(out) if v==UNRES ]
    mo={"phase":23,"map_id":map_id,"name":name,"width":w,"height":h,"format":"u16_le_row_major",
        "semantic_input_format":"phase20_semantic_ids","secondary_tileset_id":sid,"primary_tileset_id":primary,
        "secondary_metatile_base":"0x0200","unresolved_value":"0xFFFF","mapped_cells":resolved,
        "unresolved_cells":len(unresolved),"source_semantic_counts":dict(collections.Counter(map(str,vals))),
        "mean_confidence":round(statistics.mean(confs),6) if confs else 0.0,
        "min_confidence":round(min(confs),6) if confs else 0.0,"selection_thresholds":thresholds,
        "unresolved":unresolved,"status":"candidate_real_visual_blockdata","rom_integration_allowed":False}
    json.dump(mo,open(od/"manifest.json","w"),indent=2)
    global_counts["maps"]+=1; global_counts["input_cells"]+=len(vals); global_counts["resolved_cells"]+=resolved; global_counts["unresolved_cells"]+=len(unresolved)
    for k,v in collections.Counter(vals).items(): global_counts[f"input_role_{k}"]+=v
    for k,v in reasons.items(): global_counts[f"reason_{k}"]+=v
    records.append({"map_id":map_id,"name":name,"width":w,"height":h,"primary_tileset_id":primary,"secondary_tileset_id":sid,
                    "resolved_cells":resolved,"unresolved_cells":len(unresolved),"mean_confidence":mo["mean_confidence"],
                    "min_confidence":mo["min_confidence"],"rom_integration_allowed":False})

errors=[]
if len(records)!=204: errors.append(f"unique_map_count:{len(records)}")
for r in records:
    p=OUT/"visual_blockdata"/f'{r["map_id"]:03d}_{r["name"]}'/"visual_metatile_map.bin"
    b=p.read_bytes()
    if len(b)!=r["width"]*r["height"]*2: errors.append(f"size:{r['name']}")
    vs=struct.unpack("<"+"H"*(len(b)//2),b)
    bad=[v for v in vs if v!=UNRES and not(SECONDARY_BASE<=v<=SECONDARY_BASE+511)]
    if bad: errors.append(f"range:{r['name']}:{bad[0]}")

validation={"phase":23,"base_rom_sha256":ROM_SHA,"unique_maps":len(records),"map_references_in_phase20":len(map_validation),
"input_semantic_coverage":{"base_grass_0":global_counts["input_role_0"],"dirt_7":global_counts["input_role_7"],"water_12":global_counts["input_role_12"],"unresolved_ffff":global_counts["input_role_65535"]},
"output":{"resolved_cells":global_counts["resolved_cells"],"unresolved_cells":global_counts["unresolved_cells"]},
"validation_errors":errors,"rom_integration_allowed":False,
"important_limitation":"Phase20 currently contains only semantic IDs 0, 7 and 12 plus 0xFFFF. Phase23 does not invent missing road, wall, tree, fence or shoreline semantics."}
json.dump(validation,open(OUT/"phase23_validation.json","w"),indent=2)
json.dump({"phase":23,"base_rom_sha256":ROM_SHA,"statistics":dict(global_counts),"maps":records,"rom_integration_allowed":False},open(OUT/"phase23_statistics.json","w"),indent=2)
report=f"""# Phase 23 - Contextual Real Visual Blockdata

Base ROM SHA-256: {ROM_SHA}
Unique maps processed: {len(records)}
Resolved cells: {global_counts["resolved_cells"]}
Unresolved cells: {global_counts["unresolved_cells"]}
Validation errors: {len(errors)}
ROM integration: NOT ALLOWED

Phase20 semantic cells were converted into real GBA secondary metatile IDs.
The combined GBA metatile space uses 0x0200 + secondary_metatile_id.
Selection uses map-specific tilesets, Phase22 confidence gates, and neighborhood consistency.
0xFFFF remains unresolved.

Current Phase20 semantic coverage is only 0=base grass, 7=dirt ground, 12=water, plus 0xFFFF.
Missing road, wall, tree, fence, shoreline and other semantics are not fabricated.
"""
open(OUT/"PHASE23_REPORT.md","w").write(report)
z=Path("/tmp/sinnoh_reconstruction_phase23.zip")
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED) as f:
    for x in OUT.rglob("*"):
        if x.is_file(): f.write(x,x.relative_to(OUT.parent))
print("PHASE23_SIZE",z.stat().st_size)
print("PHASE23_SHA256",hashlib.sha256(z.read_bytes()).hexdigest())
print("MAPS",len(records),"RESOLVED",global_counts["resolved_cells"],"UNRESOLVED",global_counts["unresolved_cells"],"ERRORS",len(errors))
