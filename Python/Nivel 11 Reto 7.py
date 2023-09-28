#Copiando una lista

letras = list()
letras.append("a")
#Esta es una copia de la lista con una id diferente
copia_letras = list(letras)
copia_letras.append("b")
#Esta no recibe las modificaciones que se hacen en la copia
print(letras)
#La copia mostrará los cambios sin afectar a la lista original
print(copia_letras)