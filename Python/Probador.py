from colorama import init, Fore # Una libreria para cambiar los colores de la consola donde se ejecuta el codigo 
import os # Una libreria que nos permitira limpiar pantalla y los comando disponibles en una terminal de windows
import random # Una libreria para usar numeros aleatorios en donde se necesite llenar datos

# Vamos a definir unas funciones que serán las más usadas en la mayoria de los puntos para llamarlas

# Un Separador para dar más orden
def separador():
    print("\n-----------------------------------------------------------------------------------------\n")

# Función para determinar primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

# Función para determinar si es fibonacci
def es_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

# Función para determinar si es perfecto
def es_perfecto(numero):
    if numero <= 1:
        return False
    suma_divisores = 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            suma_divisores += i
            if i != numero // i:
                suma_divisores += numero // i
    return suma_divisores == numero

# Función para hacer una matriz
def hacer_matriz(dimensiones):
    matriz = []
    for _ in range(dimensiones):
        fila_actual = []
        for _ in range(dimensiones):
            fila_actual.append(random.randint(1, 50))
        matriz.append(fila_actual)
    return matriz

# Función para calcular el factorial
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

# Función para saber si es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

# Función para saber si es impar
def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

# Funciónn para saber si es multiplo de 5
def es_multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    return False

# Limpiar pantalla
def limpiar():
    input("Presione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")















def evaluacion_1_punto_3(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 1 - Punto 3:\n\n")
    stdscr.addstr("""3.	Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Formar dos conjuntos asi:
Conjunto 1 con los número pares de la lista valor de aquellas claves que son primos 
Conjunto 2 con los número pares de la lista valor de aquella claves que son fibonacci
Con estos dos conjuntos formar dos cadenas
Cadena1 con los pares comunes
Cadena2 con la unión de los pares sin elementos comunes\n\n""")
    
    diccionario = diccionario()

    conjunto1 = set()
    conjunto2 = set()
    claves_primos = [clave for clave in diccionario if es_primo(clave)]
    claves_fibonacci = [clave for clave in diccionario if es_fibonacci(clave)]

    for clave, valores in diccionario.items():
        if es_primo(clave):
            for valor in valores:
                if valor % 2 == 0:
                    conjunto1.add(valor)
        if es_fibonacci(clave):
            for valor in valores:
                if valor % 2 == 0:
                    conjunto2.add(valor)

    pares_comunes = conjunto1.intersection(conjunto2)
    union_pares = conjunto1.union(conjunto2)

    cadena1 = pares_comunes
    cadena2 = union_pares

    stdscr.addstr(f"\n\nDiccionario generado aleatoriamente: {diccionario}\n")

    stdscr.addstr(f"\nConjunto 1 (Pares en claves primos {claves_primos}):\n")
    stdscr.addstr(', '.join(map(str, conjunto1)))

    stdscr.addstr(f"\nConjunto 2 (Pares en claves Fibonacci {claves_fibonacci}):\n")
    stdscr.addstr(', '.join(map(str, conjunto2)))

    stdscr.addstr("\nCadena 1 (pares comunes):\n")
    stdscr.addstr(cadena1)

    stdscr.addstr("\nCadena 2 (unión de pares):\n")
    stdscr.addstr(cadena2)

    stdscr.refresh()
    stdscr.getch()
evaluacion_1_punto_3()