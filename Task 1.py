from __future__ import print_function
import numpy as np
from ase import Atoms
from ase.units import eV, Ang, GPa
d = 2.5*Ang
a = Atoms('2Cu', positions=[(0., 0., 0.), (0., 0., d)])
import sys
sys.path.append(r'files')
import Morse
calc = Morse.MorsePotential()

a.set_calculator(calc) 
a.get_potential_energy()