#Identificar si una cadena o palabra es un palindromo, es decir si se lee igual de atras hacia delante

cadena1 = "Hola"
cadena2 = "a luna ese anula"
cadena3 = "somos"

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    reverso = cadena[::-1]
    return cadena == reverso

if es_palindromo(cadena1):
    print(f"La cadena: '{cadena1}' es un palíndromo")
else:
    print(f"La cadena: '{cadena1}' no es un palíndromo")

if es_palindromo(cadena2):
    print(f"La cadena: '{cadena2}' es un palíndromo")
else:
    print(f"La cadena: '{cadena2}' no es un palíndromo")

if es_palindromo(cadena3):
    print(f"La cadena: '{cadena3}' es un palíndromo")
else:
    print(f"La cadena: '{cadena3}' no es un palíndromo")
