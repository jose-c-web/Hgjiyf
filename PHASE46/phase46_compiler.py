#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,struct,pathlib,hashlib

SAFE_NAME_MAP={"End":"END","Return":"RETURN","WaitTime":"ADAPTER_PENDING:WAIT_TIME","SetFlag":"SETFLAG","ClearFlag":"CLEARFLAG","CheckFlag":"CHECKFLAG","Message":"MESSAGE","CloseMessage":"CLOSE_MESSAGE","WaitButton":"WAIT_BUTTON","GiveItem":"GIVE_ITEM","TrainerBattle":"TRAINER_BATTLE","Warp":"WARP","FadeScreen":"FADE_SCREEN"}

def parse_narc(data):
    if data[:4]!=b'NARC': raise ValueError('not a NARC')
    _,_,_,_,hdr,blocks=struct.unpack_from('<4sHHIHH',data,0); pos=hdr; fat=img=None
    for _ in range(blocks):
        magic=data[pos:pos+4]; blen=struct.unpack_from('<I',data,pos+4)[0]; block=data[pos:pos+blen]
        if magic==b'BTAF': fat=block
        elif magic==b'GMIF': img=block
        pos+=blen
    if not fat or img is None: raise ValueError('NARC missing FAT/GMIF')
    count=struct.unpack_from('<H',fat,8)[0]; out=[]; off=12
    for _ in range(count):
        a,b=struct.unpack_from('<II',fat,off); off+=8; out.append(img[8+a:8+b])
    return out

def load_db(path):
    d=json.load(open(path,encoding='utf-8')); return {v.get('id'):(k,v) for k,v in d.get('commands',{}).items() if v.get('type')=='script_cmd' and isinstance(v.get('id'),int)}

def audit(blob,db):
    if len(blob)<2:return []
    op=struct.unpack_from('<H',blob,0)[0]
    if op not in db:return [{'offset':0,'opcode':op,'status':'UNKNOWN_OPCODE'}]
    name,_=db[op]; return [{'offset':0,'opcode':op,'name':name,'target':SAFE_NAME_MAP.get(name),'status':'MAPPED' if name in SAFE_NAME_MAP else 'ADAPTER_PENDING'}]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--db',required=True);ap.add_argument('--scripts');ap.add_argument('--out',required=True);a=ap.parse_args();o=pathlib.Path(a.out);o.mkdir(parents=True,exist_ok=True);db=load_db(a.db);r={'phase':46,'command_database_commands':len(db),'verified_emission':False,'scripts_source_present':bool(a.scripts),'records':[],'unresolved':[]}
    if a.scripts:
        entries=parse_narc(pathlib.Path(a.scripts).read_bytes());r['narc_members']=len(entries)
        for i,b in enumerate(entries):
            x={'member':i,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'audit':audit(b,db)};r['records'].append(x);r['unresolved'] += [{'member':i,**q} for q in x['audit'] if q['status']!='MAPPED']
    else:r['blocked_reason']='Missing Pearl scr_seq_release.narc in supplied artifacts.'
    json.dump(r,open(o/'phase46_report.json','w'),indent=2);print(json.dumps(r,indent=2))
if __name__=='__main__':main()
