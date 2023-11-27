from colorama import init, Fore
from Funciones import *
import subprocess
from datetime import datetime

class Factura:
    def __init__(self):
        self.numero_factura = 0
        self.datos_factura = {}

    def generar_factura(self, venta_total, costo_total_venta):
        self.numero_factura += 1
        numero_factura = self.numero_factura

        nombre_archivo = f"Factura N° {numero_factura}.txt"
        fecha_hora_venta = datetime.now().strftime("%Y-%m-%d    %H:%M:%S")

        Funciones.mostrar_encabezado(f"Factura N° {numero_factura}")
        Funciones.mostrar_separador()
        print(f"Fecha y Hora de Venta: {fecha_hora_venta}")
        print("-----------------------------------------------------------------------------------")
        print("Detalles de la factura")
        for i, venta in enumerate(venta_total, start=1):
            id_producto, nombre, precio, cantidad, costo_total_producto = venta
            print(f"{i}.   {nombre:<10}   -   $ {precio:<5.2f}  x  {cantidad} unidades   -   costo: $ {costo_total_producto:.2f}")
        
        print("-----------------------------------------------------------------------------------")
        print(f"{'Total compra:':<60} $ {costo_total_venta:.2f}")
        Funciones.mostrar_separador()
        print("                  * NO GRACIAS POR SU COMPRA *")
        print("                          NO VUELVA     ")
        print()

        try:
            pregunta = input("¿Desea imprimir Factura? si/no: ")
            if pregunta.lower() == "si":
                with open(nombre_archivo, "w") as archivo:
                    archivo.write("\n\n                         Tienda Adios Mundo          \n\n")
                    archivo.write(f"\nFactura N° {numero_factura}\n") 
                    archivo.write(Funciones.mostrar_separador_factura())
                    archivo.write(f"\nFecha y Hora de Venta: {fecha_hora_venta}")
                    archivo.write("\n---------------------------------------------------------------------------\n")
                    archivo.write("\nDetalles de la venta")
                    archivo.write("\n---------------------------------------------------------------------------\n")
                    for i, venta in enumerate(venta_total, start=1):
                        id_producto, nombre, precio, cantidad, costo_total_producto = venta
                        archivo.write(f"{i}.   {nombre:<10}   -   $ {precio:<5.2f}  x  {cantidad} unidades   -   costo: $ {costo_total_producto:.2f}\n")

                    archivo.write("\n---------------------------------------------------------------------------\n")
                    archivo.write(f"{'Total compra:':<60} $ {costo_total_venta:.2f}\n\n")
                    archivo.write(Funciones.mostrar_separador_factura())
                    archivo.write("\n                        * NO GRACIAS POR SU COMPRA *\n")
                    archivo.write("                                  NO VUELVA      \n")

                print(f"La factura se ha guardado como: {nombre_archivo}")

                try:
                    subprocess.run(["notepad", nombre_archivo], check=True)
                except subprocess.CalledProcessError:
                    print(f"No se pudo abrir el archivo: {nombre_archivo}")

            elif pregunta.lower() == "no":
                Funciones.mostrar_exito("La factura se ha guardado en el sistema")
        except ValueError:
            Funciones.mostrar_error("Entrada no válida")

        
        self.datos_factura[numero_factura] = {
            "Detalles Factura": venta_total,
            "Total Factura": costo_total_venta
        }

        return numero_factura, self.datos_factura[numero_factura]


