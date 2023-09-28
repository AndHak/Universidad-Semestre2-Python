lista = [1,2,3,4,5,6,7,8,9]

#En caso de que no se pueda usar el algortimo de ordenamiento es mejor asi, si se necesita empezar del final al principio
copia = lista[::-1] 
#o podemos usar reverse
lista.reverse()
print(copia)
print(lista)

