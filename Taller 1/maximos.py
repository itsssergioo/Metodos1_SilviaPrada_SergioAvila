# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:40:34 2022

@author: Usuario
"""
 
import matplotlib.pyplot as plt  

texto = open('EstrellaEspectro.txt')
print(texto.readlines())


from scipy.signal import find_peaks
lst=texto.readlines()
peaks, _ = find_peaks(lst, height=0)
print(peaks)

plt.plot(peaks)
plt.show()