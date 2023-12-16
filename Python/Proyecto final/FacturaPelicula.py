from colorama import init, Fore
from Funciones import *
import subprocess
from datetime import datetime
from Datos import *
from MenusInteractivos import *
from Datos import *



class FacturaPelicula:
    def __init__(self):
        self.numero_de_factura_peliculas = 0
        self.facturas_peliculas = {}

    def generar_factura(self, cliente, pelicula_seleccionada, validos, id_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra):

        self.numero_de_factura_peliculas += 1

        #Obtener la fecha y hora actual
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Información del cliente
        identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()

        #Información de la película
        titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula = pelicula.obtener_datos_pelicula()

        #Información de la sala
        id_sala, dia, hora, minutos, sala_numero, pelicula_sala = sala




