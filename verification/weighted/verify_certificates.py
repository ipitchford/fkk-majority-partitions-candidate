#!/usr/bin/env python3
"""Portable stdlib exact replay; works with ordinary Python and python -O.
Run in any directory: python3 verify_certificates.py [certificate JSON path].
No graph generator or spectral/numerical package is needed for certificate replay.
"""
from fractions import Fraction
import hashlib,json,pathlib,sys

def require(condition,message):
    if not condition: raise ValueError(message)

def decode(s):
    b=s.encode('ascii');n=b[0]-63
    require(2<=n<=62 and len(b)==1+(n*(n-1)//2+5)//6,'invalid graph6 length')
    require(all(63<=x<=126 for x in b),'invalid graph6 character')
    A=[[0]*n for _ in range(n)];k=0
    for j in range(1,n):
        for i in range(j):
            v=((b[1+k//6]-63)>>(5-k%6))&1;k+=1;A[i][j]=A[j][i]=v
    return A

def complement(A):
    return [[int(i!=j and not A[i][j]) for j in range(len(A))] for i in range(len(A))]

def has_majority(A):
    n=len(A)
    for mask in range(1,1<<(n-1)):
        S=[i for i in range(n) if mask>>i&1];T=[i for i in range(n) if not(mask>>i&1)]
        if all(2*sum(A[i][j] for j in T)>len(T) for i in S) and all(2*sum(A[i][j] for j in S)>len(S) for i in T):return True
    return False

def connected(A):
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for v,e in enumerate(A[u]):
            if e and v not in seen:seen.add(v);todo.append(v)
    return len(seen)==len(A)

def matrix(A,S):
    n=len(A);S=set(S);T=set(range(n))-S
    require(S and T,'empty partition')
    m=[sum(not A[i][j] for j in (T if i in S else S)) for i in range(n)]
    a=[(len(T if i in S else S)-1)*(n-2)-(n-3)*m[i] for i in range(n)]
    return [[a[i] if i==j else -(n-1)*int((i in S)!=(j in S) and not A[i][j]) for j in range(n)] for i in range(n)]

def verify(r):
    A=decode(r['graph6']);n=len(A);S=r['S'];z=list(map(Fraction,r['z']))
    require(len(z)==n and len(S)==len(set(S)) and all(isinstance(i,int) and 0<=i<n for i in S),'dimension/partition error')
    require(connected(A),'graph disconnected');require(all(v>=1 for v in z),'weight below 1')
    C=matrix(A,S);cz=[sum(C[i][j]*z[j] for j in range(n)) for i in range(n)]
    require(all(v>=0 for v in cz),'Cz negative')
    require(not has_majority(A),'graph has majority partition')
    return not has_majority(complement(A)),min(cz)>0

def negative_controls(good):
    bad=json.loads(json.dumps(good));bad['z']=['1']*len(bad['z'])
    try:verify(bad)
    except ValueError:pass
    else:raise ValueError('constant-weight negative control was accepted')
    bad=json.loads(json.dumps(good));bad['z'][0]='-1'
    try:verify(bad)
    except ValueError:pass
    else:raise ValueError('negative-weight control was accepted')
    require(has_majority([[0,1],[1,0]]),'positive majority control rejected')

def main():
    p=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).with_name('weighted-certificates.json')
    raw=p.read_bytes();rs=json.loads(raw);seen=set();both=strict=0
    for r in rs:
        require(r['graph6'] not in seen,'duplicate graph6');seen.add(r['graph6']);b,s=verify(r);both+=b;strict+=s
    require(bool(rs),'empty certificate set');negative_controls(rs[0])
    print(json.dumps(dict(certificates=len(rs),without_majority_in_either_graph=both,strict_positive_residual=strict,negative_controls='pass',sha256=hashlib.sha256(raw).hexdigest()),indent=2))
if __name__=='__main__':main()
