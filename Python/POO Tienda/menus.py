from colorama import init, Fore
from producto import *
import os

init(autoreset=True)


class Tienda:
    def __init__(self):
        self.inventario_productos = {}  # lo haremos con un diccionario
        self.ventas = []

    def agregar_producto(self, producto): 
        self.inventario_productos[producto.id_producto] = producto 

    def eliminar_producto(self, id_producto): 
        if id_producto in self.inventario_productos:
            del self.inventario_productos[id_producto]
            print("El producto fue eliminado con éxito.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_producto(self, producto):
        print(f"ID del producto: {producto.id_producto}")
        print(f"Nombre: {producto.nombre}")
        print(f"Precio de compra: {producto.precio_compra}")
        print(f"Precio de venta: {producto.precio_venta}")
        print(f"Cantidad: {producto.stock}")
        print()
        os.system("sleep 2")

    def ver_lista_de_productos(self): 
        if not self.inventario_productos:
            print("No hay productos en el inventario.")
        else:      
            for id_producto, producto in self.inventario_productos.items():
                self.mostrar_producto(producto)

    def vender_producto(self, id_producto, cantidad):
        if id_producto in self.inventario_productos:
            producto = self.inventario_productos[id_producto]
            if cantidad <= producto.stock:
                producto.stock -= cantidad
                return True, producto.precio_venta * cantidad
            else:
                print("No hay suficiente stock para realizar la venta.")
        else:
            print("El producto no existe en el inventario.")
        return False, 0

    def menu_inventario(self):
        while True:
            self.mostrar_encabezado("Inventario")

            print("""
                1. Agregar producto
                2. Eliminar producto
                3. Ver lista de productos
                4. Regresar
            """)

            try:
                inventario_chose = int(input("Escoja una opción del menú: "))

                if inventario_chose == 1:
                    self.agregar_producto_menu()
                elif inventario_chose == 2:
                    self.eliminar_producto_menu()
                elif inventario_chose == 3:
                    self.ver_lista_de_productos_menu()
                elif inventario_chose == 4:
                    break
                else:
                    self.mostrar_error("Opción no válida. Intente de nuevo.")

            except ValueError:
                self.mostrar_error("Entrada no válida. Intente de nuevo.")

    def menu_ventas(self):
        self.mostrar_encabezado("Sistema de Ventas")

        while True:
            self.mostrar_encabezado("Realizar Venta")

            self.ver_lista_de_productos()

            id_producto = input("Ingrese el ID del producto que desea vender (o 's' para salir): ")
            if id_producto.lower() == 's':
                break

            if id_producto in self.inventario_productos:
                cantidad = int(input("Ingrese la cantidad a vender: "))
                if cantidad > 0:
                    exito, total_venta = self.vender_producto(id_producto, cantidad)
                    if exito:
                        self.registrar_venta(id_producto, cantidad, total_venta)
                        self.mostrar_exito(f"Venta realizada con éxito. Total de la venta: ${total_venta:.2f}")
                        self.imprimir_factura(id_producto)
                    else:
                        self.mostrar_error("No se pudo completar la venta.")
                else:
                    self.mostrar_error("La cantidad debe ser mayor que cero.")
            else:
                self.mostrar_error("El ID del producto no es válido. Intente de nuevo.")

    def menu_estado_cuentas(self):
        self.mostrar_encabezado("Estado de Cuentas")

        if not self.ventas:
            print("No hay transacciones registradas.")
        else:
            for venta in self.ventas:
                print(f"ID del producto: {venta['id_producto']}")
                print(f"Cantidad vendida: {venta['cantidad']}")
                print(f"Total venta: ${venta['total_venta']:.2f}")
                print()

    def menu_estadisticas(self):
        self.mostrar_encabezado("Estadísticas")

        if not self.ventas:
            print("No hay suficientes datos para mostrar estadísticas.")
        else:
            total_ventas = sum(venta['total_venta'] for venta in self.ventas)
            print(f"Total de todas las ventas: ${total_ventas:.2f}")

            for i, venta in enumerate(self.ventas, 1):
                print(f"\nEstadísticas de Venta {i}:")
                print(f"ID del producto: {venta['id_producto']}")
                print(f"Cantidad vendida: {venta['cantidad']}")
                print(f"Total venta: ${venta['total_venta']:.2f}")

            patrimonio = sum(
                producto.precio_compra * producto.stock
                for producto in self.inventario_productos.values()
            )
            print(f"\nPatrimonio de la tienda: ${patrimonio:.2f}")

    def agregar_producto_menu(self):
        self.mostrar_encabezado("Agregar Producto")
        id_producto = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        precio_compra = float(input("Precio de compra: "))
        precio_venta = float(input("Precio de venta: "))
        stock = int(input("Cantidad en stock: "))

        nuevo_producto = Producto(id_producto, nombre, precio_compra, precio_venta, stock)
        self.agregar_producto(nuevo_producto)
        self.mostrar_exito("Producto agregado con éxito.")

    def eliminar_producto_menu(self):
        self.mostrar_encabezado("Eliminar Producto")
        id_producto = input("Ingrese el ID del producto que desea eliminar: ")
        self.eliminar_producto(id_producto)

    def ver_lista_de_productos_menu(self):
        self.mostrar_encabezado("Lista de Productos")
        self.ver_lista_de_productos()

    def mostrar_encabezado(self, titulo):
        print(Fore.LIGHTCYAN_EX + f"""
                        
            ╔════════════════════════════════════════╗
            ║                                        ║
            ║          Tienda Adios Mundo            ║
            ║                                        ║
            ╚════════════════════════════════════════╝
            
            {titulo}
        """ + Fore.RESET)

    def mostrar_error(self, mensaje):
        print(Fore.LIGHTRED_EX + f"Error: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    def mostrar_exito(self, mensaje):
        print(Fore.LIGHTGREEN_EX + f"Éxito: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    def registrar_venta(self, id_producto, cantidad, total_venta):
        self.ventas.append({"id_producto": id_producto, "cantidad": cantidad, "total_venta": total_venta})

    def imprimir_factura(self, id_venta):
        nombre_archivo = f"factura_venta_{id_venta}.txt"
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write("Factura de Venta\n")
                archivo.write("=" * 20 + "\n")

                for venta in self.ventas:
                    if venta['id_producto'] == id_venta:
                        archivo.write(f"ID del producto: {venta['id_producto']}\n")
                        archivo.write(f"Cantidad vendida: {venta['cantidad']}\n")
                        archivo.write(f"Total venta: ${venta['total_venta']:.2f}\n")
                        archivo.write("=" * 20 + "\n")
                        archivo.write("Gracias por su compra")
                        archivo.write("Vuelva pronto ;)")

            print(f"Factura generada correctamente: {nombre_archivo}")
        except Exception as e:
            print(f"Error al generar la factura: {e}")

if __name__ == "__main__":
    tienda = Tienda()
    tienda.menu_inventario() 
