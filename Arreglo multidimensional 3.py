import random

def hacer_matriz_3D():
    matriz = []
    largo = random.randint(2, 5)
    alto = random.randint(2, 5)
    ancho = random.randint(2, 5)
    for _ in range(alto):
        capa = []
        for _ in range(largo):
            fila = []
            for _ in range(ancho):
                fila.append(random.randint(1, 20))
            capa.append(fila)
        matriz.append(capa)
    return matriz

def mostrar_matriz_3D(matriz):
    for i, capa in enumerate(matriz):
        print(f"Capa: {i+1}")
        for fila in capa:
            print(" ".join("{:4}".format(num) for num in fila))
        print()

matriz_3D = hacer_matriz_3D()
print("Matriz 3D: ")
mostrar_matriz_3D(matriz_3D)

#Para cambiar las capas de la matriz
matriz_3D[0], matriz_3D[-1] = matriz_3D[-1], matriz_3D[0]
print("Matriz 3D con primera capa y ultima cambiadas")
mostrar_matriz_3D(matriz_3D)