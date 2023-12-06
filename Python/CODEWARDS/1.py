

def digital_root(n):
    contador = len(str(n))
    operar = str(n)
    while contador >= 1:
        resultado = 0
        for n in operar:
            resultado += int(n)
        operar = str(resultado)
        contador -= 1
    return resultado

print(digital_root(942))

