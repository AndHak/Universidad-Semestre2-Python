#Suponga que hay un candado con 3 ruedas, cada rueda permmite agregar un numero del 0 al 9,
#la combinacion de 3 numeros es la correcta para desbloquear una rueda, pero
#hay que tener en cuenta las demas ruedas, debido a que la combinacion de las
#tres ruedas correctas desbloquea el candado, de ese modo
#hacer un programa que desbloquee el candado por fuerza bruta

numeros = "0123456789"
llave1 = "157"
llave2 = "777"
llave3 = "970"
clave_candado = llave1 + llave2 + llave3

def desbloquear_candado():
    global llave1, llave2, llave3, clave_candado
    desbloqueando = True
    while desbloqueando:
        clave_candado_found = None
        llave1_valid = False
        llave2_valid = False
        llave3_valid = False
        for i in numeros:
            for j in numeros:
                for k in numeros:
                    if i+j+k == llave1:
                        llave1_valid = True
                        llave1_found = i+j+k
                    if i+j+k == llave2:
                        llave2_valid = True
                        llave2_found = i+j+k
                    if i+j+k == llave3:
                        llave3_valid = True
                        llave3_found = i+j+k
        if llave1_valid and llave2_valid and llave3_valid:
            clave_candado_found = llave1_found + llave2_found + llave3_found
            if clave_candado_found == clave_candado:
                print(f"La clave del candado es {clave_candado_found}")
                desbloqueando = False
desbloquear_candado()