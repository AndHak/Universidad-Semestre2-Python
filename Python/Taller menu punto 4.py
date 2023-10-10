#4.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci,
#formar un tercer vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.

import random

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

vector = [random.randint(1,50) for n in range(50)]

fibonacci_mayor = 0
posicion_fibonacci_mayor = None
fibonacci_menor = float("inf")
posicion_fibonacci_menor = None

for posicion, numero in enumerate(vector):
    if es_fibonacci(numero):
        if numero > fibonacci_mayor:
            fibonacci_mayor = numero
            posicion_fibonacci_mayor = posicion
        if numero < fibonacci_menor:
            fibonacci_menor = numero
            posicion_fibonacci_menor = posicion

primos_en_el_rango = []

for n in range(posicion_fibonacci_mayor + 1, posicion_fibonacci_menor):
    if es_primo(n):
        primos_en_el_rango.append(n)

print(f"Vector original:\n{vector}\nLos primos entre el fibonacci mayor: {fibonacci_mayor} y el fibonacci menor: {fibonacci_menor} son:\n{primos_en_el_rango}")