#!/usr/bin/env python3
"""Exact checks of the archived n=10 small-eigenvalue list and recorded minimizers.
Usage: python3 audit_recorded_candidates.py [DATA_DIRECTORY] > candidate-audit.json
This checks supplied candidates, not coverage of the original n=10 enumeration.
"""
import hashlib,json,pathlib,sys
from exact_small_graphs import decode,complement,connected,threshold,require
root=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parent/'data'; p=root/'n10_small.g6'; raw=p.read_bytes(); rows=raw.splitlines(); seen=set(); equal=0
for row in rows:
    s=row.split()[0]; require(s not in seen, 'duplicate candidate'); seen.add(s); A=decode(s); C=complement(A)
    require(len(A)==10, 'candidate must have order 10'); require(connected(A) and connected(C), 'candidate and complement must be connected')
    good,rank=threshold(A); require(not good,('not strictly below threshold',s,rank))
    good,rank=threshold(C); require(good and rank==len(A)-1,('complement not strictly above',s))
require(len(seen)==72677, 'expected 72677 archived candidates')
results=[]
minimizer_rows=(root/'recorded_minimizers.g6').read_text().splitlines()
require(len(minimizer_rows)==7 and len(set(minimizer_rows))==7, 'expected seven distinct minimizers')
for s in minimizer_rows:
    A=decode(s.encode()); vals=[threshold(B) for B in [A,complement(A)]]
    require(any(good and rank==len(A)-1 for good,rank in vals), 'recorded minimizer not strictly above in either graph')
    results.append(dict(graph6=s,exact_psd_and_rank=vals))
print(json.dumps(dict(candidate_file=p.name,sha256=hashlib.sha256(raw).hexdigest(),distinct_candidates=len(seen),all_exactly_below_threshold=True,all_complements_exactly_strictly_above_threshold=True,recorded_minimizers=results),indent=2))
