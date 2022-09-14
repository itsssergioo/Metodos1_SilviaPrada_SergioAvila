import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#NO SE LOGRÓ INSTALAR WGET, ANACONDA PROMPT LANZABA UN ERRORr

X = np.array([1.4, 3.5, 5.6])
Y = np.array([0.4007954931819738, 0.594128102489774, 0.29802795523938164])

def metodolagr(x,xi,j):
    
    c = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            c *= (x - xi[i])/(xi[j]-xi[i])
    return c

def polinomio(x,xi,yi):
    
    k = 0.
    n = len(xi)
        
    for j in range(n):
        k += yi[j]*metodolagr(x,xi,j)
        
    return k

#x = np.linspace(10,-10,1000)
#y = polinomio(x,X,Y)

#plt.scatter(X,Y,color='r')
#plt.plot(x,y,color='k')

#t = np.interp(x,X,Y)

#plt.scatter(X,Y,color='r')
#plt.plot(x,t,color='b')

x = sym.Symbol('x')
f = polinomio(x,X,Y)
print(f)

f = sym.expand(f)
print(f)

#CÓDIGO DE CLASE