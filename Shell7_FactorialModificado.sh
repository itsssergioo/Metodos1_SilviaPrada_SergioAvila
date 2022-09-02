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
