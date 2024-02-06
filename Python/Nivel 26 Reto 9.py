#Mostrar lista recursion

lista = [3,5,7,9,11]

def mostrar(lista, indice=0):
    if indice != len(lista):
        print(lista[indice])
        mostrar(lista, indice+1)

mostrar(lista)

#Forma descendente
def descendente(n):
    if not n:
        return[0]
    else:
        return [n] + descendente(n-1)
    
print(descendente(10))