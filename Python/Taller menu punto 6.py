#6.	Se tienen dos vectores con datos numéricos donde hay varios repetidos,
#formar un tercer vector con la unión de solo números Fibonacci sin repetidos,
#sin tener en cuenta aquellos Fibonacci que sean comunes.

import random

def es_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

vector1 = [random.randint(1,50) for n in range(20)]
vector2 = [random.randint(1,50) for n in range(20)]
vector3 = []

for n in vector1:
    if es_fibonacci(n):
        if n not in vector2 and n not in vector3:
            vector3.append(n)
for n in vector2:
    if es_fibonacci(n):
        if n not in vector1 and n not in vector3:
            vector3.append(n)
print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\nVector 3:\n{vector3}")
