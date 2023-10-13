#19.	Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
#el par mayor y las veces que se repite
#el primo menor y las veces que se repite
#el Fibonacci menor y las veces que se repite
#Con estos datos hallar:
#El factorial de la suma del par y del primo
#La multiplicación con sumas de los contadores del primo y del Fibonacci.

import random
vector = [random.randint(1,20) for i in range(10)]
matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
def es_par(x):
    if x % 2 == 0:
        return True
    return False
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
par_mayor = 0
primo_menor = float("inf")
fibonacci_menor = float("inf")
for numero in vector:
    if es_par(numero):
        if numero > par_mayor:
            par_mayor = numero
    if es_fibonacci(numero):
        if numero < fibonacci_menor:
            fibonacci_menor = numero
    if es_primo(numero):
        if numero < primo_menor:
            primo_menor = numero
for fila in matriz:
    for numero in fila:
        if es_par(numero):
            if numero > par_mayor:
                par_mayor = numero
        if es_fibonacci(numero):
            if numero < fibonacci_menor:
                fibonacci_menor = numero
        if es_primo(numero):
            if numero < primo_menor:
                primo_menor = numero
#Repeticiones
diccionario = {}
for numero in vector:
    #Usa los or de esta manera porque el diccionario solo permite una entrada por clave
    if numero == par_mayor or numero == fibonacci_menor or numero == primo_menor:
        if numero in diccionario:
            diccionario[numero] += 1
        else:
            diccionario[numero] = 1

for fila in matriz:
    for numero in fila:
        if numero == par_mayor or numero == fibonacci_menor or numero == primo_menor:
            if numero in diccionario:
                diccionario[numero] += 1
            else:
                diccionario[numero] = 1
print(f"Vector:\n{vector}\n")
print("Matriz")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))
print()
for numero, repeticiones in diccionario.items():
    if numero == par_mayor:
        print(f"Par mayor: {par_mayor} Repeticiones: {repeticiones}")
    if numero == fibonacci_menor:
        repeticiones_fibonacci = repeticiones
        print(f"Fibonacci menor: {fibonacci_menor} Repeticiones: {repeticiones}")
    if numero == primo_menor:
        repeticiones_primo = repeticiones
        print(f"Primo menor: {primo_menor} Repeticiones: {repeticiones}")
#Factorial suma par primo
factorial_par_mas_primo = calcular_factorial(par_mayor + primo_menor)
print(f"\nFactorial de {primo_menor} + {par_mayor} = {factorial_par_mas_primo}")
condicion = 1
suma = 0
while condicion <= repeticiones_fibonacci:
    suma += repeticiones_primo
    condicion += 1
#multiplicación con sumas de los contadores del primo y del Fibonacci
print(f"Multiplicacion de {repeticiones_fibonacci} x {repeticiones_primo} = {suma}")