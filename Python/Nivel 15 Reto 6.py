#Muertos y heridos juego de adivinar el numero por digitos

import random
import os

digitos = "0123456789"
numero = ""
muertos = 0
heridos = 0
intento = None
intentos = []
salir = False

os.system("cls")

print("""
        Juego muertos y heridos
          Tienes 10 intentos
      
        Pulsa enter para empezar
         """)

input()

while len(numero) < 4:
    digito = random.choice(digitos)
    if digito not in numero:
        numero += digito


while True:

    os.system("cls")

    print("""}
---------------------------------------------------
                 Muertos y Heridos
---------------------------------------------------
          
        numero          -           M   -   H      
       --------         -          -----------""")
    
    for i in range(len(intentos)):
        plantilla = "         {}           -           {}   -   {}"
        print(plantilla.format(intentos[i][0], intentos[i][1], intentos[i][2]))
        print()

    if numero == intento:
        print("Has ganado")
        print(f"Has necesitado {len(intentos)} intentos")
        break

    if len(intentos) >= 15:
        print("Has agotado los intentos, Has perdido")
        print(f"El numero era: {numero}")

    while True:
        intento = input("introduce un numero: ('q' para salir): ")
        if intento == "q":
            salir = True
            break

        elif len(intento) < 4 or len(intento) > 4:
            print("Intrduce un numero de 4 digitos")
        elif intento[0] not in digitos or intento[1] not in digitos or \
            intento[2] not in digitos or intento[3] not in digitos:
            print("Introduce un numero del 0 al 9")
        elif intento[0] == intento[1] or intento[0] == intento[2] or intento[0] == intento[3] \
            or intento[1] == intento[2] or intento[1] == intento[3] \
            or intento[2] == intento[3]:
            print("No se puede repetir numeros")
        else:
            break

    if salir:
        print(f"El numero era: {numero}")
        break

    for i in range(4):
        if intento[i] in numero:
            if intento[i] == numero[i]:
                muertos += 1
            else:
                heridos += 1

    intentos.append([intento, muertos, heridos])

    muertos = 0
    heridos = 0

