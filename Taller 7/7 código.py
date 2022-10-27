# PUNTO 7
import numpy as np
import matplotlib.pyplot as plt
# a 

def ModAjus(x,theta):
    return theta[0] / (theta[1] + np.exp(- theta[2] * x))

# b 

def FunCos(p,x,y):
    t = y - ModAjus(x,p)
    return np.sum(t ** 2)

# e 
pair1 = np.array([1,1,1])
print(pair1)

def Grad(FunCos, theta, x, h=1e-6):
    lentheta = len(theta)
    rellj = np.zeros(lentheta)
    for j in range(lentheta):
        h_= np.zeros(lentheta)
        h_[j] = h           
        rellj[j] = (FunCos(x, theta + h_) - FunCos(x, theta - h_)) / (2 * h)            
    return rellj

def DescGrad(FunCos, theta, x, y, listr = 1e-3, e = int(1e4), mis = 1e-2):
    ddd = 1
    ttt = 0
    print("Entrenamiento en curso...")
    while ddd > mis and ttt < e:
        CurrentMe = FunCos(theta, x, y)
        #print(CurrentMe)
        Sum=0
        #Machine Learning
        for i in range(len(y)):
            Sum += (y[i] - FunCos(x[i],theta)) * Grad(FunCos,theta,x[i])
        #print(Sum)
        theta = theta - listr * (-2)*Sum
        NewMe = FunCos(theta, x, y)
        #print(NewMe)
        d= np.abs(CurrentMe-NewMe)/NewMe
        d=np.sqrt(NewMe/len(y))  
        ttt += 1
    if d < mis:
        print(' Entrenamiento completo ', d, 'iteraciones', ttt)
    if ttt == mis:
        print(' Máximo de iteraciones alcanzado ',d)
    return theta, ttt

    par, num_it = DescGrad(FunCos, pair1, x, y)
    print(par)
    
# f

gr = np.linspace(-10,10,120)
plt.scatter(x, y, color="r")
plt.plot(gr, ModAjus(gr, par))
plt.show()



