import struct,json,zipfile,hashlib,os
from collections import defaultdict
BASE='/mnt/data'
os.makedirs(BASE+'/phase81_83',exist_ok=True)
# Pearl NDS
nds=open(BASE+'/pearl.nds','rb').read()
arm=nds[0x4000:0x4000+33556480]
# headers: 559 * 24
ho=0x020EEDBC-0x02000000
headers=[]
for i in range(0x3468//24):
 v=struct.unpack('<BBHHHHHHHHHBBBB',arm[ho+i*24:ho+(i+1)*24])
 headers.append({'header_id':i,'area':v[0],'move':v[1],'matrix':v[2],'scripts':v[3],'level_scripts':v[4],'msg':v[5],'wild':v[8],'events':v[9],'mapsec':v[10]})
# event NARC
narc=open(BASE+'/zone_event_release.narc','rb').read(); pos=0x10; sec={}
while pos<len(narc):
 tag=narc[pos:pos+4]; sz=struct.unpack_from('<I',narc,pos+4)[0]; sec[tag]=narc[pos+8:pos+sz]; pos+=sz
btaf=sec[b'BTAF']; gm=sec[b'GMIF']; n=struct.unpack_from('<I',btaf,0)[0]
banks=[gm[struct.unpack_from('<II',btaf,4+i*8)[0]:struct.unpack_from('<II',btaf,4+i*8)[1]] for i in range(n)]
# source event features
src=[]
for i,d in enumerate(banks):
 p=0; fc=struct.unpack_from('<I',d,p)[0]; p+=4+fc*20
 oc=struct.unpack_from('<I',d,p)[0]; p+=4
 objs=[]
 for j in range(oc):
  vals=struct.unpack_from('<8I',d,p+j*32); objs.append(vals)
 p+=oc*32; wc=struct.unpack_from('<I',d,p)[0]; p+=4
 warps=[struct.unpack_from('<3I',d,p+j*12) for j in range(wc)]
 p+=wc*12; tc=struct.unpack_from('<I',d,p)[0] if p+4<=len(d) else 0
 src.append({'event_bank':i,'furniture_count':fc,'object_count':oc,'warp_count':wc,'trigger_count':tc,'warp_records':[list(x) for x in warps]})
# event bank -> headers
rev=defaultdict(list)
for h in headers: rev[h['events']].append(h['header_id'])
for x in src: x['header_ids']=rev.get(x['event_bank'],[])
# GBA ROM + manifest
rom=open(BASE+'/sinnoh_step45d_fixed.gba','rb').read()
tab=0x1fe0ec4
maps=[]
for mi in range(204):
 rec=rom[tab+mi*28:tab+(mi+1)*28]
 events_ptr=struct.unpack_from('<I',rec,4)[0]; ep=events_ptr-0x8000000
 oc,wc,cc,bc=rom[ep:ep+4]
 op=struct.unpack_from('<I',rom,ep+4)[0]-0x8000000
 wp=struct.unpack_from('<I',rom,ep+8)[0]-0x8000000
 wars=[]
 for j in range(wc):
  x,y,warp,dst=struct.unpack_from('<HHHH',rom,wp+j*8); wars.append({'x':x,'y':y,'warp':warp,'dest_group_map':dst})
 lp=0x1fdb6a8+mi*24
 layout_id=993+mi
 raw=rom[lp:lp+24]
 vals=struct.unpack('<6I',raw)
 maps.append({'map_index':mi,'layout_id':layout_id,'object_count':oc,'warp_count':wc,'coord_count':cc,'bg_count':bc,'warps':wars,'layout_raw':[hex(v) for v in vals]})
pilots=[('Twinleaf Town',389,411),('Route 201',327,342),('Sandgem Town',396,418),('Jubilife City',2,3),('Oreburgh City',44,45)]
cand={}
for name,eb,hid in pilots:
 s=src[eb]; rows=[]
 for g in maps:
  score=0
  score-=abs(g['object_count']-s['object_count'])*3
  score-=abs(g['warp_count']-s['warp_count'])*5
  if g['object_count']==s['object_count']: score+=12
  if g['warp_count']==s['warp_count']: score+=20
  rows.append({'gba_map':g['map_index'],'score':score,'gba_objects':g['object_count'],'gba_warps':g['warp_count']})
 cand[name]=sorted(rows,key=lambda r:(-r['score'],r['gba_map']))[:20]
report={
 'phase':'81-83',
 'input_rom_sha256':hashlib.sha256(rom).hexdigest(),
 'source_nds_sha256':hashlib.sha256(nds).hexdigest(),
 'source_headers':len(headers),'source_event_banks':len(banks),'gba_maps':len(maps),
 'pilot_catalog':[],
 'status':'CATALOG_AND_MATCHING_AUDIT_ONLY',
 'patch_applied':False,
 'warp_fix':rom[0x0dff3a:0x0dff40].hex()=='041c002846d0'
}
for name,eb,hid in pilots:
 report['pilot_catalog'].append({'name':name,'event_bank':eb,'header_id':hid,'header':headers[hid],'source_events':src[eb],'candidates':cand[name]})
json.dump(report,open(BASE+'/phase81_83/phase81_83_mapping_catalog.json','w'),indent=2)
with open(BASE+'/phase81_83/PHASE81_83_REPORT.md','w') as f:
 f.write('# Fases 81–83 — catálogo determinístico e matching estrutural\n\n')
 f.write(f"ROM: sinnoh_step45d_fixed.gba\n\nSHA-256: `{report['input_rom_sha256']}`\n\n")
 f.write(f"Pearl: {len(headers)} headers / {len(banks)} bancos de eventos. GBA: {len(maps)} mapas.\n\n")
 f.write('## Pilotos\n\n')
 for name,eb,hid in pilots:
  s=src[eb]; f.write(f'- **{name}**: header `{hid}`, event `{eb}`, objetos `{s["object_count"]}`, warps `{s["warp_count"]}`.\n')
  f.write('  - Top candidatos por estrutura: '+', '.join(f"GBA {r['gba_map']} (score {r['score']}, obj {r['gba_objects']}, warp {r['gba_warps']})" for r in cand[name][:5])+'\n')
 f.write('\n## Gate\n\n')
 f.write('- Nenhum ObjectEvent foi alterado.\n- Nenhum script foi ligado a um NPC por hipótese.\n- Warp-fix preservado.\n')
import zipfile
zipout=BASE+'/sinnoh-reconstruction-phase81-83-mapping.zip'
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED) as z:
 for fn in ['phase81_83/phase81_83_mapping_catalog.json','phase81_83/PHASE81_83_REPORT.md']:
  z.write(BASE+'/'+fn,fn)
print(zipout,os.path.getsize(zipout),hashlib.sha256(open(zipout,'rb').read()).hexdigest())
print(report['input_rom_sha256'])
for p in report['pilot_catalog']:
 print(p['name'],p['candidates'][:3])
