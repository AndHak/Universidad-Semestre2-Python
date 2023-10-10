#7.	Se tienen un vector con datos numéricos donde hay varios repetidos,
#hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.

import random

vector = [random.randint(1,20) for n in range(20)]

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) +1):
        if numero % i == 0:
            return False
    return True

primo_mas_repetido = 0
primo_mas_repetido_repeticiones = 0
primo_menos_repetido = 0
primo_menos_repetido_repeticiones = float("inf")
repeticiones = []
primos = []


for n in vector:
    if es_primo(n):
        if n in primos:
            repeticiones[primos.index(n)] += 1
        else:
            primos.append(n)
            repeticiones.append(1)

for i in range(len(primos)):
    if repeticiones[i] > primo_mas_repetido_repeticiones:
        primo_mas_repetido_repeticiones = repeticiones[i]
        primo_mas_repetido = primos[i]
    if repeticiones[i] < primo_menos_repetido_repeticiones:
        primo_menos_repetido_repeticiones = repeticiones[i]
        primo_menos_repetido = primos[i]

condicion = 1
suma = 0
while condicion <= primo_mas_repetido:
    suma += primo_menos_repetido
    condicion += 1
print(f"\nVector original: \n{vector}\n")
print(f"La multiplicación con sumas del primo mas repetido: {primo_mas_repetido} con {primo_mas_repetido_repeticiones} repeticiones\npor el primo menos repetido: {primo_menos_repetido} con {primo_menos_repetido_repeticiones} repeticiones\nEs igual a: {suma}")
