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

# Iniciamos el menu con una funcion
def menu_inicio():
    while True: 
        print(Fore.LIGHTCYAN_EX + """
              
            ╔════════════════════════════════════════╗
            ║                                        ║
            ║           Bienvenido al Menú           ║
            ║                                        ║
            ╠════════════════════════════════════════╣
            ║                                        ║
            ║ Escoja una opción:                     ║
            ║                                        ║
            ║ 1. Taller                              ║                
            ║ 2. Evaluación Grupo 1                  ║
            ║ 3. Evaluación Grupo 2                  ║
            ║ 4. Ejercicios en clase                 ║
            ║ 5. Salir                               ║
            ║                                        ║
            ╚════════════════════════════════════════╝
              
        """ + Fore.RESET) # Reseteamos Fore para que el color vuelva al predeterminado

        try:
            respuesta = int(input(Fore.YELLOW + "Ingrese su elección: " + Fore.RESET))

            separador()
            
            if respuesta == 1:
                def menu_taller(): #Entramos al menu del taller
                    while True:
                        try:
                            respuesta_taller = int(input("""
                UNIVERSIDAD DE NARIÑO
                FACULTAD DE INGENIERÍA
                INGENIERIA DE INGENIERÍA
                Programación II
                                                        
                3.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.
                                                        
                4.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, formar un tercer vector
                    con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.
                                                        
                6.	Se tienen dos vectores con datos numéricos donde hay varios repetidos, formar un tercer vector
                    con la unión de solo números Fibonacci sin repetidos, sin tener en cuenta aquellos Fibonacci que sean comunes.
                                                        
                7.	Se tienen un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación
                    con sumas del primo que más se repite con el primo que menos se repite.
                                                        
                8.	Se tienen dos vectores con datos numéricos donde hay varios repetidos,
                    formar un tercer vector con la unión de solo números Fibonacci sin repetidos,
                    sin tener en cuenta aquellos Fibonacci que sean comunes.
                                                        
                9.	Se tienen un vector con datos numéricos donde hay varios repetidos,
                    hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.
                                                        
                10.	Intercambiar las columnas donde se encuentre el Fibonacci 2 con la fila 
                    donde se encuentra el Fibonacci 4 según el recorrido por filas de la matriz.
                                                        
                11.	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz,
                    son consecutivos, es decir, no hay un número primo entre los dos 
                                                        
                12.	Se tienen dos matrices cuadradas con datos numéricos formar dos conjuntos, conjunto uno
                    con los primos de las diagonales principales, conjunto 2 con los primos de las diagonales secundarias,
                    con estos dos conjuntos, encontrar los elementos comunes y formar un diccionario
                    con cada uno de estos valores como clave y su factorial como valor
                                                        
                13.	Se tiene un conjunto y una matriz con datos numéricos, hallar el primo mayor del conjunto
                    y su factorial y llenar este valor en las posiciones comprendidas
                    entre el par menor y el Fibonacci mayor de la matriz
                                                        
                14.	Se tiene un vector y una matriz con datos numéricos, formar un conjunto con
                    los múltiplos de cinco  y Fibonacci, ordenado ascendentemente. 
                                                        
                15.	Se tienen dos matrices con datos numéricos Formar un diccionario con los primos
                    como clave y las veces que aparecen como valor, ordenado por la clave.
                                                        
                16.	Se tiene una matriz con datos numéricos, formar un diccionario con clave Fibonacci y valor,
                    las veces que se repite y modificar el valor para aquellos contadores que son primos por su factorial
                                                        
                17.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
                    Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
                    Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave
                                                        
                18.	Se tiene un vector y una matriz formar conjuntos con los números primos de cada una 
                    y realizar las operaciones de conjuntos:    Unión
                                                                Intersección
                                                                Diferencia
                                                                Diferencia simétrica
                                                        
                19.	Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
                    el par mayor y las veces que se repite
                    el primo menor y las veces que se repite
                    el Fibonacci menor y las veces que se repite
                    Con estos datos hallar:
                    El factorial de la suma del par y del primo
                    La multiplicación con sumas de los contadores del primo y del Fibonacci.
                                                        
                20.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios así:
                    Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
                    Diccionario 2 con clave carácter y valor las veces que se repite, ordenado ascendentemente por clave 
                    Almacenar esta información en un archivo, recuperarla y mostrar los dos diccionarios.
                                                         
                21. Regresar...
                                                        
                """ + Fore.YELLOW + "¿Qué punto desea escoger a continuación:  " + Fore.RESET))
                            
                            separador()

                            if respuesta_taller == 3:

                                vector1 = [random.randint(1,50) for n in range(20)]
                                vector2 = [random.randint(1,50) for n in range(20)]

                                primos_comunes = []

                                for n in vector1:
                                    if es_primo(n):
                                        if n in vector2 and n not in primos_comunes:
                                            primos_comunes.append(n)
                                for n in vector2:
                                    if es_primo(n):
                                        if n in vector1 and n not in primos_comunes:
                                            primos_comunes.append(n)

                                print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\nPrimos comunes:\n{primos_comunes}\n")
                                limpiar()
                            if respuesta_taller == 4:

                                vector = [random.randint(1,50) for n in range(50)]

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

                                print(f"Vector original:\n{vector}\nLos primos entre el fibonacci mayor: {fibonacci_mayor} y el fibonacci menor: {fibonacci_menor} son:\n{primos_en_el_rango}")
                                limpiar()
                            if respuesta_taller == 6:
                                
                                vector1 = [random.randint(1,50) for n in range(20)]
                                vector2 = [random.randint(1,50) for n in range(20)]
                                vector3 = []

                                for n in vector1:
                                    if es_fibonacci(n):
                                        if n not in vector2 and n not in vector3:
                                            vector3.append(n)
                                for n in vector2:
                                    if es_fibonacci(n):
                                        if n not in vector1 and n not in vector3:
                                            vector3.append(n)
                                print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\nVector 3:\n{vector3}")
                                limpiar()
                            if respuesta_taller == 7:

                                vector = [random.randint(1,20) for n in range(20)]

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

                                print(f"\nVector original: \n{vector}\n")
                                print(f"La multiplicación con sumas del primo mas repetido: {primo_mas_repetido} con {primo_mas_repetido_repeticiones} repeticiones\npor el primo menos repetido: {primo_menos_repetido} con {primo_menos_repetido_repeticiones} repeticiones\nEs igual a: {suma}")
                                limpiar()
                            if respuesta_taller == 8:

                                vector1 = [random.randint(1,10) for n in range(10)]
                                vector2 = [random.randint(1,10) for n in range(10)]
                                vector3 = []

                                for n in vector1:
                                    if es_fibonacci(n) and n not in vector2 and n not in vector3:
                                        vector3.append(n)
                                for n in vector2:
                                    if es_fibonacci(n) and n not in vector1 and n not in vector3:
                                        vector3.append(n)

                                print(f"\nVector 1: {vector1}\nVector 2: {vector2}\nFibonaccis no comunes: {vector3}")
                                limpiar()
                            if respuesta_taller == 9:

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
                                    if repeticiones[i] > primo_menos_repetido_repeticiones:
                                        primo_menos_repetido_repeticiones = repeticiones[i]
                                        primo_mas_repetido = primos[i]
                                    if repeticiones[i] < primo_menos_repetido_repeticiones:
                                        primo_menos_repetido_repeticiones = repeticiones[i]
                                        primo_menos_repetido = primos[i]

                                condicion = 1
                                producto = 0
                                while condicion <= primo_mas_repetido:
                                    producto += primo_menos_repetido
                                    condicion += 1

                                print(f"\nVector: {vector}\nLa multiplicacion del primo mas repetido: {primo_mas_repetido}\n   Con el primo menos repetido: {primo_menos_repetido}\n\n es: {producto}")
                                limpiar()
                            if respuesta_taller == 10:

                                # Crear una matriz aleatoria de 5x5
                                matriz = [[random.randint(1, 35) for _ in range(5)] for _ in range(5)]
                                print("Matriz original:")
                                mostrar_matriz(matriz)

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

                                print(f"\nSegundo Fibonacci: {segundo} Posición: {posicion_segundo}")
                                print(f"Cuarto Fibonacci: {cuarto} Posición: {posicion_cuarto}")

                                # Intercambiar las columnas
                                for i in range(len(matriz)):
                                    matriz[i][posicion_segundo], matriz[i][posicion_cuarto] = matriz[i][posicion_cuarto], matriz[i][posicion_segundo]

                                print("\nMatriz modificada:")
                                mostrar_matriz(matriz)
                                limpiar()
                            if respuesta_taller == 11:

                                matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                                contador = 0

                                for i in range(len(matriz)):
                                    for j in range(len(matriz)):
                                        if es_primo(matriz[i][j]):
                                            contador += 1
                                            if contador == 2:
                                                segundo_primo = matriz[i][j]
                                            if contador == 4:
                                                cuarto_primo = matriz[i][j]

                                print("Matriz original")
                                mostrar_matriz(matriz)

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
                                            print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} NO son consecutivos")
                                            es_consecutivo = False
                                            break
                                        condicion += 1
                                    if es_consecutivo:
                                        print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} SI son consecutivos")
                                else:
                                    print(f"El segundo primo: {segundo_primo} y el cuarto primo: {cuarto_primo} NO son consecutivos")
                                limpiar()
                            if respuesta_taller == 12:

                                matriz1 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                                matriz2 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                                
                                def primos_diagonal_princiapal(matriz):
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
                                
                                conjunto1 = primos_diagonal_princiapal(matriz1) + primos_diagonal_princiapal(matriz2)
                                conjunto2 = primos_diagonal_secundaria(matriz1) + primos_diagonal_secundaria(matriz2)

                                print("Martiz 1")
                                mostrar_matriz(matriz1)

                                print("\nMartiz 2")
                                mostrar_matriz(matriz2)

                                print(f"\nPrimos diagonales primarias: {conjunto1}")
                                print(f"Primos diagonales secundarias: {conjunto2}")

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

                                print("\nDiccionario con elementos comunes como claves y sus factoriales:")
                                for elemento, factorial in diccionario.items():
                                    print(f"Elemento común: {elemento}, Factorial: {factorial}")

                                limpiar()
                            if respuesta_taller == 13:

                                vector = [random.randint(1,10) for i in range(10)]
                                matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                
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
                                        if es_par(matriz[i][j]):
                                            if matriz[i][j] < par_menor:
                                                par_menor = matriz[i][j]
                                                posicion_par_menor_columna = j
                                                posicion_par_menor_fila = i

                                print(f"Vector:\n{vector}\n")
                                print("Matriz")
                                mostrar_matriz(matriz)

                                print(f"\nPrimo mayor vector: {primo_mayor} Su factoria: {factorial_primo_mayor}")
                                print(f"Par menor matriz: {par_menor} posicion fila: {posicion_par_menor_fila+1} columna: {posicion_par_menor_columna+1}")
                                print(f"Fibonacci mayor matriz: {fibonacci_mayor} posicion fila: {posicion_fibonacci_mayor_fila+1} columna: {posicion_fibonacci_mayor_columna+1}")

                                #Matriz modificada dentro del rango del par menor al fibonacci mayor de la matriz con el factorial
                                matriz_modificada = matriz.copy()
                                for i in range(len(matriz_modificada)):
                                    for j in range(len(matriz_modificada)):
                                        if i >= posicion_par_menor_fila and i <= posicion_fibonacci_mayor_fila:
                                            if i == posicion_par_menor_fila:
                                                if j > posicion_par_menor_columna:
                                                    matriz_modificada[i][j] = factorial_primo_mayor
                                            if i == posicion_fibonacci_mayor_fila:
                                                if j < posicion_fibonacci_mayor_columna:
                                                    matriz_modificada[i][j] = factorial_primo_mayor
                                            if i > posicion_par_menor_fila and i < posicion_fibonacci_mayor_fila:
                                                matriz_modificada[i][j] = factorial_primo_mayor

                                print("\nMatriz Modificada")
                                mostrar_matriz(matriz_modificada)

                                limpiar()
                            if respuesta_taller == 14:

                                vector = [random.randint(1,20) for n in range(10)]
                                matriz = [[random.randint(1,20) for n in range(5)] for i in range(5)]
                                conjunto = set()

                                for n in vector:
                                    if es_multiplo_de_5(n):
                                        conjunto.add(n)
                                    if es_fibonacci(n):
                                        conjunto.add(n)

                                for fila in matriz:
                                    for n in fila:
                                        if es_multiplo_de_5(n):
                                            conjunto.add(n)
                                        if es_fibonacci(n):
                                            conjunto.add(n)

                                for i in range(len(conjunto)):
                                    for j in range(len(conjunto)-1-i):
                                        if conjunto[j] > conjunto[j+1]:
                                            conjunto[j], conjunto[j+1] = conjunto[j+1], conjunto[j]

                                print(f"Vector:\n{vector}")
                                print(f"\nMatriz:")
                                mostrar_matriz(matriz)

                                print(f"\nConjunto con fibonaccis y multiplos de 5:\n{conjunto}")

                                limpiar()
                            if respuesta_taller == 15:

                                matriz1 = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                                matriz2 = [[random.randint(1,20) for j in range(5)] for i in range(5)]

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

                                print("Matriz 1")
                                mostrar_matriz(matriz1)
                                separador()
                                print("Matriz 2")
                                mostrar_matriz(matriz2)
                                separador()

                                #Ordenamiento por clave con algoritmo
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

                                for primo, repeticiones in diccionario_ordenado.items():
                                    print(f"Primo: {primo}  Repeticiones: {repeticiones}")

                                limpiar()
                            if respuesta_taller == 16: 

                                matriz = [[random.randint(1,10) for j in range(5)] for i in range(5)]
                                diccionario = {}

                                for i in range(len(matriz)):
                                    for j in range(len(matriz)):
                                        if es_fibonacci(matriz[i][j]):
                                            if matriz[i][j] in diccionario:
                                                diccionario[matriz[i][j]] += 1
                                            else:
                                                diccionario[matriz[i][j]] = 1
                                print("Matriz")
                                mostrar_matriz(matriz)
                                separador()

                                for fibonacci, repeticiones in diccionario.items():
                                    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")
                                separador()

                                #Ahora cambiaremos las repeticiones que son los contadores por el factorial si es que el contador es primo
                                for fibonacci, repeticiones in diccionario.items():
                                    if es_primo(repeticiones):
                                        diccionario[fibonacci] = calcular_factorial(repeticiones)
                                print("Con los contadores primos por su factorial")
                                for fibonacci, repeticiones in diccionario.items():
                                    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")

                                #Esto no esta en el ejercicio pero es adicional
                                separador()
                                print("Esto no esta en el ejercicio pero es adicional")

                                #Crear un nuevo diccionario con claves convertidas en factoriales
                                nuevo_diccionario = {}
                                for fibonacci, repeticiones in diccionario.items():
                                    factorial_clave = calcular_factorial(fibonacci)
                                    nuevo_diccionario[factorial_clave] = repeticiones

                                #Reemplazar el diccionario original por el nuevo diccionario
                                diccionario = nuevo_diccionario
                                for fibonacci, repeticiones in diccionario.items():
                                    print(f"Fibonacci: {fibonacci}  Repeticioness: {repeticiones}")

                                limpiar()
                            if respuesta_taller == 17:

                                cadena1 = "Hola Mundo 2023"
                                cadena2 = "Universidad de Nariño semestre 2"
                                cadena3 = "Numero de estudiantes aproximadamente 35000"
                                cadenatotal = cadena1 + cadena2 + cadena3

                                diccionario1 = {}
                                diccionario2 = {}

                                for caracter in cadenatotal:
                                    if caracter.isnumeric():
                                        if caracter in diccionario1:
                                            diccionario1[caracter] += 1
                                        else:
                                            diccionario1[caracter] = 1
                                    if caracter.isalpha():
                                        caracter = caracter.lower()
                                        if caracter in diccionario2:
                                            diccionario2[caracter] += 1
                                        else:
                                            diccionario2[caracter] = 1

                                # Ordenar diccionario1 por valor (repeticiones) usando el algoritmo de burbuja
                                valores = list(diccionario1.values())
                                claves = list(diccionario1.keys())
                                for i in range(len(valores)):
                                    for j in range(len(valores) - i - 1):
                                        if valores[j] > valores[j + 1]:
                                            valores[j], valores[j + 1] = valores[j + 1], valores[j]
                                            claves[j], claves[j + 1] = claves[j + 1], claves[j]

                                # Reorganizar diccionario1 con claves y valores ordenados
                                diccionario1 = {}
                                for i in range(len(claves)):
                                    diccionario1[claves[i]] = valores[i]

                                # Ordenar diccionario2 por clave usando el algoritmo de burbuja
                                claves2 = list(diccionario2.keys())
                                for i in range(len(claves2)):
                                    for j in range(len(claves2) -i -1):
                                        if claves2[j] > claves2[j + 1]:
                                            claves2[j], claves2[j + 1] = claves2[j + 1], claves2[j]

                                # Crear un nuevo diccionario2 ordenado por clave
                                diccionario2_ordenado = {k: diccionario2[k] for k in claves2}

                                print("Repeticiones de números")
                                for numero, repeticiones in diccionario1.items():
                                    print(f"Número: {numero}  Repeticiones: {repeticiones}")

                                print("Repeticiones de Letras")
                                for letra, repeticiones in diccionario2_ordenado.items():
                                    print(f"Letra: {letra}  Repeticiones: {repeticiones}")

                                limpiar()
                            if respuesta_taller == 18:

                                vector = [random.randint(1,10) for i in range(10)]
                                matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]

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

                                # Imprimir los resultados
                                print("Unión:", union)
                                print("Intersección:", interseccion)
                                print("Diferencia:", diferencia)
                                print("Diferencia simétrica:", diferencia_simetrica)

                                limpiar()
                            if respuesta_taller == 19:
                                
                                vector = [random.randint(1,20) for i in range(10)]
                                matriz = [[random.randint(1,20) for j in range(5)] for i in range(5)]
                                
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

                                #Repeticiones
                                diccionario = {}
                                for numero in vector:
                                    #Usa los or de esta manera porque el diccionario solo permite una entrada por clave
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

                                print(f"Vector:\n{vector}\n")
                                separador()
                                print("Matriz")
                                mostrar_matriz(matriz)
                                separador()

                                for numero, repeticiones in diccionario.items():
                                    if numero == par_mayor:
                                        print(f"Par mayor: {par_mayor} Repeticiones: {repeticiones}")
                                    if numero == fibonacci_menor:
                                        repeticiones_fibonacci = repeticiones
                                        print(f"Fibonacci menor: {fibonacci_menor} Repeticiones: {repeticiones}")
                                    if numero == primo_menor:
                                        repeticiones_primo = repeticiones
                                        print(f"Primo menor: {primo_menor} Repeticiones: {repeticiones}")

                                #Factorial suma par primo
                                factorial_par_mas_primo = calcular_factorial(par_mayor + primo_menor)
                                print(f"\nFactorial de {primo_menor} + {par_mayor} = {factorial_par_mas_primo}")

                                condicion = 1
                                suma = 0
                                while condicion <= repeticiones_fibonacci:
                                    suma += repeticiones_primo
                                    condicion += 1
                                
                                #multiplicación con sumas de los contadores del primo y del Fibonacci
                                print(f"Multiplicacion de {repeticiones_fibonacci} x {repeticiones_primo} = {suma}")

                                limpiar()
                            if respuesta_taller == 20:
                                
                                cadena1 = input("Ingrese una cadena de texto")
                                cadena2 = input("Ingrese la segunda cadena de texto")
                                cadena3 = input("Ingrese la tercera cadena de texto")
                                separador()
                                print(f"Cadena 1: {cadena1}\nCadena 2: {cadena2}\nCadena 3: {cadena3}")
                                separador()
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

                                #Ordenar diccionario 1 por valor, es decir las repeticiones, usando el algoritmo burbuja
                                repeticiones = list(diccionario1.values())
                                numeros = list(diccionario1.keys())
                                for i in range(len(repeticiones)):
                                    for j in range(len(repeticiones)-i-1):
                                        if repeticiones[j] > repeticiones[j+1]:
                                            repeticiones[j], repeticiones[j+1] = repeticiones[j+1], repeticiones[j]
                                            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

                                #Creo el diccionario de nuevo para reubicar los valores
                                diccionario1 = {}
                                for i in range(len(numeros)):
                                    diccionario1[numeros[i]] = repeticiones[i]

                                #Ordenar el diccionario 2 por claves, es decir las letras y mostrar sus repetciones
                                letras = list(diccionario2.keys())
                                repeticiones = list(diccionario2.values())
                                for i in range(len(letras)):
                                    for j in range(len(letras)-i-1):
                                        if letras[j] > letras[j+1]:
                                            letras[j], letras[j+1] = letras[j+1], letras[j]
                                            repeticiones[j], repeticiones[j+1] = repeticiones[j+1], repeticiones[j]
                                            
                                diccionario2 = {letra: diccionario2[letra] for letra in letras}

                                print("Diccionario 1 con los numeros y sus repeticiones:")
                                for numero, repeticiones in diccionario1.items():
                                    print(f"Numero: {numero} Repeticiones: {repeticiones}")

                                print("\nDiccionario dos con letras y repeticiones: ")
                                for letra, repeticiones in diccionario2.items():
                                    print(f"Letra: {letra} Repeticiones: {repeticiones}")

                                limpiar()
                            if respuesta_taller == 21:
                                break
                            if respuesta_taller < 1 or respuesta_taller > 21:
                                separador()
                                print("Esa opción no existe en el menú, intente con otra")
                                limpiar()
                        except ValueError:
                            separador()
                            print("Ingrese un valor valido")
                            limpiar()
                menu_taller()
            if respuesta == 2:
                def menu_evaluacion_grupo1():
                    while True:
                        try:
                            respuesta_menu_evaluacion_grupo1 = int(input("""
                UNIVERSIDAD DE NARIÑO
                FACULTAD DE INGENIERÍA
                INGENIERIA DE SISTEMAS
                PROGRAMACIÓN II
                EVALUACIÓN 1

                1.	Se tiene un vector y una matriz con datos numéricos, buscar un dato en el vector que tiene estas condiciones:
                    El dato es el segundo Fibonacci de un rango en un vector cuyos límites están determinados por el primo1 y primo2
                    presentes en el rango de la matriz comprendido entre el mayor y el menor es esta.
                    Mostrar el dato y su posición.

                2.	Se tiene un diccionario con la siguiente información
                    Clave numero entero
                    Valor lista de números
                    Hallar la clave del primo mayor y Fibonacci menor que están en las listas de los valores y
                    formar una lista con los pares comprendidos entre estos dos valores y el promedio de estos.
                                                                        
                3.	Se tiene un diccionario con la siguiente información
                    Clave numero entero
                    Valor lista de números
                    Formar dos conjuntos asi:
                    Conjunto 1 con los número pares de la lista valor de aquellas claves que son primos 
                    Conjunto 2 con los número pares de la lista valor de aquella claves que son fibonacci
                    Con estos dos conjuntos formar dos cadenas
                    Cadena1 con los pares comunes
                    Cadena2 con la unión de los pares sin elementos comunes

                4.  Regresar...
                                                                         
                """ + Fore.YELLOW + "¿Qué punto desea escoger a continuación:  " + Fore.RESET))
                            
                            separador()

                            if respuesta_menu_evaluacion_grupo1 == 1:

                                def punto_1_1():

                                    lista_numeros = [random.randint(1,20) for n in range(10)]
                                    matriz_numeros= [[random.randint(1,20) for n in range(5)] for i in range(5)]
                                    print("Matriz de números:")
                                    for fila in matriz_numeros:
                                        print(fila)

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
                                    segundo_fibonacci = 0
                                    i_segundo_fibonacci = 0

                                    for i in range(len(lista_numeros)):
                                        if segundo_primo < lista_numeros[i] and es_fibonacci(lista_numeros[i]):
                                            contador += 1
                                            if contador == 2:
                                                segundo_fibonacci = lista_numeros[i]
                                                i_segundo_fibonacci = i

                                    print(f"El segundo número Fibonacci en el rango entre el primer y segundo número primo de la matriz es: {segundo_fibonacci} y su posición en la lista es: {i_segundo_fibonacci}")
                                punto_1_1()
                                limpiar()
                            if respuesta_menu_evaluacion_grupo1 == 2:

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
                                    for i in range(min_clave, max_clave):
                                        if i % 2 == 0:
                                            numeros_pares.append(i)
                                    return numeros_pares

                                diccionario_aleatorio = generar_diccionario_aleatorio()
                                print(f"Diccionario generado aleatoriamente: {diccionario_aleatorio}")

                                mayor_primo, clave_mayor_primo = encontrar_mayor_primo_en_diccionario(diccionario_aleatorio)
                                menor_fibonacci, clave_menor_fibonacci = encontrar_menor_fibonacci_en_diccionario(diccionario_aleatorio)

                                print(f"El número primo mayor es {mayor_primo} y se encuentra en la clave {clave_mayor_primo}")
                                print(f"El número de Fibonacci menor es {menor_fibonacci} y se encuentra en la clave {clave_menor_fibonacci}")

                                numeros_pares_entre_claves = encontrar_numeros_pares_entre_claves(clave_mayor_primo, clave_menor_fibonacci)
                                print(f"Números pares entre las claves {clave_mayor_primo} y {clave_menor_fibonacci}: {numeros_pares_entre_claves}")

                                limpiar()
                            if respuesta_menu_evaluacion_grupo1 == 3:
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

                                    return conjunto1, conjunto2, cadena1, cadena2, claves_primos, claves_fibonacci

                                def generar_diccionario_aleatorio():
                                    diccionario = {}
                                    for _ in range(4):
                                        clave = random.randint(1, 20)
                                        valores = [random.randint(1, 20) for _ in range(random.randint(3, 5))]
                                        diccionario[clave] = valores
                                    return diccionario

                                diccionario_aleatorio = generar_diccionario_aleatorio()

                                conjunto1, conjunto2, cadena1, cadena2, claves_primos, claves_fibonacci = formar_cadenas_con_pares_comunes(diccionario_aleatorio)
                                print("Diccionario aleatorio:", diccionario_aleatorio)
                                print(f"Conjunto 1 (Pares en claves primos {', '.join([str(clave) for clave in claves_primos])}):", conjunto1)
                                print(f"Conjunto 2 (Pares en claves Fibonacci {', '.join([str(clave) for clave in claves_fibonacci])}):", conjunto2)
                                print("Cadena 1 (pares comunes):", cadena1)
                                print("Cadena 2 (unión de pares):", cadena2)
                                limpiar()
                            if respuesta_menu_evaluacion_grupo1 == 4:
                                break
                            if respuesta_menu_evaluacion_grupo1 < 1 or respuesta_menu_evaluacion_grupo1 > 4:
                                separador()
                                print("Esa opción no existe en el menú, intente con otra")
                                limpiar()
                        except ValueError:
                            separador()
                            print("Ingrese un valor valido")
                            limpiar()
                menu_evaluacion_grupo1()
            if respuesta == 3:
                def menu_evaluacion_grupo2():
                    while True:
                        try:
                            respuesta_menu_evaluacion_grupo2 = int(input("""
                UNIVERSIDAD DE NARIÑO
                FACULTAD DE INGENIERÍA
                INGENIERIA DE SISTEMAS
                PROGRAMACIÓN II
                EVALUACIÓN 1



                1.	Se tiene un vector y una matriz con datos numéricos
                    Buscar un dato en una matriz.
                    El dato es el segundo primo de un rango de la matriz cuyos límites están determinados por el
                    Fibonacci 1 y 2 del rango del vector determinado por el número mayor y menor de este.
                    Mostrar el dato y su posición

                2.	Se tiene un diccionario con la siguiente información
                    Clave numero entero
                    Valor lista de números
                    Modificar las claves de la clave mayor y la clave menor con la siguiente información:
                    Clave mayor: conjunto1
                    Clave menor: conjunto2
                    Los  conjuntos están formados así:
                    Conjunto 1 con los número primos presentes en las diferentes listas sin repetidos 
                    Conjunto 2 con los número Fibonacci de las diferentes listas de valores sin repetidos
                                                                        
                3.	Se tiene un diccionario con la siguiente información
                    Clave numero entero
                    Valor lista de números
                    Ordenar las listas de los valores asi:
                    En orden ascendente aquellas claves que sean primos
                    En orden descendente aquellas claves que sen Fibonacci
                    Primero se ordenan primos y luego Fibonacci con los que resten, es decir, no se vuelven a ordenar los Fibonacci que son primos
                
                4.  Regresar...
                                                                         
                """ + Fore.YELLOW + "¿Qué punto desea escoger a continuación:  " + Fore.RESET))
                            
                            separador()

                            if respuesta_menu_evaluacion_grupo2 == 1:
                                list = [7,7,10,4,8,4,5,6,4,2,4,4]
                                print(f"lista ingresada {list}")
                                matriz = [
                                    [4,3,5,4],
                                    [4,7,4,3],
                                    [4,4,4,4],
                                    [4,4,8,4]
                                ]
                                print("matriz ingresada :")
                                for i in matriz:
                                    print(i)
                                may = None
                                men = None
                                for i in range(len(list)):
                                    if may is None or list[i] > may:
                                        may = list[i]
                                        may_i = i
                                    if men is None or list[i] < men:
                                        men = list[i]
                                        men_i = i
                                cont = 0
                                fibo_1 = 0
                                fibo_2 = 0
                                if may_i < men_i:
                                    while may_i < len(list):
                                        if es_fibonacci(list[may_i]):
                                            cont +=1
                                            if cont == 1:
                                                fibo_1 = list[may_i]
                                            elif cont == 2:
                                                fibo_2 = list[may_i]
                                        may_i += 1
                                for i in range(len(matriz)):
                                    for j in range(len(matriz[0])):
                                        if matriz[i][j] == fibo_1:
                                            i_1 = i
                                            j_1 = j
                                        if matriz[i][j] == fibo_2:
                                            i_2 = i
                                            j_2 = j
                                if i_1 < i_2:
                                    b = 0
                                    cont = 0
                                    i = i_1+1
                                    while i < len(matriz)-1 and b == 0:
                                        while j_1 < len(matriz[0]) and b == 0:
                                            if i_1 == i_2 and j_1 == j_2:
                                                b = 1
                                            else:
                                                if es_primo(matriz[i_1][j_1]):
                                                    cont +=1
                                                    
                                                    if cont == 2:
                                                        primo_2 = matriz[i_1][j_1]
                                                        primo_i = i_1
                                                        primo_j = j_1
                                                        
                                            j_1 +=1
                                        j_1 = 0
                                        i_1 +=1
                                else:
                                    if i_2 < i_1:
                                        b = 0
                                        cont = 0
                                        j_2 =j_2 + 1
                                        while i_2 < len(matriz) and b == 0:
                                            while j_2 < len(matriz[0]) and b == 0:
                                                if i_2 == i_1 and j_2 == j_1:
                                                    b = 1
                                                else:
                                                    if es_primo(matriz[i_2][j_2]):
                                                        cont +=1
                                                        if cont == 1:
                                                            print(matriz[i_2][j_2])
                                                        if cont == 2:
                                                            primo_2 = matriz[i_2][j_2]
                                                            primo_i = i_2
                                                            primo_j = j_2
                                                            
                                                j_2 +=1
                                            j_2 = 0
                                            i_2 +=1

                                print(f"el primo es : {primo_2} y sus posicion es {primo_i},{primo_j}")
                                limpiar()
                            if respuesta_menu_evaluacion_grupo2 == 2:
                                
                                dic = {
                                    5: [4,7,7,5],
                                    12: [9,13,8,8],
                                    8: [5,5,4,34,2],
                                    2: [9,5,11,11,2]
                                }
                                print(f"diccionario ingresado : {dic}")
                                key_may = max(dic.keys())
                                key_men = min(dic.keys())
                                set_1 = set()
                                set_2 = set()
                                for lista in dic.values():
                                    for num in lista:
                                        if es_primo(num):
                                            set_1.add(num)
                                        if es_fibonacci(num):
                                            set_2.add(num)

                                dic[key_may] = set_1
                                dic[key_men] = set_2
                                print(key_may)
                                print(key_men)
                                print(dic)

                                limpiar()
                            if respuesta_menu_evaluacion_grupo2 == 3:
                                dic = {
                                    4: [3,2,9,6],
                                    5: [14,10,2,7],
                                    8: [2,9,4,6],
                                    11: [20,10,5,30],
                                    13: [20,12,4],
                                    21: [7,2,9],
                                    3: [4,8,3],  
                                }
                                print(f"diccionario ingresado : {dic}")
                                for key, lista in dic.items():
                                    if es_primo(key):
                                        list_orden = sorted(lista)
                                        dic[key] = list_orden
                                    if es_fibonacci(key) and not es_primo(key):
                                        list_orden = sorted(lista, reverse=True)
                                        dic[key] = list_orden
                                print (dic)

                                limpiar()
                            if respuesta_menu_evaluacion_grupo2 == 4:
                                break
                            if respuesta_menu_evaluacion_grupo2 < 1 or respuesta_menu_evaluacion_grupo2 > 4:
                                separador()
                                print("Esa opción no existe en el menú, intente con otra")
                                limpiar()
                        except ValueError:
                            separador()
                            print("Ingrese un valor valido")
                            limpiar()
                menu_evaluacion_grupo2()
            if respuesta == 4:
                def menu_ejercicios_en_clase():
                    while True:
                        try:
                            respuesta_menu_ejericicios_en_clase = int(input("""
                1.  Se tiene dos listas con datos, formar dos listas asi
                    lista 1 con los primos no comunes de las dos listas sin repetidos
                    lista 2 con los imapres comunes de las dos listas sin repetidos
                                                                            
                2.  Una lista que contenga todos los números perfectos en ambas matrices sin duplicados.
                                                                            
                3.  Se tiene una lista de datos, formar dos listas asi
                    lista 1 con los primos sin repetids y lista 2 con los fibonaccis sin repetidos
                                                                            
                4.  Se tiene una matriz y un vector con datos, sacar listas asi
                    Lista 1 con los numeros no comunes sin repetidos
                    lista 2 con los primos no repetidos
                                                                            
                5.  Se tiene una lista con datos numericos repetidos, formar un diccionario
                    con clave el numero y con valor las veces que se repite
                                                                            
                6.  Se tienen dos listas con datos numericos, formar dos diccionarios asi
                    Diccionario 1 con claves, primos comunes de las dos listas
                    Y valor el factorial de la clave, Diccionario 2 con clave fibonaccis
                    no comunes de las dos listas y valor los pares menores que el fibonacci clave
                                                                            
                7.  Se tiene una cadena, donde hay caracteres numericos y alfabeticos
                    formar dos diccionarios asi: diccionario 1 clave digito valor las veces que se repite
                    diccionario dos clave letra y valor las veces que aparece

                8.  Determinar cuantas palabras hay en un párrafo.
                                                                            
                9.  Reemplazar un caracter de una cadena por otro carácter dado.
                                                                            
                10. Se tiene una cadena. Encontrar el carácter que mas se repite.

                11. Regresar...
                                                                                                                                
                """ + Fore.YELLOW + "¿Qué punto desea escoger a continuación:  " + Fore.RESET))
                            
                            separador()

                            if respuesta_menu_ejericicios_en_clase == 1:
                                lista1 = [random.randint(1,50) for i in range(20)]
                                lista2 = [random.randint(1,50) for i in range(20)]

                                print(f"Lista 1:\n{lista1}")
                                print(f"Lista 2:\n{lista2}")

                                primos_no_comunes = []
                                impares_comunes = []

                                #Identificar los primos no comunes de las dos listas
                                for i in range(len(lista1)):
                                    if es_primo(lista1[i]):
                                        if lista1[i] not in lista2 and lista1[i] not in primos_no_comunes:
                                            primos_no_comunes.append(lista1[i])
                                for j in range(len(lista2)):
                                    if es_primo(lista2[j]):
                                        if lista2[j] not in lista1 and lista2[j] not in primos_no_comunes:
                                            primos_no_comunes.append(lista2[j])

                                for i in range(len(primos_no_comunes)):
                                    for j in range(len(primos_no_comunes)-i-1):
                                        if primos_no_comunes[j] > primos_no_comunes[j+1]:
                                            temporal = primos_no_comunes[j]
                                            primos_no_comunes[j] = primos_no_comunes[j+1]
                                            primos_no_comunes[j+1] = temporal
                                print(f"Primos no comunes de las dos listas:\n{primos_no_comunes}")

                                #identificar los impares comunes de las dos listas
                                for i in range(len(lista1)):
                                    if es_impar(lista1[i]):
                                        if lista1[i] in lista2 and lista1[i] not in impares_comunes:
                                            impares_comunes.append(lista1[i])

                                for i in range(len(impares_comunes)):
                                    for j in range(len(impares_comunes)-i-1):
                                        if impares_comunes[j] > impares_comunes[j+1]:
                                            temporal = impares_comunes[j]
                                            impares_comunes[j] = impares_comunes[j+1]
                                            impares_comunes[j+1] = temporal
                                print(f"Impares comunes de las dos listas:\n{impares_comunes}")

                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 2:
                                
                                dimensiones = random.randint(5, 10)

                                matriz1 = hacer_matriz(dimensiones)
                                matriz2 = hacer_matriz(dimensiones)

                                print("\nMatriz 1:")
                                mostrar_matriz(matriz1)
                                print("\nMatriz 2:")
                                mostrar_matriz(matriz2)

                                numeros_perfectos = []

                                for fila in matriz1:
                                    for numero in fila:
                                        if es_perfecto(numero) and numero not in numeros_perfectos:
                                            numeros_perfectos.append(numero)

                                for fila in matriz2:
                                    for numero in fila:
                                        if es_perfecto(numero) and numero not in numeros_perfectos:
                                            numeros_perfectos.append(numero)

                                print("\nNúmeros perfectos en ambas matrices:")
                                print(numeros_perfectos)
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 3:

                                lista = [random.randint(1,50) for _ in range(20)]
                                fibonaccis = []
                                primos = []
                                
                                for numero in lista:
                                    if es_fibonacci(numero) and numero not in fibonaccis:
                                        fibonaccis.append(numero)
                                    if es_primo(numero) and numero not in primos:
                                        primos.append(numero)

                                print(f"Lista original:\n{lista}")
                                print(f"Lista de primos:\n{primos}")
                                print(f"Lista de fibonaccis:\n{fibonaccis}")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 4:
                                #Vector con numeros random
                                vector = [random.randint(1,50) for n in range(20)]
                                
                                #Las dimensiones que le vamos a dar a la matriz, en este caso será cuadrada
                                dimensiones = random.randint(2,5)

                                #Hacemos la matriz
                                matriz = hacer_matriz(dimensiones)

                                #Mostramos el vector
                                print(f"Vector:\n{vector}")
                                #Mostramos la matriz
                                mostrar_matriz(matriz)


                                #Lista 1 con los numeros no comunes sin repetidos
                                lista1 = []
                                #Verificar y agregar números de la matriz que no están en vector ni en lista1
                                numeros_matriz = []
                                for fila in matriz:
                                    for numero in fila:
                                        #Metemos los numeros de la matriz en un vector lineal
                                        numeros_matriz.append(numero)
                                #Verificamos que los numeros del vector no esten en la matriz
                                for numero in vector:
                                    if numero not in numeros_matriz and numero not in lista1:
                                        lista1.append(numero)
                                #Verificamos que los numeros de la matriz no esten en el vector
                                for numero in numeros_matriz:
                                    if numero not in vector and numero not in lista1:
                                        lista1.append(numero)
                                #Mostramos la lista 1 con los numeros no comunes
                                print(f"\nLista 1 con los numeros no comunes sin repetidos:\n{lista1}")

                                #Lista 2 con lo primos no repetidos
                                lista2 = []
                                #Verificar y agregar primos de la matriz y el vector siempre que no se repitan 
                                for i in range(len(numeros_matriz)):
                                    repeticiones = 0
                                    if es_primo(numeros_matriz[i]):
                                        for j in numeros_matriz:
                                            #Comprobamos si no se repite en la matriz
                                            if j == numeros_matriz[i]:
                                                repeticiones += 1
                                        #Si se repite una vez es porque se comparo asi mismo y verificamos que no este en el vector
                                        if repeticiones == 1 and numeros_matriz[i] not in vector:
                                            lista2.append(numeros_matriz[i])
                                #Hacemos lo mismo pero con el vector ahora
                                for i in range(len(vector)):
                                    repeticiones = 0
                                    if es_primo(vector[i]):
                                        for j in vector:
                                            if j == vector[i]:
                                                repeticiones += 1
                                        if repeticiones == 1 and vector[i] not in numeros_matriz:
                                            lista2.append(vector[i])
                                #Mostramos la lista 2 con los primos no repetidos
                                print(f"\nLista 2 con los primos que no se repiten:\n{lista2}")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 5:

                                vector = [random.randint(1,10) for i in range(10)]
                                diccionario = {}

                                for i in vector:
                                    if i in diccionario:
                                        diccionario[i] += 1
                                    else:
                                        diccionario[i] = 1

                                print(f"Vector:\n{vector}\n")

                                for numero, repeticiones in diccionario.items():
                                    print(f"Numero:  {numero}   Repeticiones:  {repeticiones}")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 6:

                                vector1 = [random.randint(1,20) for n in range(10)]
                                vector2 = [random.randint(1,20) for n in range(10)]
                                diccionario1 = {}
                                diccionario2 = {}
                                
                                #Diccionario 1 con primos comunes de clave y de valor el factorial de su clave
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

                                print(f"Vector 1:\n{vector1}\nVector 2:\n{vector2}\n")
                                print("Diccionario 1 con primo y su factorial")

                                for primo, factorial in diccionario1.items():
                                    print(f"Primo:  {primo}  Factorial:  {factorial}")
                                #Diccionario 2 con fibonaccis no comunes de clave y los pares menores que el fibonacci de valor
                                for i in vector1:
                                    if i not in vector2:
                                        if es_fibonacci(i):
                                            pares_menores = []
                                            for k in vector1:
                                                if es_par(k) and k < i and k not in pares_menores:
                                                    pares_menores.append(k)
                                            for k in vector2:
                                                if es_par(k) and k  < i and k not in pares_menores:
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
                                                if es_par(k) and k  < i and k not in pares_menores:
                                                    pares_menores.append(k)
                                            if i not in diccionario2:
                                                diccionario2[i] = pares_menores

                                print("\nFibonaccis y pares menores que el fibonacci")
                                for fibonacci, pares_menores in diccionario2.items():
                                    print(f"Fibonacci:  {fibonacci}  Pares menores:  {pares_menores}")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 7:
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

                                print(f"Cadena de letras:\n{vector}\n")
                                print("Diccionario 1 (dígitos y repeticiones):")

                                for clave, valor in diccionario1.items():
                                    print(f"Numero: {clave}, Repeticiones: {valor}")

                                print("\nDiccionario 2 (letras y repeticiones):")
                                for clave, valor in diccionario2.items():
                                    print(f"Letra: {clave}, Repeticiones: {valor}")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 8:
                                # Obtiene el párrafo del usuario o desde algún otro origen
                                parrafo = input("Ingresa el párrafo: ")

                                # Divide el párrafo en palabras usando el espacio en blanco como separador
                                palabras = parrafo.split()

                                # Cuenta la cantidad de palabras en el párrafo
                                cantidad_palabras = len(palabras)

                                print(f"El párrafo contiene {cantidad_palabras} palabras.")
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 9:
                                # Solicita al usuario que ingrese la cadena original
                                cadena_original = input("Ingresa la cadena original: ")

                                # Solicita al usuario que ingrese el carácter a reemplazar
                                caracter_a_reemplazar = input("Ingresa el carácter que deseas reemplazar: ")

                                # Solicita al usuario que ingrese el nuevo carácter
                                nuevo_caracter = input("Ingresa el nuevo carácter con el que deseas reemplazar: ")

                                # Realiza el reemplazo utilizando un bucle
                                cadena_modificada = ""
                                for caracter in cadena_original:
                                    if caracter == caracter_a_reemplazar:
                                        cadena_modificada += nuevo_carácter
                                    else:
                                        cadena_modificada += caracter

                                # Imprime la cadena modificada
                                print("Cadena original:", cadena_original)
                                print("Cadena modificada:", cadena_modificada)
                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 10:
                                # Solicita al usuario que ingrese una cadena
                                cadena = input("Ingresa una cadena: ")

                                # Crea un diccionario para realizar un seguimiento del recuento de cada carácter
                                contador_caracteres = {}

                                # Recorre la cadena y cuenta la frecuencia de cada carácter
                                for caracter in cadena:
                                    if caracter in contador_caracteres:
                                        contador_caracteres[caracter] += 1
                                    else:
                                        contador_caracteres[caracter] = 1

                                # Encuentra el carácter con el recuento más alto
                                caracter_mas_repetido = ""
                                max_repeticiones = 0

                                for caracter, repeticiones in contador_caracteres.items():
                                    if repeticiones > max_repeticiones:
                                        caracter_mas_repetido = caracter
                                        max_repeticiones = repeticiones

                                # Imprime el resultado
                                if caracter_mas_repetido:
                                    print(f"En la cadena ingresada, el carácter que más se repite es '{caracter_mas_repetido}' con {max_repeticiones} repeticiones.")
                                else:
                                    print("La cadena está vacía, no hay caracteres para contar.")

                                limpiar()
                            if respuesta_menu_ejericicios_en_clase == 11:
                                break
                            if respuesta_menu_ejericicios_en_clase < 1 or respuesta_menu_ejericicios_en_clase > 14:
                                separador()
                                print("Esa opción no existe en el menú, intente con otra")
                                limpiar()
                        except ValueError:
                            separador()
                            print("Ingrese un valor valido")
                            limpiar()
                menu_ejercicios_en_clase()
            if respuesta == 5:
                print(Fore.LIGHTCYAN_EX + """
                      
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║              ¡Hasta Luego!             ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║           Desarrollado por:            ║
                ║     Andrés Felipe Martínez Guerra      ║
                ║                                        ║
                ║                                        ║
                ║         UNIVERSIDAD DE NARIÑO          ║
                ║         FACULTA DE INGENIERÍA          ║
                ║         INGENIERIA DE SISTEMAS         ║
                ║                  2023                  ║
                ║                                        ║
                ╚════════════════════════════════════════╝
                      
                """ + Fore.RESET)
                return
            if respuesta < 1 or respuesta > 5:
                print("Esa opción no existe en el menú, intente con otra")
                limpiar()
        except ValueError:
            separador()
            print("Ingrese un valor valido")
            limpiar()
init(autoreset=True) 
menu_inicio()