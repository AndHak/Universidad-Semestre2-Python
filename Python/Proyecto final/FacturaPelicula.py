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

class FacturaPelicula:

    def __init__(self):
        self.numero_de_factura_peliculas = 0
        self.facturas_peliculas = {}
        self.archivo = archivo

    def generar_factura(self, cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra):
        self.numero_de_factura_peliculas += 1
        numero_factura = self.numero_de_factura_peliculas

        # Obtener la fecha y hora actual
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Información del cliente
        identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()

        # Información de la película
        titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula = pelicula_seleccionada.obtener_datos_pelicula()

        total_venta = costo_pelicula * len(validos)

        # Crear un boleto estilo cine
        boleto = f"""
        ---------------------------------------------
                CINE UDENAR - FACTURA DE VENTA
        ---------------------------------------------
        Número de factura: {numero_factura:04}
        Fecha de venta: {fecha_venta}
        ---------------------------------------------
        Película: {titulo_pelicula}        {edad_minima}+
        Duración: {duracion} minutos
        Sala: {sala_de_compra}
        Día y hora: {dia_de_compra} - {hora_de_compra:02}:{minutos_de_compra:02}
        Asientos: {' '.join(validos)}
        ---------------------------------------------
        Cliente: {nombre_cliente} ({edad_cliente} años)
        C.C/I.T: {identificacion_cliente}
        ---------------------------------------------
        Total: ${total_venta:.2f}
        ---------------------------------------------
        ¡Gracias por su compra!
        ---------------------------------------------
        """

        # Imprimir el boleto
        print(boleto)

        datos = [fecha_venta, cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra]
        datos_archivo = [fecha_venta, cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra, "NUEVA"]
        self.facturas_peliculas[numero_factura] = datos
        self.archivo.archivo_factura_peliculas.append(datos_archivo)

        while True:
            try:
                imprimir_factura_pregunta = Funciones.hacer_pregunta("Imprimir factura  si/no: ")
                if imprimir_factura_pregunta.lower() == "no":
                    Funciones.mostrar_alerta("No se imprimió factura, puede buscarla en facturas")
                    break
                elif imprimir_factura_pregunta.lower() == "si":
                    self.imprimir_factura(numero_factura)
                    os.system("pause")
                    break
            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")
            
        return numero_factura

    def imprimir_factura(self, numero_factura):
        for numeros_facturas, datos_facturas in self.facturas_peliculas.items():
            if numeros_facturas == numero_factura:
                fecha_venta, cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra = datos_facturas

                # Información del cliente
                identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()

                # Información de la película
                titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula = pelicula_seleccionada.obtener_datos_pelicula()

                total_venta = costo_pelicula * len(validos)

                # Crear un boleto estilo cine
                boleto = f"""
                ---------------------------------------------
                        CINE UDENAR - FACTURA DE VENTA
                ---------------------------------------------
                Número de factura: {numero_factura:04}
                Fecha de venta: {fecha_venta}
                ---------------------------------------------
                Película: {titulo_pelicula}        {edad_minima}+
                Duración: {duracion} minutos
                Sala: {sala_de_compra}
                Día y hora: {dia_de_compra} - {hora_de_compra:02}:{minutos_de_compra:02}
                Asientos: {', '.join(validos)}
                ---------------------------------------------
                Cliente: {nombre_cliente} ({edad_cliente} años)
                C.C/I.T: {identificacion_cliente}
                ---------------------------------------------
                Total: ${total_venta:.2f}
                ---------------------------------------------
                ¡Gracias por su compra!
                ---------------------------------------------
                """

                # Imprimir el boleto
                print(boleto)

                # Crear un archivo temporal para almacenar el boleto
                with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".txt") as tmp_file:
                    tmp_file.write(boleto)

                # Abrir el archivo con Notepad
                subprocess.run(["notepad.exe", tmp_file.name], shell=True)

                # Borrar el archivo temporal después de cerrar Notepad
                subprocess.run(["del", tmp_file.name], shell=True)







