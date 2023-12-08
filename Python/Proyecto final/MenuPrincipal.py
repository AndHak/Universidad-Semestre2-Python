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
        4.  Informacion de mantenimiento
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
                manejo_de_cuentas()
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
        5.  Buscar productos
        6.  Buscar combos
        7.  Consultar ventas confiteria
        8.  Salir""")
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
                abrir_menu.buscar_productos()
            elif opcion_seleccionada == 6:
                pass
            elif opcion_seleccionada == 7:
                pass
            elif opcion_seleccionada == 8:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def administracion_de_combos():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu sistema de confiteria")
        print("""
        1.  Agregar combo
        2.  Eliminar combo
        3.  Modificar combo
        4.  Estadisticas de combos
        5.  Ver combos
        6.  Registro de combos
        7.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.agregar_combo()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_combo()
            elif opcion_seleccionada == 3:
                abrir_menu.modificar_combo()
            elif opcion_seleccionada == 4:
                abrir_menu.estadisticas_de_combos()
            elif opcion_seleccionada == 5:
                abrir_menu.ver_combos()
            elif opcion_seleccionada == 6:
                abrir_menu.registro_de_combos()
            elif opcion_seleccionada == 7:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def sistema_de_ventas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Sistema de ventas")
        print("""
        1.  Realizar venta
        2.  Modificar venta
        3.  Deshacer venta
        4.  Menu cuadre de caja y cuentas
        5.  Buscar facturas
        6.  Ver ventas
        7.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.realizar_venta()
            elif opcion_seleccionada == 2:
                abrir_menu.modificar_venta()
            elif opcion_seleccionada == 3:
                abrir_menu.deshacer_venta()
            elif opcion_seleccionada == 4:
                menu_cuadre_de_caja_y_cuentas()
            elif opcion_seleccionada == 5:
                abrir_menu.buscar_facturas()
            elif opcion_seleccionada == 6:
                abrir_menu.ver_ventas()
            elif opcion_seleccionada == 7:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def manejo_de_cuentas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu Manejo de cuentas y datos estadisticos")
        pass

def menu_cuadre_de_caja_y_cuentas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu cuadre de caja y cuentas")
        pass






menu_principal()