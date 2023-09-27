#Se tiene dos listas con datos, formar dos listas asi
#lista 1 con los primos no comunes de las dos listas sin repetidos
#lista 2 con los imapres comunes de las dos listas sin repetidos

import random

lista1 = [random.randint(1,50) for i in range(20)]
lista2 = [random.randint(1,50) for i in range(20)]

print(f"Lista 1:\n{lista1}")
print(f"Lista 2:\n{lista2}")

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

def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

primos_no_comunes = []
impares_comunes = []

#Identificar los primos no comunes de las dos listas
for i in range(len(lista1)):
    if es_primo(lista1[i]):
        if lista1[i] not in lista2 and lista1[i] not in primos_no_comunes:
            primos_no_comunes.append(lista1[i])
for j in range(len(lista2)):
    if es_primo(lista2[j]):
        if lista2[j] not in lista1 and lista2[j] not in primos_no_comunes:
            primos_no_comunes.append(lista2[j])

for i in range(len(primos_no_comunes)):
    for j in range(len(primos_no_comunes)-i-1):
        if primos_no_comunes[j] > primos_no_comunes[j+1]:
            temporal = primos_no_comunes[j]
            primos_no_comunes[j] = primos_no_comunes[j+1]
            primos_no_comunes[j+1] = temporal
print(f"Primos no comunes de las dos listas:\n{primos_no_comunes}")

#identificar los impares comunes de las dos listas
for i in range(len(lista1)):
    if es_impar(lista1[i]):
        if lista1[i] in lista2 and lista1[i] not in impares_comunes:
            impares_comunes.append(lista1[i])

for i in range(len(impares_comunes)):
    for j in range(len(impares_comunes)-i-1):
        if impares_comunes[j] > impares_comunes[j+1]:
            temporal = impares_comunes[j]
            impares_comunes[j] = impares_comunes[j+1]
            impares_comunes[j+1] = temporal
print(f"Impares comunes de las dos listas:\n{impares_comunes}")
