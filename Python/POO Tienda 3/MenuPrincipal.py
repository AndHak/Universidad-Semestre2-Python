from colorama import init, Fore
from Menus import *
from Funciones import *
import os

init(autoreset=True)

def MenuPrincipal():
    menus = Menus()
    while True:
        Funciones.mostrar_encabezado("Menu Principal")
        print("""
        1.  Inventario
        2.  Sistema de ventas
        3.  Facturas
        4.  Estadisticas
        5.  Salir
""")
        
        try:
            opcion_selecionada = int(input("Escoja una opción del menú: "))
            
            if opcion_selecionada == 1:
                menus.menu_inventario()
            elif opcion_selecionada == 2:
                menus.menu_sistema_de_ventas()
            elif opcion_selecionada == 3:
                menus.facturas()
            elif opcion_selecionada == 4:
                menus.estadisticas()
            elif opcion_selecionada == 5:
                break

        except ValueError:
            Funciones.mostrar_error("Entrada no valida, intente de nuevo")

if __name__ == "__main__":
    MenuPrincipal()