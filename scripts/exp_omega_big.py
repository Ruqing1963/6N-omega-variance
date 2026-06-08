#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np, math, time, sys
t0=time.time()
def tlog(m): print(f"[{time.time()-t0:6.1f}s] {m}", flush=True)

def run(NMAX):
    PMAX = 6*NMAX + 2
    tlog(f"NMAX={NMAX:,}  (6N up to {6*NMAX:,}); allocating sieve ~{PMAX/1e6:.0f}MB")
    sieve = np.ones(PMAX+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(PMAX**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    tlog("prime sieve done")
    primes = np.nonzero(sieve[:NMAX+1])[0]
    tlog(f"primes<=NMAX extracted: {len(primes):,}")
    # twin mask via strided views, then free the big sieve
    lower = sieve[5:6*NMAX:6][:NMAX]; upper = sieve[7:6*NMAX+2:6][:NMAX]
    twin = (lower & upper).copy()
    del sieve, lower, upper
    tlog(f"twin mask built; twin centres = {int(twin.sum()):,}")
    # distinct prime-factor count, then in-place omega_{>3}
    omega = np.zeros(NMAX+1, dtype=np.int8)
    for p in primes: omega[p::p]+=1
    del primes
    omega[2::2]-=1; omega[3::3]-=1     # remove factors 2 and 3 -> omega_{>3}
    tlog("omega_{>3} done")
    og = omega[1:NMAX+1]               # N=1..NMAX  (view)
    return og, twin

# attempt 1e8, fall back if memory fails
for target in (100_000_000, 50_000_000, 16_666_666):
    try:
        og, twin = run(target); NMAX=target; break
    except MemoryError:
        tlog(f"MemoryError at NMAX={target:,}; falling back"); 
        import gc; gc.collect()
else:
    sys.exit("all attempts failed")

cuts = [c for c in (250_000,1_000_000,5_000_000,16_666_666,50_000_000,100_000_000) if c<=NMAX]
print("\n  6N_max      lnln   mean_all  mean_twin  d(mean)   var_all  var_twin  var_ratio  (v/m)all (v/m)twin   ntwin")
for cut in cuts:
    oa = og[:cut]
    tw = twin[:cut]
    ot = oa[tw]
    mA=float(oa.mean()); vA=float(oa.var()); mT=float(ot.mean()); vT=float(ot.var())
    llx=math.log(math.log(6*cut))
    print(f"{6*cut:>11,} {llx:6.3f}  {mA:8.4f}  {mT:8.4f}  {mT-mA:+.4f}  {vA:8.4f} {vT:8.4f}  {vT/vA:7.4f}   {vA/mA:6.4f}  {vT/mT:6.4f}  {int(tw.sum()):>9,}")

# save full-scale hist + stats
oa=og; ot=og[twin]; kmax=int(max(oa.max(),ot.max()))
pa=np.bincount(oa.clip(0,kmax),minlength=kmax+1)/len(oa)
pt=np.bincount(ot.clip(0,kmax),minlength=kmax+1)/len(ot)
np.save('ek_hist.npy', np.vstack([np.arange(kmax+1),pa,pt]))
np.save('ek_stats.npy', np.array([float(oa.mean()),float(oa.var()),float(ot.mean()),float(ot.var()),
                                  math.log(math.log(6*NMAX)),int(twin.sum()),len(oa)]))
tlog(f"saved full-scale hist/stats at NMAX={NMAX:,}")
