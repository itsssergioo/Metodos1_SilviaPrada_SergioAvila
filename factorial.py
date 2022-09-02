# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(n):
    if n < 0:
        print("factoriales de numeros negativos no existen")
    else:
        fact = 1
        if n>= 1:
            for x in range(1,n+1):
                fact=fact*x
                print ("el factorial de", x, "es", fact)
factorial(20)    

def variaciones (n, r):
    if r > n:
        print("factoriales de numeros negativos no existen")
    else:
        fact = 1
        x = 1
        while x<=n:
          fact = x*fact
          x = x+1

        numerador = fact         
        dn = n - r              
        fact = 1
        x = 1
        while x<=dn:
          fact = x*fact
          x = x+1
        denominador = fact       
        var = numerador/denominador

        print("las variaciones de", n, "elementos tomados de", r, "en", r, "son", var)
        
variaciones(6, 3)

def combinaciones (n, m):
    fact = x = 1
    while x<=n:
        fact = x*fact
        x += 1

    numerador = fact
    dn = n-m
    fact = x = 1

    while x<=dn:
        fact = x*fact
        x += 1

    denominador = fact
    fact = x = 1
    while x<=m:
        fact = x*fact
        x += 1

    denominador = fact*denominador
    comb = numerador/denominador
    print("las combinaciones de ", n, "elementos tomados de", m, "en", m, "son", comb)

combinaciones (21, 10)


def fibonnaci(n):
    a, b= 0,1
    while a < n:
        a,b = b,a +b
        return a
          
def fi(n):
    return fibonnaci(n)/fibonnaci(n-1)

print (format(fibonnaci(100)))
print(fi)
    
fibonnaci(30)
fi(5)