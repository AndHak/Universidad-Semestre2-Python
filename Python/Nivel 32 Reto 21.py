metales = {
    "Hierro": "2",
    "Plata": "23",
    "Zinc": "7",
    "Cobre": "11",
    "Aluminio": "4",
    "Plomo": "15",
    "Oro": "30"
}

lista1 = [clave for clave, valor in metales.items() if int(valor) >= 10]

print(lista1)

lista2 = [clave for clave, valor in metales.items() if int(valor) >= 10 if "e" in clave]

print(lista2)

lista1 = list(filter(lambda x: int(metales[x]) >= 10, metales))

print(lista1)

lista2 = list(filter(lambda x: int(metales[x]) >= 10, filter(lambda x: "e" in x, metales)))

print(lista2)

lista2 = list(filter(lambda x: int(metales[x]) >= 10 and "e" in x, metales))

print(lista2)

