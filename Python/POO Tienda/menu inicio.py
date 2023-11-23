from colorama import init, Fore
from menus import *
from producto import *
import os

init(autoreset=True)

def main():
    tienda = Tienda()
    while True:
        tienda.mostrar_encabezado("Menú Principal")

        print("""
            1. Inventario
            2. Sistema de ventas
            3. Estado de cuentas
            4. Estadísticas
            5. Salir
        """)

        try:
            dashboard_chose = int(input("Escoja una opción del menú: "))

            if dashboard_chose == 1:
                tienda.menu_inventario()
            elif dashboard_chose == 2:
                tienda.menu_ventas()
            elif dashboard_chose == 3:
                tienda.menu_estado_cuentas()
            elif dashboard_chose == 4:
                tienda.menu_estadisticas()
            elif dashboard_chose == 5:
                tienda.mostrar_encabezado("¡Vuelva Pronto!")
                os.system("sleep 1")
                os.system("clear" if os.name == "posix" else "cls")
                break
            else:
                tienda.mostrar_error("Opción no válida. Intente de nuevo.")

        except ValueError:
            tienda.mostrar_error("Entrada no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()