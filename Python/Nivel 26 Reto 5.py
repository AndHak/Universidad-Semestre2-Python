#Sumar 
lista = [1,2,3,4,5]

def sumar(lista):
    if not lista:
        suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])
    return suma

print(sumar(lista))

#Inversa
def inversa(lista):
    if not lista:
        return lista
    else:
        inv = [lista[-1]] + inversa(lista[:-1])
    return inv

print(inversa(lista))