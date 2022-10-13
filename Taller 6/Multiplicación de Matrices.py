def MatriceProduct (x, y): 
    
    xcol = len(x[0])
    ycol = len(y[0])
    xrow = len(x)
    yrow = len(y)
    prod = []
    
    if xrow == ycol:
        for i in range(yrow):    
            prod.append([])
            for j in range(ycol):
                prod[i].append(None)
                
        for c in range (ycol):
            for i in range (xrow):
                mult = 0
                for j in range(xcol):
                    mult += x[i][j]*y[j][c]
                prod[i][c] = mult
        return prod 
    else: 
        return None
    
matriz1 = [[1, 0, 0], [5, 1, 0], [-2, 3, 1]]
matriz2 = [[4, -2, 1], [0, 3, 7], [0, 0 , 2]]
A = matriz1
B = matriz2
print(MatriceProduct(A, B))
    