#18.	Se tiene un vector y una matriz formar conjuntos con los números primos de cada una  y realizar las operaciones de conjuntos:
#Unión
#Intersección
#Diferencia
#Diferencia simétrica

import random

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

vector = [random.randint(1,10) for i in range(10)]
matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]

# Crear conjuntos de números primos
conjunto_vector = set(vector)
conjunto_matriz = set()

for fila in matriz:
    conjunto_matriz.update(fila)

# Realizar operaciones de conjuntos
union = conjunto_vector.union(conjunto_matriz)
interseccion = conjunto_vector.intersection(conjunto_matriz)
diferencia = conjunto_vector.difference(conjunto_matriz)
diferencia_simetrica = conjunto_vector.symmetric_difference(conjunto_matriz)

# Imprimir los resultados
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Diferencia simétrica:", diferencia_simetrica)
