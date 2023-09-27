#Una lista que contenga todos los números perfectos en ambas matrices sin duplicados.

import random

def hacer_matriz(dimensiones):
    matriz = []
    for _ in range(dimensiones):
        fila_actual = []
        for _ in range(dimensiones):
            fila_actual.append(random.randint(1, 500))
        matriz.append(fila_actual)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

def es_perfecto(numero):
    if numero <= 1:
        return False
    suma_divisores = 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            suma_divisores += i
            if i != numero // i:
                suma_divisores += numero // i
    return suma_divisores == numero

dimensiones = random.randint(5, 10)

matriz1 = hacer_matriz(dimensiones)
matriz2 = hacer_matriz(dimensiones)

print("\nMatriz 1:")
mostrar_matriz(matriz1)
print("\nMatriz 2:")
mostrar_matriz(matriz2)

numeros_perfectos = []

for fila in matriz1:
    for numero in fila:
        if es_perfecto(numero) and numero not in numeros_perfectos:
            numeros_perfectos.append(numero)

for fila in matriz2:
    for numero in fila:
        if es_perfecto(numero) and numero not in numeros_perfectos:
            numeros_perfectos.append(numero)

print("\nNúmeros perfectos en ambas matrices:")
print(numeros_perfectos)
