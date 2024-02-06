#Aplanar lista recursivamente

datos = [[1,2],[[3,4],[[[5,6],[[7,8],[9,10]]],11]],12]


def aplanar(lista):
    plana = []
    
    for elemento in lista:
        if type(elemento) == int:
            plana.append(elemento)
        else:
            plana.extend(aplanar(elemento))
    return plana

print(aplanar(datos))


