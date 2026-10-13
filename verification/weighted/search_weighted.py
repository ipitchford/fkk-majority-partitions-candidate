#!/usr/bin/env python3
"""Exhaustive bounded discovery. Usage: python3 search_weighted.py 8 [geng_path]."""
import sys,subprocess,json,time
from verify_certificates import decode as decode_text, require
def decode(s): return decode_text(s.decode())
from fractions import Fraction

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
                require(x%prev==0, 'nonexact Schur division')
                row.append(x//prev)
            C.append(row)
        B=C; prev=pivot; rank+=1
    return True,rank


def parts(A):
 n=len(A)
 for mask in range(1,1<<(n-1)):
  S=[i for i in range(n) if mask>>i&1];T=[i for i in range(n) if not(mask>>i&1)]
  m=[sum(not A[i][j] for j in (T if i in S else S)) for i in range(n)]
  q=[len(T if i in S else S)-1-2*m[i] for i in range(n)]
  yield S,T,m,q

def matrix(A,S,T,m):
 n=len(A);side=set(S)
 a=[(len(T if i in side else S)-1)*(n-2)-(n-3)*m[i] for i in range(n)]
 return [[a[i] if i==j else -(n-1)*int((i in side)!=(j in side) and not A[i][j]) for j in range(n)] for i in range(n)]

def witness(C):
 n=len(C); B=[[Fraction(x) for x in row]+[Fraction(1)] for row in C]
 for k in range(n):
  pivot=next((i for i in range(k,n) if B[i][k]),None)
  if pivot is None:return None
  B[k],B[pivot]=B[pivot],B[k];v=B[k][k];B[k]=[x/v for x in B[k]]
  for i in range(n):
   if i!=k:
    v=B[i][k];B[i]=[x-v*y for x,y in zip(B[i],B[k])]
 return [str(row[-1]) for row in B]

start=time.time()
for n in range(5,int(sys.argv[1])+1):
 count=no=0;proc=subprocess.Popen([sys.argv[2] if len(sys.argv)>2 else 'geng','-cq',str(n)],stdout=subprocess.PIPE)
 for line in proc.stdout:
  count+=1;A=decode(line.strip());P=list(parts(A))
  if any(min(q)>=0 for S,T,m,q in P):continue
  no+=1
  for S,T,m,q in P:
   C=matrix(A,S,T,m)
   if any(C[i][i]<0 for i in range(n)):continue
   if psd_rank(C)[0]:
    print(json.dumps(dict(n=n,graph6=line.decode().strip(),S=S,T=T,q=q,C=C,z=witness(C))),flush=True);break
 require(proc.wait()==0, 'geng failed')
 print(json.dumps(dict(summary=n,graphs=count,no_majority=no,seconds=time.time()-start)),flush=True)
