#Recursion cuenta hacia adelante

def hacia_atras(n):
    if n < 0:
        print("Fin")
    else:
        print(n)
        hacia_atras(n-1)

def hacia_adelante(n, m):
    if n > m:
        print("Fin")
    else:
        print(n)
        hacia_adelante(n+1, m)

hacia_adelante(5,10)
