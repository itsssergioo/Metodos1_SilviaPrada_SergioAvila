# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hqqBKff8U9_m8ainVRPj79G6yAy_npJM
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import sympy as sym
import os.path as path

X = np.array([1.4,3.5,5.6])
Y = np.array([0.4007954931819738,0.594128102489774,0.29802795523938164])

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod

def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

x = np.linspace(-3,10,25)
y = Poly(x,X,Y)

plt.scatter(X,Y,color='r')
plt.plot(x,y,color='k')

y1 = np.interp(x,X,Y)

plt.scatter(X,Y,color='r')
plt.plot(x,y1,color='k')

x = sym.Symbol('x')
f = Poly(x,X,Y)

f

f = sym.expand(f)
f
