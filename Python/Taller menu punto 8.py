#8.	Se tienen dos vectores con datos numéricos donde hay varios repetidos,
#formar un tercer vector con la unión de solo números Fibonacci sin repetidos,
#sin tener en cuenta aquellos Fibonacci que sean comunes.
import random
vector1 = [random.randint(1,10) for n in range(10)]
vector2 = [random.randint(1,10) for n in range(10)]
def es_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero
vector3 = []
for n in vector1:
    if es_fibonacci(n) and n not in vector2 and n not in vector3:
        vector3.append(n)
for n in vector2:
    if es_fibonacci(n) and n not in vector1 and n not in vector3:
        vector3.append(n)
print(f"\nVector 1: {vector1}\nVector 2: {vector2}\nFibonaccis no comunes: {vector3}")