"""
Root of Equations
Example: Find root of the equation x + cos(x):
"""

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)



"""
Finding Minima
Example
Minimize the function x^2 + x + 2 with BFGS:
"""
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)