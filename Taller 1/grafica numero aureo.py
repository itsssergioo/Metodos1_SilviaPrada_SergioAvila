# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:33:56 2022

@author: Usuario
"""

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


resultadosphi = [ ]
for i in range(1,len(resultados)):
    phi= resultados[i]/resultados[i-1]
    resultadosphi.append(phi)  
    
numeroaureo= ((1+pow(5,1/2))/2)

plt.axhline(numeroaureo, color= "red")
    
x= np.linspace(0,20,21)
plt.plot( resultadosphi)
plt.legend(["numero aureo", "estimacion"])