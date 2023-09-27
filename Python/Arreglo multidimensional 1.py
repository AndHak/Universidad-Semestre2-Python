import random

def hacer_matriz_3D(matriz):
    dimensiones = random.randint(3,6)
    for _ in range(dimensiones):
        capa_actual = []
        for _ in range(dimensiones):
            fila_actual = []
            for _ in range(dimensiones):
                fila_actual.append(random.randint(1,50))
            capa_actual.append(fila_actual)
        matriz.append(capa_actual)
    return matriz

def mostrar_matriz_3D(matriz):
    for i, capa in enumerate(matriz):
        print(f"Capa: {i}")
        for fila in capa:
            print(" ".join("{:4}".format(num) for num in fila))
        print()

matriz_3D = []
hacer_matriz_3D(matriz_3D)
print("\nMatriz 3D:")
mostrar_matriz_3D(matriz_3D)