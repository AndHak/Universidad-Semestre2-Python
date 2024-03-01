datos = ["Sara", "marta", "daniel", "Andres", "felipe"]

nombres = list(map(lambda x: x[:-1].lower() + x[-1].upper(), datos))

print(nombres)

nombres = [x[:-1].lower() +  x[-1].upper() for x in datos]

print(nombres)

#-------------numeros--------#

primera = [7, 9, 6, 8, 5]
segunda = [3, 2, 1, 5, 4]

totales = [x-y for x,y in zip(primera, segunda)]

print(totales)

totales = list(map(lambda x,y: x-y, primera, segunda))

print(totales)

#------uso interesante-------------#

metales = [("Hierro", 415, 12), ("Cobre", 158, 32), ("Zinc", 243, 21)]

metales2 = list(map(lambda x: {"Nombre": x[0], "Peso": x[1], "Precio": x[2]}, metales))

for elemento in metales2:
    print(elemento)

metales2 = [{"Nombre": x[0], "Peso": x[1], "Precio": x[2]} for x in metales]

for elemento in metales2:
    print(elemento)
