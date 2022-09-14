import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

X = np.array([0, 1.5, 2, 3.8, 4.2, 5.9])
Y = np.array([-18, -13, 0, 5, 3, 10])

D = np.zeros((len(X),len(Y)))
D[:,0] = Y

for i in range(1,len(X)):
    for j in range(i,len(Y)):
        D[j,i] = D[j,i-1]-D[j-1,i-1]
print(D)

def metodonew(X,Y,x):
    
    a = Y[0]
    
    D = np.zeros((len(X),len(Y)))
    D[:,0] = Y

    h = X[1] - X[0]
            
    poly = 1.0
    
    for i in range(1,len(X)):
        poly *= ( x - X[i-1] )
        for j in range(i, len(X)):
            D[j,i] = D[j,i-1]-D[j-1,i-1]
        a += poly*(D[i,i])/(np.math.factorial(i)*h**(i))
    
    return a, np.round(D,2)

#x = np.linspace(np.min(X),np.max(X),1000)
#y,_ = metodonew(X,Y,x)

#plt.scatter(X,Y,color='r')
#plt.plot(X,Y)

x = sym.Symbol('x',Real='True')
y,_ = metodonew(X,Y,x)

print(y)

y = y.simplify()

print (y)