from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
from ase.units import eV, Ang, GPa
import sys
sys.path.append(r'files')
import Morse
calc = Morse.MorsePotential()

def potential_energy(distance):
    atoms = Atoms('2Cu', positions=[(0., 0., 0.), (0., 0., distance)])
    atoms.set_calculator(calc) 
    return atoms.get_potential_energy()


def annot_min(x,y, ax=None):
    xmin = x[np.argmin(y)]
    ymin = y.min()
    text= "x={:.3f}, y={:.3f}".format(xmin, ymin)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmin, ymin), xytext=(0.94,0.96), **kw)

x = np.linspace(2.2*Ang,5*Ang,1000)
y = np.zeros(len(x))

for i in range(len(x)-1):
    p = x[i]
    y[i]=potential_energy(x[i])

plt.plot(x,y)
plt.plot(x,np.zeros(len(x)),'--')
plt.xlabel("Distance (Arn)")
plt.ylabel("Potential Energy (eV)")
annot_min(x,y)
