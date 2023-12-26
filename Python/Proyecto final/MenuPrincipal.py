from MenusInteractivos import *
from Funciones import *
import os

#Abriri terminal...
#digitar        pip install colorama
#               pip install tabulate


archivo = Archivo()
abrir_menu = Menus(archivo)

def menu_principal():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("menu principal")
        print("""
        1.  Sistema de peliculas
        2.  Sistema de confiteria
        3.  Sistema de ventas peliculas
        4.  Sistema de ventas confiteria
        5.  Administracion de datos y estadisticas
        6.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                sistema_de_peliculas()
            elif opcion_seleccionada == 2:
                sistema_de_confiteria()
            elif opcion_seleccionada == 3:
                sistema_de_ventas_peliculas()
            elif opcion_seleccionada == 4:
                sistema_de_ventas_confiteria()
            elif opcion_seleccionada == 5:
                manejo_de_datos()
            elif opcion_seleccionada == 6:
                abrir_menu.salir()
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
                abrir_menu.buscar_productos()
            elif opcion_seleccionada == 6:
                pass
            elif opcion_seleccionada == 7:
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
        4.  Registro de combos
        5.  Ver combos
        6.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.agregar_combo()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_combo()
            elif opcion_seleccionada == 3:
                abrir_menu.modificar_combo()
            elif opcion_seleccionada == 4:
                abrir_menu.registro_de_combos()
            elif opcion_seleccionada == 5:
                abrir_menu.ver_combos()
            elif opcion_seleccionada == 6:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def sistema_de_ventas_peliculas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Sistema de ventas peliculas")
        print("""
        1.  Realizar venta
        2.  Deshacer venta
        3.  Disponibilidad de salas
        4.  Menu cuadre de caja y cuentas
        5.  Buscar facturas
        6.  Ver ventas
        7.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.realizar_venta_pelicula()
            elif opcion_seleccionada == 2:
                abrir_menu.deshacer_venta_pelicula()
            elif opcion_seleccionada == 3:
                abrir_menu.administracion_de_salas()
            elif opcion_seleccionada == 4:
                menu_cuadre_de_caja_y_cuentas()
            elif opcion_seleccionada == 5:
                abrir_menu.factura_pelicula.buscar_facturas_peliculas()
            elif opcion_seleccionada == 6:
                abrir_menu.ver_ventas_peliculas()
            elif opcion_seleccionada == 7:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def sistema_de_ventas_confiteria():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Sistema de ventas confiteria")
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
                abrir_menu.realizar_venta_producto()
            elif opcion_seleccionada == 2:
                abrir_menu.modificar_venta_producto()
            elif opcion_seleccionada == 3:
                abrir_menu.deshacer_venta_producto()
            elif opcion_seleccionada == 4:
                menu_cuadre_de_caja_y_cuentas()
            elif opcion_seleccionada == 5:
                abrir_menu.buscar_facturas_confiteria()
            elif opcion_seleccionada == 6:
                abrir_menu.ver_ventas_confiteria()
            elif opcion_seleccionada == 7:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def manejo_de_datos():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("administracion y datos estadisticos")
        print("""
        1.  Ver archivos
        2.  Clientes
        3.  Cuadre de caja
        4.  Egresos e Ingresos
        5.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                menu_archivos()
            elif opcion_seleccionada == 2:
                menu_clientes()
            if opcion_seleccionada == 3:
                menu_cuadre_de_caja_y_cuentas()
            elif opcion_seleccionada == 4:
                egresos()
            elif opcion_seleccionada == 5:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def menu_archivos():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Archivos")
        print("""
        1.  Archivos Peliculas
        2.  Archivos Productos
        3.  Archivos Combos
        4.  Archivos manejo de salas
        5.  Archivos Facturas Confiteria
        6.  Archivos Facturas Peliculas
        7.  Archivos Egresos
        9.  Borrar Archivos
        0.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.archivo.mostrar_archivo_peliculas()
            if opcion_seleccionada == 2:
                abrir_menu.archivo.mostrar_archivo_productos()
            if opcion_seleccionada == 3:
                abrir_menu.archivo.mostrar_archivo_combos()
            if opcion_seleccionada == 4:
                abrir_menu.archivo.mostrar_archivo_ocupacion_sala()
            elif opcion_seleccionada == 6:
                abrir_menu.archivo.mostrar_archivo_facturas_peliculas() #
            elif opcion_seleccionada == 7:
                abrir_menu.archivo.mostrar_archivo_egresos()
            elif opcion_seleccionada == 8:
                abrir_menu.archivo.mostrar_archivo_ingresos()
            elif opcion_seleccionada == 9:
                abrir_menu.archivo.borrar_archivos()
            elif opcion_seleccionada == 0:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def menu_clientes():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Manejo de clientes")
        print("""
        1.  Agregar un cliente
        2.  Eliminar un cliente
        3.  Modificar un cliente
        4.  Ver clientes
        5.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.agregar_un_cliente()
            elif opcion_seleccionada == 2:
                abrir_menu.eliminar_un_cliente()
            elif opcion_seleccionada == 3:
                abrir_menu.modificar_un_cliente()
            elif opcion_seleccionada == 4:
                abrir_menu.ver_clientes()
            elif opcion_seleccionada == 5:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")


def menu_cuadre_de_caja_y_cuentas():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu cuadre de caja y cuentas")
        print(f"Dinero en caja: $ {abrir_menu.dinero_en_caja:.2f}")
        print("""
        1.  Dejar caja en 0
        2.  Restar dinero en caja
        3.  Sumar dinero en caja
        4.  Ver movimientos de caja
        5.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.vaciar_dinero_caja()
            elif opcion_seleccionada == 2:
                abrir_menu.restar_dinero_caja()
            elif opcion_seleccionada == 3:
                abrir_menu.aumentar_dinero_caja()
            elif opcion_seleccionada == 4:
                abrir_menu.ver_movimientos_caja()
            elif opcion_seleccionada == 5:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

def egresos():
    while True:
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Menu cuadre de caja y cuentas")
        print(f"Dinero en caja: $ {abrir_menu.dinero_en_caja:.2f}")
        print("""
        1.  Registrar un egreso
        2.  Cancelar un egreso
        3.  Ver egresos e Ingresos
        4.  Salir""")
        try:
            opcion_seleccionada = int(Funciones.hacer_pregunta("Escoja una opción del menú: "))
            if opcion_seleccionada == 1:
                abrir_menu.registrar_un_egreso()
            elif opcion_seleccionada == 2:
                abrir_menu.cancelar_un_egreso()
            elif opcion_seleccionada == 3:
                abrir_menu.ver_egresos()
            elif opcion_seleccionada == 4:
                break
        except ValueError:
            Funciones.mostrar_error("Ingrese una opción válida")

menu_principal()