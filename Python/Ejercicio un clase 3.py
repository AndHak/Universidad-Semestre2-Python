#Se tiene una lista de datos, formar dos listas asi
#lista 1 con los primos sin repetids y lista 2 con los fibonaccis sin repetidos

import random

def crear_lista():
    lista = [random.randint(1,50) for _ in range(20)]
    fibonaccis = []
    primos = []
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
    def es_fibonacci(numero):
        num1 = 0
        num2 = 1
        secuencia = 0
        while secuencia <= numero:
            secuencia = num1 + num2
            num1 = num2
            num2 = secuencia
            if secuencia == numero:
                return True
        return False
    for numero in lista:
        if es_fibonacci(numero) and numero not in fibonaccis:
            fibonaccis.append(numero)
        if es_primo(numero) and numero not in primos:
            primos.append(numero)
    print(f"Lista original:\n{lista}")
    print(f"Lista de primos:\n{primos}")
    print(f"Lista de fibonaccis:\n{fibonaccis}")
crear_lista()