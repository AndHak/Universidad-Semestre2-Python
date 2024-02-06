from Persona import Persona
from Zombie import Zombie
import os

os.system("cls")

print("""
      La ciudad se ha llenado de zombies
      Llega a la calle 40 para salvarte

      los zombies avanzan de 1 a 3 calles
      y tu igual, no te topes con uno
""")

numero = None
while numero not in (1,2,3,4):
    numero = int(input("Numero de jugadores (1/4): "))
    
jugadores = []
for i in range(1, numero+1):
    nombre = input(f"Nombre del {i}° jugador").capitalize()
    jugador = Persona(nombre)
    jugadores.append(jugador)


zombies = []
for i in range(10):
    z = Zombie()
    zombies.append(z)

while len(jugadores) > 0:
    os.system("cls")
    
    print("Nombre   -   Calle   -   Energia")
    print("--------------------------------")
    for jugador in jugadores:
        nombre, calle, energia = jugador.situacion()
        print(f"{nombre:8}   -   {calle:2}   -   {energia:2}")
    print()

    calles = []
    for zombie in zombies:
        calles.append(zombie.calle)
    calles.sort()
    print("Hay zombies en las calles:")
    for elemento in calles:
        print(elemento, end=" ")
    print()
    print()

    ganadores = []
    for jugador in jugadores:
        if jugador.calle >= 40:
            ganadores.append(jugador)

    if len(ganadores) > 0:
        for jugador in ganadores:
            print(f"{jugador.nombre} ha logrado llegar a la base")
        print("Has ganado el juego")
        print()
        break

    if jugador.calle > 40:
        print("Has coneguido llegar a la base")
        print("Felicidades ganaste el juego")
        break

    for jugador in list(jugadores):
        if jugador.energy <= 0:
            print(f"{jugador.nombre} ha perdido su energia")
            jugadores.remove(jugador)

    for jugador in list(jugadores):
        for zombie in zombies:
            if zombie.calle == jugador.calle:
                if jugador in jugadores:
                    print(f"{jugador.nombre}, un zombi te ha vista, Has muerto")
                    jugadores.remove(jugador)


    for jugador in jugadores:
        velocidad = None
        while velocidad not in (1,2,3):
            velocidad = int(input(f"{jugador.nombre}, Cuanto quieres avanzar(1/2/3): "))
        jugador.moverse(velocidad)

    for zombie in list(zombies):
        zombie.moverse()
        if zombie.no_visible():
            zombies.remove(zombie)
    
else:
    print("Todos han sido comidos, Game Over")


