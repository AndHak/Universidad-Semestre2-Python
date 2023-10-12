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
def agregar_a_diccionario(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if es_primo(matriz[i][j]):
        if matriz[i][j] in diccionario:
          diccionario[]
