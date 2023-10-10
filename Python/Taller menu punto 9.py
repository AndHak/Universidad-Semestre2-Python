#9.	Se tienen un vector con datos numéricos donde hay varios repetidos,
#hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.
import random
vector = [random.randint(1,10) for n in range(10)]
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True
primos = []
repeticiones = []
for n in vector:
    if es_primo(n):
        if n in primos:
            repeticiones[primos.index(n)] += 1
        else:
            primos.append(n)
            repeticiones.append(1)
primo_mas_repetido_repeticiones, primo_menos_repetido_repeticiones = 0, float("inf")
primo_mas_repetido, primo_menos_repetido = 0, 0
for i in range(len(primos)):
    if repeticiones[i] > primo_menos_repetido_repeticiones:
        primo_menos_repetido_repeticiones = repeticiones[i]
        primo_mas_repetido = primos[i]
    if repeticiones[i] < primo_menos_repetido_repeticiones:
        primo_menos_repetido_repeticiones = repeticiones[i]
        primo_menos_repetido = primos[i]
condicion = 1
producto = 0
while condicion <= primo_mas_repetido:
    producto += primo_menos_repetido
    condicion += 1
print(f"\nVector: {vector}\nLa multiplicacion del primo mas repetido: {primo_mas_repetido}\n   Con el primo menos repetido: {primo_menos_repetido}\n\n es: {producto}")