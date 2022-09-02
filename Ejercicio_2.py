import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x,y)

R = 2
h = 0.001
def phi (x, y):
    potencial = 2*x*(1-(2**2/(x**2+y**2)))
    return potencial
    
V_x = np.zeros((25,25))
V_y = np.zeros((25,25))

for i in range(0, 25):
    for j in range(0, 25):
        
        x = X[i, j]
        y = Y[i, j]
        r = (x**2+y**2)**(1/2)
        
        if r > R: 
            V_x[i, j] = (phi(x+h, y) - phi(x -h, y))/(2*h)
            V_y[i, j] = -(phi(x, y+h) - phi(x, y-h))/(2*h)
            
plt.title("Campo de velocidades")
plt.xlabel("x[cm]")
plt.ylabel("y[cm]")
plt.plot
plt.plot(x, y, color="red")
plt.quiver(X, Y, V_x, V_y, color="blue")



