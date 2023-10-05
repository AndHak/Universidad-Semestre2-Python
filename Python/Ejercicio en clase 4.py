#Se tiene una matriz y un vector con datos, sacar listas asi
#Lista 1 con los numeros no comunes sin repetidos
#lista 2 con los primos no repetidos

import random

#Vector con numeros random
vector = [random.randint(1,50) for n in range(20)]
#Matriz vacia
matriz = []
#Las dimensiones que le vamos a dar a la matriz, en este caso será cuadrada
dimensiones = random.randint(2,5)
#Definimos las filas con i
for i in range(dimensiones):
    fila_actual = []
    #Definimos las columnas con j
    for j in range(dimensiones):
        #Asignamos numeros ramndon a el vector fila_actual
        fila_actual.append(random.randint(1,50))
    #Seguido lo agregamos a la matriz
    matriz.append(fila_actual)

#Mostramos el vector
print(f"Vector:\n{vector}")
#Mostramos la matriz
print("\nMatriz:")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#Funcion para identificar si es primo
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

#Lista 1 con los numeros no comunes sin repetidos
lista1 = []
#Verificar y agregar números de la matriz que no están en vector ni en lista1
numeros_matriz = []
for fila in matriz:
    for numero in fila:
        #Metemos los numeros de la matriz en un vector lineal
        numeros_matriz.append(numero)
#Verificamos que los numeros del vector no esten en la matriz
for numero in vector:
    if numero not in numeros_matriz and numero not in lista1:
        lista1.append(numero)
#Verificamos que los numeros de la matriz no esten en el vector
for numero in numeros_matriz:
    if numero not in vector and numero not in lista1:
        lista1.append(numero)
#Mostramos la lista 1 con los numeros no comunes
print(f"\nLista 1 con los numeros no comunes sin repetidos:\n{lista1}")

#Lista 2 con lo primos no repetidos
lista2 = []
#Verificar y agregar primos de la matriz y el vector siempre que no se repitan 
for i in range(len(numeros_matriz)):
    repeticiones = 0
    if es_primo(numeros_matriz[i]):
        for j in numeros_matriz:
            #Comprobamos si no se repite en la matriz
            if j == numeros_matriz[i]:
                repeticiones += 1
        #Si se repite una vez es porque se comparo asi mismo y verificamos que no este en el vector
        if repeticiones == 1 and numeros_matriz[i] not in vector:
            lista2.append(numeros_matriz[i])
#Hacemos lo mismo pero con el vector ahora
for i in range(len(vector)):
    repeticiones = 0
    if es_primo(vector[i]):
        for j in vector:
            if j == vector[i]:
                repeticiones += 1
        if repeticiones == 1 and vector[i] not in numeros_matriz:
            lista2.append(vector[i])
#Mostramos la lista 2 con los primos no repetidos
print(f"\nLista 2 con los primos que no se repiten:\n{lista2}")