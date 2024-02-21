letras = ["A","E","I","a","e","i"]

letras.sort(key=str.lower)

print(letras)

letras = ["Ec","ar","ij","Iw","An","es"]

letras.sort(key=lambda cadena: cadena.lower())

print(letras)