from colorama import init, Fore
from MenusInteractivos import *
from Funciones import *
import os

#Abriri terminal...
#digitar        pip install colorama
#               pip install tabulate

abrir_menu = Menus()

def menu_principal():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("menu principal")
        print("""
        1.  Sistema de peliculas
        2.  Sistema de confiteria
        3.  Sistema de ventas
        4.  Informacion ventas
        5.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                sistema_de_peliculas()
            elif opcion_seleccionada == 2:
                sistema_de_confiteria()
            elif opcion_seleccionada == 3:
                sistema_de_ventas()
            elif opcion_seleccionada == 4:
                informacion_ventas()
            elif opcion_seleccionada == 5:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")


def sistema_de_peliculas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de peliculas")
        print("""
        1.  Agregar nuevas peliculas
        2.  Eliminar peliculas
        3.  Manejo de salas
        4.  Ver cartelera y cronograma
        5.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.agregar_peliculas()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_peliculas()
            elif opcion_seleccionada == 3:
                menu_salas()
            elif opcion_seleccionada == 4:
                abrir_menu.mostrar_cartelera_y_cronograma()
            elif opcion_seleccionada == 5:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def menu_salas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de peliculas")
        print("""
        1.  Asignacion de salas
        2.  Deshacer asignacion de sala
        3.  Modificar una asignacion
        4.  Salir   
                    """)
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.asignar_salas()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_salas()
            elif opcion_seleccionada == 3:
                abrir_menu.modificar_salas()
            elif opcion_seleccionada == 4:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def sistema_de_confiteria():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de confiteria")
        print("""
        1.  Agregar producto
        2.  Eliminar producto
        3.  Modificar producto
        4.  Administracion de combos
        5.  Mostrar productos y combos
        6.  Consultar ventas confiteria
        7.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.agregar_producto()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_producto()
            elif opcion_seleccionada == 3:
                abrir_menu.modificar_producto()
            elif opcion_seleccionada == 4:
                administracion_de_combos()
            elif opcion_seleccionada == 5:
                pass
            elif opcion_seleccionada == 6:
                pass
            elif opcion_seleccionada == 7:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def administracion_de_combos():
    pass

def sistema_de_ventas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de ventas")

def informacion_ventas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de informacion y estadisticas")


menu_principal()