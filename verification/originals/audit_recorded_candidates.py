#!/usr/bin/env python3
"""Exact checks of the archived n=10 small-eigenvalue list and recorded minimizers.
Usage: python3 audit_recorded_candidates.py PATH_TO_CYCLE15 > candidate-audit.json
This checks supplied candidates, not coverage of the original n=10 enumeration.
"""
import hashlib,json,pathlib,sys
from exact_small_graphs import decode,complement,connected,threshold
root=pathlib.Path(sys.argv[1]); p=root/'data/n10_small.txt'; raw=p.read_bytes(); rows=raw.splitlines(); seen=set(); equal=0
for row in rows:
    s=row.split()[0]; assert s not in seen; seen.add(s); A=decode(s); C=complement(A)
    assert connected(A) and connected(C)
    good,rank=threshold(A); assert not good,('not strictly below threshold',s,rank)
    good,rank=threshold(C); assert good and rank==len(A)-1,('complement not strictly above',s)
results=[]
for s in ['DCw','ECZo','FQjVo','GCXnf_','HQhTVvy','I?ABrpw~?','J?ABrpw]Fw?']:
    A=decode(s.encode()); vals=[threshold(B) for B in [A,complement(A)]]
    assert any(good and rank==len(A)-1 for good,rank in vals)
    results.append(dict(graph6=s,exact_psd_and_rank=vals))
print(json.dumps(dict(candidate_file=str(p),sha256=hashlib.sha256(raw).hexdigest(),distinct_candidates=len(seen),all_exactly_below_threshold=True,all_complements_exactly_strictly_above_threshold=True,recorded_minimizers=results),indent=2))
