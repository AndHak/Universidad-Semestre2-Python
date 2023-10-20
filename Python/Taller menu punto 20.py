#20.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios así:
#Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
#Diccionario 2 con clave carácter y valor las veces que se repite, ordenado ascendentemente por clave 
#Almacenar esta información en un archivo, recuperarla y mostrar los dos diccionarios.

cadena1 = "Hola Mundo 2023"
cadena2 = "Universidad de Nariño semestre 2"
cadena3 = "Numero de estudiantes aproximadamente 35000"
cadenatotal = cadena1 + cadena2 + cadena3
diccionario1 = {}
diccionario2 = {}
for i in range(len(cadenatotal)):
    if cadenatotal[i].isnumeric():
        if cadenatotal[i] in diccionario1:
            diccionario1[cadenatotal[i]] += 1
        else:
            diccionario1[cadenatotal[i]] = 1
    if cadenatotal[i].isalpha():
        if cadenatotal[i] in diccionario2:
            diccionario2[cadenatotal[i]] += 1
        else:
            diccionario2[cadenatotal[i]] = 1

#Ordenar diccionario 1 por valor, es decir las repeticiones, usando el algoritmo burbuja
repeticiones = list(diccionario1.values())
numeros = list(diccionario1.keys())
for i in range(len(repeticiones)):
    for j in range(len(repeticiones)-i-1):
        if repeticiones[j] > repeticiones[j+1]:
            repeticiones[j], repeticiones[j+1] = repeticiones[j+1], repeticiones[j]
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

#Creo el diccionario de nuevo para reubicar los valores
diccionario1 = {}
for i in range(len(numeros)):
    diccionario1[numeros[i]] = repeticiones[i]

#Ordenar el diccionario 2 por claves, es decir las letras y mostrar sus repetciones
letras = list(diccionario2.keys())
repeticiones = list(diccionario2.values())
for i in range(len(letras)):
    for j in range(len(letras)-i-1):
        if letras[j] > letras[j+1]:
            letras[j], letras[j+1] = letras[j+1], letras[j]
            repeticiones[j], repeticiones[j+1] = repeticiones[j+1], repeticiones[j]
            
diccionario2 = {letra: diccionario2[letra] for letra in letras}

print("Diccionario 1 con los numeros y sus repeticiones:")
for numero, repeticiones in diccionario1.items():
    print(f"Numero: {numero} Repeticiones: {repeticiones}")

print("\nDiccionario dos con letras y repeticiones: ")
for letra, repeticiones in diccionario2.items():
    print(f"Letra: {letra} Repeticiones: {repeticiones}")