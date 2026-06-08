#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
ks, pa, pt = np.load("ek_hist.npy")
mA,vA,mT,vT,llx,ntwin,nall = np.load("ek_stats.npy")
fig,(a,b)=plt.subplots(1,2,figsize=(13.5,5.2))
fig.suptitle("Erdos-Kac second moment on the 6N skeleton: omega_{>3}(N) over all vs twin centres",
             fontsize=12.5,fontweight="bold")
w=0.4
a.bar(ks-w/2, pa, w, label=f"all centres (mean {mA:.3f}, var {vA:.3f})", color="#9e9e9e", edgecolor="k")
a.bar(ks+w/2, pt, w, label=f"twin centres (mean {mT:.3f}, var {vT:.3f})", color="#b4341f", edgecolor="k")
a.axvline(mA,color="#555",ls="--",lw=1); a.axvline(mT,color="#b4341f",ls="--",lw=1)
a.set_xlabel("omega_{>3}(N)  (distinct prime factors > 3)"); a.set_ylabel("probability")
a.set_title(f"(A) distribution shifts right (+{mT-mA:.3f}) and widens (var x{vT/vA:.3f})")
a.legend(fontsize=8.5)
# enrichment ratio
e = np.where(pa>0, pt/pa, np.nan)
b.plot(ks, e, "o-", color="#1f4e79", ms=6)
b.axhline(1,color="red",ls="--",lw=1)
for k,ev in zip(ks,e):
    if pa[int(k)]>1e-5: b.annotate(f"{ev:.2f}",(k,ev),fontsize=8,xytext=(0,5),textcoords="offset points",ha="center")
b.set_xlabel("omega_{>3}(N)"); b.set_ylabel("P(omega | twin) / P(omega | all)")
b.set_title("(B) twin enrichment rises monotonically with omega (the wind-tunnel tilt)")
b.grid(alpha=.3)
fig.tight_layout(rect=[0,0,1,0.94])
fig.savefig("fig_omega_variance.png",dpi=200); fig.savefig("fig_omega_variance.pdf")
print("wrote fig_omega_variance.{png,pdf}")
