#Funciones optimizadas, mayor y menor, intermedio de 3

def mayor(a,b):
    if a < b:
        return b
    else:
        return a
    
def menor(a, b):
    if a < b:
        return a
    else:
        return b
    
"""   
def intermedio_de_tres(a, b, c):
    if a < b:
        m = menor(b, c)
        n = mayor(m, a)
        return n
    else:
        m = menor(a, c)
        n = mayor(m, a)
        return n
"""   

def intermedio_de_tres(a, b, c):
    if a < b:
        return mayor(a, menor(b,c))
    else:
        return mayor(b, menor(a,c))
    
print(intermedio_de_tres(2,8,7))