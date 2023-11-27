from colorama import init, Fore
from datetime import datetime
from Producto import *
from Funciones import *
from Factura import Factura
import os

init(autoreset=True)

class Menus():
    def __init__(self):
        self.inventario_productos = {}
        self.ventas = {}
        self.ganancias_totales = 0
        self.cuadre_de_caja = 0
        self.factura = Factura()
        self.modificaciones_caja = {}
        self.numero_de_modificacion = 0
        self.productos_vendidos = 0

        producto1 = CaracteristicasProducto("1", "Gomas", "Dulceria", 100, 300, 50)
        producto2 = CaracteristicasProducto("2", "Lápiz", "Oficina", 500, 1000, 10)
        producto3 = CaracteristicasProducto("3", "Arroz", "Alimentos", 1000, 2500, 20)
        producto4 = CaracteristicasProducto("4", "Aspirina", "Farmacia", 100, 200, 30)

        self.inventario_productos[producto1.id_producto] = producto1
        self.inventario_productos[producto2.id_producto] = producto2
        self.inventario_productos[producto3.id_producto] = producto3
        self.inventario_productos[producto4.id_producto] = producto4

    #Menu inventario y submenus

    def menu_inventario(self):
        while True:
            Funciones.mostrar_encabezado("Inventario")
            print("""
        1.  Agregar producto
        2.  Eliminar producto
        3.  Ver productos
        4.  Regresar                                 
            """)

            try:
                opcion_selecionada = int(input("Escoja una opción del menú: "))
                if opcion_selecionada == 1:
                    self.agregar_producto()
                if opcion_selecionada == 2:
                    self.eliminar_producto()
                if opcion_selecionada == 3:
                    self.ver_lista_de_productos()
                    input("presione enter para continuar...")
                if opcion_selecionada == 4:
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no válida. Intente de nuevo.")

    def agregar_producto(self):
        Funciones.mostrar_encabezado("Agregar Producto")
        seguir = True
        while seguir:
            id_producto = input("ID de producto: ")
            nombre_producto = input("Nombre del producto: ")
            categoria = input("Categoria del producto: ")
            precio_compra = float(input("Precio de compra: "))
            precio_venta = float(input("Precio de Venta: "))
            cantidad = int(input("Cantidad: "))

            nuevo_producto = CaracteristicasProducto(id_producto, nombre_producto, categoria, precio_compra, precio_venta, cantidad)
            self.inventario_productos[id_producto] = nuevo_producto
            Funciones.mostrar_exito("Producto agregado con éxito")
            try:
                pregunta = input("¿Agregar otro producto? si/no: ")
                if pregunta.lower() == "si":
                    seguir = True
                elif pregunta.lower() == "no":
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no valida, intente de nuevo")
            
    def eliminar_producto(self):
        Funciones.mostrar_encabezado("Eliminar Producto")
        seguir = True
        while seguir:
            producto_a_eliminar = input("Ingre la ID del producto que desea eliminar: ")
            if producto_a_eliminar in self.inventario_productos:
                Funciones.mostrar_alerta("Eliminar: ")
                Funciones.mostrar_producto(self.inventario_productos[producto_a_eliminar])
                pregunta = input(Fore.LIGHTMAGENTA_EX + "¿Esta seguro de eliminar este producto? si/no: " + Fore.RESET)
                try:
                    if pregunta == "si":
                        del self.inventario_productos[producto_a_eliminar]
                        Funciones.mostrar_exito("Producto Eliminado con éxito")
                        try:
                            pregunta = input("¿Eliminar otro producto? si/no: ")
                            if pregunta.lower() == "si":
                                seguir = True
                            elif pregunta.lower() == "no":
                                break
                            else:
                                Funciones.mostrar_error("Entrada no válida, intente de nuevo")
                        except ValueError:
                            Funciones.mostrar_error("Entrada no valida, intente de nuevo")
                    elif pregunta == "no":
                        Funciones.mostrar_error("La eliminacion del producto de ha cancelado")
                        break
                    else:
                        Funciones.mostrar_error("Entrada no válida, intente de nuevo")
                except ValueError:
                    Funciones.mostrar_error("Entrada no valida, intente de nuevo")

    def ver_lista_de_productos(self):
        if not self.inventario_productos:
            Funciones.mostrar_alerta("No hay productos en el inventario")
        else:
            for id_producto, producto in self.inventario_productos.items():
                Funciones.mostrar_producto(producto)

    #Menu Sistema de ventas
    def menu_sistema_de_ventas(self):
        while True:
            Funciones.mostrar_encabezado("Sistema de Ventas")
            print("""
        1.  Vender
        2.  Devoluciones
        3.  Cuadre de caja
        4.  Regresar
                  """)
            try:
                opcion_seleccionada = int(input("Escoja una opción del menú: "))

                if opcion_seleccionada == 1:
                    self.vender()
                if opcion_seleccionada == 2:
                    self.devoluciones()
                if opcion_seleccionada == 3:
                    self.cuadre_de_caja_menu()
                if opcion_seleccionada == 4:
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no válida, Intente de nuevo")

    def vender(self):
        while True:
            venta_total = []
            generar_factura = False
            costo_total_venta = 0
            while True:
                try:
                    venta_actual = []
                    print("('s' para salir, 'g' para guardar venta)")
                    producto_a_vender = input("Ingrese la ID del producto: ")
                    if producto_a_vender.lower() == "s":
                        Funciones.mostrar_alerta("Saliendo")
                        break

                    if producto_a_vender.lower() == "g":
                        generar_factura = True
                        if generar_factura:
                            numero_factura, factura_info = self.factura.generar_factura(venta_total, costo_total_venta)
                            self.cuadre_de_caja += costo_total_venta
                            self.ventas[numero_factura] = factura_info
                            self.ganancias_totales += self.cuadre_de_caja
                            break

                    if producto_a_vender in self.inventario_productos:
                        producto = self.inventario_productos[producto_a_vender]
                        Funciones.mostrar_producto(producto)
                        try:
                            cantidad_venta = int(input("Ingrese la cantidad a vender: "))
                            if cantidad_venta > 0:
                                if cantidad_venta <= producto.cantidad_producto:
                                    producto.cantidad_producto -= cantidad_venta
                                    self.productos_vendidos += cantidad_venta
                                    costo_total_producto = producto.precio_venta_producto * cantidad_venta
                                    venta_actual.extend((producto.id_producto, producto.nombre_producto, producto.precio_venta_producto, cantidad_venta, costo_total_producto))
                                    venta_total.append(venta_actual)
                                    costo_total_venta += costo_total_producto
                                else:
                                    Funciones.mostrar_error("No hay suficientes stock para realizar la venta")
                            else:
                                Funciones.mostrar_error("Esa cantidad no está permitida")    
                        except ValueError:
                            Funciones.mostrar_error("Ingrese una cantidad válida")
                    else:
                        Funciones.mostrar_error("El producto no existe en el inventario")
                except ValueError:
                    Funciones.mostrar_error("Entrada no válida. Intente de nuevo.")
            break
    
    #En proceso...
    def devoluciones(self):

        pass

    #Menu informacion de ventas
    def cuadre_de_caja_menu(self):
        while True:
            Funciones.mostrar_encabezado("Cuadre de caja")
            print(f"Dinero total en caja: $ {self.cuadre_de_caja}")
            print("""
        1.  Mostrar informacion de todas las ventas
        2.  Mostrar informacion de una venta
        3.  Modificar dinero de la caja
        4.  Ver movimientos caja
        5.  Regresar
    """)    
            try:
                opcion_selecionada = int(input("Escoja una opción del menú: "))
                if opcion_selecionada == 1:
                    self.ver_todas_las_ventas()
                elif opcion_selecionada == 2:
                    self.ver_detalles_venta()
                elif opcion_selecionada == 3:
                    self.modificar_dinero_caja()
                elif opcion_selecionada == 4:
                    self.ver_movimientos_caja()
                elif opcion_selecionada == 5:
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no válida. Intente de nuevo.")
        
    def ver_todas_las_ventas(self):
        if not self.ventas:
            Funciones.mostrar_alerta("No hay ventas realizadas")
        else:
            for numero_factura, informacion_venta in self.ventas.items():
                print(f"\n\nFactura N°  {numero_factura}")
                print(f"\nDetalles Factura:")
                Funciones.mostrar_separador()
                
                detalles_factura = informacion_venta['Detalles Factura']
                
                for articulo, venta in enumerate(detalles_factura, start=1):
                    id_producto, nombre, precio, cantidad, costo_total_producto = venta
                    print(f"{articulo}.     id: {id_producto} Nombre: {nombre:<10}   -   $ {precio} x {cantidad} unidades  {costo_total_producto} ")
                
                Funciones.mostrar_separador()
                print(f"{'Total:':<60} $ {informacion_venta['Total Factura']:.2f}")
                print()
        input("Presione una tecla para continuar...")

    def ver_detalles_venta(self):
        if not self.ventas:
            Funciones.mostrar_alerta("No hay ventas realizadas")
        else:
            try:
                n_factura_a_buscar = int(input("Ingrese el número de la factura: "))
                if n_factura_a_buscar in self.ventas:
                    
                    informacion_venta = self.ventas[n_factura_a_buscar]
                    print(f"Factura N°  {n_factura_a_buscar}")
                    Funciones.mostrar_separador()
                    print(f"\nDetalle Factura:")
                    Funciones.mostrar_separador()

                    for articulo, venta in enumerate(informacion_venta["Detalles Factura"], start=1):
                        id_producto, nombre, precio, cantidad, costo_total_producto = venta
                        print(f"{articulo}.     id: {id_producto} Nombre: {nombre:<10} - $ {precio} x {cantidad} unidades  {costo_total_producto} ")
                    Funciones.mostrar_separador()
                    print(f"{'Total:':<60} $ {informacion_venta['Total Factura']:.2f}")
                    input("Preseione una tecla para continuar...")
                else:
                    Funciones.mostrar_alerta("La factura buscada no existe")
            except ValueError:
                Funciones.mostrar_error("Entrada no válida. Intente de nuevo.")

    def modificar_dinero_caja(self):
        while True:
            Funciones.mostrar_encabezado("Modificar dinero caja")
            print(f"Dinero en caja: {self.cuadre_de_caja}")
            print("""
            1.  Vaciar caja, dejar en 0
            2.  Restar dinero caja
            3.  Agregar dinero caja
            4.  Regresar
        """)
            try:
                opcion_selecionada = int(input("Escoja una opción del menú: "))
                if opcion_selecionada == 1:
                    self.vaciar_dinero_caja()
                if opcion_selecionada == 2:
                    self.restar_dinero_caja()
                if opcion_selecionada == 3:
                    self.aumentar_dinero_caja()
                if opcion_selecionada == 4:
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no válida, Intente de nuevo")
    
    #Modificaciones de caja
    def vaciar_dinero_caja(self):
        self.numero_de_modificacion += 1
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        datos = {
            "Fecha": fecha,
            "Hora": hora,
            "Monto": self.cuadre_de_caja,
            "Descripcion": "Se dejo la caja en $ 0",
        }
        self.modificaciones_caja[self.numero_de_modificacion] = datos
        self.cuadre_de_caja = 0
        Funciones.mostrar_exito("La caja a quedado en $ 0")

    def restar_dinero_caja(self):
        resta = float(input("¿Cuanto dinero desea retirar de la caja?: "))
        if resta < self.cuadre_de_caja:
            self.numero_de_modificacion += 1
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")
            datos = {
                "Fecha": fecha,
                "Hora": hora,
                "Monto": self.cuadre_de_caja,
                "Descripcion": f"Se quitó ${resta:.2f} del dinero en caja",
            }
            self.modificaciones_caja[self.numero_de_modificacion] = datos
            self.cuadre_de_caja -= resta
            Funciones.mostrar_exito(f"La caja quedó en: $ {self.cuadre_de_caja:.2f}")
        elif resta == self.cuadre_de_caja:
            self.vaciar_dinero_caja()
        else:
            Funciones.mostrar_error("No se puede quitar mas dinero del que hay en caja")
    
    def aumentar_dinero_caja(self):
        suma = float(input("¿Cuanto dinero desea sumar a la caja?: "))
        if suma > 0:
            self.numero_de_modificacion += 1
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")
            datos = {
                "Fecha": fecha,
                "Hora": hora,
                "Monto": self.cuadre_de_caja,
                "Descripcion": f"Se sumó ${suma:.2f} a la caja",
            }
            self.modificaciones_caja[self.numero_de_modificacion] = datos
            self.cuadre_de_caja += suma
            Funciones.mostrar_exito(f"La caja quedó en: ${self.cuadre_de_caja:.2f}")

    #Ver movimientos caja
    def ver_movimientos_caja(self):
        if not self.modificaciones_caja:
            Funciones.mostrar_alerta("Aun no hay movimientos de caja")
        else:
            Funciones.mostrar_encabezado("Movimientos de caja")
            print("{:<5} {:<25} {:<15} {:<20} {:<35}".format("N°", "Fecha modificación", "Hora", "Caja original", "Modificación"))
            for numero, datos in self.modificaciones_caja.items():
                fecha = datos["Fecha"]
                hora = datos["Hora"]
                dinero_en_caja = datos["Monto"]
                descripcion_de_modificacion = datos["Descripcion"]
                print("{:<5} {:<25} {:<15} {:<20} {:<35}".format(numero, fecha, hora, dinero_en_caja, descripcion_de_modificacion))
        input("Preseione una tecla para continuar...")

    #Facturas
    def facturas(self):
        if not self.ventas:
            Funciones.mostrar_alerta("No hay facturas que mostrar")
        else:
            for numero_factura, informacion_venta in self.ventas.items():
                print(f"\n\nFactura N°  {numero_factura}")
                print("\nDetalles Factura")
                Funciones.mostrar_separador()

                detalles_factura = informacion_venta['Detalles Factura']

                for numero, venta in enumerate(detalles_factura, start=1):
                    id_producto, nombre, precio, cantidad, costo_total_producto = venta
                    print(f"{numero}.       id: {id_producto} Nombre: {nombre:<10}   -   $ {precio} x {cantidad} unidades  {costo_total_producto}")
                
                Funciones.mostrar_separador()
                print(f"{'Total:':<60} $ {informacion_venta['Total Factura']:.2f}")
                print()
        input("Presione una tecla para continuar...")

    #Menu estadisticas generales
    def estadisticas(self):
        while True:
            Funciones.mostrar_encabezado("Menú de estadisticas")
            print("""
        1.  Estadisticas de ventas
        2.  Estadisticas de productos
        3.  Patrimonio tienda
        4.  Balance Ventas vs Compras
        5.  Salir
""")
            try:
                opcion_seleccionada = int(input("Escoja una opción del menú: "))

                if opcion_seleccionada == 1:
                    self.estadisticas_de_ventas()
                if opcion_seleccionada == 2:
                    self.estadisticas_de_productos()
                if opcion_seleccionada == 3:
                    self.patrimonio_tienda()
                if opcion_seleccionada == 4:
                    self.balance_ventas_compras()
                if opcion_seleccionada == 5:
                    break
            except ValueError:
                Funciones.mostrar_error("Entrada no válida, Intente de nuevo")

    def estadisticas_de_ventas(self):
        if not self.ventas:
            Funciones.mostrar_alerta("No hay ventas para analizar")
        else:
            promedio_ventas = 0
            contador_ventas = 0
            suma_ventas = 0
            mayor_venta = [0, 0, 0]
            menor_venta = [0, 0, float("inf")]
            print("\n\n\nTodas la ventas:")
            Funciones.mostrar_separador()
            for numero_factura, informacion_venta in self.ventas.items():
                cantidad_total_factura = 0
                detalles_factura = informacion_venta['Detalles Factura']
                total_factura = informacion_venta['Total Factura']
                for datos in detalles_factura:
                    id_producto, nombre, precio, cantidad, costo_total_producto = datos
                    cantidad_total_factura += cantidad
                contador_ventas += 1
                suma_ventas += total_factura
                print(f"Factura N° {numero_factura}         Cantidad vendida: {cantidad_total_factura}          Valor Factura: $ {total_factura}")
                if total_factura > mayor_venta[2]:
                    mayor_venta = [numero_factura, cantidad, total_factura]
                if total_factura < menor_venta[2]:
                    menor_venta = [numero_factura, cantidad, total_factura]
            print("\n\nDatos Estadisticos:")
            promedio_ventas = suma_ventas / contador_ventas
            print(f"\nPromedio ventas: $ {promedio_ventas:.2f}\n")
            print(f"\nMayor venta:\nFactura N° {mayor_venta[0]}         Cantidad vendida: {mayor_venta[1]}          Valor Factura: $ {mayor_venta[2]}")
            print(f"\nMenor venta:\nFactura N° {menor_venta[0]}         Cantidad vendida: {menor_venta[1]}          Valor Factura: $ {menor_venta[2]}")
            input("\n\nPresione una tecla para continuar...")

    def estadisticas_de_productos(self):
        if not self.ventas:
            Funciones.mostrar_alerta("No hay ventas para analizar")
        else:
            productos_estadisticas = {}
            for numero_factura, informacion_venta in self.ventas.items():
                detalles_factura = informacion_venta['Detalles Factura']

                for datos in detalles_factura:
                    id_producto, nombre, precio, cantidad, costo_total_producto = datos

                    if id_producto not in productos_estadisticas:
                        productos_estadisticas[id_producto] = {
                            "Nombre": nombre,
                            "Cantidad Vendida": 0,
                            "Ingresos Totales": 0,
                        }

                    productos_estadisticas[id_producto]['Cantidad Vendida'] += cantidad
                    productos_estadisticas[id_producto]['Ingresos Totales'] += costo_total_producto

            producto_mas_vendido = None
            cantidad_mas_vendida = 0
            producto_menos_vendido = None
            cantidad_menos_vendida = float("inf")

            producto_mas_rentable = None
            ingresos_mas_rentables = 0
            producto_menos_rentable = None
            ingresos_menos_rentables = float("inf")

            for id_producto, estadisticas in productos_estadisticas.items():
                cantidad_vendida = estadisticas["Cantidad Vendida"]
                ingresos_totales = estadisticas["Ingresos Totales"]

                if cantidad_vendida > cantidad_mas_vendida:
                    producto_mas_vendido = estadisticas["Nombre"]
                    cantidad_mas_vendida = cantidad_vendida

                if cantidad_vendida < cantidad_menos_vendida:
                    producto_menos_vendido = estadisticas["Nombre"]
                    cantidad_menos_vendida = cantidad_vendida

                if ingresos_totales > ingresos_mas_rentables:
                    producto_mas_rentable = estadisticas["Nombre"]
                    ingresos_mas_rentables = ingresos_totales

                if ingresos_totales < ingresos_menos_rentables:
                    producto_menos_rentable = estadisticas["Nombre"]
                    ingresos_menos_rentables = ingresos_totales

            print("\n\nEstadisticas de productos:")
            Funciones.mostrar_separador()
            print("Todos los productos:")
            for id_producto, datos_producto in self.inventario_productos.items():
                nombre_producto = datos_producto.nombre_producto

                if id_producto in productos_estadisticas:
                    estadisticas = productos_estadisticas[id_producto]
                    cantidad_vendida = estadisticas["Cantidad Vendida"]
                    ingresos_totales = estadisticas["Ingresos Totales"]
                else:
                    cantidad_vendida = 0
                    ingresos_totales = 0

                print(f"\nProducto: {nombre_producto}")
                print(f"Cantidad Vendida: {cantidad_vendida}")
                print(f"Ingresos Totales: {ingresos_totales}")
            Funciones.mostrar_separador()
            print(f"Producto mas vendido: {producto_mas_vendido}  cantidad vendida: {cantidad_mas_vendida}")
            print(f"Producto menos vendido: {producto_menos_vendido}  cantidad vendida: {cantidad_menos_vendida}")
            print(f"Productos mas rentable: {producto_mas_rentable}  ingresos totales: {ingresos_mas_rentables}")
            print(f"Producto menos rentable: {producto_menos_rentable}  ingresos totales: {ingresos_menos_rentables}")
            input("\n\nPresione una tecla para continuar")

    def patrimonio_tienda(self):
        total_patrimonio = 0
        dinero_bienes = 0
        total_cantidad_de_productos = 0
        for id_producto, Producto in self.inventario_productos.items():
            precio_compra = Producto.precio_compra_producto
            cantidad = Producto.cantidad_producto
            dinero_bienes += precio_compra * cantidad
            total_cantidad_de_productos += cantidad
        total_patrimonio = dinero_bienes + self.ganancias_totales
        print("\nPatrimonio")
        Funciones.mostrar_separador()
        print(f"Dinero en bienes: {dinero_bienes}")
        print(f"Dinero Ventas: {self.ganancias_totales}")
        print(f"Patrimonio total: {total_patrimonio}")
        input("\nPresione una tecla para continuar...")

    def balance_ventas_compras(self):
        total_compras = 0
        total_ventas = 0
        total_cantidad_de_productos = 0
        for id_producto, Producto in self.inventario_productos.items():
            precio_compra = Producto.precio_compra_producto
            precio_veta = Producto.precio_venta_producto
            cantidad = Producto.cantidad_producto
            total_compras += precio_compra * cantidad
            total_ventas += precio_veta * cantidad
            total_cantidad_de_productos += cantidad
        total_ventas += self.ganancias_totales
            
        print(f"\nTotal inversion compras: $ {total_compras:.2f}")
        print(f"Total supuestas ventas: $ {total_ventas:.2f}")
        print(f"Total ganancias: $ {self.ganancias_totales}")
        Funciones.mostrar_separador()
        print(f"Total cantidad de productos vendidos {self.productos_vendidos}")
        print(f"Total cantidad de productos en inventario: {total_cantidad_de_productos}")
        Funciones.mostrar_separador()
        balance = self.ganancias_totales - total_compras
        print(f"Balance de cuenta: ${balance:.2f}")
        input("\nPresione una tecla para continuar...")

            