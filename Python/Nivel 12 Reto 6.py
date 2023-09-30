#Para un juego que va a tener 20.000 planetas, necesitamos formar nombres para cada uno de ellos
#Crear una lista con todos los nombres de tres silabas que se puedan formar
#Con 10 consonantes y 5 vocales de tal forma que se intercambien consonante y vocal
#Y no se repita ninguna letra en cada nombre.
#Mostrar la cantidad de nombres de la lista y mostrar 10 al azar

import random

consonats = "bcdfghjklmnpqrstvwxyz"
vocals = "aeiou"
planet_names = []

for c1 in consonats:
    for v1 in vocals:
        for c2 in consonats:
            for v2 in vocals:
                for c3 in consonats:
                    for v3 in vocals:
                        if c1 != c2 and c2 != c3 and c3 != c1 \
                        and v1 != v2 and v2 != v3 and v3 != v1:
                            name = c1 + v1 + c2 + v2 + c3 + v3
                            planet_names.append(name)

#Mostrar 10 al azar

for i in range(1,11):
    planet_name = random.choice(planet_names)
    print(f"Nombre planeta:  {planet_name}")