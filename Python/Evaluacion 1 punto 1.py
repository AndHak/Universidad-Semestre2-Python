#1.	Se tiene un vector y una matriz con datos numéricos, buscar un dato en el vector que tiene estas condiciones:
#El dato es el segundo Fibonacci de un rango en un vector cuyos límites están determinados por el primo1 y primo2
#presentes en el rango de la matriz comprendido entre el mayor y el menor es esta.
#Mostrar el dato y su posición.

import random

matriz = [[random.randint(1,20) for j in range(10)] for i in range(10)]
vector = [random.randint(1,20) for i in range(100)]

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
        a, b = b, a + b
    return a == x

posicion_inicio_fila, posicion_inicio_columna = None, None
posicion_fin_fila, posicion_fin_columna = None, None
mayor_de_la_matriz, menor_de_la_matriz = 0, float("inf")

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > mayor_de_la_matriz:
            mayor_de_la_matriz = matriz[i][j]
            posicion_inicio_fila = i
            posicion_inicio_columna = j
        if matriz[i][j] < menor_de_la_matriz:
            menor_de_la_matriz = matriz[i][j]
            posicion_fin_fila = i
            posicion_fin_columna = j

primo1 = 0
primo2 = 0
contador_primos = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == posicion_inicio_fila:
            if j >= posicion_inicio_columna:
                if es_primo(matriz[i][j]):
                    contador_primos += 1
                    if contador_primos == 1:
                        primo1 = matriz[i][j]
                    if contador_primos == 2:
                        primo2 = matriz[i][j]
        if i == posicion_fin_fila:
            if j <= posicion_fin_columna:
                if es_primo(matriz[i][j]):
                    contador_primos += 1
                    if contador_primos == 1:
                        primo1 = matriz[i][j]
                    if contador_primos == 2:
                        primo2 = matriz[i][j]
        if i > posicion_inicio_fila and i < posicion_fin_fila:
            if es_primo(matriz[i][j]):
                    contador_primos += 1
                    if contador_primos == 1:
                        primo1 = matriz[i][j]
                    if contador_primos == 2:
                        primo2 = matriz[i][j]

posicion_inicio_vector, posicion_fin_vector = None, None
for i in range(len(vector)):
    if vector[i] == primo1:
        posicion_inicio_vector = i
    if vector[i] == primo2:
        posicion_fin_vector = i

dato = 0
posicion_dato = 0
contador_fibonaccis = 0

for i in range(posicion_inicio_vector, posicion_fin_vector + 1):
    if es_fibonacci(vector[i]):
        contador_fibonaccis += 1
        if contador_fibonaccis == 2:
            dato = vector[i]
            posicion_dato = i

print(f"Dato: {dato}  Posicion dato: {posicion_dato}")

