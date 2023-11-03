import curses # Una libretia que nos permite hacer un menor menu
import random # Una libreria para usar numeros aleatorios en donde se necesite llenar datos
import time # Libreria de tiempo

#---------------------------------------------------------------------------------------------------------------#
# Desarrollado por: Andrés Feipe Martínez Guerra   |   cod: 223034091    |   Universidad de Nariños 2° Semestre #
#---------------------------------------------------------------------------------------------------------------#

#--------------------------------------------- A T E N C I O N ---------------------------------------------------#
# Los calculos se hicieron con random, puede que no siempre se cumplan los requisitos para mostrar los resultados #
#------------------ si algun programa no funciona ejecutelo de nuevo hasta que funcione --------------------------#

#---------------------------------------------------------------------------------------------------------------#
# Funciones rapidas como identificar primo, fibonacci, par, impar, factorial, hacer matriz, mostrar matriz, etc #
#---------------------------------------------------------------------------------------------------------------#

# Un Separador para dar más orden
def separador(stdscr):
    stdscr.addstr("-----------------------------------------------------------------------------------------")

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

# Función para saber si es multiplo de 5
def es_multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    return False

# Función para mostrar matriz
def mostrar_matriz(stdscr, matriz):
    for fila in matriz:
        stdscr.addstr("  [")
        stdscr.addstr(" ".join("{:5}".format(n) for n in fila))
        stdscr.addstr("   ]  ")

# Primos de las diagonales
def primos_diagonal_principal(matriz):
    primos = []
    for i in range(len(matriz)):
        if es_primo(matriz[i][i]):
            primos.append(matriz[i][i])
    return primos
def primos_diagonal_secundaria(matriz):
    primos = []
    for i in range(len(matriz)):
        if es_primo(matriz[i][-i-1]):
            primos.append(matriz[i][-i-1])
    return primos

#Funciones para diccionarios varias
def generar_diccionario_aleatorio():
    diccionario = {}
    for _ in range(4):
        clave = random.randint(1, 20)
        valores = [random.randint(1, 20) for _ in range(random.randint(3, 5))]
        diccionario[clave] = valores
    return diccionario
def encontrar_mayor_primo_en_diccionario(diccionario):
    mayor_primo = None
    clave_mayor_primo = None
    for clave, valores in diccionario.items():
        for valor in valores:
            if es_primo(valor):
                if mayor_primo is None or valor > mayor_primo:
                    mayor_primo = valor
                    clave_mayor_primo = clave
    return mayor_primo, clave_mayor_primo
def encontrar_menor_fibonacci_en_diccionario(diccionario):
    menor_fibonacci = None
    clave_menor_fibonacci = None
    for clave, valores in diccionario.items():
        for valor in valores:
            if es_fibonacci(valor):
                if menor_fibonacci is None or valor < menor_fibonacci:
                    menor_fibonacci = valor
                    clave_menor_fibonacci = clave
    return menor_fibonacci, clave_menor_fibonacci
def encontrar_numeros_pares_entre_claves(clave1, clave2):
    numeros_pares = []
    min_clave, max_clave = min(clave1, clave2), max(clave1, clave2)
    for i in range(min_clave+1, max_clave):
        if i % 2 == 0:
            numeros_pares.append(i)
    return numeros_pares
def formar_cadenas_con_pares_comunes(diccionario):
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

    cadena1 = ', '.join(map(str, pares_comunes))
    cadena2 = ', '.join(map(str, union_pares))




#---------------------------------------------------------------------------------------------------------------#
# Ejercicios del taller 1 en funciones para hacer un menu corto y llamar a las funciones en un menu mas general #
#---------------------------------------------------------------------------------------------------------------#

