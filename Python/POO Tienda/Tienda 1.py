from colorama import init, Fore
import os

init(autoreset=True)

class Producto:
    #Esta clase es lo que va a llevar el producto en si, le podemos agregar mas cosas pero por el
    #momento estos datos seran mas que suficientes como la id, el nombre precio de compra y precio de venta
    #stock, no agregare categorias, aun no es momento de usar un filtro de forma adecuada
    def __init__(self, id_producto, nombre, precio_compra, precio_venta, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock


class Inventario:
    #Esta clase se encargara de almacenar en un inventario los productos que se agreguen
    def __init__(self):
        self.inventario_productos = {} #lo haremos con un diccionario

    def agregar_producto(self, producto): #llamamos a la funcion agregar prodcuto y
        self.inventario_productos[producto.id_producto] = producto #pondremos de clave la id y los datos que se piden en la funcion de valores

    def eliminar_producto(self, id_producto): #buscaremos por id para eliminar producto y asi ubicarla rapido en el diccionario para su eliminacion
        if id_producto in self.inventario_productos:
            del self.inventario_productos[id_producto]
            print("El producto fue eliminado con éxito.")
        else:
            print("El producto no existe en el inventario.")


    #Para los productos en el inventario los mostramos con la funcion de abajo
    def ver_lista_de_productos(self): 
        if not self.inventario_productos:
            print("No hay productos en el inventario.")
        else:
            for id_producto, producto in self.inventario_productos.items():
                self.mostrar_producto(producto)


    # Funcion mostrar producto
    def mostrar_producto(self, producto):
        print(f"ID del producto: {producto.id_producto}")
        print(f"Nombre: {producto.nombre}")
        print(f"Precio de compra: {producto.precio_compra}")
        print(f"Precio de venta: {producto.precio_venta}")
        print(f"Cantidad: {producto.stock}")
        print()

    #Definimos la funcion vender producto
    def vender_producto(self, id_producto, cantidad):
        #Buscamos en el diccionario la id
        if id_producto in self.inventario_productos:
            producto = self.inventario_productos[id_producto]
            #Revisamos que la cantidad que hay no exeda la que se vende
            if cantidad <= producto.stock:
                #reducimos lo que se vendio en el stock
                producto.stock -= cantidad
                return True, producto.precio_venta * cantidad #esto lo devolvemos como datos estadisticos
            else:
                print("No hay suficiente stock para realizar la venta.")
        else:
            print("El producto no existe en el inventario.")
        return False, 0



class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.ventas = []
    
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
                    self.agregar_producto()
                elif inventario_chose == 2:
                    self.eliminar_producto()
                elif inventario_chose == 3:
                    self.ver_lista_de_productos()
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

            id_producto = input("Ingrese el ID del producto que desea vender (o 'q' para salir): ")
            if id_producto.lower() == 'q':
                break

            if id_producto in self.inventario.inventario_productos:
                cantidad = int(input("Ingrese la cantidad a vender: "))
                if cantidad > 0:
                    exito, total_venta = self.inventario.vender_producto(id_producto, cantidad)
                    if exito:
                        self.registrar_venta(id_producto, cantidad, total_venta)
                        self.mostrar_exito(f"Venta realizada con éxito. Total de la venta: ${total_venta:.2f}")
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
                for producto in self.inventario.inventario_productos.values()
            )
            print(f"\nPatrimonio de la tienda: ${patrimonio:.2f}")

    def agregar_producto(self):
        self.mostrar_encabezado("Agregar Producto")
        id_producto = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        precio_compra = float(input("Precio de compra: "))
        precio_venta = float(input("Precio de venta: "))
        stock = int(input("Cantidad en stock: "))

        nuevo_producto = Producto(id_producto, nombre, precio_compra, precio_venta, stock)
        self.inventario.agregar_producto(nuevo_producto)
        self.mostrar_exito("Producto agregado con éxito.")

    def eliminar_producto(self):
        self.mostrar_encabezado("Eliminar Producto")
        id_producto = input("Ingrese el ID del producto que desea eliminar: ")
        self.inventario.eliminar_producto(id_producto)

    def ver_lista_de_productos(self):
        self.mostrar_encabezado("Lista de Productos")
        self.inventario.ver_lista_de_productos()

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

def main():
    #Es un menu incial
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
