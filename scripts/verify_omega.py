#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier for Part XXVI (fast, standard library).

(A) Second-moment signal at a small scale (6N <= 1.2e6): twin-conditioning shifts
    the mean of omega_{>3} up, inflates the variance ~x1.1, and conserves the
    dispersion ratio Var/mean (twin/all ratio ~ 1.0). (Large-scale numbers in the
    paper come from exp_omega_big.py.)
(B) The annihilation/tiling criterion (Part XXI) = classical Hardy-Littlewood
    admissibility: a tuple is inadmissible iff it covers Z/p for some prime p.
"""
import math

def moments_small(NMAX=200_000):
    P = 6*NMAX+2
    sieve = bytearray([1])*(P+1); sieve[0]=sieve[1]=0
    for i in range(2,int(P**0.5)+1):
        if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
    omega = [0]*(NMAX+1)
    for p in range(2,NMAX+1):
        if sieve[p]:
            for m in range(p,NMAX+1,p): omega[m]+=1
    og=[0.0]*(NMAX+1)
    for N in range(1,NMAX+1):
        og[N]=omega[N]-(N%2==0)-(N%3==0)
    allv=[]; twv=[]
    for N in range(1,NMAX+1):
        allv.append(og[N])
        if sieve[6*N-1] and sieve[6*N+1]: twv.append(og[N])
    def mv(a):
        m=sum(a)/len(a); v=sum((x-m)**2 for x in a)/len(a); return m,v
    mA,vA=mv(allv); mT,vT=mv(twv)
    print(f"(A) 6N<=1.2e6: twin centres={len(twv):,}")
    print(f"    mean: all {mA:.4f}  twin {mT:.4f}  shift {mT-mA:+.4f}  (>0)")
    print(f"    var : all {vA:.4f}  twin {vT:.4f}  ratio {vT/vA:.4f}  (~1.1)")
    print(f"    Var/mean: all {vA/mA:.4f}  twin {vT/mT:.4f}  ratio {(vT/mT)/(vA/mA):.4f}  (~1.0 conserved)")
    return (mT-mA)>0 and 1.05 < vT/vA < 1.16 and abs((vT/mT)/(vA/mA)-1) < 0.03

def covers_modp(H,p): return len({h%p for h in H})==p
def inadmissible(H):
    for p in (2,3,5,7,11,13):
        if p<=len(H) and covers_modp(H,p): return p
    return None
def check_admissibility():
    tests={'{0,2,4}':[0,2,4],'{0,2,6}':[0,2,6],'{0,4,6}':[0,4,6],
           '{0,2,6,8,12}':[0,2,6,8,12],'{0,2,4,6}':[0,2,4,6]}
    expect={'{0,2,4}':3,'{0,2,6}':None,'{0,4,6}':None,'{0,2,6,8,12}':None,'{0,2,4,6}':3}
    ok=True
    print("(B) annihilation/tiling = classical admissibility:")
    for name,H in tests.items():
        p=inadmissible(H); ok=ok and (p==expect[name])
        print(f"    {name:14}: "+(f"covers Z/{p} -> inadmissible (annihilates)" if p else "admissible"))
    return ok

if __name__=="__main__":
    a=moments_small(); b=check_admissibility()
    print("\nALL CHECKS PASS:", a and b)
