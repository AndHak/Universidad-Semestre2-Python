from colorama import init, Fore
from Producto import *
import os

class Funciones:
    @staticmethod
    def mostrar_encabezado(titulo):
        print(Fore.LIGHTCYAN_EX + f"""
                        
            ╔════════════════════════════════════════╗
            ║                                        ║
            ║          Tienda Adios Mundo            ║
            ║                                        ║
            ╚════════════════════════════════════════╝
            
                    {titulo}
        """ + Fore.RESET)

    @staticmethod
    def mostrar_error(mensaje):
        print(Fore.LIGHTRED_EX + f"Error: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def mostrar_exito(mensaje):
        print(Fore.LIGHTGREEN_EX + f"Éxito: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def mostrar_alerta(mensaje):
        print(Fore.LIGHTMAGENTA_EX + f"Alerta: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def mostrar_producto(producto):
        print()
        print(f"ID del producto: {producto.id_producto}")
        print(f"Nombre: {producto.nombre_producto}")
        print(f"Categoria: {producto.categoria_producto}")
        print(f"Precio Compra: {producto.precio_compra_producto}")
        print(f"Precio Venta: {producto.precio_venta_producto}")
        print(f"Cantidad: {producto.cantidad_producto}")
        print()

    @staticmethod
    def mostrar_separador():
        print()
        print("=====================================================================")
        print()

    @staticmethod
    def mostrar_separador_factura():
        return """
===========================================================================
"""