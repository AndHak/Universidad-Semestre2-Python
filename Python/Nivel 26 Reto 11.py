#Cuadrados en un intervalo

def cuadrados(n, m):
    if n > m:
        return []
    else:
        return [n**2] + cuadrados(n+1,m)
    
print(cuadrados(3,7))

#Crear listas de forma recursiva con los pares de intervalo

def pares(n,m):
    if n > m:
        return []
    if n % 2 == 0:
        return [n] + pares(n+1,m)
    else:
        return pares(n+1,m)
    
print(pares(2,10))
    
