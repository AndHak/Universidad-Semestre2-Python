#16.	Se tiene una matriz con datos numéricos, formar un diccionario con clave Fibonacci
#y valor, las veces que se repite y modificar el valor para aquellos contadores que son primos por su factorial
import random
matriz = [[random.randint(1,10) for j in range(5)] for i in range(5)]
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
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
diccionario = {}
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if es_fibonacci(matriz[i][j]):
            if matriz[i][j] in diccionario:
                diccionario[matriz[i][j]] += 1
            else:
                diccionario[matriz[i][j]] = 1
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))
print()
for fibonacci, repeticiones in diccionario.items():
    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")
print()
#Ahora cambiaremos las repeticiones que son los contadores por el factorial si es que el contador es primo
for fibonacci, repeticiones in diccionario.items():
    if es_primo(repeticiones):
        diccionario[fibonacci] = calcular_factorial(repeticiones)
print("Con los contadores primos por su factorial")
for fibonacci, repeticiones in diccionario.items():
    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")
#Esto no esta en el ejercicio pero es adicional
print()
#Crear un nuevo diccionario con claves convertidas en factoriales
nuevo_diccionario = {}
for fibonacci, repeticiones in diccionario.items():
    factorial_clave = calcular_factorial(fibonacci)
    nuevo_diccionario[factorial_clave] = repeticiones
#Reemplazar el diccionario original por el nuevo diccionario
diccionario = nuevo_diccionario
for fibonacci, repeticiones in diccionario.items():
    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")