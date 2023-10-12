#se tiene un vector y una matriz con datos numericos
#Formar un conjunto con los multiplos de 5
#y fibonacci ordenado ascendentemente
import random
vector = [random.randint(1,20) for n in range(10)]
matriz = [[random.randint(1,20) for n in range(5)] for i in range(5)]
def es_multiplo_de_5(x):
  if x % 5 == 0:
    return True
  return False
def es_fibonacci(x):
  if x < 0:
    return False
  a, b = 0, 1
  while a < x:
    a, b = b, a+b
  return a == x
conjunto = []
for n in vector:
  if es_multiplo_de_5(n) and n not in conjunto:
    conjunto.append(n)
  if es_fibonacci(n) and n not in conjunto:
    conjunto.append(n)
for fila in matriz:
  for n in fila:
    if es_multiplo_de_5(n) and n not in conjunto:
        conjunto.append(n)
    if es_fibonacci(n) and n not in conjunto:
        conjunto.append(n)
print(f"Vector:\n{vector}")
print(f"\nMatriz:")
for fila in matriz:
  print(" ".join("{:4}".format(n) for n in fila))
print(f"\nConjunto con fibonaccis y multiplos de 5:\n{conjunto}")
