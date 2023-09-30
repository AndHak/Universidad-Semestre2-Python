#En una loteria hay un bombo que tiene 10 bolas, con los números del 1 al 10
#En un sorteo se sacan 5 bolas, sin que se introduzcan las bolas que se han sacado previamente
#Has un programa que muestre todas las apuestas posibles, es decir
#Todas las combinaciones posibles que se pueden dar en esta loteria
#Incluye un contador para saber el numero de combinaciones que se dan

import random

bolas = [1,2,3,4,5,6,7,8,9,10]
combinaciones = []
for b1 in bolas:
    for b2 in bolas:
        for b3 in bolas:
            for b4 in bolas:
                for b5 in bolas:
                    if b1 != b2 and b1 != b3 and b1 != b4 and b1 != b5 and \
                        b2 != b3 and b2 != b4 and b2 != b5 and \
                        b3 != b4 and b3 != b5 and b4 != b5:
                        combinacion_posible = [b1,b2,b3,b4,b5]
                        combinacion_posible.sort()
                        if combinacion_posible not in combinaciones:
                            combinaciones.append(combinacion_posible)
print(f"Combinaciones posibles: {len(combinaciones)}")
