from colorama import init, Fore
from Funciones import *
from datetime import datetime
from Datos import *
from MenusInteractivos import *
from Datos import *
from Archivo import *
import tempfile
import subprocess

archivo = Archivo()

class FacturaConfiteria:

    def __init__(self):
        self.numero_de_factura_confiteria = 0
        self.facturas_confiteria = {}
        self.archivo = archivo

    def generar_factura(self, cliente, productos_vendidos):
        self.numero_de_factura_confiteria += 1
        numero_factura = self.numero_de_factura_confiteria

        # Obtener la fecha y hora actual
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Información del cliente
        identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()

        # Crear el encabezado de la factura
        factura_encabezado = f"""
        ------------------------------------------------
                CINE UDENAR - FACTURA DE VENTA
        ------------------------------------------------
        Número de factura: {numero_factura:04}
        Fecha de venta: {fecha_venta}
        ------------------------------------------------
        Cliente: {nombre_cliente} ({edad_cliente} años)
        C.C/I.T: {identificacion_cliente}
        ------------------------------------------------
        """

        # Crear la sección de productos vendidos
        productos_vendidos_seccion = ""
        total_venta = 0

        for producto, cantidad_vendida in productos_vendidos:
            # Información del producto
            id_producto, nombre_producto, categoria_producto, precio_compra_producto, precio_venta_producto, cantidad_producto = producto.obtener_datos_producto()

            # Calcular el total para este producto
            total_producto = precio_venta_producto * cantidad_vendida
            total_venta += total_producto

            # Añadir la información del producto a la sección
            productos_vendidos_seccion += f"""
            Producto: {nombre_producto}+
            Precio unitario: {precio_venta_producto}
            Cantidad: {cantidad_vendida}
            Total: ${total_producto:.2f}
            ------------------------------------------------
            """

        # Crear el pie de la factura
        factura_pie = f"""
        ------------------------------------------------
        Total venta: ${total_venta:.2f}
        ------------------------------------------------
        ¡Gracias por su compra!
        ------------------------------------------------
        """

        # Unir todas las secciones
        factura_completa = f"{factura_encabezado}{productos_vendidos_seccion}{factura_pie}"

        # Imprimir la factura
        print(factura_completa)

        # Guardar los datos en la estructura de facturas
        datos_factura = [fecha_venta, cliente, productos_vendidos, total_venta]
        datos_archivo = [numero_factura, fecha_venta, cliente, productos_vendidos, cantidad_vendida, total_venta, "NUEVA"]
        self.facturas_confiteria[numero_factura] = datos_factura
        self.archivo.archivo_facturas_confiteria.append(datos_archivo)

        return fecha_venta, numero_factura, total_venta


    def buscar_facturas_confiteria(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Buscar Factura")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            if not self.archivo.archivo_facturas_confiteria:
                Funciones.mostrar_alerta("No hay ventas realizadas")
                break
            else:
                Funciones.mostrar_facturas_confiteria(self.archivo.archivo_facturas_confiteria)

                encontrar_factura = Funciones.hacer_pregunta("Número de factura: ")
                if encontrar_factura.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                encontrar_factura = int(encontrar_factura)

                factura_encontrada = None
                productos_vendidos_encontrados = None

                for factura in self.archivo.archivo_facturas_confiteria:
                    numero_factura, fecha_venta, cliente, productos_vendidos, cantidad_vendida, total_venta, estado = factura
                    if numero_factura == encontrar_factura:
                        factura_encontrada = factura
                        productos_vendidos_encontrados = productos_vendidos

                        if factura_encontrada:
                            # Accede a la función mostrar_factura con la factura y los productos encontrados
                            self.mostrar_factura(factura_encontrada, productos_vendidos_encontrados)
                            os.system("pause")
                            break
                        else:
                            Funciones.mostrar_alerta("No se encontró la factura con el número ingresado.")
                            break


    @staticmethod
    def mostrar_factura(factura, productos_vendidos):
        print("FACTURA:")
        print("Número de factura:", factura[1])
        print("Fecha de venta:", factura[0])
        print("Cliente:", factura[2].nombre_cliente)
        print("Productos vendidos:")

        for producto, cantidad in productos_vendidos:
            print(f"- {cantidad} {producto.nombre_producto} - ${producto.precio_venta_producto:.2f} c/u")

        print("Total venta: ${:.2f}".format(factura[5]))
        print("¡Gracias por su compra!")
