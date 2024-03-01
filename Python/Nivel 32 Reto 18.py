datos = [3, 4, 5, 6, 7]

dobles = list(map(lambda x: x*2, datos))

print(dobles)

dobles = [x*2 for x in datos]

print(dobles)

#--------------------------------------#

def cels_fahr(c):
    return round((c * 1.8) + 32)

temp_cels = [17, 21, 22, 18, 19, 25]

temp_fahr = list(map(cels_fahr, temp_cels))

print("Temperatura")
print(temp_fahr)

temp_fahr = list(map(lambda x: round((x * 1.8) + 32), temp_cels))
print(temp_fahr)

#-------------------------STR - INT---------------#

print("Str a int")

cadenas = ["1", "2", "3", "4", "5"]

numeros = list(map(int, cadenas))

print(numeros)

numeros = [int(x) for x in cadenas]

print(numeros)

#------------------------Modificar cadena------------#

print("Cadenas modificadas")

datos = ["Sara", "marta", "daniel", "Andres", "felipe"]

nombres = [x.capitalize() for x in datos]

print(nombres)

nombres = list(map(lambda x: x.capitalize(), datos))

print(nombres)

nombres = list(map(str.capitalize, datos))

print(nombres)
