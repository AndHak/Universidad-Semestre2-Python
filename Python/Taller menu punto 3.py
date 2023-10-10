#3.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.

import random

vector1 = [random.randint(1,50) for n in range(20)]
vector2 = [random.randint(1,50) for n in range(20)]

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

primos_comunes = []

for n in vector1:
    if es_primo(n):
        if n in vector2 and n not in primos_comunes:
            primos_comunes.append(n)
for n in vector2:
    if es_primo(n):
        if n in vector1 and n not in primos_comunes:
            primos_comunes.append(n)

print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\nPrimos comunes:\n{primos_comunes}\n")