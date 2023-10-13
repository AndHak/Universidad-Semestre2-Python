#Se tiene una lista con datos numericos repetidos, formar un diccionario
#con clave el numero y con valor las veces que se repite
import random
vector = [random.randint(1,10) for i in range(10)]
diccionario = {}
for i in vector:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(f"Vector:\n{vector}\n")
for numero, repeticiones in diccionario.items():
    print(f"Numero:  {numero}   Repeticiones:  {repeticiones}")