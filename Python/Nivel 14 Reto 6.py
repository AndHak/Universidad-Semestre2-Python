#baraja de cartas mas repartir cartas a 4 jugadores

#Crear una baraja de cartas que contenga todas las cartas
import random

numbers = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
type_of_card = ["Corazones", "Diamantes", "Picas", "Treboles"]
cards = []

for i in type_of_card:
    for j in numbers:
        cards.append(f"{j} de {i}")

print(f"\nLas cartas son:\n")
# Imprime las cartas en cuatro columnas (una por cada tipo de carta)
for i in range(len(numbers)):
    for j in range(len(type_of_card)):
        # Calcula el índice en la lista de cartas
        index = i + j * len(numbers)
        # Imprime la carta con un ancho fijo
        print("{:25}".format(cards[index]), end="")
    print()  # Salto de línea al final de cada fila

#Repartir cartas
random.shuffle(cards)

jugadores = [[],[],[],[]]

for i in range(5):
    for j in range(4):
        jugadores[j].append(cards.pop())

#mostrar cartas
for i in range(4):
    print(f"\nJugador {i+1}\n")
    for j in range(5):
        print(f"-{jugadores[i][j]}\n")

# Verificar si quedan cartas antes de intentar imprimir
if cards:
    print(f"\nLas cartas restantes son:\n")
    for i in range(len(numbers)):
        for j in range(len(type_of_card)):
            # Calcula el índice en la lista de cartas
            index = i + j * len(numbers)
            # Imprime la carta con un ancho fijo
            if index < len(cards):
                print("{:25}".format(cards[index]), end="")
        print()  # Salto de línea al final de cada fila
else:
    print("\nNo quedan cartas en la baraja.")
