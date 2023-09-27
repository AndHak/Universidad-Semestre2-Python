#Numeros perfectos en una matriz 3D

import random

def hacer_matriz_3d(dimensiones):
    matriz = []
    for _ in range(dimensiones):
        capa = []
        for _ in range(dimensiones):
            fila = []
            for _ in range(dimensiones):
                fila.append(random.randint(1, 100))
            capa.append(fila)
        matriz.append(capa)
    return matriz

def mostrar_matriz_3d(matriz):
    for capa in matriz:
        for fila in capa:
            print(" ".join("{:4}".format(n) for n in fila))
        print()

def es_perfecto(numero):
    if numero <= 1:
        return False
    
    suma_divisores = 1
    for divisor in range(2, numero // 2 + 1):
        if numero % divisor == 0:
            suma_divisores += divisor

    return suma_divisores == numero

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

def es_primo(numero):
    condicion = 1
    divisores = 0
    while condicion <= numero:
        if numero % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        return True
    return False

dimensiones = random.randint(3,6)
matriz_3d = hacer_matriz_3d(dimensiones)

print("\nMatriz 3D:")
mostrar_matriz_3d(matriz_3d)

numeros_perfectos = []
primos = []
pares = []
impares = []

for capa in matriz_3d:
    for fila in capa:
        for numero in fila:
            if es_perfecto(numero) and numero not in numeros_perfectos:
                numeros_perfectos.append(numero)
            if es_impar(numero) and numero not in impares:
                impares.append(numero)
            if es_par(numero) and numero not in pares:
                pares.append(numero)
            if es_primo(numero) and numero not in primos:
                primos.append(numero)

print(f"\nNúmeros perfectos en la matriz 3D: {numeros_perfectos}")
print(f"Números impares en la matriz 3D: {impares}")
print(f"Números pares en la matriz 3D: {pares}")
print(f"Números primos en la matriz 3D: {primos}")