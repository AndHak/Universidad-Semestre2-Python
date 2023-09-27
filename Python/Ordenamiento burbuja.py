import random

#Ordenamiento burbuja para un vector

#Generar vector con numeros random forma abreviada
vector = [random.randint(1,50) for i in range(20)]
print(f"vector desordenado:\n{vector}")

#Ordenamiento ascendente con burbuja
for i in range(len(vector)-1):
    for j in range(len(vector)-i-1):
        #Para ordenar ascendentemente > de lo contrario <
        if vector[j] > vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]
print(f"Vector ordenado:\n{vector}")

#Generar matriz con numero random
matriz = []
dimensiones = random.randint(5,10)
for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)
print("Matriz con numeros random:")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))
#Ordenar matriz ascendentemente con burbuja
for i in range(len(matriz) * len(matriz)):
    for j in range(len(matriz) * len(matriz)-1):
        fila_actual = j // len(matriz)
        columna_actual = j % len(matriz)
        fila_siguiente = (j+1) // len(matriz)
        columna_siguiente = (j+1) % len(matriz)
        #Para ordenar ascendentemente > de lo contrario <
        if matriz[fila_actual][columna_actual] > matriz[fila_siguiente][columna_siguiente]:
            temporal = matriz[fila_actual][columna_actual]
            matriz[fila_actual][columna_actual] = matriz[fila_siguiente][columna_siguiente]
            matriz[fila_siguiente][columna_siguiente] = temporal
print("Matriz ordenada:")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))