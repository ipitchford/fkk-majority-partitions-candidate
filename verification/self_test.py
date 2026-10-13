#!/usr/bin/env python3
"""Semantic negative controls. Run identically with python3 or python3 -O."""
import json
import sys
from exact_small_graphs import (decode, complement, threshold, psd_rank,
                               validate_outcomes, require)

checks=[]
def check(name, condition):
    require(condition, name)
    checks.append(name)

def rejects(name, action):
    try:
        action()
    except ValueError:
        checks.append(name)
        return
    raise ValueError('negative control failed: '+name)

def graph(n, edges):
    A=[[0]*n for _ in range(n)]
    for u,v in edges:
        A[u][v]=A[v][u]=1
    return A

for raw in [b'',b'?',b'~',b'A',b'A??',b'A@',b'A\x7f',b'A!',b'AA']:
    rejects('malformed graph6 '+repr(raw),lambda raw=raw:decode(raw))
check('valid empty order-two graph',decode(b'A?')==[[0,0],[0,0]])
check('valid order-two edge',decode(b'A_')==[[0,1],[1,0]])
check('zero diagonal nonzero offdiagonal rejected',psd_rank([[0,1],[1,0]])==(False,None))
check('rank-one PSD',psd_rank([[1,1],[1,1]])==(True,1))
check('zero PSD',psd_rank([[0,0],[0,0]])==(True,0))
check('positive pivot swaps',psd_rank([[0,0],[0,2]])==(True,1))
check('indefinite despite positive diagonals',psd_rank([[1,2],[2,1]])==(False,None))
P5=graph(5,[(i,i+1) for i in range(4)])
check('connected P5 below threshold',threshold(P5)==(False,None))
K5=graph(5,[(i,j) for i in range(5) for j in range(i)])
check('K5 strictly above threshold',threshold(K5)==(True,4))
H=graph(5,[(0,i) for i in range(1,5)]+[(1,2),(3,4)])
check('hub and equal cliques exact equality',threshold(H)==(True,3))
validate_outcomes(H,*threshold(H),*threshold(complement(H)))
checks.append('true equality accepted')
rejects('unexpected equality mutation',lambda:validate_outcomes(H,*threshold(H),*threshold(complement(H)),family=lambda A:False))
rejects('both spectral decisions flipped below threshold',lambda:validate_outcomes(K5,False,None,False,None))
rejects('D2 spectral decision mutation',lambda:validate_outcomes(K5,False,None,True,4))
# A sign-flipped target matrix incorrectly rejects K5. This verifies that a
# scientific positive control catches a sign mutation in the defining form.
n=5;d=[4]*5;w=20
B=[[w*((n-3)*d[i] if i==j else -(n-1)*K5[i][j])+2*d[i]*d[j] for j in range(4)] for i in range(4)]
check('matrix sign mutation is detected by K5 control',psd_rank([[-x for x in row] for row in B])[0] is False)
# Replacing threshold 2/(n-1) by 3/(n-1) must reject the exact equality graph.
d=list(map(sum,H));w=sum(d)
mutant=[[w*((n-1)*((d[i] if i==j else -H[i][j]))-3*(d[i] if i==j else 0))+3*d[i]*d[j] for j in range(4)] for i in range(4)]
check('threshold mutation is detected by equality control',psd_rank(mutant)[0] is False)
print(json.dumps({'status':'pass','optimized':bool(sys.flags.optimize),'count':len(checks),'checks':checks},indent=2))
