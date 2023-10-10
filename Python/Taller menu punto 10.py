#10.	Intercambiar las columnas donde se encuentre el Fibonacci 2
#con la fila donde se encuentra el Fibonacci 4 según el recorrido por filas de la matriz.
import random

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

# Función para verificar si un número es un número de Fibonacci
def es_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

# Crear una matriz aleatoria de 5x5
matriz = [[random.randint(1, 35) for _ in range(5)] for _ in range(5)]
print("Matriz original:")
mostrar_matriz(matriz)

contador = 0
segundo, cuarto = None, None
posicion_segundo, posicion_cuarto = None, None

# Encontrar el segundo y cuarto número de Fibonacci y sus posiciones
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if es_fibonacci(matriz[i][j]):
            contador += 1
            if contador == 2:
                segundo = matriz[i][j]
                posicion_segundo = j
            if contador == 4:
                cuarto = matriz[i][j]
                posicion_cuarto = j

print(f"\nSegundo Fibonacci: {segundo} Posición: {posicion_segundo}")
print(f"Cuarto Fibonacci: {cuarto} Posición: {posicion_cuarto}")

# Intercambiar las columnas
for i in range(len(matriz)):
    matriz[i][posicion_segundo], matriz[i][posicion_cuarto] = matriz[i][posicion_cuarto], matriz[i][posicion_segundo]

print("\nMatriz modificada:")
mostrar_matriz(matriz)