# PARCIAL 2 MÉTODOS COMPUTACIONALES - SILVIA J. PRADA VELÁSQUEZ, SERGIO D. AVILA SUÁREZ

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def Interpolate(x, y, coeficientes):
    loss=0
    for i in range(2):
        for j in range(2):
            loss += coeficientes[i][j]* x*i * y*j
    return loss

a00 = sym.Symbol('a00')
a01 = sym.Symbol('a01')
a10 = sym.Symbol('a10')
a11 = sym.Symbol('a11')

x = sym.Symbol('x')
y = sym.Symbol('y') 

coeficientes = np.array([[a00 , a01] , [a10 , a11]])
Interpolate(x,y,coeficientes)

# 10 B

position=np.zeros((4,2))
position[0]= [1,1]
position[1]= [-1,1]
position[2]= [-1,-1]
position[3]= [1,-1]

position

# 10 C

M = np.array([ [1,1,1,1], [1,-1,1,-1], [1,-1,-1,1], [1,1,-1,-1] ])
N = np.array([1,2,0.5,0.3])

Sol = np.linalg.solve(M,N)
coeficientes = np.array( [ [Sol[0],Sol[2]],[Sol[1],Sol[3]] ] )

print(coeficientes)

# 10 D

F = lambda p , x , y: p[0] + p[1]*x + p[2]*y + p[3]*x*y
tem={'P1':F(Sol , 1,1),'P2':F(Sol , -1,1),'P3':F(Sol , -1,-1),'P4':round(F(Sol,1,-1),2)}
print(tem)
    
# 10 E

X = np.arange(-1,1.01, 0.02)
Y = np.arange(-1,1.01, 0.02)
X,Y = np.meshgrid(X,Y)
Z = X.copy()

rows = X.shape[0]
cols = X.shape[1]

for i in range(rows): 
    for j in range(cols):
        Z[i,j] =  F(Sol , X[i,j] , Y[i,j])

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(1,1,1)
ax1.pcolor(X,Y,Z,cmap = "coolwarm") 

fig2 = plt.figure(figsize=(5,5))
ax2 = fig2.add_subplot(1,1,1,projection = "3d")
ax2.plot_surface(X,Y,Z,cmap = "coolwarm") 
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('T(X,Y)')

# 10 F

sol = Interpolate(0, 0.5, coeficientes)
print(sol)

# 10 G

def Rotar(theta, b):
    matriz=[[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]
    return np.matmul(matriz,b.T).T

print("Matriz rotada 180°:")
Rotar(np.pi,position)
# 10 H


# 10 I


