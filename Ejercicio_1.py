import numpy as np

h = 0.05
x = np.arange (-10, 10, h)
f = 1/((1+np.exp(-x**2))**(1/2))

df = []
for i in range(2, len(f)-2):
    df.append((1*f[i+2]-2*f[i]+f[i-2])/(2*h))