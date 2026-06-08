#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
sixN = np.array([1.5e6,6e6,3e7,1e8,3e8,6e8])
dmean= np.array([0.1710,0.1845,0.1995,0.2085,0.2120,0.2149])
vmA  = np.array([0.2896,0.3066,0.3252,0.3380,0.3489,0.3554])
vmT  = np.array([0.2916,0.3117,0.3303,0.3414,0.3518,0.3585])
vrat = np.array([1.097,1.109,1.111,1.105,1.102,1.102])

fig,(a,b)=plt.subplots(1,2,figsize=(13.5,5.2))
fig.suptitle("Pinning the trend to 6N <= 6e8 (2.17M twin centres): "
             "mean shift saturates, dispersion ratio is conserved",
             fontsize=12,fontweight="bold")
# A: mean shift, decelerating toward a finite limit
a.semilogx(sixN, dmean, "o-", color="#b4341f", ms=7, lw=1.5)
a.axhline(0.215, color="0.5", ls=":", lw=1, label="apparent limit ~0.215")
for x,y in zip(sixN,dmean): a.annotate(f"{y:.3f}",(x,y),fontsize=8,xytext=(0,6),textcoords="offset points",ha="center")
a.set_xlabel(r"$6N_{\max}$"); a.set_ylabel(r"mean shift  $\langle\omega\rangle_{\rm twin}-\langle\omega\rangle_{\rm all}$")
a.set_title("(A) mean shift grows but decelerates (small-prime-dominated)")
a.set_ylim(0.15,0.24); a.legend(fontsize=9); a.grid(alpha=.3,which="both")
# B: dispersion conservation
b.semilogx(sixN, vmA, "s-", color="#9e9e9e", ms=6, lw=1.4, label="all centres  Var/mean")
b.semilogx(sixN, vmT, "o-", color="#b4341f", ms=6, lw=1.4, label="twin centres Var/mean")
b.set_xlabel(r"$6N_{\max}$"); b.set_ylabel("Var / mean  of $\\omega_{>3}$")
b.set_title("(B) both rise in parallel; twin/all ratio = "
            f"{np.mean(vmT/vmA):.3f}$\\pm${np.std(vmT/vmA):.3f} (conserved)")
b.legend(fontsize=9); b.grid(alpha=.3,which="both")
# annotate the ratio stability
for x,ra in zip(sixN, vmT/vmA):
    b.annotate(f"{ra:.3f}",(x,vmT[list(sixN).index(x)]),fontsize=7,xytext=(0,6),
               textcoords="offset points",ha="center",color="#555")
fig.tight_layout(rect=[0,0,1,0.94])
fig.savefig("fig_omega_trend.png",dpi=200); fig.savefig("fig_omega_trend.pdf")
print("wrote fig_omega_trend.{png,pdf}")
print("var/mean twin/all ratio: mean=%.4f std=%.4f"%(np.mean(vmT/vmA),np.std(vmT/vmA)))
print("var_ratio(twin/all): mean=%.4f std=%.4f"%(vrat.mean(),vrat.std()))
