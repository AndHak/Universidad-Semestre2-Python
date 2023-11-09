#---------------PROGRAMA LISTA COMPRA-----------------#



#Librerias
from colorama import init, Fore
import os



#Funciones rapidas
def pausa():
    input("Presione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


# Bases de datos
inventario_productos = {}

#Encendido y apagado
def encendido():
    print(Fore.LIGHTCYAN_EX + """
                      
          


                ╔════════════════════════════════════════╗
                ║                                        ║
                ║              ¡Bienvenido!              ║
                ║                                        ║
                ╚════════════════════════════════════════╝
                      
                """ + Fore.RESET)

    os.system("sleep 1")
    limpiar()


#Inventario

def agregar_producto():
    print(Fore.LIGHTCYAN_EX + """

            ╔════════════════════════════════════════╗
            ║                                        ║
            ║           ¡Agregar producto!           ║
            ║                                        ║
            ╚════════════════════════════════════════╝
                    
            """ + Fore.RESET)
    while True:
        try:
            yesornot = input("Desea agregar un producto si/no: ")
            if yesornot.lower() == "si":

                datos_producto = {}

                id_producto = input(Fore.LIGHTYELLOW_EX + "ID del producto:" + Fore.RESET + " ")
                nombre_producto = input(Fore.LIGHTYELLOW_EX + "Nombre del producto:" + Fore.RESET + " ")
                precio_de_compra = float(input(Fore.LIGHTYELLOW_EX + "Precio de compra:" + Fore.RESET + " "))
                precio_de_venta = float(input(Fore.LIGHTYELLOW_EX + "Precio de venta:" + Fore.RESET + " "))
                cantidad = int(input(Fore.LIGHTYELLOW_EX + "        Stock:" + Fore.RESET + " "))

                datos_producto["Nombre producto: "] = nombre_producto
                datos_producto["Precio de compra: "] = precio_de_compra
                datos_producto["Precio de venta: "] = precio_de_venta
                datos_producto["Stock: "] = cantidad

                inventario_productos[id_producto] = datos_producto

            if yesornot.lower() == "no":                                                             
                break
        except ValueError:
            print(Fore.LIGHTRED_EX + "Entrada no valida" + Fore.RESET)
            os.system("sleep 0.5")

def eliminar_producto():
    eliminando = True
    while eliminando:
        try:
            producto_a_eliminar = input("Ingrese el ID del producto que desea eliminar: ")
            if producto_a_eliminar in inventario_productos:
                caracteristicas = inventario_productos[producto_a_eliminar]
                print(f"ID del producto: {producto_a_eliminar}")
                print(f"Nombre: {caracteristicas['Nombre producto: ']}")
                print(f"Precio de Compra: {caracteristicas['Precio de compra: ']}")
                print(f"Precio de Venta: {caracteristicas['Precio de venta: ']}")
                print(f"Cantidad: {caracteristicas['Stock: ']}")
                eliminar = input("\n¿Este es el producto que desea eliminar? (si/no): ")
                if eliminar.lower() == "si":
                    del inventario_productos[producto_a_eliminar]
                    print("El producto fue eliminado con éxito.")
                    eliminar_nuevo = input("\n¿Desea eliminar otro producto? (si/no): ")
                    if eliminar_nuevo.lower() == "si":
                        eliminando = True
                    elif eliminar_nuevo.lower() == "no":
                        eliminando = False
                    else:
                        print("Opción no válida, pruebe con si o no.")
                elif eliminar.lower() == "no":
                    eliminando = False
                else:
                    print("Opción no válida, pruebe con si o no.")
            else:
                print("El producto no existe en el inventario.")
                pausa()
        except ValueError:
            print("Error")


def ver_lista_de_productos():
    if not inventario_productos:
        print("No hay productos en el inventario.")
    else:
        for id_producto, caracteristicas in inventario_productos.items():
            print(f"ID del producto: {id_producto}")
            print(f"Nombre: {caracteristicas['Nombre producto: ']}")
            print(f"Precio de compra: {caracteristicas['Precio de compra: ']}")
            print(f"Precio de venta: {caracteristicas['Precio de venta: ']}")
            print(f"Cantidad: {caracteristicas['Stock: ']}")
            print()

    pausa()

#Menus 
def dashboard_inventario():
    while True:
        print(Fore.LIGHTCYAN_EX + """
                        
                    ╔════════════════════════════════════════╗
                    ║                                        ║
                    ║          Tienda Adios Mundo            ║
                    ║                                        ║
                    ╚════════════════════════════════════════╝

                    """ + Fore.RESET) 
        
        print(Fore.LIGHTCYAN_EX + """
            
                        1.      Agregar producto
                        2.      Eliminar producto
                        3.      Ver lista de productos
                        4.      Regresar

                    """ + Fore.RESET)

        try:
            inventario_chose = int(input(Fore.LIGHTYELLOW_EX + "Escoja una opción del menú:" + Fore.RESET + " "))

            if inventario_chose < 1 or inventario_chose > 4:
                print(Fore.LIGHTRED_EX + "Esta opcion no se encunetra en el menu" + Fore.RESET)
                os.system("sleep 0.5")

            if  inventario_chose == 1:
                agregar_producto()
            if inventario_chose == 2:
                eliminar_producto()
            if inventario_chose == 3:
                ver_lista_de_productos()
            if inventario_chose == 4:
                break

        except ValueError:
            print(Fore.LIGHTRED_EX + "Entrada no valida" + Fore.RESET)
            os.system("sleep 0.5")

def inicio():
    #encendido()
    while True:
        print(Fore.LIGHTCYAN_EX + """
                        
                    ╔════════════════════════════════════════╗
                    ║                                        ║
                    ║          Tienda Adios Mundo            ║
                    ║                                        ║
                    ╚════════════════════════════════════════╝ 
        
            
                        1.      Inventario
                        2.      Sistema de ventas
                        3.      Estado de cuentas
                        4.      Salir

              
                    """ + Fore.RESET)

        try:
            dashboard_chose = int(input(Fore.LIGHTYELLOW_EX + "Escoja una opción del menú:" + Fore.RESET + " "))

            if dashboard_chose < 1 or dashboard_chose > 4:
                print(Fore.LIGHTRED_EX + "Esta opcion no se encunetra en el menu" + Fore.RESET)
                os.system("sleep 0.5")

            if dashboard_chose == 1:
                dashboard_inventario()

            if dashboard_chose == 4:
                print(Fore.LIGHTCYAN_EX + """
                      
          


                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            ¡Vuelva Pronto!             ║
                ║                                        ║
                ╚════════════════════════════════════════╝
                      
                """ + Fore.RESET)
                os.system("sleep 1")
                limpiar()
                break

        except ValueError:
            print(Fore.LIGHTRED_EX + "Entrada no valida" + Fore.RESET)
            os.system("sleep 0.5")
dashboard_inventario()