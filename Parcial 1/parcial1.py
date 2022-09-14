# C 
import numpy as np
import math as m
import sympy as sp
import matplotlib.pyplot as plt

def f(x): 
    fc = (np.tan(x))**0.5
    return fc


def dpr(f, x, h=0.01):
    dfc = ((f(x)+h)-f(x))/h
    return dfc
intervalo = np.linspace(0.1, 1.1, 100)


# D
def dc(f, x, h=0.01):
    return (f(x+h)-f(x-h))/(2*h)
intervalo = np.linspace(0.1, 1.1, 100)
print(dc(f(5),5))


dc = dc(x, cos, h)
dpr = dpr(x, cos, h)



fig = plt.figure(figsize=(7,3))
ax = fig.add_suplot(2,2,1)
ax1 = fig.add_supplot(2,2,2)
ax2 = figr.add_suplot(2,2,3)

ax.scatter(x,f)
ax1.scatter(x, dpr)
ax2.scatter(x, dc)

ax1.scatter(x, np.sen(x)-dc(x))
ax2.scatter(x, np.sen(x)-dpr(x))
