#Factorial con recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#Potenciacion con recursion
def potencia(n, e):
    if e == 0:
        resultado = 1
    else:
        resultado = n * potencia(n, e-1)
    return resultado

print(potencia(5, 3))