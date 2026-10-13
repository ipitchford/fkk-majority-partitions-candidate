#!/usr/bin/env python3
"""Exact small-graph check of the uniform nonsingleton-majority surplus.
Usage: python3 check_parity.py [geng_path]. Generator nauty is trusted.
"""
import json,subprocess,sys
from fractions import Fraction as F
from verify_certificates import decode,require

def psd(B):
    B=[[F(x) for x in r] for r in B]
    while B:
        if any(B[i][i]<0 for i in range(len(B))):return False
        k=next((i for i in range(len(B)) if B[i][i]>0),None)
        if k is None:return all(x==0 for r in B for x in r)
        B[0],B[k]=B[k],B[0]
        for r in B:r[0],r[k]=r[k],r[0]
        v=B[0][0];B=[[B[i][j]-B[i][0]*B[0][j]/v for j in range(1,len(B))] for i in range(1,len(B))]
    return True

def main():
    rows=[]
    for n in range(4,8):
        proc=subprocess.Popen([sys.argv[1] if len(sys.argv)>1 else 'geng','-cq',str(n)],stdout=subprocess.PIPE)
        count=checked=0;types=set()
        for raw in proc.stdout:
            count+=1;A=decode(raw.strip().decode());parities=set()
            for mask in range(1,1<<(n-1)):
                S=[i for i in range(n) if mask>>i&1];T=[i for i in range(n) if not(mask>>i&1)]
                if min(len(S),len(T))<2:continue
                if all(2*sum(A[i][j] for j in T)>len(T) for i in S) and all(2*sum(A[i][j] for j in S)>len(S) for i in T):parities.add(tuple(sorted((len(S)%2,len(T)%2))))
            if not parities:continue
            checked+=1;types.update(parities);d=list(map(sum,A));v=sum(d)
            target=F(2,n-1)+F(1,2*(n-1)**2*(n-2));a=target.numerator;b=target.denominator
            Q=[[v*(b*(d[i] if i==j else -A[i][j])-a*d[i]*int(i==j))+a*d[i]*d[j] for j in range(n-1)] for i in range(n-1)]
            require(psd(Q),'uniform parity surplus failed '+raw.decode().strip())
        require(proc.wait()==0,'geng failed');rows.append(dict(n=n,connected=count,checked=checked,parities=sorted(types)))
    require(not psd([[1,2],[2,1]]),'indefinite negative control accepted')
    require(psd([[1,1],[1,1]]),'singular positive control rejected')
    print(json.dumps(dict(arithmetic='exact Fraction Schur elimination',results=rows,controls='pass'),indent=2))
if __name__=='__main__':main()
