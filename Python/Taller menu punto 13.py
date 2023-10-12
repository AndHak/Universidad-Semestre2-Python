#13.	Se tiene un conjunto y una matriz con datos numéricos,
#hallar el primo mayor del conjunto y su factorial
#y llenar este valor en las posiciones comprendidas entre el par menor y el Fibonacci mayor de la matriz
import random
vector = [random.randint(1,10) for i in range(10)]
matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def calcular_factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial
def es_par(x):
    if x % 2 == 0:
        return True
    return False
def es_fibonacci(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x
primo_mayor = 0
for i in vector:
    if es_primo(i):
        if i > primo_mayor:
            primo_mayor = i
factorial_primo_mayor = calcular_factorial(primo_mayor)
par_menor = float("inf")
posicion_par_menor_columna = None
posicion_par_menor_fila = None
fibonacci_mayor = 0
posicion_fibonacci_mayor_columna = None
posicion_fibonacci_mayor_fila = None
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if es_fibonacci(matriz[i][j]):
            if matriz[i][j] > fibonacci_mayor:
                fibonacci_mayor = matriz[i][j]
                posicion_fibonacci_mayor_columna = j
                posicion_fibonacci_mayor_fila = i
        if es_par(matriz[i][j]):
            if matriz[i][j] < par_menor:
                par_menor = matriz[i][j]
                posicion_par_menor_columna = j
                posicion_par_menor_fila = i
print(f"Vector:\n{vector}\n")
print("Matriz")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))
print(f"\nPrimo mayor vector: {primo_mayor} Su factoria: {factorial_primo_mayor}")
print(f"Par menor matriz: {par_menor} posicion fila: {posicion_par_menor_fila+1} columna: {posicion_par_menor_columna+1}")
print(f"Fibonacci mayor matriz: {fibonacci_mayor} posicion fila: {posicion_fibonacci_mayor_fila+1} columna: {posicion_fibonacci_mayor_columna+1}")

#Matriz modificada dentro del rango del par menor al fibonacci mayor de la matriz con el factorial
matriz_modificada = matriz.copy()
for i in range(posicion_par_menor_fila, posicion_fibonacci_mayor_fila):
    for j in range(len(matriz_modificada)):
        matriz_modificada[i][j] = factorial_primo_mayor
print("\nMatriz Modificada")
for fila in matriz_modificada:
    print(" ".join("{:4}".format(n) for n in fila))