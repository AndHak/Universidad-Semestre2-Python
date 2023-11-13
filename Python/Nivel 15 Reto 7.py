#Juego del ahorcado

#1. Elegir aleatoriamente una palabra
#2. mostrar el dibujo de una horca
#3. mostrar un guion bajo por cada letra de la palabra
#4. pedir al usuario que introduzca una letra
#5. comprobar si esa letra esta contenida en la palabra
#6. si esta mostrar la horca sin cambios y sustituir el guion por la letra en el lugar que le corresponde
#7. si no esta mostrar el dibujo de la horca al que se añade una parte y mostrar los guiones como la ultima vez
#8. si falla 6 veces esta completo el dibujo del ahorcado se indica que perdio y muestra la palabra
#9. si acierta se muestra que gano

import random
import os

palabras = ["ANDRES", "LAURA", "AMOR", "COMUNIDAD", "RESPONSABILIDAD", "SUPRA", "BORUSSIA", "ARMARIO", "TELEVISOR", "CONCIERTO", "CANTANTE", "CELULAR", "COMPUTADOR"]

palabra = random.choice(palabras)

fallo0 = """
            -----------------------------
                         |              -
                                        -
                                        -
                                        -
                                        -
                                        -
            -----------------------------                                        
"""

fallo1 = """
            -----------------------------
                         |              -
                         O              -
                                        -
                                        -
                                        -
                                        -
            -----------------------------                                        
"""

fallo2 = """
            -----------------------------
                         |              -
                         O              -
                         |              -
                                        -
                                        -
                                        -
            -----------------------------                                        
"""

fallo3 = """
            -----------------------------
                         |              -
                         O              -
                         |\             -
                                        -
                                        -
                                        -
            -----------------------------                                        
"""

fallo4 = """
            -----------------------------
                         |              -
                         O              -
                        /|\             -
                                        -
                                        -
                                        -
            -----------------------------                                        
"""

fallo5 = """
            -----------------------------
                         |              -
                         O              -
                        /|\             -
                          \             -
                                        -
                                        -
            -----------------------------                                        
"""

fallo6 = """
            -----------------------------
                         |              -
                         O              -
                        /|\             -
                        / \             -
                                        -
                                        -
            -----------------------------                                        
"""

letras_correctas = ""
letras_totales = ""
fallos = 0

while True:

    os.system("cls")

    print("\n\njuego del ahorcado\n\n")

    if fallos == 0:
        print(fallo0)
    if fallos == 1:
        print(fallo1)
    if fallos == 2:
        print(fallo2)
    if fallos == 3:
        print(fallo3)
    if fallos == 4:
        print(fallo4)
    if fallos == 5:
        print(fallo5)
    if fallos == 6:
        print(fallo6)

    resultado = ""

    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"

    print("     {}".format(resultado))
    print()

    if resultado == palabra:
        print("\n\nHas ganado, felicitaciones\n\n")
        break
    
    if fallos > 5:
        print(f"\n\nLa palabra era: {palabra}\nHas perdido\n")
        break

    while True:
        letra_usuario = input("Introduce una letra:  ")
        letra = letra_usuario.upper()
        if len(letra) > 1 or len(letra) < 1:
            print("introduce una letra")
        elif letra in letras_totales:
            print("Esa letra ya la has dicho")
        elif not letra.isalpha():
            print("Introduce una letra")
        else:
            letras_totales += letra
            break

    if letra not in palabra:
        fallos += 1
    else:
        letras_correctas += letra

    