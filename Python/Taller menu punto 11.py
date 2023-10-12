#11.	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz,
#son consecutivos, es decir, no hay un número primo entre los dos 
import random
matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
def es_primo(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if es_primo(matriz[i][j]):
            contador += 1
            if contador == 2:
                segundo_primo = matriz[i][j]
            if contador == 4:
                cuarto_primo = matriz[i][j]
print("Matriz original")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))
if segundo_primo < cuarto_primo:
    es_consecutivo = True
    condicion = segundo_primo + 1
    while condicion < cuarto_primo:
        contador = 1
        divisores = 0
        while contador <= condicion:
            if condicion % contador == 0:
                divisores += 1
            contador += 1
        if divisores == 2:
            print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} NO son consecutivos")
            es_consecutivo = False
            break
        condicion += 1
    if es_consecutivo:
        print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} SI son consecutivos")
else:
    print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} NO son consecutivos")