#!/usr/bin/env python3
"""Exact family algebra and finite controls. No third-party dependencies."""
from fractions import Fraction as F
import json
from verify_certificates import require,matrix,has_majority,complement

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def sub(a,b):return add(a,[-x for x in b])

def main():
    # Coefficients are in ascending powers of k. These identities hold formally.
    a=[-4,3];B=[5,-6,2];c=[-1,2];zc=[-7,4];r=[18,-12,2]
    require(sub(mul(a,zc),mul([-10,5],c))==r,'center polynomial identity')
    require(sub(mul([5],B),mul(c,zc))==r,'leaf polynomial identity')
    require(sub(mul([8],[-5,2,1]),mul([-7,4],[-1,2]))==[-47,34,0],'one-eighth margin polynomial')
    rows=[]
    for k in range(4,101):
        n=2*k
        # Missing pairs: vertex zero to k,...,2k-3.
        A=[[int((i<k)!=(j<k) and not(i==0 and k<=j<2*k-2) and not(j==0 and k<=i<2*k-2)) for j in range(n)] for i in range(n)]
        z=[4*k-7]+[1]*(k-1)+[5]*(k-2)+[1]*2
        C=matrix(A,list(range(k)))
        residual=[sum(C[i][j]*z[j] for j in range(n)) for i in range(n)]
        expected=[2*(k-3)**2 if i==0 or k<=i<2*k-2 else 2*(k-1)**2 for i in range(n)]
        require(residual==expected,'family residual mismatch')
        tau=F((k-3)**2,4*k-7)
        require(min(F(residual[i],z[i]*sum(A[i])) for i in range(n))==tau,'tau not sharp vertexwise minimum')
        bound=F(k*k+2*k-5,(4*k-7)*(2*k-1))
        require(bound==(2+tau)/(2*k-1) and bound>F(1,8),'spectral bound formula failure')
        if k<=6:require(not has_majority(A) and not has_majority(complement(A)),'unexpected majority partition')
        rows.append(dict(k=k,tau=str(tau),bound=str(bound)))
    print(json.dumps(dict(formal_polynomial_identities='pass',exact_family_range=[4,100],both_partition_exclusions_checked=[4,5,6],checks=rows),indent=2))
if __name__=='__main__':main()
