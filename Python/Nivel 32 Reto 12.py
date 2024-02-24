lista = [(3, "a"), (1, "b"), (5, "c"), (2, "d"), (1, "e"), (7, "f"), (4, "g")]

reverso = reversed(lista)

while True:
    try:
        elemento = next(reverso)
        if elemento[0] == 1:
            print(elemento)
    except StopIteration:
        break