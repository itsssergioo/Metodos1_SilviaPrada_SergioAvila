#PUNTO 5 GENERALES DE PROBABILIDAD
import numpy as np
import matplotlib.pyplot as plt

def Probab(n):
    if 365 < n:
        print("El valor que ingresó está fuera del rango.")
    else:
        f = 365
        p = 365
        prob = 1
        for i in range(int(n)):
            prob *= f/p
            f -= 1
        return prob
    
n = np.linspace(1,80,80)
p = np.zeros((80))

for j in range(80):
    p[j] = Probab(n[j])
    
figura = plt.figure(figsize=(10,10))
axis = figura.add_subplot()
axis.plot(n, p, c="r", label="Probabilidad")
axis.legend()
axis.grid()
axis.set_xlabel("n")
axis.set_ylabel("P(n)")

