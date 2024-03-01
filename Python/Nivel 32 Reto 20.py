datos = [4, 3, -1, 9, 6, -5, 8, 7, 2]

positivos = list(filter(lambda x: x % 2 == 0, datos))

print(positivos)

datos = [21, 0, 14, 0, 0, 27, 0, 0, 0, 19, 0, 32]

valores = list(filter(lambda x: x, datos))

print(valores)
