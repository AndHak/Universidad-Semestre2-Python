#12.	Se tienen dos matrices cuadradas con datos numéricos formar dos conjuntos,
#conjunto uno con los primos de las diagonales principales,
#conjunto 2 con los primos de las diagonales secundarias, con estos dos conjuntos,
#encontrar los elementos comunes y  formar un diccionario con cada uno de estos valores como clave y su factorial como valor
import random
matriz1 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
matriz2 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def primos_diagonal_princiapal(matriz):
    primos = []
    for i in range(len(matriz)):
        if es_primo(matriz[i][i]):
            primos.append(matriz[i][i])
    return primos
def primos_diagonal_secundaria(matriz):
    primos = []
    for i in range(len(matriz)):
        if es_primo(matriz[i][-i-1]):
            primos.append(matriz[i][-i-1])
    return primos
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
conjunto1 = primos_diagonal_princiapal(matriz1) + primos_diagonal_princiapal(matriz2)
conjunto2 = primos_diagonal_secundaria(matriz1) + primos_diagonal_secundaria(matriz2)
print("Martiz 1")
for fila in matriz1:
    print(" ".join("{:4}".format(n) for n in fila))
print("\nMartiz 2")
for fila in matriz2:
    print(" ".join("{:4}".format(n) for n in fila))
print(f"\nPrimos diagonales primarias: {conjunto1}")
print(f"Primos diagonales secundarias: {conjunto2}")
diccionario = {}
elementos_comunes = []
for n in conjunto2:
    if n in conjunto1 and n not in elementos_comunes:
        elementos_comunes.append(n)
for n in conjunto1:
    if n in conjunto2 and n not in elementos_comunes:
        elementos_comunes.append(n)
for n in elementos_comunes:
    factorial = calcular_factorial(n)
    diccionario[n] = factorial
print("\nDiccionario con elementos comunes como claves y sus factoriales:")
for elemento, factorial in diccionario.items():
    print(f"Elemento común: {elemento}, Factorial: {factorial}")