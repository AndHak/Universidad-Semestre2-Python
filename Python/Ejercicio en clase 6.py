#Se tienen dos listas con datos numericos, formar dos diccionarios asi
#Diccionario 1 con claves, primos comunes de las dos listas
#Y valor el factorial de la clave, Diccionario 2 con clave fibonaccis
#no comunes de las dos listas y valor los pares menores que el fibonacci clave
import random
vector1 = [random.randint(1,20) for n in range(10)]
vector2 = [random.randint(1,20) for n in range(10)]
diccionario1 = {}
diccionario2 = {}
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def es_fibonacci(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a+b
    return a == x
def calcular_factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial
def es_par(x):
    if x % 2 != 0:
        return False
    return True
#Diccionario 1 con primos comunes de clave y de valor el factorial de su clave
for i in vector1:
    for j in vector2:
        if es_primo(j) and j == i:
            if j not in diccionario1:
                diccionario1[j] = calcular_factorial(j)
for i in vector2:
    for j in vector1:
        if es_primo(j) and j == i:
            if j not in diccionario1:
                diccionario1[j] = calcular_factorial(j)
print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\n")
print("Diccionario 1 con primo y su factorial")
for primo, factorial in diccionario1.items():
    print(f"Primo:  {primo}  Factorial:  {factorial}")
#Diccionario 2 con fibonaccis no comunes de clave y los pares menores que el fibonacci de valor
for i in vector1:
    if i not in vector2:
        if es_fibonacci(i):
            pares_menores = []
            for k in vector1:
                if es_par(k) and k < i and k not in pares_menores:
                    pares_menores.append(k)
            for k in vector2:
                if es_par(k) and k  < i and k not in pares_menores:
                    pares_menores.append(k)
            if i not in diccionario2:
                diccionario2[i] = pares_menores
for i in vector2:
    if i not in vector1:
        if es_fibonacci(i):
            pares_menores = []
            for k in vector1:
                if es_par(k) and k < i and k not in pares_menores:
                    pares_menores.append(k)
            for k in vector2:
                if es_par(k) and k  < i and k not in pares_menores:
                    pares_menores.append(k)
            if i not in diccionario2:
                diccionario2[i] = pares_menores
print("\nFibonaccis y pares menores que el fibonacci")
for fibonacci, pares_menores in diccionario2.items():
    print(f"Fibonacci:  {fibonacci}  Pares menores:  {pares_menores}")