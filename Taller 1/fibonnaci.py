# -*- coding: utf-8 -*-
"""


Created on Sun Aug 21 22:09:04 2022

@author: Usuario
"""  

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
          
fibonnaci(20)

#usando fibonnaci para calcular el numero aureo

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
for i in range(2,len(resultados)):
    phi= resultados[i]/resultados[i-1]
    print(phi)

     
        