def ejercicio_taller_1_1(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 1 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos,
determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada,
es un numero Fibonacci, si no lo es determinar si es primo y su factorial.\n\n""")
    
    stdscr.addstr("Ejercicio no comprensible")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_2(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 2 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos, en el primer vector hay números múltiplos de tres que determinan la cantidad
de datos de cada rango correspondientes al vector dos, formar tres listas con el mayor, el menor y el promedio de cada rango.\n\n""")
    
    stdscr.addstr("Ejercicio no comprensible")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_3(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 3 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")

    vector1 = [random.randint(1, 50) for n in range(20)]
    vector2 = [random.randint(1, 50) for n in range(20)]
    primos_comunes = []

    for n in vector1:
        if es_primo(n):
            if n in vector2 and n not in primos_comunes:
                primos_comunes.append(n)
    for n in vector2:
        if es_primo(n):
            if n in vector1 and n not in primos_comunes:
                primos_comunes.append(n)

    stdscr.addstr(f"Vector 1:\n{vector1}\n")
    stdscr.addstr(f"Vector 2:\n{vector2}\n")
    stdscr.addstr(f"Primos comunes:\n{primos_comunes}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_4(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 4 - Taller 1:\n\n")
    stdscr.addstr("Se tienen un vector con datos numéricos donde hay varios números Fibonacci, formar un tercer vector\n")
    stdscr.addstr("con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.\n\n")

    vector = [random.randint(1, 50) for n in range(50)]

    fibonacci_mayor = 0
    posicion_fibonacci_mayor = None
    fibonacci_menor = float("inf")
    posicion_fibonacci_menor = None

    for posicion, numero in enumerate(vector):
        if es_fibonacci(numero):
            if numero > fibonacci_mayor:
                fibonacci_mayor = numero
                posicion_fibonacci_mayor = posicion
            if numero < fibonacci_menor:
                fibonacci_menor = numero
                posicion_fibonacci_menor = posicion

    primos_en_el_rango = []

    for n in range(posicion_fibonacci_mayor + 1, posicion_fibonacci_menor):
        if es_primo(n):
            primos_en_el_rango.append(n)

    stdscr.addstr(f"Vector original:\n{vector}\n")
    stdscr.addstr(f"Los primos entre el Fibonacci mayor: {fibonacci_mayor} y el Fibonacci menor: {fibonacci_menor} son:\n")
    stdscr.addstr(f"{primos_en_el_rango}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_5(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 5 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos,
determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo
al orden de entrada, es un numero Fibonacci, si no lo es determinar si es primo y su factorial.\n\n""")
    
    stdscr.addstr("Ejercicio: Verificar si la suma de perímetros es un número Fibonacci, primo o su factorial\n")
    
    num_ternas = 3  # Cantidad de ternas (puedes ajustarla)

    suma_perimetros = 0

    for i in range(num_ternas):
        # Generar lados aleatorios de un triángulo
        lado1 = random.randint(1, 10)
        lado2 = random.randint(1, 10)
        lado3 = random.randint(1, 10)

        # Calcular el perímetro del triángulo
        perimetro = lado1 + lado2 + lado3
        suma_perimetros += perimetro

    stdscr.addstr(f"Suma de perímetros: {suma_perimetros}\n")

    if es_fibonacci(suma_perimetros):
        stdscr.addstr("La suma de perímetros es un número Fibonacci.\n")
    else:
        if es_primo(suma_perimetros):
            stdscr.addstr("La suma de perímetros no es un número Fibonacci, pero es un número primo.\n")
            factorial = calcular_factorial(suma_perimetros)
            stdscr.addstr(f"Factorial de {suma_perimetros}: {factorial}\n")
        else:
            stdscr.addstr("La suma de perímetros no es un número Fibonacci ni un número primo.\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_6(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 6 - Taller 1:\n\n")
    stdscr.addstr("Se tienen dos vectores con datos numéricos donde hay varios repetidos, formar un tercer vector\n")
    stdscr.addstr("con la unión de solo números Fibonacci sin repetidos, sin tener en cuenta aquellos Fibonacci que sean comunes.\n\n")

    vector1 = [random.randint(1, 50) for n in range(20)]
    vector2 = [random.randint(1, 50) for n in range(20)]
    vector3 = []

    for n in vector1:
        if es_fibonacci(n) and n not in vector2 and n not in vector3:
            vector3.append(n)
    for n in vector2:
        if es_fibonacci(n) and n not in vector1 and n not in vector3:
            vector3.append(n)

    stdscr.addstr(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\nVector 3:\n{vector3}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_7(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 7 - Taller 1:\n\n")
    stdscr.addstr("Se tienen un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.\n\n")

    vector = [random.randint(1, 20) for n in range(20)]

    primo_mas_repetido = 0
    primo_mas_repetido_repeticiones = 0
    primo_menos_repetido = 0
    primo_menos_repetido_repeticiones = float("inf")
    repeticiones = []
    primos = []

    for n in vector:
        if es_primo(n):
            if n in primos:
                repeticiones[primos.index(n)] += 1
            else:
                primos.append(n)
                repeticiones.append(1)

    for i in range(len(primos)):
        if repeticiones[i] > primo_mas_repetido_repeticiones:
            primo_mas_repetido_repeticiones = repeticiones[i]
            primo_mas_repetido = primos[i]
        if repeticiones[i] < primo_menos_repetido_repeticiones:
            primo_menos_repetido_repeticiones = repeticiones[i]
            primo_menos_repetido = primos[i]

    condicion = 1
    suma = 0
    while condicion <= primo_mas_repetido:
        suma += primo_menos_repetido
        condicion += 1

    stdscr.addstr(f"Vector original:\n")
    stdscr.addstr(" ".join(map(str, vector)) + "\n")
    stdscr.addstr(f"La multiplicación con sumas del primo mas repetido: {primo_mas_repetido} con {primo_mas_repetido_repeticiones} repeticiones\npor el primo menos repetido: {primo_menos_repetido} con {primo_menos_repetido_repeticiones} repeticiones\nEs igual a: {suma}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_8(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 8 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos donde hay varios repetidos,
formar un tercer vector con la unión de solo números Fibonacci sin repetidos,
sin tener en cuenta aquellos Fibonacci que sean comunes.\n\n""")
    
    vector1 = [random.randint(1,10) for n in range(10)]
    vector2 = [random.randint(1,10) for n in range(10)]
    vector3 = []

    for n in vector1:
        if es_fibonacci(n) and n not in vector2 and n not in vector3:
            vector3.append(n)
    for n in vector2:
        if es_fibonacci(n) and n not in vector1 and n not in vector3:
            vector3.append(n)

    stdscr.addstr(f"\nVector 1: {vector1}\nVector 2: {vector2}\nFibonaccis no comunes: {vector3}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_9(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 9 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen un vector con datos numéricos donde hay varios repetidos,
hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.\n\n""")
    
    vector = [random.randint(1,10) for n in range(10)]
    primos = []
    repeticiones = []

    for n in vector:
        if es_primo(n):
            if n in primos:
                repeticiones[primos.index(n)] += 1
            else:
                primos.append(n)
                repeticiones.append(1)
    
    primo_mas_repetido_repeticiones, primo_menos_repetido_repeticiones = 0, float("inf")
    primo_mas_repetido, primo_menos_repetido = 0, 0

    for i in range(len(primos)):
        if repeticiones[i] > primo_mas_repetido_repeticiones:
            primo_mas_repetido_repeticiones = repeticiones[i]
            primo_mas_repetido = primos[i]
        if repeticiones[i] < primo_menos_repetido_repeticiones:
            primo_menos_repetido_repeticiones = repeticiones[i]
            primo_menos_repetido = primos[i]

    condicion = 1
    producto = 0
    while condicion <= primo_mas_repetido:
        producto += primo_menos_repetido
        condicion += 1

    stdscr.addstr(f"\nVector: {vector}\nLa multiplicacion del primo mas repetido: {primo_mas_repetido}\n   Con el primo menos repetido: {primo_menos_repetido}\n\n es: {producto}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_10(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 10 - Taller 1:\n\n")
    stdscr.addstr("""Intercambiar las columnas donde se encuentre el Fibonacci 2 con la fila 
donde se encuentra el Fibonacci 4 según el recorrido por filas de la matriz.\n\n""")

    # Crear una matriz aleatoria de 5x5
    matriz = [[random.randint(1, 35) for _ in range(5)] for _ in range(5)]
    stdscr.addstr("Matriz original:\n")
    mostrar_matriz(stdscr, matriz)

    contador = 0
    segundo, cuarto = None, None
    posicion_segundo, posicion_cuarto = None, None

    # Encontrar el segundo y cuarto número de Fibonacci y sus posiciones
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if es_fibonacci(matriz[i][j]):
                contador += 1
                if contador == 2:
                    segundo = matriz[i][j]
                    posicion_segundo = j
                if contador == 4:
                    cuarto = matriz[i][j]
                    posicion_cuarto = j

    stdscr.addstr(f"\nSegundo Fibonacci: {segundo} Posición: {posicion_segundo}\n")
    stdscr.addstr(f"Cuarto Fibonacci: {cuarto} Posición: {posicion_cuarto}\n")

    # Intercambiar las columnas
    for i in range(len(matriz)):
        matriz[i][posicion_segundo], matriz[i][posicion_cuarto] = matriz[i][posicion_cuarto], matriz[i][posicion_segundo]

    stdscr.addstr("\nMatriz modificada:\n")
    mostrar_matriz(stdscr, matriz)

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_11(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 11 - Taller 1:\n\n")
    stdscr.addstr("""Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz,
son consecutivos, es decir, no hay un número primo entre los dos\n\n""")

    matriz = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

    stdscr.addstr("Matriz original:\n")
    mostrar_matriz(stdscr, matriz)

    segundo_primo = None
    cuarto_primo = None
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if es_primo(matriz[i][j]):
                contador += 1
                if contador == 2:
                    segundo_primo = matriz[i][j]
                if contador == 4:
                    cuarto_primo = matriz[i][j]

    stdscr.addstr("\nSegundo primo: {}\n".format(segundo_primo))
    stdscr.addstr("Cuarto primo: {}\n".format(cuarto_primo))

    if segundo_primo < cuarto_primo:
        es_consecutivo = True
        condicion = segundo_primo + 1
        while condicion < cuarto_primo:
            contador = 1
            divisores = 0
            while contador <= condicion:
                if condicion % contador == 0:
                    divisores += 1
                contador += 1
            if divisores == 2:
                stdscr.addstr("El segundo primo y el cuarto primo NO son consecutivos\n")
                es_consecutivo = False
                break
            condicion += 1
        if es_consecutivo:
            stdscr.addstr("El segundo primo y el cuarto primo SI son consecutivos\n")
    else:
        stdscr.addstr("El segundo primo y el cuarto primo NO son consecutivos\n")

    stdscr.addstr("\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_12(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 12 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen dos matrices cuadradas con datos numéricos formar dos conjuntos, conjunto uno
con los primos de las diagonales principales, conjunto 2 con los primos de las diagonales secundarias,
con estos dos conjuntos, encontrar los elementos comunes y formar un diccionario
con cada uno de estos valores como clave y su factorial como valor\n\n""")

    matriz1 = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
    matriz2 = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

    def primos_diagonal_principal(matriz):
        primos = []
        for i in range(len(matriz)):
            if es_primo(matriz[i][i]):
                primos.append(matriz[i][i])
        return primos

    def primos_diagonal_secundaria(matriz):
        primos = []
        for i in range(len(matriz)):
            if es_primo(matriz[i][-i-1]):
                primos.append(matriz[i][-i-1])
        return primos

    conjunto1 = primos_diagonal_principal(matriz1) + primos_diagonal_principal(matriz2)
    conjunto2 = primos_diagonal_secundaria(matriz1) + primos_diagonal_secundaria(matriz2)

    stdscr.addstr("Matriz 1:\n")
    mostrar_matriz(stdscr, matriz1)

    stdscr.addstr("\nMatriz 2:\n")
    mostrar_matriz(stdscr, matriz2)

    stdscr.addstr("\nPrimos diagonales principales: " + str(conjunto1) + "\n")
    stdscr.addstr("Primos diagonales secundarias: " + str(conjunto2) + "\n")

    diccionario = {}
    elementos_comunes = []

    for n in conjunto2:
        if n in conjunto1 and n not in elementos_comunes:
            elementos_comunes.append(n)
    for n in conjunto1:
        if n in conjunto2 and n not in elementos_comunes:
            elementos_comunes.append(n)
    for n in elementos_comunes:
        factorial = calcular_factorial(n)
        diccionario[n] = factorial

    stdscr.addstr("\nDiccionario con elementos comunes como claves y sus factoriales:\n")
    for elemento, factorial in diccionario.items():
        stdscr.addstr(f"Elemento común: {elemento}, Factorial: {factorial}\n")

    stdscr.addstr("\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_13(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 13 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene un conjunto y una matriz con datos numéricos, hallar el primo mayor del conjunto
y su factorial y llenar este valor en las posiciones comprendidas
entre el par menor y el Fibonacci mayor de la matriz\n\n""")

    vector = [random.randint(1, 10) for _ in range(10)]
    matriz = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

    primo_mayor = 0

    for i in vector:
        if es_primo(i):
            if i > primo_mayor:
                primo_mayor = i

    factorial_primo_mayor = calcular_factorial(primo_mayor)
    par_menor = float("inf")
    posicion_par_menor_columna = None
    posicion_par_menor_fila = None
    fibonacci_mayor = 0
    posicion_fibonacci_mayor_columna = None
    posicion_fibonacci_mayor_fila = None

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if es_fibonacci(matriz[i][j]):
                if matriz[i][j] > fibonacci_mayor:
                    fibonacci_mayor = matriz[i][j]
                    posicion_fibonacci_mayor_columna = j
                    posicion_fibonacci_mayor_fila = i
            if es_primo(matriz[i][j]):
                if matriz[i][j] < par_menor:
                    par_menor = matriz[i][j]
                    posicion_par_menor_columna = j
                    posicion_par_menor_fila = i

    stdscr.addstr(f"Vector:\n{vector}\n")
    stdscr.addstr("Matriz\n")
    mostrar_matriz(stdscr, matriz)

    stdscr.addstr(f"\nPrimo mayor vector: {primo_mayor} Su factorial: {factorial_primo_mayor}\n")
    stdscr.addstr(f"Par menor matriz: {par_menor} posicion fila: {posicion_par_menor_fila+1} columna: {posicion_par_menor_columna+1}\n")
    stdscr.addstr(f"Fibonacci mayor matriz: {fibonacci_mayor} posicion fila: {posicion_fibonacci_mayor_fila+1} columna: {posicion_fibonacci_mayor_columna+1}\n")

    matriz_modificada = matriz

    for i in range(len(matriz_modificada)):
        for j in range(len(matriz_modificada[0])):
            if i >= posicion_par_menor_fila and i <= posicion_fibonacci_mayor_fila:
                if i == posicion_par_menor_fila:
                    if j > posicion_par_menor_columna:
                        matriz_modificada[i][j] = factorial_primo_mayor
                if i == posicion_fibonacci_mayor_fila:
                    if j < posicion_fibonacci_mayor_columna:
                        matriz_modificada[i][j] = factorial_primo_mayor
                if i > posicion_par_menor_fila and i < posicion_fibonacci_mayor_fila:
                    matriz_modificada[i][j] = factorial_primo_mayor

    stdscr.addstr("\nMatriz Modificada\n")
    mostrar_matriz(stdscr, matriz_modificada)

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_14(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 14 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene un vector y una matriz con datos numéricos, formar un conjunto con
los múltiplos de cinco  y Fibonacci, ordenado ascendentemente.\n\n""")
    
    vector = [random.randint(1, 20) for n in range(10)]
    matriz = [[random.randint(1, 20) for n in range(5)] for i in range(5)]
    conjunto = set()

    for n in vector:
        if es_multiplo_de_5(n) or es_fibonacci(n):
            conjunto.add(n)

    for fila in matriz:
        for n in fila:
            if es_multiplo_de_5(n) or es_fibonacci(n):
                conjunto.add(n)

    stdscr.addstr(f"Vector:\n{vector}\n")
    stdscr.addstr(f"\nMatriz:\n")
    mostrar_matriz(stdscr, matriz)
    stdscr.addstr(f"\nConjunto con números de Fibonacci y múltiplos de 5:\n{conjunto}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_15(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 15 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen dos matrices con datos numéricos Formar un diccionario con los primos
como clave y las veces que aparecen como valor, ordenado por la clave.\n\n""")
    
    matriz1 = [[random.randint(1, 20) for j in range(5)] for i in range(5)]
    matriz2 = [[random.randint(1, 20) for j in range(5)] for i in range(5)]

    diccionario = {}

    def agregar_a_diccionario(matriz, diccionario):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if es_primo(matriz[i][j]):
                    if matriz[i][j] not in diccionario:
                        diccionario[matriz[i][j]] = 1
                    else:
                        diccionario[matriz[i][j]] += 1

    agregar_a_diccionario(matriz1, diccionario)
    agregar_a_diccionario(matriz2, diccionario)

    stdscr.addstr("Matriz 1:\n")
    mostrar_matriz(stdscr, matriz1)
    stdscr.addstr("\nMatriz 2:\n")
    mostrar_matriz(stdscr, matriz2)

    def ordenar_claves(diccionario):
        claves = list(diccionario.keys())
        for i in range(len(claves)):
            for j in range(len(claves)-1-i):
                if claves[j] > claves[j+1]:
                    claves[j], claves[j+1] = claves[j+1], claves[j]

        diccionario_ordenado = {}
        for clave in claves:
            diccionario_ordenado[clave] = diccionario[clave]
        return diccionario_ordenado

    diccionario_ordenado = ordenar_claves(diccionario)

    stdscr.addstr("\nResultados ordenados por clave:\n")
    for primo, repeticiones in diccionario_ordenado.items():
        stdscr.addstr(f"Primo: {primo}  Repeticiones: {repeticiones}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_16(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 16 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene una matriz con datos numéricos, formar un diccionario con clave Fibonacci y valor,
las veces que se repite y modificar el valor para aquellos contadores que son primos por su factorial\n\n""")
    
    matriz = [[random.randint(1, 10) for j in range(5)] for i in range(5)]
    diccionario = {}

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if es_fibonacci(matriz[i][j]):
                if matriz[i][j] in diccionario:
                    diccionario[matriz[i][j]] += 1
                else:
                    diccionario[matriz[i][j]] = 1

    stdscr.addstr("Matriz:\n")
    mostrar_matriz(stdscr, matriz)

    stdscr.addstr("\nResultados:\n")
    for fibonacci, repeticiones in diccionario.items():
        stdscr.addstr(f"Fibonacci: {fibonacci}  Repeticiones: {repeticiones}\n")

    for fibonacci, repeticiones in diccionario.items():
        if es_primo(repeticiones):
            diccionario[fibonacci] = calcular_factorial(repeticiones)

    stdscr.addstr("\nResultados con primos reemplazados por su factorial:\n")
    for fibonacci, repeticiones in diccionario.items():
        stdscr.addstr(f"Fibonacci: {fibonacci}  Repeticiones: {repeticiones}\n")

    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_17(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 17 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave\n\n""")
    
    cadena1 = "Hola Mundo 2023"
    cadena2 = "Universidad de Nariño semestre 2"
    cadena3 = "Numero de estudiantes aproximadamente 35000"
    cadenatotal = cadena1 + cadena2 + cadena3

    diccionario_numeros = {}
    diccionario_letras = {}

    stdscr.addstr(f"Cadena 1: {cadena1}\nCadena 2: {cadena2}\nCadena 3: {cadena3}\n")

    for caracter in cadenatotal:
        if caracter.isnumeric():
            if caracter in diccionario_numeros:
                diccionario_numeros[caracter] += 1
            else:
                diccionario_numeros[caracter] = 1
        if caracter.isalpha():
            caracter = caracter.lower()
            if caracter in diccionario_letras:
                diccionario_letras[caracter] += 1
            else:
                diccionario_letras[caracter] = 1

    # Ordenar diccionario_numeros por clave (números) usando el algoritmo de burbuja
    claves_numeros = list(diccionario_numeros.keys())
    for i in range(len(claves_numeros)):
        for j in range(len(claves_numeros) - i - 1):
            if claves_numeros[j] > claves_numeros[j + 1]:
                claves_numeros[j], claves_numeros[j + 1] = claves_numeros[j + 1], claves_numeros[j]

    # Crear un nuevo diccionario_numeros ordenado por clave
    diccionario_numeros_ordenado = {k: diccionario_numeros[k] for k in claves_numeros}

    # Ordenar diccionario_letras por clave (letras) usando el algoritmo de burbuja
    claves_letras = list(diccionario_letras.keys())
    for i in range(len(claves_letras)):
        for j in range(len(claves_letras) - i - 1):
            if claves_letras[j] > claves_letras[j + 1]:
                claves_letras[j], claves_letras[j + 1] = claves_letras[j + 1], claves_letras[j]

    # Crear un nuevo diccionario_letras ordenado por clave
    diccionario_letras_ordenado = {k: diccionario_letras[k] for k in claves_letras}

    stdscr.addstr("\n\nRepeticiones de números:\n\n")
    for numero, repeticiones in diccionario_numeros_ordenado.items():
        stdscr.addstr(" [ ")
        stdscr.addstr(f"Número: {numero}  Repeticiones: {repeticiones}")
        stdscr.addstr(" ] ")

    stdscr.addstr("\n\nRepeticiones de Letras:\n\n")
    for letra, repeticiones in diccionario_letras_ordenado.items():
        stdscr.addstr(" [ ")
        stdscr.addstr(f"Letra: {letra}  Repeticiones: {repeticiones}")
        stdscr.addstr(" ] ")

    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_18(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 18 - Taller 1:\n\n")
    stdscr.addstr("""Se tiene un vector y una matriz formar conjuntos con los números primos de cada una 
y realizar las operaciones de conjuntos:    Unión
                                            Intersección
                                            Diferencia
                                            Diferencia simétrica\n\n""")
    
    vector = [random.randint(1, 10) for _ in range(10)]
    matriz = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

    # Crear conjuntos de números primos
    conjunto_vector = set(vector)
    conjunto_matriz = set()

    for fila in matriz:
        conjunto_matriz.update(fila)

    # Realizar operaciones de conjuntos
    union = conjunto_vector.union(conjunto_matriz)
    interseccion = conjunto_vector.intersection(conjunto_matriz)
    diferencia = conjunto_vector.difference(conjunto_matriz)
    diferencia_simetrica = conjunto_vector.symmetric_difference(conjunto_matriz)

    stdscr.addstr("Vector:\n")
    stdscr.addstr(f"{vector}\n\n")

    mostrar_matriz(stdscr, matriz)

    stdscr.addstr("\n\nOperaciones de conjuntos:\n")
    stdscr.addstr(f"Unión: {union}\n")
    stdscr.addstr(f"Intersección: {interseccion}\n")
    stdscr.addstr(f"Diferencia: {diferencia}\n")
    stdscr.addstr(f"Diferencia simétrica: {diferencia_simetrica}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_19(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 19 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
el par mayor y las veces que se repite
el primo menor y las veces que se repite
el Fibonacci menor y las veces que se repite
Con estos datos hallar:
El factorial de la suma del par y del primo
La multiplicación con sumas de los contadores del primo y del Fibonacci.\n\n""")
    
    vector = [random.randint(1, 20) for i in range(10)]
    matriz = [[random.randint(1, 20) for j in range(5)] for i in range(5)]

    par_mayor = 0
    primo_menor = float("inf")
    fibonacci_menor = float("inf")

    for numero in vector:
        if es_par(numero):
            if numero > par_mayor:
                par_mayor = numero
        if es_fibonacci(numero):
            if numero < fibonacci_menor:
                fibonacci_menor = numero
        if es_primo(numero):
            if numero < primo_menor:
                primo_menor = numero

    for fila in matriz:
        for numero in fila:
            if es_par(numero):
                if numero > par_mayor:
                    par_mayor = numero
            if es_fibonacci(numero):
                if numero < fibonacci_menor:
                    fibonacci_menor = numero
            if es_primo(numero):
                if numero < primo_menor:
                    primo_menor = numero

    # Repeticiones
    diccionario = {}
    for numero in vector:
        if numero == par_mayor or numero == fibonacci_menor or numero == primo_menor:
            if numero in diccionario:
                diccionario[numero] += 1
            else:
                diccionario[numero] = 1

    for fila in matriz:
        for numero in fila:
            if numero == par_mayor or numero == fibonacci_menor or numero == primo_menor:
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1

    stdscr.addstr(f"Vector:\n{vector}\n")
    stdscr.addstr("Matriz\n")
    mostrar_matriz(stdscr, matriz)
    stdscr.addstr("\n")

    for numero, repeticiones in diccionario.items():
        if numero == par_mayor:
            stdscr.addstr(f"Par mayor: {par_mayor} Repeticiones: {repeticiones}\n")
        if numero == fibonacci_menor:
            repeticiones_fibonacci = repeticiones
            stdscr.addstr(f"Fibonacci menor: {fibonacci_menor} Repeticiones: {repeticiones}\n")
        if numero == primo_menor:
            repeticiones_primo = repeticiones
            stdscr.addstr(f"Primo menor: {primo_menor} Repeticiones: {repeticiones}\n")

    # Factorial suma par primo
    factorial_par_mas_primo = calcular_factorial(par_mayor + primo_menor)
    stdscr.addstr(f"\nFactorial de {primo_menor} + {par_mayor} = {factorial_par_mas_primo}\n")

    condicion = 1
    suma = 0
    while condicion <= repeticiones_fibonacci:
        suma += repeticiones_primo
        condicion += 1

    # Multiplicación con sumas de los contadores del primo y del Fibonacci
    stdscr.addstr(f"Multiplicación de {repeticiones_fibonacci} x {repeticiones_primo} = {suma}\n")

    stdscr.refresh()
    stdscr.getch()

def ejercicio_taller_1_20(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicio 20 - Taller 1:\n\n")
    stdscr.addstr("""Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios así:
Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
Diccionario 2 con clave carácter y valor las veces que se repite, ordenado ascendentemente por clave 
Almacenar esta información en un archivo, recuperarla y mostrar los dos diccionarios.\n\n""")
    
    # Cadena 1
    stdscr.addstr("Ingrese la primera cadena de texto:\n")
    stdscr.refresh()
    curses.echo()  # Habilitar la retroalimentación de entrada
    cadena1 = stdscr.getstr().decode("utf-8")
    curses.noecho()  # Deshabilitar la retroalimentación de entrada

    # Cadena 2
    stdscr.addstr("\nIngrese la segunda cadena de texto:\n")
    stdscr.refresh()
    curses.echo()  # Habilitar la retroalimentación de entrada
    cadena2 = stdscr.getstr().decode("utf-8")
    curses.noecho()  # Deshabilitar la retroalimentación de entrada
    
    # Cadena 3
    stdscr.addstr("\nIngrese la tercera cadena de texto:\n")
    stdscr.refresh()
    curses.echo()  # Habilitar la retroalimentación de entrada
    cadena3 = stdscr.getstr().decode("utf-8")
    curses.noecho()  # Deshabilitar la retroalimentación de entrada

    stdscr.clear()
    stdscr.addstr(f"Cadena 1: {cadena1}\nCadena 2: {cadena2}\nCadena 3: {cadena3}")
    stdscr.refresh()

    cadenatotal = cadena1 + cadena2 + cadena3
    diccionario1 = {}
    diccionario2 = {}

    for i in range(len(cadenatotal)):
        if cadenatotal[i].isnumeric():
            if cadenatotal[i] in diccionario1:
                diccionario1[cadenatotal[i]] += 1
            else:
                diccionario1[cadenatotal[i]] = 1
        if cadenatotal[i].isalpha():
            if cadenatotal[i] in diccionario2:
                diccionario2[cadenatotal[i]] += 1
            else:
                diccionario2[cadenatotal[i]] = 1

    # Ordenar diccionario1 por valor, es decir las repeticiones, usando el algoritmo burbuja
    repeticiones = list(diccionario1.values())
    numeros = list(diccionario1.keys())
    for i in range(len(repeticiones)):
        for j in range(len(repeticiones) - i - 1):
            if repeticiones[j] > repeticiones[j + 1]:
                repeticiones[j], repeticiones[j + 1] = repeticiones[j + 1], repeticiones[j]
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    # Creo el diccionario de nuevo para reubicar los valores
    diccionario1 = {}
    for i in range(len(numeros)):
        diccionario1[numeros[i]] = repeticiones[i]

    # Ordenar el diccionario 2 por claves, es decir las letras y mostrar sus repeticiones
    letras = list(diccionario2.keys())
    repeticiones = list(diccionario2.values())
    for i in range(len(letras)):
        for j in range(len(letras) - i - 1):
            if letras[j] > letras[j + 1]:
                letras[j], letras[j + 1] = letras[j + 1], letras[j]
                repeticiones[j], repeticiones[j + 1] = repeticiones[j + 1], repeticiones[j]

    diccionario2 = {letra: diccionario2[letra] for letra in letras}

    stdscr.addstr("\n\nDiccionario 1 con los números y sus repeticiones:\n")
    for numero, repeticiones in diccionario1.items():
        stdscr.addstr(f"Numero: {numero} Repeticiones: {repeticiones}\n")

    stdscr.addstr("\nDiccionario 2 con letras y repeticiones:\n")
    for letra, repeticiones in diccionario2.items():
        stdscr.addstr(f"Letra: {letra} Repeticiones: {repeticiones}\n")


    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()




#-----------------------------------------------------------------------------------------------------------------#
# Puntos de la evaluacion 1 en funciones para hacer un menu corto y llamar a las funciones en un menu mas general #
#-----------------------------------------------------------------------------------------------------------------#

def evaluacion_1_punto_1(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 1 - Punto 1:\n\n")
    stdscr.addstr("""1.	Se tiene un vector y una matriz con datos numéricos, buscar un dato en el vector que tiene estas condiciones:
El dato es el segundo Fibonacci de un rango en un vector cuyos límites están determinados por el primo1 y primo2 presentes en el rango de la matriz comprendido entre el mayor y el menor es esta.
Mostrar el dato y su posición.\n\n""")
    
    lista_numeros = [random.randint(1, 20) for _ in range(10)]
    matriz_numeros = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

    stdscr.addstr(f"Lista de numeros: {lista_numeros}\n")

    stdscr.addstr("Matriz de numeros:\n")
    for fila in matriz_numeros:
        stdscr.addstr(" ".join("{:4}".format(numero) for numero in fila))
        stdscr.addstr("\n")

    mayor_primo = None
    menor_primo = None

    for fila_idx, fila in enumerate(matriz_numeros):
        for columna_idx, numero in enumerate(fila):
            if es_primo(numero):
                if mayor_primo is None or numero > mayor_primo:
                    mayor_primo = numero
                if menor_primo is None or numero < menor_primo:
                    menor_primo = numero

    i_mayor_primo, j_mayor_primo, i_menor_primo, j_menor_primo = 0, 0, 0, 0
    for i in range(len(matriz_numeros)):
        for j in range(len(matriz_numeros[0])):
            if matriz_numeros[i][j] == mayor_primo:
                i_mayor_primo, j_mayor_primo = i, j
            if matriz_numeros[i][j] == menor_primo:
                i_menor_primo, j_menor_primo = i, j

    contador = 0
    segundo_primo = 0
    i_segundo_primo = 0

    while i_mayor_primo < len(matriz_numeros) and contador < 2:
        while j_mayor_primo < len(matriz_numeros[0]) and contador < 2:
            if i_mayor_primo == i_menor_primo and j_mayor_primo == j_menor_primo:
                break
            elif es_primo(matriz_numeros[i_mayor_primo][j_mayor_primo]):
                contador += 1
                if contador == 2:
                    segundo_primo = matriz_numeros[i_mayor_primo][j_mayor_primo]
                    i_segundo_primo = i_mayor_primo
                else:
                    i_mayor_primo, j_mayor_primo = i_menor_primo, j_menor_primo
            j_mayor_primo += 1
        i_mayor_primo += 1
        j_mayor_primo = 0

    contador = 0
    segundo_fibonacci = None
    i_segundo_fibonacci = None

    for i in range(len(lista_numeros)):
        if segundo_primo < lista_numeros[i] and es_fibonacci(lista_numeros[i]):
            contador += 1
            if contador == 2:
                segundo_fibonacci = lista_numeros[i]
                i_segundo_fibonacci = i

    stdscr.addstr(f"El segundo número Fibonacci en el rango entre el primer y segundo número primo de la matriz es: {segundo_fibonacci} y su posición en la lista es: {i_segundo_fibonacci}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def evaluacion_1_punto_2(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 1 - Punto 2:\n\n")
    stdscr.addstr("""2.	Se tiene un diccionario con la siguiente información
Clave numero entero.
Valor lista de números
Hallar la clave del primo mayor y Fibonacci menor que están en las listas de los valores y
formar una lista con los pares comprendidos entre estos dos valores y el promedio de estos.\n\n""")
    
    diccionario_aleatorio = generar_diccionario_aleatorio()

    stdscr.addstr(f"Diccionario generado aleatoriamente: {diccionario_aleatorio}\n")

    mayor_primo, clave_mayor_primo = encontrar_mayor_primo_en_diccionario(diccionario_aleatorio)
    menor_fibonacci, clave_menor_fibonacci = encontrar_menor_fibonacci_en_diccionario(diccionario_aleatorio)

    stdscr.addstr(f"El número primo mayor es {mayor_primo} y se encuentra en la clave {clave_mayor_primo}\n")
    stdscr.addstr(f"El número de Fibonacci menor es {menor_fibonacci} y se encuentra en la clave {clave_menor_fibonacci}\n")

    numeros_pares_entre_claves = encontrar_numeros_pares_entre_claves(clave_mayor_primo, clave_menor_fibonacci)

    stdscr.addstr(f"Números pares entre las claves {clave_mayor_primo} y {clave_menor_fibonacci}: {numeros_pares_entre_claves}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def evaluacion_1_punto_3(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluación 1 - Punto 3:\n\n")
    stdscr.addstr("""3. Se tiene un diccionario con la siguiente información
Clave número entero
Valor lista de números
Formar dos conjuntos así:
Conjunto 1 con los números pares de la lista valor de aquellas claves que son primos
Conjunto 2 con los números pares de la lista valor de aquellas claves que son Fibonacci
Con estos dos conjuntos, formar dos cadenas:
Cadena 1 con los pares comunes
Cadena 2 con la unión de los pares sin elementos comunes\n\n""")
    
    diccionario = generar_diccionario_aleatorio()

    stdscr.addstr(f"\n\nDiccionario generado aleatoriamente: {diccionario}")

    conjunto1 = set()
    conjunto2 = set()

    claves_primos = []
    claves_fibonacci = []

    for clave, valores in diccionario.items():
        if es_primo(clave):
            claves_primos.append(clave)
            for valor in valores:
                if valor % 2 == 0:
                    conjunto1.add(valor)
        if es_fibonacci(clave):
            claves_fibonacci.append(clave)
            for valor in valores:
                if valor % 2 == 0:
                    conjunto2.add(valor)

    pares_comunes = []
    union_pares = []

    for n in conjunto1:
        if n in conjunto2:
            pares_comunes.append(n)
    for n in conjunto2:
        if n in conjunto1:
            pares_comunes.append(n)

    for n in conjunto1:
        union_pares.append(n)
    for n in conjunto2:
        union_pares.append(n)


    stdscr.addstr(f"\n Cadena 1 (pares comunes): {pares_comunes}\n Cadena 2(union pares): {union_pares}")



    stdscr.refresh()
    stdscr.getch()




#-----------------------------------------------------------------------------------------------------------------#
# Puntos de la evaluacion 2 en funciones para hacer un menu corto y llamar a las funciones en un menu mas general #
#-----------------------------------------------------------------------------------------------------------------#

def evaluacion_2_punto_1(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 2 - Punto 1:\n\n")
    stdscr.addstr("""1.	Se tiene un vector y una matriz con datos numéricos
Buscar un dato en una matriz.
El dato es el segundo primo de un rango de la matriz cuyos límites están determinados por el Fibonacci 1 y 2 del rango del vector determinado por el número mayor y menor de este.
Mostrar el dato y su posición\n\n""")

    fibo1 = None
    fibo2 = None

    lista_aleatoria = [random.randint(1, 20) for _ in range(20)]
    matriz_aleatoria = [[random.randint(1, 20) for _ in range(10)] for _ in range(10)]
    
    stdscr.addstr(f"\nLista aleatoria:\n{lista_aleatoria}")
    stdscr.addstr("\nMatriz aleatoria:\n")
    mostrar_matriz(stdscr, matriz_aleatoria)
    
    maximo = max(lista_aleatoria)
    minimo = min(lista_aleatoria)
    
    i_fibo1 = 0
    i_fibo2 = 0
    cont = 0

    if lista_aleatoria.index(maximo) < lista_aleatoria.index(minimo):
        while lista_aleatoria[i_fibo1] != maximo:
            if es_fibonacci(lista_aleatoria[i_fibo1]):
                cont += 1
                if cont == 1:
                    fibo1 = lista_aleatoria[i_fibo1]
                elif cont == 2:
                    fibo2 = lista_aleatoria[i_fibo1]
            i_fibo1 += 1
    else:
        while lista_aleatoria[i_fibo2] != minimo:
            if es_fibonacci(lista_aleatoria[i_fibo2]):
                cont += 1
                if cont == 1:
                    fibo1 = lista_aleatoria[i_fibo2]
                elif cont == 2:
                    fibo2 = lista_aleatoria[i_fibo2]
            i_fibo2 += 1

    stdscr.addstr(f"\nEl primer número de Fibonacci es: {fibo1}")
    stdscr.addstr(f"\nEl segundo número de Fibonacci es: {fibo2}")

    primo_2 = None
    primo_i = None
    primo_j = None

    for i in range(len(matriz_aleatoria)):
        for j in range(len(matriz_aleatoria[0])):
            if matriz_aleatoria[i][j] == fibo1:
                i_1, j_1 = i, j
            if matriz_aleatoria[i][j] == fibo2:
                i_2, j_2 = i, j

    if i_1 < i_2:
        b = 0
        cont = 0
        i = i_1 + 1
        while i < len(matriz_aleatoria) - 1 and b == 0:
            while j_1 < len(matriz_aleatoria[0]) and b == 0:
                if i_1 == i_2 and j_1 == j_2:
                    b = 1
                else:
                    if es_primo(matriz_aleatoria[i_1][j_1]):
                        cont += 1
                        if cont == 2:
                            primo_2 = matriz_aleatoria[i_1][j_1]
                            primo_i = i_1
                            primo_j = j_1
                j_1 += 1
            j_1 = 0
            i_1 += 1
    else:
        if i_2 < i_1:
            b = 0
            cont = 0
            j_2 = j_2 + 1
            while i_2 < len(matriz_aleatoria) and b == 0:
                while j_2 < len(matriz_aleatoria[0]) and b == 0:
                    if i_2 == i_1 and j_2 == j_1:
                        b = 1
                    else:
                        if es_primo(matriz_aleatoria[i_2][j_2]):
                            cont += 1
                            if cont == 1:
                                print(matriz_aleatoria[i_2][j_2])
                            if cont == 2:
                                primo_2 = matriz_aleatoria[i_2][j_2]
                                primo_i = i_2
                                primo_j = j_2
                    j_2 += 1
                j_2 = 0
                i_2 += 1

    if primo_2 is None or primo_i is None or primo_j is None:
        stdscr.addstr("\n\nPero No se cumplieron los parametros para los resultados, intenta otra vez con otra lista y matriz")
    else:
        stdscr.addstr(f"\nEl primo es: {primo_2} y su posición es ({primo_i}, {primo_j})")

    stdscr.refresh()
    stdscr.getch()

def evaluacion_2_punto_2(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 2 - Punto 2:\n\n")
    stdscr.addstr("""2.	Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Modificar las claves de la clave mayor y la clave menor con la siguiente información:
Clave mayor: conjunto1
Clave menor: conjunto2
Los  conjuntos están formados así:
Conjunto 1 con los número primos presentes en las diferentes listas sin repetidos 
Conjunto 2 con los número Fibonacci de las diferentes listas de valores sin repetidos\n\n""")
    
    diccionario = generar_diccionario_aleatorio()
    stdscr.addstr(f"Diccionario ingresado:  {diccionario}")

    key_mayor = max(diccionario.keys())
    key_menor = min(diccionario.keys())

    conjunto_primos = set()
    conjunto_fibonacci = set()

    for lista in diccionario.values():
        for num in lista:
            if es_primo(num):
                conjunto_primos.add(num)
            if es_fibonacci(num):
                conjunto_fibonacci.add(num)

    diccionario[key_mayor] = conjunto_primos
    diccionario[key_menor] = conjunto_fibonacci

    stdscr.addstr(f"\n\nClave del número mayor: {key_mayor}")
    stdscr.addstr(f"\nClave del número menor: {key_menor}")
    stdscr.addstr(f"\nDiccionario actualizado: {diccionario}")

    stdscr.refresh()
    stdscr.getch()

def evaluacion_2_punto_3(stdscr):
    stdscr.clear()
    stdscr.addstr("Evaluacion 2 - Punto 3:\n\n")
    stdscr.addstr("""3.	Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Ordenar las listas de los valores asi:
En orden ascendente aquellas claves que sean primos
En orden descendente aquellas claves que sen fibonacci\n\n""")
    
    diccionario = generar_diccionario_aleatorio()

    stdscr.addstr(f"Diccionario ingresado:\n{diccionario}\n")

    for key, lista in diccionario.items():
        if es_primo(key):
            list_ordenada = sorted(lista)
            diccionario[key] = list_ordenada
        if es_fibonacci(key) and not es_primo(key):
            list_ordenada = sorted(lista, reverse=True)
            diccionario[key] = list_ordenada

    stdscr.addstr("Diccionario actualizado:\n")
    for key, lista in diccionario.items():
        stdscr.addstr(f" {key}:  {lista} ")

    stdscr.refresh()
    stdscr.getch()





#------------------------------------------------------------------------------------------------------------------#
# Ejercicios hechos en clase en funciones para hacer un menu corto y llamar a las funciones en un menu mas general #
#------------------------------------------------------------------------------------------------------------------#

def ejercicio_en_clase_1(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 1:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    lista1 = [random.randint(1, 50) for i in range(20)]
    lista2 = [random.randint(1, 50) for i in range(20)]

    stdscr.addstr("\n\nLista 1:\n")
    for item in lista1:
        stdscr.addstr(f"   {item}")

    stdscr.addstr("\n\nLista 2:\n")
    for item in lista2:
        stdscr.addstr(f"   {item} ")

    primos_no_comunes = []
    impares_comunes = []

    # Identificar los primos no comunes de las dos listas
    for i in range(len(lista1)):
        if es_primo(lista1[i]):
            if lista1[i] not in lista2 and lista1[i] not in primos_no_comunes:
                primos_no_comunes.append(lista1[i])
    for j in range(len(lista2)):
        if es_primo(lista2[j]):
            if lista2[j] not in lista1 and lista2[j] not in primos_no_comunes:
                primos_no_comunes.append(lista2[j])

    for i in range(len(primos_no_comunes)):
        for j in range(len(primos_no_comunes) - i - 1):
            if primos_no_comunes[j] > primos_no_comunes[j + 1]:
                temporal = primos_no_comunes[j]
                primos_no_comunes[j] = primos_no_comunes[j + 1]
                primos_no_comunes[j + 1] = temporal

    stdscr.addstr("\n\nPrimos no comunes de las dos listas:\n")
    for item in primos_no_comunes:
        stdscr.addstr(f"   {item}")

    # Identificar los impares comunes de las dos listas
    for i in range(len(lista1)):
        if es_impar(lista1[i]):
            if lista1[i] in lista2 and lista1[i] not in impares_comunes:
                impares_comunes.append(lista1[i])

    for i in range(len(impares_comunes)):
        for j in range(len(impares_comunes) - i - 1):
            if impares_comunes[j] > impares_comunes[j + 1]:
                temporal = impares_comunes[j]
                impares_comunes[j] = impares_comunes[j + 1]
                impares_comunes[j + 1] = temporal

    stdscr.addstr("\n\nImpares comunes de las dos listas:\n")
    for item in impares_comunes:
        stdscr.addstr(f"   {item}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_2(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 2:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    dimensiones = random.randint(5, 10)

    matriz1 = hacer_matriz(dimensiones)
    matriz2 = hacer_matriz(dimensiones)

    stdscr.addstr("\nMatriz 1:\n")
    mostrar_matriz(stdscr, matriz1)
    stdscr.addstr("\nMatriz 2:\n")
    mostrar_matriz(stdscr, matriz2)

    numeros_perfectos = []

    for fila in matriz1:
        for numero in fila:
            if es_perfecto(numero) and numero not in numeros_perfectos:
                numeros_perfectos.append(numero)

    for fila in matriz2:
        for numero in fila:
            if es_perfecto(numero) and numero not in numeros_perfectos:
                numeros_perfectos.append(numero)

    stdscr.addstr("\nNúmeros perfectos en ambas matrices:\n")
    for numero in numeros_perfectos:
        stdscr.addstr(f"   {numero}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_3(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 3:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    lista = [random.randint(1, 50) for _ in range(20)]
    fibonaccis = []
    primos = []

    for numero in lista:
        if es_fibonacci(numero) and numero not in fibonaccis:
            fibonaccis.append(numero)
        if es_primo(numero) and numero not in primos:
            primos.append(numero)

    stdscr.addstr(f"Lista original:\n")
    for numero in lista:
        stdscr.addstr(f"   {numero}")

    stdscr.addstr(f"\nLista de primos:\n")
    for numero in primos:
        stdscr.addstr(f"   {numero}")

    stdscr.addstr(f"\nLista de Fibonacci:\n")
    for numero in fibonaccis:
        stdscr.addstr(f"   {numero}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_4(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 4:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    vector = [random.randint(1, 50) for n in range(20)]
    dimensiones = random.randint(2, 5)
    matriz = hacer_matriz(dimensiones)

    stdscr.addstr("Vector:\n")
    for item in vector:
        stdscr.addstr(f"   {item}")

    stdscr.addstr("\nMatriz:\n")
    mostrar_matriz(stdscr, matriz)

    lista1 = []
    numeros_matriz = []

    for fila in matriz:
        for numero in fila:
            numeros_matriz.append(numero)

    for numero in vector:
        if numero not in numeros_matriz and numero not in lista1:
            lista1.append(numero)

    for numero in numeros_matriz:
        if numero not in vector and numero not in lista1:
            lista1.append(numero)

    stdscr.addstr("\nLista 1 con los números no comunes sin repetir:\n")
    for item in lista1:
        stdscr.addstr(f"   {item}")

    lista2 = []

    for i in range(len(numeros_matriz)):
        repeticiones = 0
        if es_primo(numeros_matriz[i]):
            for j in numeros_matriz:
                if j == numeros_matriz[i]:
                    repeticiones += 1
            if repeticiones == 1 and numeros_matriz[i] not in vector:
                lista2.append(numeros_matriz[i])

    for i in range(len(vector)):
        repeticiones = 0
        if es_primo(vector[i]):
            for j in vector:
                if j == vector[i]:
                    repeticiones += 1
            if repeticiones == 1 and vector[i] not in numeros_matriz:
                lista2.append(vector[i])

    stdscr.addstr("\nLista 2 con los primos que no se repiten:\n")
    for item in lista2:
        stdscr.addstr(f"   {item}")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_5(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 5:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    vector = [random.randint(1, 10) for i in range(10)]
    diccionario = {}

    for i in vector:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1

    stdscr.addstr("Vector:\n")
    for numero in vector:
        stdscr.addstr(f" {numero} ")

    stdscr.addstr("\n\nDiccionario:\n")
    for numero, repeticiones in diccionario.items():
        stdscr.addstr(f"Numero: {numero}   Repeticiones: {repeticiones}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_6(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 6:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    vector1 = [random.randint(1, 20) for n in range(10)]
    vector2 = [random.randint(1, 20) for n in range(10)]
    diccionario1 = {}
    diccionario2 = {}

    # Diccionario 1 con primos comunes y su factorial
    for i in vector1:
        for j in vector2:
            if es_primo(j) and j == i:
                if j not in diccionario1:
                    diccionario1[j] = calcular_factorial(j)

    for i in vector2:
        for j in vector1:
            if es_primo(j) and j == i:
                if j not in diccionario1:
                    diccionario1[j] = calcular_factorial(j)

    stdscr.addstr("Vector 1:\n")
    for numero in vector1:
        stdscr.addstr(f"{numero} ")

    stdscr.addstr("\n\nVector 2:\n")
    for numero in vector2:
        stdscr.addstr(f"{numero} ")

    stdscr.addstr("\n\nDiccionario 1 con primo y su factorial:\n")
    for primo, factorial in diccionario1.items():
        stdscr.addstr(f"Primo: {primo}  Factorial: {factorial}\n")

    # Diccionario 2 con fibonaccis no comunes y los pares menores
    for i in vector1:
        if i not in vector2:
            if es_fibonacci(i):
                pares_menores = []
                for k in vector1:
                    if es_par(k) and k < i and k not in pares_menores:
                        pares_menores.append(k)
                for k in vector2:
                    if es_par(k) and k < i and k not in pares_menores:
                        pares_menores.append(k)
                if i not in diccionario2:
                    diccionario2[i] = pares_menores
    for i in vector2:
        if i not in vector1:
            if es_fibonacci(i):
                pares_menores = []
                for k in vector1:
                    if es_par(k) and k < i and k not in pares_menores:
                        pares_menores.append(k)
                for k in vector2:
                    if es_par(k) and k < i and k not in pares_menores:
                        pares_menores.append(k)
                if i not in diccionario2:
                    diccionario2[i] = pares_menores

    stdscr.addstr("\n\nFibonaccis y pares menores que el fibonacci:\n")
    for fibonacci, pares_menores in diccionario2.items():
        stdscr.addstr(f"Fibonacci: {fibonacci}  Pares menores: {pares_menores}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_7(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 7:\n\n")
    stdscr.addstr("""Se tienen dos vectores con datos numéricos. Formar un tercer vector con los números primos que
están en ambos vectores sin datos repetidos.\n\n""")
    
    vector = "universidad de nariño, ingenieria de sistmas semestre 2, ejercicio 7 fecha 12 de 10 del 2023"
    diccionario1 = {}
    diccionario2 = {}

    for caracter in vector:
        if caracter.isnumeric():
            if caracter in diccionario1:
                diccionario1[caracter] += 1
            else:
                diccionario1[caracter] = 1
        elif caracter.isalpha():
            caracter = caracter.lower()
            if caracter in diccionario2:
                diccionario2[caracter] += 1
            else:
                diccionario2[caracter] = 1

    stdscr.addstr(f"Cadena de letras:\n{vector}\n")
    stdscr.addstr("\nDiccionario 1 (dígitos y repeticiones):\n")

    for clave, valor in diccionario1.items():
        stdscr.addstr(f"Numero: {clave}, Repeticiones: {valor}\n")

    stdscr.addstr("\nDiccionario 2 (letras y repeticiones):\n")
    for clave, valor in diccionario2.items():
        stdscr.addstr(f"Letra: {clave}, Repeticiones: {valor}\n")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_8(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 8:\n\n")
    stdscr.addstr("""Determinar cuantas palabras hay en un párrafo.\n\n""")
    
    stdscr.addstr("Ingrese el párrafo: ")

    # Habilitar la entrada de texto
    curses.echo()
    
    # Leer el párrafo ingresado
    parrafo = stdscr.getstr().decode("utf-8")
    
    # Dividir el párrafo en palabras usando el espacio en blanco como separador
    palabras = parrafo.split()
    
    # Calcular la cantidad de palabras
    cantidad_palabras = len(palabras)
    
    # Mostrar el resultado en la pantalla
    stdscr.addstr(f"El párrafo contiene {cantidad_palabras} palabras.")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_9(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 9:\n\n")
    stdscr.addstr("""Reemplazar un caracter de una cadena por otro carácter dado.\n\n""")
    
    stdscr.addstr("Ingresa la cadena original: ")
    curses.echo()
    cadena_original = stdscr.getstr().decode("utf-8")
    
    stdscr.addstr("Ingresa el carácter que deseas reemplazar: ")
    curses.echo()
    caracter_a_reemplazar = stdscr.getstr().decode("utf-8")
    
    stdscr.addstr("Ingresa el nuevo carácter con el que deseas reemplazar: ")
    curses.echo()
    nuevo_caracter = stdscr.getstr().decode("utf-8")

    cadena_modificada = ""
    for caracter in cadena_original:
        if caracter == caracter_a_reemplazar:
            cadena_modificada += nuevo_caracter
        else:
            cadena_modificada += caracter

    stdscr.addstr("Cadena original: " + cadena_original)
    stdscr.addstr("\nCadena modificada: " + cadena_modificada)

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def ejercicio_en_clase_10(stdscr):
    stdscr.clear()
    stdscr.addstr("Ejercicios en clase - 10:\n\n")
    stdscr.addstr("""Se tiene una cadena. Encontrar el carácter que mas se repite.\n\n""")
    
    stdscr.addstr("Ingresa una cadena: ")
    curses.echo()
    cadena = stdscr.getstr().decode("utf-8")

    contador_caracteres = {}
    for caracter in cadena:
        if caracter in contador_caracteres:
            contador_caracteres[caracter] += 1
        else:
            contador_caracteres[caracter] = 1

    caracter_mas_repetido = ""
    max_repeticiones = 0

    for caracter, repeticiones in contador_caracteres.items():
        if repeticiones > max_repeticiones:
            caracter_mas_repetido = caracter
            max_repeticiones = repeticiones

    stdscr.addstr("\n\nResultado:\n")
    if caracter_mas_repetido:
        stdscr.addstr(f"En la cadena ingresada, el carácter que más se repite es '{caracter_mas_repetido}' con {max_repeticiones} repeticiones.")
    else:
        stdscr.addstr("La cadena está vacía, no hay caracteres para contar.")

    stdscr.addstr("\n\nPresiona Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()




#--------------------------------------------------------------------------------------------------------------------------------#
# Este son los submenus solamente para llamar funciones, para tener ordenado el menu interactivo por si se quiere modificar algo #
#--------------------------------------------------------------------------------------------------------------------------------#

def sub_menu_taller(stdscr):

    # Definir las opciones del submenú
    opciones_submenu = [
        "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4", "Ejercicio 5",
        "Ejercicio 6", "Ejercicio 7", "Ejercicio 8", "Ejercicio 9", "Ejercicio 10",
        "Ejercicio 11", "Ejercicio 12", "Ejercicio 13", "Ejercicio 14", "Ejercicio 15",
        "Ejercicio 16", "Ejercicio 17", "Ejercicio 18", "Ejercicio 19", "Ejercicio 20",
        "Regresar"
    ]
    
    # Inicializar la fila actual en la primera opción
    fila_actual = 0

    while True:
        stdscr.clear()
        stdscr.refresh()

        max_height, max_width = stdscr.getmaxyx()
        menu_width = 40
        menu_height = len(opciones_submenu)
        start_y = (max_height - menu_height) // 2
        start_x = (max_width - menu_width) // 2

        for idx, item in enumerate(opciones_submenu):
            if idx == fila_actual:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(start_y + idx, start_x, f"{item}", curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(start_y + idx, start_x, f"{item}")
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        tecla = stdscr.getch()

        # Detectar las teclas de flecha arriba y abajo
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < len(opciones_submenu) - 1:
            fila_actual += 1
        # Detectar la tecla Enter (10 es el valor ASCII de Enter)
        elif tecla == 10:
            if fila_actual == 0:
                ejercicio_taller_1_1(stdscr)
            elif fila_actual == 1:
                ejercicio_taller_1_2(stdscr)
            elif fila_actual == 2:
                ejercicio_taller_1_3(stdscr)
            elif fila_actual == 3:
                ejercicio_taller_1_4(stdscr)
            elif fila_actual == 4:
                ejercicio_taller_1_5(stdscr)
            elif fila_actual == 5:
                ejercicio_taller_1_6(stdscr)
            elif fila_actual == 6:
                ejercicio_taller_1_7(stdscr)
            elif fila_actual == 7:
                ejercicio_taller_1_8(stdscr)
            elif fila_actual == 8:
                ejercicio_taller_1_9(stdscr)
            elif fila_actual == 9:
                ejercicio_taller_1_10(stdscr)
            elif fila_actual == 10:
                ejercicio_taller_1_11(stdscr)
            elif fila_actual == 11:
                ejercicio_taller_1_12(stdscr)
            elif fila_actual == 12:
                ejercicio_taller_1_13(stdscr)
            elif fila_actual == 13:
                ejercicio_taller_1_14(stdscr)
            elif fila_actual == 14:
                ejercicio_taller_1_15(stdscr)
            elif fila_actual == 15:
                ejercicio_taller_1_16(stdscr)
            elif fila_actual == 16:
                ejercicio_taller_1_17(stdscr)
            elif fila_actual == 17:
                ejercicio_taller_1_18(stdscr)
            elif fila_actual == 18:
                ejercicio_taller_1_19(stdscr)
            elif fila_actual == 19:
                ejercicio_taller_1_20(stdscr)
            elif fila_actual == 20:
                break  # Regresar al menú anterior

    # APLICARA LA MISMA LOGICA DE FUNCIONAMIENTO PARA LOS OTROS MENUS O SUBMENUS

def sub_menu_evaluacion_1(stdscr):
    # Definir las opciones del submenú
    opciones_submenu = [
        "Punto 1", "Punto 2", "Punto 3", "Regresar"
    ]
    
    # Inicializar la fila actual en la primera opción
    fila_actual = 0

    while True:
        stdscr.clear()
        stdscr.refresh()

        max_height, max_width = stdscr.getmaxyx()
        menu_width = 40
        menu_height = len(opciones_submenu)
        start_y = (max_height - menu_height) // 2
        start_x = (max_width - menu_width) // 2

        for idx, item in enumerate(opciones_submenu):
            if idx == fila_actual:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(start_y + idx, start_x, f"{item}", curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(start_y + idx, start_x, f"{item}")
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        tecla = stdscr.getch()

        # Detectar las teclas de flecha arriba y abajo
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < len(opciones_submenu) - 1:
            fila_actual += 1
        # Detectar la tecla Enter (10 es el valor ASCII de Enter)
        elif tecla == 10:
            if fila_actual == 0:
                evaluacion_1_punto_1(stdscr)
            elif fila_actual == 1:
                evaluacion_1_punto_2(stdscr)
            elif fila_actual == 2:
                evaluacion_1_punto_3(stdscr)
            elif fila_actual == 3:
                break

def sub_menu_evaluacion_2(stdscr):
    # Definir las opciones del submenú
    opciones_submenu = [
        "Punto 1", "Punto 2", "Punto 3", "Regresar"
    ]
    
    # Inicializar la fila actual en la primera opción
    fila_actual = 0

    while True:
        stdscr.clear()
        stdscr.refresh()

        max_height, max_width = stdscr.getmaxyx()
        menu_width = 40
        menu_height = len(opciones_submenu)
        start_y = (max_height - menu_height) // 2
        start_x = (max_width - menu_width) // 2

        for idx, item in enumerate(opciones_submenu):
            if idx == fila_actual:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(start_y + idx, start_x, f"{item}", curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(start_y + idx, start_x, f"{item}")
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        tecla = stdscr.getch()

        # Detectar las teclas de flecha arriba y abajo
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < len(opciones_submenu) - 1:
            fila_actual += 1
        # Detectar la tecla Enter (10 es el valor ASCII de Enter)
        elif tecla == 10:
            if fila_actual == 0:
                evaluacion_2_punto_1(stdscr)
            elif fila_actual == 1:
                evaluacion_2_punto_2(stdscr)
            elif fila_actual == 2:
                evaluacion_2_punto_3(stdscr)
            elif fila_actual == 3:
                break
                  
def sub_menu_ejercicios_en_clase(stdscr):
    # Definir las opciones del submenú
    opciones_submenu = [
        "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4", "Ejercicio 5",
        "Ejercicio 6", "Ejercicio 7", "Ejercicio 8", "Ejercicio 9", "Ejercicio 10", "Regresar"
    ]
    
    # Inicializar la fila actual en la primera opción
    fila_actual = 0

    while True:
        stdscr.clear()
        stdscr.refresh()

        max_height, max_width = stdscr.getmaxyx()
        menu_width = 40
        menu_height = len(opciones_submenu)
        start_y = (max_height - menu_height) // 2
        start_x = (max_width - menu_width) // 2

        for idx, item in enumerate(opciones_submenu):
            if idx == fila_actual:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(start_y + idx, start_x, f"{item}", curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(start_y + idx, start_x, f"{item}")
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        tecla = stdscr.getch()

        # Detectar las teclas de flecha arriba y abajo
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < len(opciones_submenu) - 1:
            fila_actual += 1
        # Detectar la tecla Enter (10 es el valor ASCII de Enter)
        elif tecla == 10:
            if fila_actual == 0:
                ejercicio_en_clase_1(stdscr)
            elif fila_actual == 1:
                ejercicio_en_clase_2(stdscr)
            elif fila_actual == 2:
                ejercicio_en_clase_3(stdscr)
            elif fila_actual == 3:
                ejercicio_en_clase_4(stdscr)
            elif fila_actual == 4:
                ejercicio_en_clase_5(stdscr)
            elif fila_actual == 5:
                ejercicio_en_clase_6(stdscr)
            elif fila_actual == 6:
                ejercicio_en_clase_7(stdscr)
            elif fila_actual == 7:
                ejercicio_en_clase_8(stdscr)
            elif fila_actual == 8:
                ejercicio_en_clase_9(stdscr)
            elif fila_actual == 9:
                ejercicio_en_clase_10(stdscr)
            elif fila_actual == 10:
                break




#----------------------------------------------------------------------------------------------------------------------------------#
# Este es el menu general solamente para llamar funciones, para tener ordenado el menu interactivo por si se quiere modificar algo #
#----------------------------------------------------------------------------------------------------------------------------------#

def main(stdscr):
    # Inicializar curses
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Opciones del menú
    opciones_menu = ["Taller", "Evaluación Grupo 1", "Evaluación Grupo 2", "Ejercicios en clase", "Salir"]
    fila_actual = 0

    while True:
        stdscr.clear()
        stdscr.refresh()

        # Configuración de tamaño y posición del menú
        max_height, max_width = stdscr.getmaxyx()
        menu_width = 20
        menu_height = len(opciones_menu)
        start_y = (max_height - menu_height) // 2
        start_x = (max_width - menu_width) // 2

        for idx, item in enumerate(opciones_menu):
            if idx == fila_actual:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(start_y + idx, start_x, f"{item}", curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(start_y + idx, start_x, f"{item}")
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < len(opciones_menu) - 1:
            fila_actual += 1
        elif tecla == 10:
            if fila_actual == 0:
                sub_menu_taller(stdscr)
            if fila_actual == 1:
                sub_menu_evaluacion_1(stdscr)
            if fila_actual == 2:
                sub_menu_evaluacion_2(stdscr)
            if fila_actual == 3:
                sub_menu_ejercicios_en_clase(stdscr)
            elif fila_actual == 4:
                stdscr.clear()
                stdscr.addstr("""Saliendo del programa en 2 segundos...

Desarrollado por:

Andres Felipe Martinez Guerra""")
                stdscr.refresh()
                curses.napms(3000)  # Esperar 3 segundos
                break  # Salir

# Ejecuta la aplicación
curses.wrapper(main)
