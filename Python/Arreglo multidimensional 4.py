#Aqui quiero hacer un una matriz donde me prgunte las dimensiones del alto
#el largo y el ancho, crearla y llenarla con numeros random, despues de eso,
#en la primera capa buscar los primos, en la capa 2 los fibonaccis, y en la capa 3
#buscar los numeros que tienen una raiz, en el caso de que no halla esa capa
#indicar que no existe tal capa por lo que no habra numeros ya sean solo raices debido
#a que debe tener mas de una capa

from colorama import init, Fore
import random
import os

matriz_3d = None
primos_primera_capa = []
fibonaccis_segunda_capa = []
raices_exactas_tercera_capa = []

def crear_matriz():
    #Aqui creamos la matriz con las dimensiones que desee el usuario
    matriz_3d = []
    print("\nCreación de matriz 3D:")
    alto = int(input("Ingrese el número de capas: "))
    largo = int(input("Ingrese el número de filas por capa: "))
    ancho = int(input("Ingrese el número de columnas por capa: "))
    for _ in range(alto):
        capa_actual = []
        for _ in range(largo):
            fila_actual = []
            for _ in range(ancho):
                fila_actual.append(random.randint(1, 20))
            capa_actual.append(fila_actual)
        matriz_3d.append(capa_actual)
    return matriz_3d

def mostrar_matriz(matriz):
    #Esta funcion es para mostrar la matriz 3d de la forma más intuitiva posible
    for i, capa in enumerate(matriz):
        print(f"Capa: {i+1}")
        for fila in capa:
            print(" ".join("{:4}".format(num) for num in fila))
        print()

def es_primo(numero):
    #Forma mas eficiente de calcular un número primo
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    #Esta es la forma mas eficiente de calcular el fibonacci
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def tiene_raiz(numero):
    # Verificamos si el número tiene una raíz cuadrada exacta
    raiz = int(numero ** 0.5)
    return raiz * raiz == numero

def menu():
    #Definimos estos arriglos ya sean 1d, 2d o 3d como global porque estan fiera de la funcion menu y necesitamos operar con ellas
    global matriz_3d, primos_primera_capa, fibonaccis_segunda_capa, raices_exactas_tercera_capa
    while True:
        print("""__________Dashboard__________
              
                1. Crear Matriz 3D
                2. Mostrar Matriz 3D
                3. Mostrar datos de la matriz 3D
                4. Salir""")
        respuesta_dashboard = int(input("\nSeleccione una opción: "))
        if respuesta_dashboard == 1:
            matriz_3d = crear_matriz()
            input("Presione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        if respuesta_dashboard == 2:
            if not matriz_3d:
                #Si no hay matriz mostrar en rojo que primero debe crear la matriz
                print(Fore.RED + "\nDebe crear una matriz 3D antes\n" + Fore.RESET)
            else:
                mostrar_matriz(matriz_3d)
            input("Presione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        if respuesta_dashboard == 3:
            if not matriz_3d:
                #Si no hay matriz mostrar en rojo que primero debe crear la matriz
                print(Fore.RED + "\nDebe crear una matriz 3D antes\n" + Fore.RESET)
            else:
                primos_primera_capa = []
                fibonaccis_segunda_capa = []
                raices_exactas_tercera_capa = []
                #buscamos por capa en matriz, en este caso la primera es 0
                for capa in matriz_3d:
                    if matriz_3d.index(capa) == 0:
                        #ahora identificamos por filas en la capa
                        for fila in capa:
                            #Para proceder a cada numero en la fila
                            for num in fila:
                                #analizar el numero y lo que querramos hacer con el
                                if es_primo(num):
                                    primos_primera_capa.append(num)
                    elif matriz_3d.index(capa) == 1:
                        for fila in capa:
                            for num in fila:
                                if es_fibonacci(num):
                                    fibonaccis_segunda_capa.append(num)
                    elif matriz_3d.index(capa) == 2:
                        for fila in capa:
                            for num in fila:
                                if tiene_raiz(num):
                                    raices_exactas_tercera_capa.append(num)
                print(f"Primos primera capa: {primos_primera_capa}")
                print(f"Fibonaccis segunda capa: {fibonaccis_segunda_capa}")
                print(f"Raices exactas tercera capa: {raices_exactas_tercera_capa}")
            input("Presione Enter para continuar.. ")
            os.system("cls" if os.name == "nt" else "clear")
        if respuesta_dashboard == 4:
            return

init(autoreset=True)
menu()
