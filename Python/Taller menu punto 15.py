#Se tienen dos matrices con datos numericos
#Formar un diccionario con los primos como clave
#Y las veces que aparece como valor, ordenarlo por clave
import random
matriz1 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
matriz2 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
diccionario = {}
def es_primo(x):
  if x <= 1:
    return False
  for i in range(2,int(x**0.5)+1):
    if x % i == 0:
      return False
  return True
def agregar_a_diccionario(matriz, diccionario):
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if es_primo(matriz[i][j]):
        if matriz[i][j] not in diccionario:
          diccionario[matriz[i][j]] = 1
        else:
          diccionario[matriz[i][j]] += 1
agregar_a_diccionario(matriz1, diccionario)
agregar_a_diccionario(matriz2, diccionario)
print("Matriz 1")
for fila in matriz1:
  print(" ".join("{:4}".format(n) for n in fila))
print("\nMatriz 1")
for fila in matriz2:
  print(" ".join("{:4}".format(n) for n in fila))
print()
#Ordenamiento por clave con algoritmo
def ordenar_claves(diccionario):
  claves = list(diccionario.keys())
  for i in range(len(claves)):
    for j in range(len(claves)-1-i):
      if claves[j] > claves[j+1]:
        claves[j], claves[j+1] = claves[j+1], claves[j]
  diccionario_ordenado = {}
  for clave in claves:
      diccionario_ordenado[clave] = diccionario[clave]
  return diccionario_ordenado
diccionario_ordenado = ordenar_claves(diccionario)
for primo, repeticiones in diccionario_ordenado.items():
  print(f"Primo: {primo}  Repeticiones: {repeticiones}")
