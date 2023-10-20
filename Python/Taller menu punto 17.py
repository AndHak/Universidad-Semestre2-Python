#17.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
#Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
#Diccionario 2 con clave carácter y valor las veces que se repite, ordenarlo ascendentemente por clave 

cadena1 = "Hola Mundo 2023"
cadena2 = "Universidad de Nariño semestre 2"
cadena3 = "Numero de estudiantes aproximadamente 35000"
cadenatotal = cadena1 + cadena2 + cadena3

diccionario1 = {}
diccionario2 = {}

for caracter in cadenatotal:
    if caracter.isnumeric():
        if caracter in diccionario1:
            diccionario1[caracter] += 1
        else:
            diccionario1[caracter] = 1
    if caracter.isalpha():
        caracter = caracter.lower()
        if caracter in diccionario2:
            diccionario2[caracter] += 1
        else:
            diccionario2[caracter] = 1

# Ordenar diccionario1 por valor (repeticiones) usando el algoritmo de burbuja
valores = list(diccionario1.values())
claves = list(diccionario1.keys())
for i in range(len(valores)):
    for j in range(len(valores) - i - 1):
        if valores[j] > valores[j + 1]:
            valores[j], valores[j + 1] = valores[j + 1], valores[j]
            claves[j], claves[j + 1] = claves[j + 1], claves[j]

# Reorganizar diccionario1 con claves y valores ordenados
diccionario1 = {}
for i in range(len(claves)):
    diccionario1[claves[i]] = valores[i]

# Ordenar diccionario2 por clave usando el algoritmo de burbuja
claves2 = list(diccionario2.keys())
for i in range(len(claves2)):
    for j in range(len(claves2) -i -1):
        if claves2[j] > claves2[j + 1]:
            claves2[j], claves2[j + 1] = claves2[j + 1], claves2[j]

# Crear un nuevo diccionario2 ordenado por clave
diccionario2_ordenado = {k: diccionario2[k] for k in claves2}

print("Repeticiones de números")
for numero, repeticiones in diccionario1.items():
    print(f"Número: {numero}  Repeticiones: {repeticiones}")

print("Repeticiones de Letras")
for letra, repeticiones in diccionario2_ordenado.items():
    print(f"Letra: {letra}  Repeticiones: {repeticiones}")
