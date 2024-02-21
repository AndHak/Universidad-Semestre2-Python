datos = [(4,2,1), (5,4,2), (2,1,3), (3,0,1), (3,4,2)]

def suma_tupla(datos):
    return datos[0] + datos[1] + datos[2]

print(sorted(datos, key=suma_tupla))

def reverso(tupla):
    return (tupla[2], tupla[1], tupla[0])

ordenada = sorted(datos, key=reverso)
print(ordenada)

