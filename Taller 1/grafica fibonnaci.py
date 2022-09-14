# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:16:02 2022

@author: Usuario
"""
#grafica de fibonnaci

import numpy as np
import matplotlib.pyplot as plt  

def fibonnaci(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)

n=20
resultados = [ ]
a=1
b=1
for i in range(n-3):
    total = a + b
    b=a
    a= total
    resultados.append(total)   

x= np.linspace(0,20,21)
plt.plot( resultados)
plt.legend(["fibonnaci"])




