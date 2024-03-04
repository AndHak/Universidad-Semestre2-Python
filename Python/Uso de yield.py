numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cuadrados(numeros):
    for number in numeros:
        yield number * number

for numero in cuadrados(numeros):
    print(numero)

def es_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def primos_lista(numeros):
    for numero in numeros:
        if es_primo(numero):
            yield numero

for primo in primos_lista(numeros):
    print(primo)

def es_fibonacci(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a+b
    return a == x

def fibos_lista(numeros):
    for n in numeros:
        if es_fibonacci(n):
            yield n

for fibo in fibos_lista(numeros):
    print(fibo)