frutas = ["manzana", "naranja", "plátano", "pera", "melón"]

for elemento in enumerate(frutas, start=1):
    print(elemento)

for n, fruta in enumerate(frutas, start=1):
    print(n, fruta)

numerado = [[x,y] for x, y in enumerate(frutas)]

print(numerado)


matriz = [[0, 0, 0, 1],
          [0, 1, 0, 1],
          [1, 0, 0, 0],
          [0, 0, 1, 0]]

indices_de_uno = [i for fila in matriz for i, v in enumerate(fila) if v == 1]
print(indices_de_uno)

numeros = [43, 27, 58, 12, 39, 58, 54, 33, 21, 58, 17, 46]

i_mayor = max(enumerate(numeros), key=lambda x: x[1])[0]

print(i_mayor)

i_mayor = numeros.index(max(numeros))

print(i_mayor)

i_mayores = [i for i, n in enumerate(numeros) if n == max(numeros)]

print(i_mayores)