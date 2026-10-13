#!/usr/bin/env python3
"""Independent exact FKK/D2 checker; Python stdlib, external nauty geng.
Run: python3 exact_small_graphs.py --max-n 8 > exact-small-graphs.json
For connected H: lambda2 >= 2/(n-1) iff Q=vol*((n-1)L-2D)+2dd^T is PSD.
Q1=0, so delete its last row/column; congruence reduces PSD to that block.
Fraction-free Schur elimination uses only integers and exact division.
"""
import argparse, hashlib, json, subprocess, time

def require(condition, detail):
    if not condition:
        raise ValueError(detail)

def decode(s):
    require(isinstance(s, bytes) and len(s)>0, 'graph6 must be nonempty bytes')
    require(all(63 <= c <= 126 for c in s), 'invalid graph6 character')
    n=s[0]-63
    require(2 <= n <= 62, 'unsupported graph6 order (supported: 2..62)')
    bits=n*(n-1)//2
    require(len(s)==1+(bits+5)//6, 'invalid graph6 length')
    pad=(-bits)%6
    require(not pad or ((s[-1]-63)&((1<<pad)-1))==0, 'nonzero graph6 padding')
    A=[[0]*n for _ in range(n)]; k=0
    for j in range(1,n):
        for i in range(j):
            b=((s[1+k//6]-63)>>(5-k%6))&1; k+=1
            A[i][j]=A[j][i]=b
    return A

def complement(A):
    return [[int(i!=j and not A[i][j]) for j in range(len(A))] for i in range(len(A))]

def connected(A):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v,e in enumerate(A[u]):
            if e and v not in seen: seen.add(v); stack.append(v)
    return len(seen)==len(A)

def psd_rank(B):
    B=[r[:] for r in B]; prev=1; rank=0
    while B:
        if any(B[i][i]<0 for i in range(len(B))): return False,None
        k=next((i for i in range(len(B)) if B[i][i]>0),None)
        if k is None: return (True,rank) if all(x==0 for row in B for x in row) else (False,None)
        if k:
            B[0],B[k]=B[k],B[0]
            for row in B: row[0],row[k]=row[k],row[0]
        pivot=B[0][0]; C=[]
        for i in range(1,len(B)):
            row=[]
            for j in range(1,len(B)):
                x=pivot*B[i][j]-B[i][0]*B[0][j]
                require(x%prev==0, 'fraction-free division was not exact')
                row.append(x//prev)
            C.append(row)
        B=C; prev=pivot; rank+=1
    return True,rank

def threshold(A):
    n=len(A); d=list(map(sum,A)); vol=sum(d)
    if not connected(A): return False,None
    B=[[vol*((n-3)*d[i] if i==j else -(n-1)*A[i][j])+2*d[i]*d[j] for j in range(n-1)] for i in range(n-1)]
    return psd_rank(B)

def diam2(A):
    n=len(A)
    return all(A[i][j] or any(A[i][k] and A[k][j] for k in range(n)) for i in range(n) for j in range(i))

def equality_family(A):
    n=len(A)
    if n%2==0: return False
    m=(n-1)//2
    for h in range(n):
        if sum(A[h])!=n-1: continue
        vertices=set(range(n))-{h}; u=min(vertices)
        S={u}|{v for v in vertices if A[u][v]}; T=vertices-S
        if len(S)==len(T)==m and all(A[i][j]==int((i in S)==(j in S)) for i in vertices for j in vertices if i!=j): return True
    return False

def validate_outcomes(A, good, rank, goodc, rankc, family=equality_family):
    """Validate scientific claims; explicit arguments support mutation controls."""
    n=len(A); C=complement(A)
    require(good or goodc, 'FKK failure')
    eq=good and rank<n-1 and not (goodc and rankc==n-1) or goodc and rankc<n-1 and not (good and rank==n-1)
    if eq:
        require(family(A) or family(C), 'unexpected FKK equality')
    d2=connected(A) and diam2(A)
    if d2:
        require(good, 'D2 failure')
        if rank<n-1:
            require(family(A), 'unexpected D2 equality')
    return bool(eq), bool(d2), bool(d2 and rank<n-1)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--max-n',type=int,default=8); p.add_argument('--geng',default='geng'); args=p.parse_args(); require(5 <= args.max_n <= 62, 'max-n must be 5..62')
    results=[]; start=time.time()
    for n in range(5,args.max_n+1):
        cmd=[args.geng,'-q',str(n)]; proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        counts=dict(n=n,all_graphs=0,both_connected=0,diameter2=0,fkk_equalities=0,d2_equalities=0); digest=hashlib.sha256()
        for raw in proc.stdout:
            digest.update(raw); s=raw.strip(); A=decode(s); C=complement(A); counts['all_graphs']+=1
            ac=connected(A); cc=connected(C); counts['both_connected']+=int(ac and cc)
            good,rank=threshold(A); goodc,rankc=threshold(C)
            eq,d2,d2eq=validate_outcomes(A,good,rank,goodc,rankc)
            counts['fkk_equalities']+=int(eq)
            counts['diameter2']+=int(d2)
            counts['d2_equalities']+=int(d2eq)
        stderr=proc.stderr.read().decode(); require(proc.wait()==0,stderr)
        counts['graph6_sha256']=digest.hexdigest(); counts['command']=cmd; results.append(counts)
    print(json.dumps(dict(arithmetic='exact integer fraction-free Schur elimination',elapsed_seconds=time.time()-start,results=results),indent=2))
if __name__=='__main__': main()
