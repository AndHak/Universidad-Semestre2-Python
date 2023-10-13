#Se tiene una cadena, donde hay caracteres numericos y alfabeticos
#formar dos diccionarios asi: diccionario 1 clave digito valor las veces que se repite
#diccionario dos clave letra y valor las veces que aparece
vector = "universidad de nariño, ingenieria de sistmas semestre 2, ejercicio 7 fecha 12 de 10 del 2023"
diccionario1 = {}
diccionario2 = {}
for caracter in vector:
    if caracter.isnumeric():  
        if caracter in diccionario1:
            diccionario1[caracter] += 1
        else:
            diccionario1[caracter] = 1
    elif caracter.isalpha():
        caracter = caracter.lower()  
        if caracter in diccionario2:
            diccionario2[caracter] += 1
        else:
            diccionario2[caracter] = 1
print(f"Cadena de letras:\n{vector}\n")
print("Diccionario 1 (dígitos y repeticiones):")
for clave, valor in diccionario1.items():
    print(f"Numero: {clave}, Repeticiones: {valor}")
print("\nDiccionario 2 (letras y repeticiones):")
for clave, valor in diccionario2.items():
    print(f"Letra: {clave}, Repeticiones: {valor}")
