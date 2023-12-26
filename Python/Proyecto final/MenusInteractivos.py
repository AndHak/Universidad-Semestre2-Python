from colorama import init
from datetime import datetime, timedelta
from Funciones import *
from FacturaPelicula import FacturaPelicula
from FacturaConfiteria import *
from Datos import *
from Archivo import *
from tabulate import *
import os
import pickle

#Iniciamos colorama con letras blancas
init(autoreset=True)

factura_pelicula = FacturaPelicula()

class Menus:

    #Este constructor hereda algunas listas que estan en la clase archivo
    def __init__(self, archivo):
        
        self.cartelera = {}     #Aqui se van a guardar las peliculas disponibles
        self.clientes = {}      #Aqui se registran los clientes con las compras que hacen en confiteria y peliculas
        self.ocupacion_sala = []        #Aqui se almacenan los horarios de funcion
        self.inventario_confiteria = {}     #Aqui se guardan los productos de la confiteria
        self.salas = {}     #Aqui se guardan las salas una vez se haya realizado alguna venta
        self.archivo = archivo      #Aqui llamamos a las listas que estan en la clase archivo
        self.factura_pelicula = factura_pelicula    #Aqui asignamos la variable para la clase pelicula

        self.egresos = {}       #Aqui se manejan egresos por pagos luz, agua, aseo, administracion, etc.
        self.ingresos = {}      #Aqui estan todos los ingresos
        self.dinero_en_caja = 0       #Aqui guardamos el dinero en caja
        self.modificaciones_caja = {}   #Aqui guardaremos las modificaciones de caja

        self.cargar_datos()     #Aqui cargamos los datos al constructor de los documentos txt
    

    def salir(self):
        self.guardar_datos()    #Antes de salir guardamos datos, se guardan datos cuando cerramos el programa corractamente


    def guardar_datos(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Guardar datos de la cartelera
        ruta_cartelera = os.path.join(directorio_actual, "datos_cine", "cartelera.pkl")
        with open(ruta_cartelera, "wb") as file:
            pickle.dump(self.cartelera, file)

        # Guardar datos de la confiteria
        ruta_confiteria = os.path.join(directorio_actual, "datos_cine", "confiteria.pkl")
        with open(ruta_confiteria, "wb") as file:
            pickle.dump(self.inventario_confiteria, file)

        # Guardar datos de la ocupacion de sala
        ruta_ocupacion_sala = os.path.join(directorio_actual, "datos_cine", "ocupacion_sala.pkl")
        with open(ruta_ocupacion_sala, "wb") as file:
            pickle.dump(self.ocupacion_sala, file)

        # Guardar datos de la ocupacion de sala
        ruta_ocupacion_asientos = os.path.join(directorio_actual, "datos_cine", "ocupacion_salas_asientos.pkl")
        with open(ruta_ocupacion_asientos, "wb") as file:
            pickle.dump(self.salas, file)

        # Guardar datos de los clientes
        ruta_clientes = os.path.join(directorio_actual, "datos_cine", "clientes.pkl")
        with open(ruta_clientes, "wb") as file:
            pickle.dump(self.clientes, file)

        # Guardar datos de los egresos
        ruta_egresos = os.path.join(directorio_actual, "datos_cine", "egresos.pkl")
        with open(ruta_egresos, "wb") as file:
            pickle.dump(self.egresos, file)

        # Guardar datos de los ingresos
        ruta_ingresos = os.path.join(directorio_actual, "datos_cine", "ingresos.pkl")
        with open(ruta_ingresos, "wb") as file:
            pickle.dump(self.ingresos, file)

        # Guardar datos del dinero en caja
        ruta_dinero_en_caja = os.path.join(directorio_actual, "datos_cine", "dinero_en_caja.pkl")
        with open(ruta_dinero_en_caja, "wb") as file:
            pickle.dump(self.dinero_en_caja, file)

        # Guardar datos de las modificaciones de caja
        ruta_modificaciones_caja = os.path.join(directorio_actual, "datos_cine", "modificaciones_caja.pkl")
        with open(ruta_modificaciones_caja, "wb") as file:
            pickle.dump(self.modificaciones_caja, file)


        #GUARDAR FACTURAS
        ###########################################################################################################
        ruta_facturas_peliculas = os.path.join(directorio_actual, "datos_cine", "facturas", "facturas_peliculas.pkl")
        with open(ruta_facturas_peliculas, "wb") as file:
            pickle.dump(self.factura_pelicula.facturas_peliculas, file)

        ruta_numero_factura = os.path.join(directorio_actual, "datos_cine", "facturas", "numero_factura.pkl")
        with open(ruta_numero_factura, "wb") as file:
            pickle.dump(self.factura_pelicula.numero_de_factura_peliculas, file)

        #GUARDAR ARCHIVOS
        ###########################################################################################################
        # Guardar datos del archivo de peliculas
        ruta_archivo_peliculas = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_peliculas.pkl")
        with open(ruta_archivo_peliculas, "wb") as file:
            pickle.dump(self.archivo.archivo_peliculas, file)

        # Guardar datos del archivo de productos
        ruta_archivo_productos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_productos.pkl")
        with open(ruta_archivo_productos, "wb") as file:
            pickle.dump(self.archivo.archivo_productos, file)

        # Guardar datos del archivo de combos
        ruta_archivo_combos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_combos.pkl")
        with open(ruta_archivo_combos, "wb") as file:
            pickle.dump(self.archivo.archivo_combos, file)

        # Guardar datos del archivo de ocupación de sala
        ruta_archivo_ocupacion_sala = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_ocupacion_sala.pkl")
        with open(ruta_archivo_ocupacion_sala, "wb") as file:
            pickle.dump(self.archivo.archivo_ocupacion_sala, file)

        # Guardar datos del archivo de facturas de confitería
        ruta_archivo_facturas_confiteria = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_facturas_confiteria.pkl")
        with open(ruta_archivo_facturas_confiteria, "wb") as file:
            pickle.dump(self.archivo.archivo_facturas_confiteria, file)

        # Guardar datos del archivo de facturas de películas
        ruta_archivo_factura_peliculas = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_factura_peliculas.pkl")
        with open(ruta_archivo_factura_peliculas, "wb") as file:
            pickle.dump(self.archivo.archivo_factura_peliculas, file)

        # Guardar datos del archivo de egresos
        ruta_archivo_egresos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_egresos.pkl")
        with open(ruta_archivo_egresos, "wb") as file:
            pickle.dump(self.archivo.archivo_egresos, file)

        # Guardar datos de los ingresos
        ruta_archivo_ingresos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_ingresos.pkl")
        with open(ruta_archivo_ingresos, "wb") as file:
            pickle.dump(self.archivo.archivo_ingresos, file)


    def cargar_datos(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))      #Buscamos el directorio donde está este documento python

        #Cargar datos a la cartelera
        try:
            ruta_cartelera = os.path.join(directorio_actual, "datos_cine", "cartelera.pkl")
            with open(ruta_cartelera, "rb") as file:
                self.cartelera = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'cartelera.pkl' no fue encontrado. Se creará por primera vez al agregar una película.")
        except Exception as e:
            print(f"Error al leer 'cartelera.pkl': {e}")

        #Cargar datos a la confiteria
        try:
            ruta_confiteria = os.path.join(directorio_actual, "datos_cine", "confiteria.pkl")
            with open(ruta_confiteria, "rb") as file:
                self.inventario_confiteria = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'confiteria.pkl' no fue encontrado. Se creará por primera vez al agregar productos.")
        except Exception as e:
            print(f"Error al leer 'confiteria.pkl': {e}")

        #Cargar datos de la ocupacion de salas
        try:
            ruta_ocupacion_sala = os.path.join(directorio_actual, "datos_cine", "ocupacion_sala.pkl")
            with open(ruta_ocupacion_sala, "rb") as file:
                self.ocupacion_sala = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'ocupacion_sala.pkl' no fue encontrado. Se creará por primera vez al asignar salas.")
        except Exception as e:
            print(f"Error al leer 'ocupacion_sala.pkl': {e}")

        # Cargar datos de la ocupacion de asientos
        try:
            ruta_ocupacion_asientos = os.path.join(directorio_actual, "datos_cine", "ocupacion_salas_asientos.pkl")
            with open(ruta_ocupacion_asientos, "rb") as file:
                self.salas = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'ocupacion_salas_asientos.pkl' no fue encontrado. Se creará por primera vez al asignar salas.")
        except Exception as e:
            print(f"Error al leer 'ocupacion_salas_asientos.pkl': {e}")

        # Cargar datos de los clientes
        try:
            ruta_clientes = os.path.join(directorio_actual, "datos_cine", "clientes.pkl")
            with open(ruta_clientes, "rb") as file:
                self.clientes = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'clientes.pkl' no fue encontrado. Se creará por primera vez al agregar clientes.")
        except Exception as e:
            print(f"Error al leer 'clientes.pkl': {e}")

        # Cargar datos de los egresos
        try:
            ruta_egresos = os.path.join(directorio_actual, "datos_cine", "egresos.pkl")
            with open(ruta_egresos, "rb") as file:
                self.egresos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'egresos.pkl' no fue encontrado. Se creará por primera vez al agregar egresos.")
        except Exception as e:
            print(f"Error al leer 'egresos.pkl': {e}")

        # Cargar datos de los ingresos
        try:
            ruta_ingresos = os.path.join(directorio_actual, "datos_cine", "ingresos.pkl")
            with open(ruta_ingresos, "rb") as file:
                self.ingresos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'ingresos.pkl' no fue encontrado. Se creará por primera vez al agregar ingresos.")
        except Exception as e:
            print(f"Error al leer 'ingresos.pkl': {e}")

        # Cargar datos del dinero en caja
        try:
            ruta_dinero_en_caja = os.path.join(directorio_actual, "datos_cine", "dinero_en_caja.pkl")
            with open(ruta_dinero_en_caja, "rb") as file:
                self.dinero_en_caja = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'dinero_en_caja.pkl' no fue encontrado. Se creará por primera vez al iniciar el programa.")
        except Exception as e:
            print(f"Error al leer 'dinero_en_caja.pkl': {e}")

        # Cargar datos de las modificaciones de caja
        try:
            ruta_modificaciones_caja = os.path.join(directorio_actual, "datos_cine", "modificaciones_caja.pkl")
            with open(ruta_modificaciones_caja, "rb") as file:
                self.modificaciones_caja = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'modificaciones_caja.pkl' no fue encontrado. Se creará por primera vez al iniciar el programa.")
        except Exception as e:
            print(f"Error al leer 'modificaciones_caja.pkl': {e}")



        #GUARDAR FACTURAS
        ###########################################################################################################
        try:
            ruta_facturas_peliculas = os.path.join(directorio_actual, "datos_cine", "facturas", "facturas_peliculas.pkl")
            with open(ruta_facturas_peliculas, "rb") as file:
                self.factura_pelicula.facturas_peliculas = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'modificaciones_caja.pkl' no fue encontrado. Se creará por primera vez al iniciar el programa.")
        except Exception as e:
            print(f"Error al leer 'modificaciones_caja.pkl': {e}")


        try:
            ruta_numero_factura = os.path.join(directorio_actual, "datos_cine", "facturas", "numero_factura.pkl")
            with open(ruta_numero_factura, "rb") as file:
                self.factura_pelicula.numero_de_factura_peliculas = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'modificaciones_caja.pkl' no fue encontrado. Se creará por primera vez al iniciar el programa.")
        except Exception as e:
            print(f"Error al leer 'modificaciones_caja.pkl': {e}")



        #GUARDAR ARCHIVOS
        ###########################################################################################################
            
        # Cargar datos para archivo_peliculas
        try:
            ruta_archivo_peliculas = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_peliculas.pkl")
            with open(ruta_archivo_peliculas, "rb") as file:
                self.archivo.archivo_peliculas = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_peliculas.pkl' no fue encontrado. Se creará por primera vez al asignar salas.")
        except Exception as e:
            print(f"Error al leer 'archivo_peliculas.pkl': {e}")

        # Cargar datos para archivo_productos
        try:
            ruta_archivo_productos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_productos.pkl")
            with open(ruta_archivo_productos, "rb") as file:
                self.archivo.archivo_productos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_productos.pkl' no fue encontrado. Se creará por primera vez al asignar productos.")
        except Exception as e:
            print(f"Error al leer 'archivo_productos.pkl': {e}")

        # Cargar datos para archivo_combos
        try:
            ruta_archivo_combos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_combos.pkl")
            with open(ruta_archivo_combos, "rb") as file:
                self.archivo.archivo_combos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_combos.pkl' no fue encontrado. Se creará por primera vez al asignar combos.")
        except Exception as e:
            print(f"Error al leer 'archivo_combos.pkl': {e}")

        # Cargar datos para archivo_ocupacion_sala
        try:
            ruta_archivo_ocupacion_sala = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_ocupacion_sala.pkl")
            with open(ruta_archivo_ocupacion_sala, "rb") as file:
                self.archivo.archivo_ocupacion_sala = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_ocupacion_sala.pkl' no fue encontrado. Se creará por primera vez al asignar salas.")
        except Exception as e:
            print(f"Error al leer 'archivo_ocupacion_sala.pkl': {e}")

        # Cargar datos para archivo_facturas_confiteria
        try:
            ruta_archivo_facturas_confiteria = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_facturas_confiteria.pkl")
            with open(ruta_archivo_facturas_confiteria, "rb") as file:
                self.archivo.archivo_facturas_confiteria = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_facturas_confiteria.pkl' no fue encontrado. Se creará por primera vez al asignar facturas de confitería.")
        except Exception as e:
            print(f"Error al leer 'archivo_facturas_confiteria.pkl': {e}")

        # Cargar datos para archivo_factura_peliculas
        try:
            ruta_archivo_factura_peliculas = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_factura_peliculas.pkl")
            with open(ruta_archivo_factura_peliculas, "rb") as file:
                self.archivo.archivo_factura_peliculas = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_factura_peliculas.pkl' no fue encontrado. Se creará por primera vez al asignar facturas de películas.")
        except Exception as e:
            print(f"Error al leer 'archivo_factura_peliculas.pkl': {e}")

        # Cargar datos para archivo_egresos
        try:
            ruta_archivo_egresos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_egresos.pkl")
            with open(ruta_archivo_egresos, "rb") as file:
                self.archivo.archivo_egresos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_egresos.pkl' no fue encontrado. Se creará por primera vez al asignar egresos.")
        except Exception as e:
            print(f"Error al leer 'archivo_egresos.pkl': {e}")
        
        # Guardar datos de los ingresos
        try:
            ruta_archivo_ingresos = os.path.join(directorio_actual, "datos_cine", "archivos", "archivo_ingresos.pkl")
            with open(ruta_archivo_ingresos, "rb") as file:
                self.archivo.archivo_ingresos = pickle.load(file)
        except FileNotFoundError:
            print("El archivo 'archivo_egresos.pkl' no fue encontrado. Se creará por primera vez al asignar egresos.")
        except Exception as e:
            print(f"Error al leer 'archivo_egresos.pkl': {e}")





#METODOS PARA EL SISTEMA DE PELICULAS

#######################################################################################

    def agregar_peliculas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Agregar pelicula")
            #Opcion siempre disponibe
            print("Opción siempre disponible: 'c' para cancelar")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")
                break
            else:
                Funciones.mostrar_peliculas(self.cartelera)

            try:

                #Nombre pelicula
                titulo_pelicula = Funciones.hacer_pregunta("Título pelicula: ")
                if titulo_pelicula.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #Ponemos la primera letra de cada palabra en mayusculas
                titulo_pelicula = titulo_pelicula.title()
                #Busca el nombre de la pelicula en el inventario
                if titulo_pelicula in self.cartelera:
                    Funciones.mostrar_error("No se agregó la película, parece que ya existe")

                #Sinapsis o breve descripcion de la pelicula
                sinopsis = Funciones.hacer_pregunta("Sinopsis: ")
                if sinopsis.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #Ponemos la primera letra de la primera palabra en mayuscula
                sinopsis = sinopsis.capitalize()

                #Duracion en minutos de la pelicula
                duracion = Funciones.hacer_pregunta("Duración minutos: ")
                if duracion.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #La convertimos a entero por la opcion siempre disponible C
                duracion = int(duracion)

                #Genero pelicula
                genero = Funciones.hacer_pregunta("Genero: ")
                if genero.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #Ponemos la primera letra de la primera palabra en mayuscula
                genero = genero.capitalize()
                
                #Edad minima para restricciones
                edad_minima = Funciones.hacer_pregunta("Edad minima permitida: ")
                if edad_minima.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #La convertimos a entero por la opcion siempre disponible c
                edad_minima = int(edad_minima)

                #Costo pelicula
                costo_pelicula = Funciones.hacer_pregunta("Costo pelicula: ")
                if costo_pelicula.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                #La convertimos a float por la opcion siempre disponible c
                costo_pelicula = float(costo_pelicula)

                #creamos una variable a la que se le asignan los datos de la clase DatosPelicula
                pelicula_a_agregar = DatosPelicula(titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula)
                pelicula_a_agregar_archivo = [titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula, 'NUEVO']

                #La agregamos al diccionario con la clave id_pelicula
                self.cartelera[titulo_pelicula] = pelicula_a_agregar
                self.archivo.archivo_peliculas.append(pelicula_a_agregar_archivo)
                Funciones.mostrar_exito("La película ha sido agregada a la cartelera")
                self.guardar_datos()

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

#--------------------------------------------------------------------------------------

    def eliminar_peliculas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Eliminar pelicula")
            #Opcion siempre disponibe
            print("Opción siempre disponible: 'c' para cancelar")
            año = datetime.now().strftime("%Y")     #Saca el año actual
            mes = datetime.now().strftime("%m")     #Saca el mes actual
            print(f"\n\nAño: {año}   mes: {mes}\n\n")       #Imprime el año y mes

            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")  
                break  
            else:
                Funciones.mostrar_peliculas(self.cartelera)

            try:

                #Código de pelicula
                titulo_pelicula = Funciones.hacer_pregunta("Ingrese el Titulo de la pelicula: ")
                if titulo_pelicula.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                titulo_pelicula = titulo_pelicula.title()


                if titulo_pelicula in self.cartelera:

                    #Agregar cambio al archivo
                    datos = self.cartelera[titulo_pelicula]

                    # Agregar cambio al archivo
                    datos_archivo_pelicula_eliminacion = [datos.titulo_pelicula, datos.sinopsis, datos.duracion, datos.genero, datos.edad_minima, datos.costo_pelicula, "ELIMINADO"]
                    self.archivo.archivo_peliculas.append(datos_archivo_pelicula_eliminacion)

                    #Eliminar pelicula de la cartelera
                    del self.cartelera[titulo_pelicula]
                    
                    #Cancelamos las salas que tengan la pelicula asignada
                    for datos in self.ocupacion_sala:
                        if datos[7] == titulo_pelicula:
                            datos[7] = f"{titulo_pelicula} CANCELADA"
                            datos[4] = "XX"
                            datos[5] = "XX"
                            datos[6] = "XX"
                    Funciones.mostrar_exito(f"La pelicula ha sido eliminada")
                    self.guardar_datos()
                else:
                    Funciones.mostrar_error("La pelicula no existe en cartelera")
            

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

#--------------------------------------------------------------------------------------

    def asignar_salas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Asignación de salas")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            try:

                #Preguntamos por la pelicula
                pelicula_a_asignar_sala = Funciones.hacer_pregunta("¿A qué película se le va a asignar sala?\n\nTítulo de la película:  ")
                if pelicula_a_asignar_sala.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                pelicula_a_asignar_sala = pelicula_a_asignar_sala.title()

                if pelicula_a_asignar_sala not in self.cartelera:
                    Funciones.mostrar_error("La película no existe en cartelera")
                else:

                    #Preguntamos el dia que se hara la funcion
                    dia = Funciones.hacer_pregunta("Ingrese el día: ")
                    if dia.lower() == "c":
                        Funciones.mostrar_alerta("La operación se ha cancelado")
                        break
                    dia = int(dia)


                    #El dia tiene que estar dentro de los dias del mes
                    if 0 < dia < 31:

                        #Creamos una lista con los datos de la lista ocupacion sala si encuentra el mismo dia
                        cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia]
                        #Si no hay pues dice que no hay funciones para ese dia
                        if not cronograma_dia:
                            Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia}")
                        else:
                            #Llamamos a la funciones del archivo funciones que muestra las ocupaciones para un dia especifico
                            Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia)

                        #Despues de ser impresa la tabla, pregunta la hora de asignacion
                        hora = Funciones.hacer_pregunta("Ingrese la hora en formato 24h: ")
                        if hora.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        hora = int(hora)

                        #La hora va en formato 24h desde la 8 am hasta las 9 pm maximo
                        if 8 <= hora < 21:
                            minutos = Funciones.hacer_pregunta("Ingrese los minutos: ")
                            if minutos.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            minutos = int(minutos)

                            #Validamos que los minutos no sean mas de 60
                            if 0 <= minutos < 60:
                                sala = Funciones.hacer_pregunta("Ingrese el número de sala: ")
                                if sala.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                sala = int(sala)

                                #En el cine contamos con 3 salas por eso la condicion, pero se puede modificar
                                if 0 < sala < 4:

                                    #Creamos una ID que nos servira de guia sumando el dia, hora, minutos y sala
                                    asignacion_id = str(dia) + str(hora) + str(minutos) + str(sala)
                                    #Creamos una lista con los datos que preguntamos anteriormente
                                    datos = [asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala]
                                    #Son los mismos datos solo que agregamos nuevo al final como informacion para el archivo
                                    datos_archivo = [asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala, "NUEVO"]

                                    #Verificamos si la sala puede ser asignada con la siguiente funcion pasandole los parametros preguntados
                                    esta_ocupada = self.verificar_disponibilidad_sala(asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala)
                                    #Si deuelve un falso entonces paso la prueba de disponibilidad de 3 horas de diferencia entre cada funcion
                                    if not esta_ocupada:
                                        #Agregamos a la lista ocupacion sala los datos
                                        self.ocupacion_sala.append(datos)
                                        #Agregamos al archivo de ocupacion sala los datos archivo
                                        self.archivo.archivo_ocupacion_sala.append(datos_archivo)
                                        #Mostramos el mensaje de que se asigno correctamente y guardamos datos
                                        Funciones.mostrar_exito(f"\nLa película {pelicula_a_asignar_sala} Se presentara en la Sala {sala}\nPara el día {dia} a las {hora:02}:{minutos:02}")
                                        self.guardar_datos()
                                    else:
                                        Funciones.mostrar_alerta(f"La sala {sala} no está disponible")
                                else:
                                    Funciones.mostrar_error("No existe la sala asignada")
                            else:
                                Funciones.mostrar_error("Los minutos deben ir desde 0 hasta 59")
                        else:
                            Funciones.mostrar_error("Los horarios disponibles son de 8:00 - 20:59")
                    else:
                        Funciones.mostrar_error("Seleccione un día del mes")

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    #Esta funcion permite saber si la sala esta disponible para los datos que le demos
    def verificar_disponibilidad_sala(self, asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala):
        #Creamos un intervalo de tiempo, en este caso de 3 horas
        intervalo_tiempo = timedelta(hours=3)
        #Convertimos a int los siguientes datos
        hora_nueva_datetime = datetime(int(año), int(mes), int(dia), int(hora), int(minutos))


        for datos in self.ocupacion_sala:
            #Extraemos los datos con un nombre para identificarlos facilmente
            asignacion_id_existente, año_existente, mes_existente, dia_existente, hora_existente, minutos_existente, sala_existente, pelicula_a_asignar_sala = datos

            #Si la asignacion dada es diferente a cualquier asignacion de la sala pasa la primera prueba y tienes que ser la misma sala para verificar disponibilidad
            if asignacion_id_existente != asignacion_id and sala_existente == sala:
                #Convertimos a int los datos que cumplan esos requisitos de la lista en ocupacion sala
                hora_asignada_datetime = datetime(int(año_existente), int(mes_existente), int(dia_existente), int(hora_existente), int(minutos_existente))
                #Mientras haya una diferencia de 3 horas entre antes y despues de otra funcion 
                if not (hora_nueva_datetime >= hora_asignada_datetime + intervalo_tiempo or hora_nueva_datetime + intervalo_tiempo <= hora_asignada_datetime):
                    return True

        return False

    def eliminar_salas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Eliminación de sala")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            print("                           'x' para borrar funciones canceladas")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            try:
            
                
                dia_cronograma = Funciones.hacer_pregunta("Mostrar cronograma del día: ")
                if dia_cronograma.lower() == "c":
                    Funciones.mostrar_alerta("La operación ha sido cancelada")
                    break
                if dia_cronograma.lower() == "x":
                    #Llamamos a una funcion que elimina salas canceladas si se elimino una pelicula
                    self.eliminar_salas_canceladas()
                    Funciones.mostrar_exito("Se eliminaron las funciones canceladas")
                    break
                dia_cronograma = int(dia_cronograma)

                if 0 < dia_cronograma < 31:
                    #Creamos una lista con los dias que coincidan con el dia preguntado
                    cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_cronograma]

                    if not cronograma_dia:
                        Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia_cronograma}")
                    else:
                        #Muestra el cronograma del dia seleccionado
                        Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia_cronograma)

                        hora_asignacion_a_eliminar = Funciones.hacer_pregunta("Ingrese la hora: ")
                        if hora_asignacion_a_eliminar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        if hora_asignacion_a_eliminar.lower() == "x":
                            self.eliminar_salas_canceladas()
                            Funciones.mostrar_exito("Se eliminaron las funciones canceladas")
                            break
                        hora_asignacion_a_eliminar = int(hora_asignacion_a_eliminar)

                        minutos_asignacion_a_eliminar = Funciones.hacer_pregunta("Ingrese los minutos: ")
                        if minutos_asignacion_a_eliminar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        if minutos_asignacion_a_eliminar.lower() == "x":
                            self.eliminar_salas_canceladas()
                            Funciones.mostrar_exito("Se eliminaron las funciones canceladas")
                            break
                        minutos_asignacion_a_eliminar = int(minutos_asignacion_a_eliminar)
                        
                        sala_asignacion_a_eliminar = Funciones.hacer_pregunta("Ingrese la sala: ")
                        if sala_asignacion_a_eliminar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        if sala_asignacion_a_eliminar.lower() == "x":
                            self.eliminar_salas_canceladas()
                            Funciones.mostrar_exito("Se eliminaron las funciones canceladas")
                            break
                        sala_asignacion_a_eliminar = int(sala_asignacion_a_eliminar)
                        
                        #Vamos a ver si los datos coinciden con los de alguna asignacion
                        se_puede_eliminar_asignacion = False
                        for datos in self.ocupacion_sala:
                            if datos[3] == dia_cronograma and datos[4] == hora_asignacion_a_eliminar and datos[5] == minutos_asignacion_a_eliminar and datos[6] == sala_asignacion_a_eliminar:
                                asignacion_a_eliminar = datos
                                id_asignacion_a_eliminar = datos[0]
                                #Si los datos coinciden se puede eliminar
                                se_puede_eliminar_asignacion = True

                        if se_puede_eliminar_asignacion:
                            
                            #Si se elimina la asinacion de sala, se eliminan los asientos de la sala del cine
                            eliminar_de_salas = False
                            if self.salas:
                                for id_sala, sala in self.salas.items():
                                    if id_sala == id_asignacion_a_eliminar:
                                        eliminar_de_salas = True

                            #Buscamos los datos para agregar al archivo que se hizo una eliminacion de sala
                            for datos_archivo in self.ocupacion_sala:
                                if datos_archivo[0] == id_asignacion_a_eliminar:
                                    datos_a_eliminar_archivo = [datos_archivo[0], datos_archivo[1], datos_archivo[2], datos_archivo[3], datos_archivo[4], datos_archivo[5], datos_archivo[6], datos_archivo[7], "ELIMINADA"]
                            self.archivo.archivo_ocupacion_sala.append(datos_a_eliminar_archivo)

                            #Eliminar la sala matriz con los asientos
                            if eliminar_de_salas:
                                del self.salas[id_asignacion_a_eliminar]

                            #Eliminamos la asignacion de la lista ocupacion sala
                            self.ocupacion_sala.remove(asignacion_a_eliminar)
                            Funciones.mostrar_exito("La Asignacion de sala ha sido eliminada")
                            self.guardar_datos()
                        else:
                            Funciones.mostrar_alerta("No existe una asignacion de sala con los datos especificados")

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")
    
    #Esta funcion se encarga de crear una nueva lista sin las salas canceladas
    def eliminar_salas_canceladas(self):
        self.ocupacion_sala = [datos for datos in self.ocupacion_sala if datos[5] != "XX" and datos[6] != "XX" and datos[7] != "XX"]

    def modificar_salas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Modificar asignación de sala")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            try:

                dia_cronograma = Funciones.hacer_pregunta("Mostrar cronograma del día: ")
                if dia_cronograma.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                dia_cronograma = int(dia_cronograma)

                if 0 < dia_cronograma < 31:
                    #Creamos una lista con los dias que coincidan con el dia preguntado
                    cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_cronograma]

                    if not cronograma_dia:
                        Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia_cronograma}")
                    else:
                        #Muestra el cronograma del dia seleccionado
                        Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia_cronograma)

                        hora_asignacion_a_modificar = Funciones.hacer_pregunta("Ingrese la hora: ")
                        if hora_asignacion_a_modificar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        hora_asignacion_a_modificar = int(hora_asignacion_a_modificar)

                        minutos_asignacion_a_modificar = Funciones.hacer_pregunta("Ingrese los minutos: ")
                        if minutos_asignacion_a_modificar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        minutos_asignacion_a_modificar = int(minutos_asignacion_a_modificar)

                        sala_asignacion_a_modificar = Funciones.hacer_pregunta("Ingrese la sala: ")
                        if sala_asignacion_a_modificar.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        sala_asignacion_a_modificar = int(sala_asignacion_a_modificar)

                        #Comporbamos que la sala buscada este registrada en la lista
                        se_puede_modificar_asignacion = False
                        for datos in self.ocupacion_sala:
                            if datos[3] == dia_cronograma and datos[4] == hora_asignacion_a_modificar and datos[5] == minutos_asignacion_a_modificar and datos[6] == sala_asignacion_a_modificar:
                                asignacion_a_modificar = datos
                                id_asignacion_vieja = datos[0]
                                se_puede_modificar_asignacion = True
                        
                        #Si los datos coinciden se puede modificar
                        if se_puede_modificar_asignacion:
                            Funciones.mostrar_exito("Sala encontrada")
                            
                            #Tiene que cumplor el requisito del intervalo de tiempo
                            cumple_requisitos_para_modificarse = False

                            #Preguntamos por una nueva hora
                            hora_modificada = Funciones.hacer_pregunta("Nueva hora: ")
                            if hora_modificada.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            hora_modificada = int(hora_modificada)

                            minutos_modificados = Funciones.hacer_pregunta("Nuevos minutos: ")
                            if minutos_modificados.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            minutos_modificados = int(minutos_modificados)

                            #Preguntamos por la sala
                            sala_modificada = Funciones.hacer_pregunta("Nueva sala: ")
                            if sala_modificada.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            sala_modificada = int(sala_modificada)

                            if 0 < sala_modificada < 4:

                                #Creamos una nueva id con los datos modificados
                                id_asignacion_nueva = str(dia_cronograma) + str(hora_modificada) + str(minutos_modificados) + str(sala_modificada)
                            
                                #Verificamos si cumple el requisito de 3 horas la modificacion
                                nueva_fecha_hora = datetime(int(año), int(mes), dia_cronograma, hora_modificada, minutos_modificados)
                                intervalo_tiempo = timedelta(hours=3)

                                fecha_hora_asignada = datetime(int(año), int(mes), asignacion_a_modificar[3], asignacion_a_modificar[4], asignacion_a_modificar[5])
                                if not (nueva_fecha_hora >= fecha_hora_asignada + intervalo_tiempo or nueva_fecha_hora + intervalo_tiempo <= fecha_hora_asignada):
                                    cumple_requisitos_para_modificarse = True

                                #Si cumple el requisito entonces modificamos los datos por los nuevos
                                if cumple_requisitos_para_modificarse:
                                    asignacion_a_modificar[4] = hora_modificada
                                    asignacion_a_modificar[5] = minutos_modificados
                                    asignacion_a_modificar[6] = sala_modificada
                                    asignacion_a_modificar[0] = id_asignacion_nueva

                                    #Si en salas se realizo alguna venta y la asignacion vieja esta en salas pues
                                    if self.salas and id_asignacion_vieja in self.salas:
                                        #creamos una sala con la asignacion nueva y como valor la matriz de la asignacion vieja
                                        self.salas[id_asignacion_nueva] = self.salas.pop(id_asignacion_vieja, None)

                                    #Registramos la modificacion en el archivo
                                    datos_a_modificar_archivo = [asignacion_a_modificar[0], asignacion_a_modificar[1], asignacion_a_modificar[2], asignacion_a_modificar[3], asignacion_a_modificar[4], asignacion_a_modificar[5], asignacion_a_modificar[6], asignacion_a_modificar[7], "MODIFICADA"]
                                    self.archivo.archivo_ocupacion_sala.append(datos_a_modificar_archivo)

                                    Funciones.mostrar_exito("La modificación ha sido exitosa")
                                    self.guardar_datos()
                                else:
                                    Funciones.mostrar_error(f"La sala {sala_modificada} no está disponible en el horario especificado")

                        else:
                            Funciones.mostrar_alerta("No existe una asignación de sala con los datos especificados")

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")
     
#--------------------------------------------------------------------------------------

    def mostrar_cartelera_y_cronograma(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Cartelera y cronograma")
            print("Opción siempre disponible: 's' para salir")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")
                break
            else:
                Funciones.mostrar_peliculas(self.cartelera)
                while True:
                    try:
                        dia_cronograma = Funciones.hacer_pregunta("Mostrar cronograma del día: ")
                        if dia_cronograma.lower() == "s":
                            Funciones.mostrar_alerta("Saliendo")
                            break
                        dia_cronograma = int(dia_cronograma)

                        if 0 < dia_cronograma < 31:
                            cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_cronograma]

                            if not cronograma_dia:
                                Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia_cronograma}")
                            else:
                                Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia_cronograma)

                    except ValueError:
                        Funciones.mostrar_error("Ingrese una opción válida")

#######################################################################################




#METODOS PARA EL SISTEMA DE CONFITERIA

#######################################################################################

    def agregar_producto(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Agregar producto")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            try:
                if not self.inventario_confiteria:
                    Funciones.mostrar_alerta("No hay productos en confiteria")
                    break
                else:
                    Funciones.mostrar_productos(self.inventario_confiteria)
                        

                id_producto = Funciones.hacer_pregunta("ID: ")
                if id_producto.lower() == "c":
                    Funciones.mostrar_alerta("La operacón se ha cancelado")
                    break
                
                nombre_producto = Funciones.hacer_pregunta("Nombre: ")
                if nombre_producto.lower() == "c":
                    Funciones.mostrar_alerta("La operacón se ha cancelado")
                    break
                nombre_producto = nombre_producto.title()
                
                categoria_producto = Funciones.hacer_pregunta("Categoria: ")
                if categoria_producto.lower() == "c":
                    Funciones.mostrar_alerta("La operacón se ha cancelado")
                    break
                categoria_producto = categoria_producto.title()

                precio_compra_producto = Funciones.hacer_pregunta("Precio compra: ")
                if precio_compra_producto.lower() == "c":
                    Funciones.mostrar_alerta("La operacón se ha cancelado")
                    break
                precio_compra_producto = float(precio_compra_producto)

                if precio_compra_producto >= 0:

                    precio_venta_producto = Funciones.hacer_pregunta("Precio venta: ")
                    if precio_venta_producto.lower() == "c":
                        Funciones.mostrar_alerta("La operacón se ha cancelado")
                        break
                    precio_venta_producto = float(precio_venta_producto)

                    if precio_venta_producto > precio_compra_producto:

                        cantidad_producto = Funciones.hacer_pregunta("Cantidad: ")
                        if cantidad_producto.lower() == "c":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                            break
                        cantidad_producto = int(cantidad_producto)

                        if cantidad_producto > 0:
                            datos_producto = DatosConfiteria(id_producto, nombre_producto, categoria_producto, precio_compra_producto, precio_venta_producto, cantidad_producto)
                            self.inventario_confiteria[id_producto] = datos_producto
                            Funciones.mostrar_exito("El producto ha sido agregado al inventario")
                            self.guardar_datos()
                        else:
                            Funciones.mostrar_alerta("La cantida no es valida")

                    else:
                        Funciones.mostrar_alerta("El precio digitado no es valido")

                else:
                    Funciones.mostrar_alerta("El precio digitado no es valido")
                    
            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    def eliminar_producto(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Eliminar producto")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            try:
                if not self.inventario_confiteria:
                    Funciones.mostrar_alerta("No hay productos en confiteria")
                    break
                else:
                    Funciones.mostrar_productos(self.inventario_confiteria)

                    id_producto_buscar = Funciones.hacer_pregunta("ID producto que desea eliminar: ")
                    if id_producto_buscar.lower() == "c":
                        Funciones.mostrar_alerta("La operacón se ha cancelado")
                        break
                    
                    if id_producto_buscar in self.inventario_confiteria:

                        Funciones.mostrar_exito("Producto encontrado: ")

                        producto_encontrado = self.inventario_confiteria[id_producto_buscar]

                        for id_producto, datos_producto in self.inventario_confiteria.items():
                            if id_producto_buscar == id_producto:

                                datos_producto = producto_encontrado.obtener_datos_producto()

                                inventario_data = [[datos_producto[0], datos_producto[1], datos_producto[2],
                                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                                    datos_producto[5]]]
                                
                                headers = ["ID", "Producto", "Categoria", "Compra", "Venta", "Cantidad"]
                                print(tabulate(inventario_data, headers=headers, tablefmt="fancy_grid"))
                                print()
                                break

                        eliminar_pregunta = Funciones.hacer_pregunta("Esta seguro que desea eliminar si/no: ")
                        if eliminar_pregunta.lower() == "c":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                            break
                        if eliminar_pregunta.lower() == "no":
                            Funciones.mostrar_alerta("No se ha eliminado el producto")
                        if eliminar_pregunta.lower() == "si":
                            del self.inventario_confiteria[id_producto_buscar]
                            Funciones.mostrar_exito("Se ha eliminado el producto")
                            self.guardar_datos()
                            
                    else:
                        Funciones.mostrar_error("El Producto buscado no esta en confiteria")

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    def modificar_producto(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Modificar producto")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            try:
                if not self.inventario_confiteria:
                    Funciones.mostrar_alerta("No hay productos en confiteria")
                    break
                else:
                    Funciones.mostrar_productos(self.inventario_confiteria)

                    id_producto_buscar = Funciones.hacer_pregunta("ID producto que desea modificar: ")
                    if id_producto_buscar.lower() == "c":
                        Funciones.mostrar_alerta("La operacón se ha cancelado")
                        break

                    if id_producto_buscar in self.inventario_confiteria:

                        Funciones.mostrar_exito("Producto encontrado: ")

                        producto_encontrado = self.inventario_confiteria[id_producto_buscar]

                        for id_producto, datos_producto in self.inventario_confiteria.items():
                            if id_producto_buscar == id_producto:

                                datos_producto = producto_encontrado.obtener_datos_producto()

                                inventario_data = [[datos_producto[0], datos_producto[1], datos_producto[2],
                                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                                    datos_producto[5]]]
                                
                                headers = ["ID", "Producto", "Categoria", "Compra", "Venta", "Cantidad"]
                                print(tabulate(inventario_data, headers=headers, tablefmt="fancy_grid"))
                                print()
       
                        modificar_pregunta = Funciones.hacer_pregunta("Esta seguro que desea modificar si/no: ")
                        if modificar_pregunta.lower() == "c":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                            break  
                        if modificar_pregunta.lower() == "no":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                        if modificar_pregunta.lower() == "si":

                            id_producto_nuevo = Funciones.hacer_pregunta("Nuevo ID: ")
                            if id_producto_nuevo.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            if id_producto_buscar in self.inventario_confiteria:
                                producto_encontrado = self.inventario_confiteria.pop(id_producto_buscar)
                                self.inventario_confiteria[id_producto_nuevo] = producto_encontrado
                            producto_encontrado.id_producto = id_producto_nuevo

                            nombre_producto = Funciones.hacer_pregunta("Nuevo Nombre: ")
                            if nombre_producto.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            producto_encontrado.nombre_producto = nombre_producto.title()

                            categoria_producto = Funciones.hacer_pregunta("Nueva Categoría: ")
                            if categoria_producto.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            producto_encontrado.categoria_producto = categoria_producto.title()

                            precio_compra_producto = Funciones.hacer_pregunta("Nuevo Precio compra: ")
                            if precio_compra_producto.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            producto_encontrado.precio_compra_producto = float(precio_compra_producto)

                            if producto_encontrado.precio_compra_producto >= 0:

                                precio_venta_producto = Funciones.hacer_pregunta("Nuevo Precio venta: ")
                                if precio_venta_producto.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                producto_encontrado.precio_venta_producto = float(precio_venta_producto)

                                if producto_encontrado.precio_venta_producto > producto_encontrado.precio_compra_producto:

                                    cantidad_producto = Funciones.hacer_pregunta("Nueva Cantidad: ")
                                    if cantidad_producto.lower() == "c":
                                        Funciones.mostrar_alerta("La operación se ha cancelado")
                                        break
                                    producto_encontrado.cantidad_producto = int(cantidad_producto)

                                    if producto_encontrado.cantidad_producto > 0:
                                        Funciones.mostrar_exito("Se ha modificado el producto")
                                        self.guardar_datos()
                                    else:
                                        Funciones.mostrar_alerta("La cantidad no es válida")

                                else:
                                    Funciones.mostrar_alerta("El precio digitado no es válido")

                            else:
                                Funciones.mostrar_alerta("El precio digitado no es válido")

            except ValueError:
                Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    #METODOS PARA MENU ADMINISTRACION DE COMBOS

    ##########################################################################################

    

    ##########################################################################################

    def buscar_productos(self):
        mostrar_productos_orden = None
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Agregar producto")
            #Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            print("Ordenar por nombre: 'on'")
            print("Ordenar por categoria 'ocat'")
            print("Ordenar por cantidad: 'ocan'")
            print("Ordenar por precio compra: 'opc'")
            print("Ordenar por precio venta 'opv'")
            print("Bucar por nombre: 'bn'")


            if not self.inventario_confiteria:
                Funciones.mostrar_alerta("No hay productos en confiteria")
                break
            else:
                if mostrar_productos_orden:
                    Funciones.mostrar_productos(mostrar_productos_orden)
                else:
                    Funciones.mostrar_productos(self.inventario_confiteria)
                    # Definir colores y estilos
                    color_titulo = Fore.LIGHTCYAN_EX
                    color_headers = Fore.LIGHTYELLOW_EX
                    estilo_reset = Style.RESET_ALL
                    try:
                        buscar_id_producto = Funciones.hacer_pregunta("Buscar id producto: ")
                        if buscar_id_producto.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break

                        if buscar_id_producto.lower() == "on":
                            orden = sorted(self.inventario_confiteria.items(), key=lambda x: x[1].nombre_producto)
                            mostrar_productos_orden = dict(orden)

                        if buscar_id_producto.lower() == "ocat":
                            orden = sorted(self.inventario_confiteria.items(), key=lambda x: x[1].categoria_producto)
                            mostrar_productos_orden = dict(orden)

                        if buscar_id_producto.lower() == "ocan":
                            orden = sorted(self.inventario_confiteria.items(), key=lambda x: x[1].cantidad_producto)
                            mostrar_productos_orden = dict(orden)

                        if buscar_id_producto.lower() == "opc":
                            orden = sorted(self.inventario_confiteria.items(), key=lambda x: x[1].precio_compra_producto)
                            mostrar_productos_orden = dict(orden)

                        if buscar_id_producto.lower() == "opv":
                            orden = sorted(self.inventario_confiteria.items(), key=lambda x: x[1].precio_venta_producto)
                            mostrar_productos_orden = dict(orden)

                        if buscar_id_producto.lower() == "bn":
                            nombre_a_buscar = Funciones.hacer_pregunta("Nombre a buscar: ").title()
                            productos_encontrados = [producto for producto in self.inventario_confiteria.values()
                                                    if nombre_a_buscar.lower() in producto.nombre_producto.lower()]

                        if productos_encontrados:
                            print(f"\n\n{color_titulo}Productos encontrados:\n{estilo_reset}")
                            encontrados = []
                            for producto_encontrado in productos_encontrados:
                                datos_producto = producto_encontrado.obtener_datos_producto()

                                encontrados.append([datos_producto[0], datos_producto[1], datos_producto[2],
                                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                                    datos_producto[5]])

                            headers = [f"{color_headers}ID", "Producto", "Categoria", "Compra", "Venta", f"Cantidad{estilo_reset}"]
                            print(tabulate(encontrados, headers=headers, tablefmt="fancy_grid"))
                            print()
                            os.system("pause")
                        else:
                            Funciones.mostrar_alerta(f"No se encontraron productos que contengan '{nombre_a_buscar}'.")


                        if buscar_id_producto.isnumeric():

                            if buscar_id_producto in self.inventario_confiteria:

                                print(f"{color_titulo}\n\nProducto encontrado:\n{estilo_reset}")

                                producto_encontrado = self.inventario_confiteria[buscar_id_producto]

                                for id_producto, datos_producto in self.inventario_confiteria.items():
                                    if buscar_id_producto == id_producto:

                                        datos_producto = producto_encontrado.obtener_datos_producto()

                                        inventario_data = [[datos_producto[0], datos_producto[1], datos_producto[2],
                                                            f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                                            datos_producto[5]]]
                                        
                                        headers = [f"{color_headers}ID", "Producto", "Categoria", "Compra", "Venta", f"Cantidad{estilo_reset}"]
                                        print(tabulate(inventario_data, headers=headers, tablefmt="fancy_grid"))
                                        print()
                                        os.system("pause")
                            else:
                                if buscar_id_producto not in self.inventario_confiteria:
                                    Funciones.mostrar_alerta("No hay ningun producto con la ID buscada")       

                    except ValueError:
                        Funciones.mostrar_error("Error de valor: Ingrese un número válido")

                    except TypeError:
                        Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")



#######################################################################################




#METODOS PARA EL SISTEMA DE VENTAS PELICULAS

#######################################################################################

    def realizar_venta_pelicula(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Venta")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            
            #Si no hay cartelera no se puede realizar venta
            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")
                break
            else:
                #si hay entonces:
                Funciones.mostrar_peliculas(self.cartelera)

                try:
                    #Preguntamos por la pelicula a vender
                    pelicula_a_comprar = Funciones.hacer_pregunta("Película: ")

                    if pelicula_a_comprar.lower() == "c":
                        Funciones.mostrar_alerta("La venta se ha cancelado")
                        break
                    pelicula_a_comprar = pelicula_a_comprar.title()

                    #Si la pelicula esta en cartelera la asignamos a la variable pelicula seleccionada
                    if pelicula_a_comprar in self.cartelera:

                        #Esto nos permite trabajar de forma mas sencilla
                        pelicula_seleccionada = self.cartelera[pelicula_a_comprar]

                        #Vamos a ver el cronograma para la pelicula escogida
                        dias = set()
                        for datos in self.ocupacion_sala:
                            #Si la pelicula esta en ocupacion sala
                            if datos[7] == pelicula_a_comprar:
                                #Agrega el dia al set dias
                                dias.add(int(datos[3]))
                        
                        if not dias:
                            Funciones.mostrar_alerta(f"No hay salas asignadas para {pelicula_a_comprar}")
                        else:
                            print(f"\nHay funciones disponibles para los días {dias}")
                            
                            #Pedimos que seleccione el dia a comprar el tiquete
                            dia_de_compra = Funciones.hacer_pregunta("Seleccione un día: ")
                            if dia_de_compra.lower() == "c":
                                Funciones.mostrar_alerta("La venta se ha cancelado")
                                break
                            dia_de_compra = int(dia_de_compra)

                            #Si esta en dias entonces mostramos los horarios de las funciones para la pelicula escogida en el dia escogido
                            if dia_de_compra in dias:
                                #Creamos una lista con los datos que coincidan en el dia y en la pelicula y la mostramos
                                cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_de_compra and datos[7] == pelicula_a_comprar]
                                Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia_de_compra)

                                #Escoja la hora
                                hora_de_compra = Funciones.hacer_pregunta("hora: ")
                                if hora_de_compra.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                hora_de_compra = int(hora_de_compra)

                                #Escoja los minutos
                                minutos_de_compra = Funciones.hacer_pregunta("minutos: ")
                                if minutos_de_compra.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                minutos_de_compra = int(minutos_de_compra)

                                #Y por ultimos la sala
                                sala_de_compra = Funciones.hacer_pregunta("sala: ")
                                if sala_de_compra.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                sala_de_compra = int(sala_de_compra)

                                #Creamos la ID de la misma manera que en las asignaciones
                                id_identificacion_sala = str(dia_de_compra) + str(hora_de_compra) + str(minutos_de_compra) + str(sala_de_compra)
                                primera_compra_de_sala = False

                                #Si la id coincide entonces los datos son correctos
                                if id_identificacion_sala in self.salas:

                                    #Buscamos en salas la id de la asignacion
                                    for id_sala, sala_a_modificar in self.salas.items():
                                        if id_sala == id_identificacion_sala:
                                            #si la encuentra entonces la asignamos a una variable sala
                                            sala = sala_a_modificar

                                    #Comprobamos si esta llena la sala encontrada
                                    sala_llena = Funciones.comprobar_sala_llena(sala)

                                    #Si devuelve verdadero entonces no se realizara la venta, la sala esta llena
                                    if sala_llena:
                                        Funciones.mostrar_alerta("La sala esta llena, no es posible hacer venta")

                                    #Si hay hacientos disponibles continuamos
                                    if not sala_llena:
                                        
                                        asignacion_de_asientos = True

                                        while asignacion_de_asientos:

                                            #Mostramos los datos de la sala
                                            print(f"\nAsignacion: {id_identificacion_sala}")
                                            print(f"\nPelicula: {pelicula_a_comprar}")
                                            print(f"dia: {dia_de_compra} - hora: {hora_de_compra:02}:{minutos_de_compra:02}")

                                            #Imprimimos los asientos de la sala
                                            Funciones.imprimir_sala_centro(sala)
                   
                                            #Preguntamos por cuantos asientos va a comprar maximo 5 porque vi que en royal films tenian un max de 5
                                            cuantos_boletos_compra = Funciones.hacer_pregunta("\nCuantos asientos (5 max): ")
                                            if cuantos_boletos_compra.lower() == "c":
                                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                                break
                                            cuantos_boletos_compra = int(cuantos_boletos_compra)

                                            #Evaluamos que se cumpla la condicion
                                            if 0 < cuantos_boletos_compra <= 5:

                                                asientos_validos = 0
                                                cancelacion_compra = False
                                                validos = []

                                                #Vamos a preguntar el numero de asiento las veces de el numero de asientos comprados
                                                while asientos_validos < cuantos_boletos_compra:

                                                    #Pregunta por el numero de asiento
                                                    asiento_a_comprar = Funciones.hacer_pregunta("Selecione un asiento: ")
                                                    #Si cancela la compra activamos una cancelacion que se ejecutara fuera del while
                                                    if asiento_a_comprar.lower() == "c":
                                                        cancelacion_compra = True
                                                        break

                                                    #Mientras el asiento sea diferente de XX porque son asientos vendidos
                                                    if asiento_a_comprar != "XX":

                                                        #Recorremos las filas de la sala
                                                        for i in range(len(sala)):
                                                            #Recorremos los asientos por fila
                                                            for j in range(len(sala[i])):
                                                                #Si el asiento a comprar coincide con uno de la sala
                                                                if sala[i][j] == asiento_a_comprar:
                                                                    #Y si el asiento ya no se escogio antes
                                                                    if sala[i][j] not in validos:
                                                                        #Agregamos el asientos a Validos
                                                                        validos.append(sala[i][j])
                                                                        #Cambiamos la presentacion para ser facil de identificar
                                                                        sala[i][j] = f"|{sala[i][j]}|"
                                                                        #Agregamos un asiento valido
                                                                        asientos_validos += 1
                                                                        #Salimos del for
                                                                        break         
                                                                    else:
                                                                        break
                                                            else:
                                                                #Salimos del segundo for ya roto el primer for
                                                                continue
                                                            break     
                                                        else:
                                                            Funciones.mostrar_error("Este asiento no es válido")
                                                    else:
                                                        Funciones.mostrar_error("No se puede seleccionar asientos vendidos")

                                                #Imprimos la sala con los asientos seleccionados
                                                Funciones.imprimir_sala_centro(sala)

                                                #Mostramos el valor total de la pelicula para los asientos seleccionados
                                                valor_total_asientos = cuantos_boletos_compra * pelicula_seleccionada.costo_pelicula
                                                print(f"\n\nTotal asientos: $ {valor_total_asientos:.2f}")

                                                #Preguntamos por confirmar los asientos
                                                confirmar_asientos = Funciones.hacer_pregunta("\n¿Confirmar asientos? si/no: ")

                                                #Si cancela la compra
                                                if confirmar_asientos.lower() == "c":
                                                    #Volvemos los asientos a la letra y el numero 
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    #La variable que se ejecutara cuand se cierre el while 
                                                    cancelacion_compra = True
                                                    #Cerramos el while
                                                    asignacion_de_asientos = False

                                                #Si "no" entonces cambio de asientos, volvemos los asientos a la normalidad sin salir del while
                                                if confirmar_asientos.lower() == "no":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
            
                                                #Creamos una variable verdadera para generar la facutura
                                                if confirmar_asientos.lower() == "si":
                                                    generar_factura = True
                                                    break

                                        #En caso de que se cancele la compra dentro de los otros while
                                        if cancelacion_compra:
                                            break

                                        #Si se confirmo los asintos entonces
                                        if generar_factura:

                                            #Preguntamos al cliente su identificacion para el registro
                                            identificacion_cliente = Funciones.hacer_pregunta("ID cliente: ")
                                            if identificacion_cliente.lower() == "c":
                                                Funciones.restablecer_asientos_seleccionados(sala)
                                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                                break
                                            identificacion_cliente = int(identificacion_cliente)

                                            #Buscamos si el cliente no esta regisrado de antes
                                            if identificacion_cliente not in self.clientes:

                                                #Si no entonces preguntamos por su noombre
                                                nombre_cliente = Funciones.hacer_pregunta("Nombre cliente: ")
                                                if nombre_cliente.lower() == "c":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                                    break
                                                nombre_cliente = nombre_cliente.title()
                                                
                                                #La edad del cliente
                                                edad_cliente = Funciones.hacer_pregunta("Edad cliente: ")
                                                if edad_cliente.lower() == "c":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                                    break
                                                edad_cliente = int(edad_cliente)

                                                #Creamos el objeto con los datos del cleinte
                                                cliente = DatosCliente(identificacion_cliente, nombre_cliente, edad_cliente)
                                                #Lo agregamos a clientes con la id como clave y los datos como valor
                                                self.clientes[identificacion_cliente] = cliente
                                            
                                            else:
                                                #Si esta registrado de antes solamente lo buscamos y lo asignamos a la variable cliente
                                                cliente = self.clientes[identificacion_cliente]
                                        
                                            #Generamos la factura pasandole los datos que esta clase solicita
                                            fecha, numero_factura, valor_total_factura = self.factura_pelicula.generar_factura(cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra)

                                            #Confirmamos los asientos seleccionados convirtiendolos a XX
                                            Funciones.confirmar_asientos_seleccionados(sala)
                                            #Esa identificacion sala va a cambiar po la nueva sala
                                            self.salas[id_identificacion_sala] = sala
                                            #Aumentamos el dinero en caja de la venta
                                            self.dinero_en_caja += valor_total_asientos
                                            ingresos = [fecha, numero_factura, valor_total_factura, "CARTELERA"]
                                            ingresos_archivo = [fecha, numero_factura, valor_total_factura, "CARTELERA", "NUEVO"]
                                            self.ingresos[fecha] = ingresos
                                            self.archivo.archivo_ingresos.append(ingresos_archivo)
                                            Funciones.mostrar_exito("La compra se ha realizado correctamente")
                                            self.guardar_datos()
                   
                            
                                else:
                                    #Verificamos que los datos cumplan con los de la asignacion sala
                                    for datos in self.ocupacion_sala:
                                        if id_identificacion_sala == datos[0] and dia_de_compra == datos[3] and hora_de_compra == datos[4] and minutos_de_compra == datos[5] \
                                            and sala_de_compra == datos[6] and pelicula_a_comprar == datos[7]:
                                            #Si es la primera compra no estanba registrada en salas anteriormente
                                            primera_compra_de_sala = True

                                    if primera_compra_de_sala:

                                        #Realizamos el mismo proceso anteriormente visto
                                        asignacion_de_asientos = True

                                        while asignacion_de_asientos:

                                            sala = Funciones.generar_sala()
                                            Funciones.imprimir_sala_centro(sala)

                                            cuantos_boletos_compra = Funciones.hacer_pregunta("\nCuantos asientos (5 max): ")
                                            if cuantos_boletos_compra.lower() == "c":
                                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                                break
                                            cuantos_boletos_compra = int(cuantos_boletos_compra)

                                            if 0 < cuantos_boletos_compra <= 5:

                                                asientos_validos = 0
                                                cancelacion_compra = False
                                                validos = []

                                                while asientos_validos < cuantos_boletos_compra:

                                                    asiento_a_comprar = Funciones.hacer_pregunta("Selecione un asiento: ")
                                                    if asiento_a_comprar.lower() == "c":
                                                        cancelacion_compra = True
                                                        break

                                                    for i in range(len(sala)):
                                                        for j in range(len(sala[i])):
                                                            if sala[i][j] == asiento_a_comprar:
                                                                if sala[i][j] not in validos:
                                                                    validos.append(sala[i][j])
                                                                    sala[i][j] = f"|{sala[i][j]}|"
                                                                    asientos_validos += 1
                                                                    break         
                                                                else:
                                                                    break
                                                        else:
                                                            continue
                                                        break     
                                                    else:
                                                        Funciones.mostrar_error("Este asiento no es válido")
                                                    

                                                Funciones.imprimir_sala_centro(sala)

                                                valor_total_asientos = cuantos_boletos_compra * pelicula_seleccionada.costo_pelicula
                                                print(f"\n\nTotal asientos: $ {valor_total_asientos:.2f}")

                                                confirmar_asientos = Funciones.hacer_pregunta("\n¿Confirmar asientos? si/no: ")

                                                if confirmar_asientos.lower() == "c":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    cancelacion_compra = True
                                                    asignacion_de_asientos = False

                                                if confirmar_asientos.lower() == "no":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
              
                                                if confirmar_asientos.lower() == "si":
                                                    generar_factura = True
                                                    break
                                        
                                        if cancelacion_compra:
                                            break
                                        
                                        if generar_factura:

                                            identificacion_cliente = Funciones.hacer_pregunta("ID cliente: ")
                                            if identificacion_cliente.lower() == "c":
                                                Funciones.restablecer_asientos_seleccionados(sala)
                                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                                break
                                            identificacion_cliente = int(identificacion_cliente)

                                            if identificacion_cliente not in self.clientes:

                                                nombre_cliente = Funciones.hacer_pregunta("Nombre cliente: ")
                                                if nombre_cliente.lower() == "c":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                                    break
                                                nombre_cliente = nombre_cliente.title()

                                                edad_cliente = Funciones.hacer_pregunta("Edad cliente: ")
                                                if edad_cliente.lower() == "c":
                                                    Funciones.restablecer_asientos_seleccionados(sala)
                                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                                    break
                                                edad_cliente = int(edad_cliente)

                                                cliente = DatosCliente(identificacion_cliente, nombre_cliente, edad_cliente)
                                                self.clientes[identificacion_cliente] = cliente
                                            
                                            else:
                                                cliente = self.clientes[identificacion_cliente]

                                            fecha, numero_factura, valor_total_factura = self.factura_pelicula.generar_factura(cliente, pelicula_seleccionada, validos, id_identificacion_sala, dia_de_compra, hora_de_compra, minutos_de_compra, sala_de_compra)

                                            Funciones.confirmar_asientos_seleccionados(sala)
                                            self.salas[id_identificacion_sala] = sala
                                            Funciones.mostrar_exito("La compra se ha realizado correctamente")
                                            self.dinero_en_caja += valor_total_asientos
                                            ingresos = [fecha, numero_factura, valor_total_factura, "CARTELERA"]
                                            ingresos_archivo = [fecha, numero_factura, valor_total_factura, "CARTELERA","NUEVO"]
                                            self.ingresos[fecha] = ingresos
                                            self.archivo.archivo_ingresos.append(ingresos_archivo)
                                            self.guardar_datos()

                                    else:
                                        Funciones.mostrar_alerta("horario incorrecto y/o sala incorrectaa")

                            else:
                                Funciones.mostrar_alerta(f"No hay funciones para el dia {dia_de_compra}")

                except ValueError:
                    Funciones.mostrar_error("Error de valor: Ingrese un número válido")

                except TypeError:
                    Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    def deshacer_venta_pelicula(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Cancelar Venta")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            if not self.factura_pelicula.facturas_peliculas:
                Funciones.mostrar_alerta("No hay ventas realizadas")
                break
            else:
                Funciones.mostrar_facturas_peliculas(self.factura_pelicula.facturas_peliculas)

                try:
                    factura_a_eliminar = Funciones.hacer_pregunta("Numero Factura: ")
                    if factura_a_eliminar.lower() == "c":
                        Funciones.mostrar_alerta("La operación se ha cancelado")
                        break
                    factura_a_eliminar = int(factura_a_eliminar)

                    for numero_factura, datos_factura in self.factura_pelicula.facturas_peliculas.items():
                        if numero_factura == factura_a_eliminar:
                            fecha_venta, cliente, pelicula, asientos, id_sala_venta, dia_compra, hora_compra, minutos_compra, sala_de_compra = datos_factura
                            identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()
                            titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula = pelicula.obtener_datos_pelicula()
                            total_venta = costo_pelicula * len(asientos)

                            Funciones.mostrar_exito("Factura encontrada")

                            boleto = f"""
                            ------------------------------------------------
                                    CINE UDENAR - FACTURA DE VENTA
                            ------------------------------------------------
                            Número de factura: {numero_factura:04}
                            Fecha de venta: {fecha_venta}
                            ------------------------------------------------
                            Película: {titulo_pelicula}        {edad_minima}+
                            Duración: {duracion} minutos
                            Sala: {sala_de_compra}
                            Día y hora: {dia_compra} - {hora_compra:02}:{minutos_compra:02}
                            Asientos: {' '.join(asientos)}
                            ------------------------------------------------
                            Cliente: {nombre_cliente} ({edad_cliente} años)
                            C.C/I.T: {identificacion_cliente}
                            ------------------------------------------------
                            Total: ${total_venta:.2f}
                            ------------------------------------------------
                            ¡Gracias por su compra!
                            ------------------------------------------------
                            """

                            # Imprimir el boleto
                            print(boleto)

                            cancelar_factura = False

                            while True:

                                imprimir_factura_pregunta = Funciones.hacer_pregunta("¿Cancelar esta compra?  si/no: ")
                                if imprimir_factura_pregunta.lower() == "no":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                elif imprimir_factura_pregunta.lower() == "si":
                                    cancelar_factura = True
                                    break
                                else:
                                    Funciones.mostrar_alerta("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")

                            if cancelar_factura:
                                
                                sala_original = Funciones.generar_sala()

                                for id_sala, sala in self.salas.items():
                                    if id_sala == id_sala_venta:
                                        sala_venta = sala

                                Funciones.imprimir_sala_centro(sala_venta)

                                for asiento in asientos:
                                    for i in range(len(sala_original)):
                                        for j in range(len(sala_original[i])):
                                            if sala_original[i][j] == asiento:
                                                # Restaurar el asiento en la sala de venta
                                                sala_venta[i][j] = sala_original[i][j]

                                for fecha, datos_ingreso in self.ingresos.items():
                                    if numero_factura == datos_ingreso[1] and datos_ingreso[3] == "CARTELERA":
                                        ingreso_eliminado_archivo = [fecha, datos_ingreso[1], datos_ingreso[2], datos_ingreso[3], "ELIMINADO"]
                                        self.archivo.archivo_ingresos.append(ingreso_eliminado_archivo)
                                        fecha_a_eliminar_ingresos = fecha

                                del self.ingresos[fecha_a_eliminar_ingresos]
                                        
                                Funciones.mostrar_exito("Ingreso eliminado con exito")
                                
                                self.dinero_en_caja -= total_venta

                                datos_archivo = [fecha_venta, cliente, pelicula, asientos, id_sala_venta, dia_compra, hora_compra, minutos_compra, sala_de_compra, "ELIMINADA"]
                                self.archivo.archivo_factura_peliculas.append(datos_archivo)

                                del self.factura_pelicula.facturas_peliculas[numero_factura]

                                Funciones.mostrar_exito("Venta eliminada") 

                                print("\nLa sala ha quedado asi:\n")
                                Funciones.imprimir_sala_centro(sala_venta)
                                
                                os.system("pause")
                                break

                except Exception as e:
                    print(f"Error {e}")

    def administracion_de_salas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Ver asientos salas")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            if not self.ocupacion_sala:
                Funciones.mostrar_alerta("No hay salas asignadas")
            else:
                try:
                    dia_mostrar_salas = Funciones.hacer_pregunta("Dia: ")
                    if dia_mostrar_salas.lower() == "c":
                        break
                    dia_mostrar_salas = int(dia_mostrar_salas)

                    salas_encontradas = False

                    for datos_sala in self.ocupacion_sala:
                        if datos_sala[3] != dia_mostrar_salas:
                            continue
                        else:
                            id_sala = datos_sala[0]
                            if id_sala in self.salas:
                                for id_busqueda, sala_actual in self.salas.items():
                                    if id_busqueda == id_sala:
                                        for datos_ocupacion in self.ocupacion_sala:
                                            if datos_ocupacion[0] == id_sala:
                                                id_sala = datos_ocupacion[0]
                                                pelicula = datos_ocupacion[7]
                                                dia = datos_ocupacion[3]
                                                hora = datos_ocupacion[4]
                                                minutos = datos_ocupacion[5]
                                                sala = datos_ocupacion[6]
                                                break

                                        print(f"\n\nID de Sala: {id_sala}")
                                        print(f"Película: {pelicula}")
                                        print(f"Día: {dia} - Hora: {hora:02}:{minutos:02} - Sala: {sala}")

                                        Funciones.imprimir_sala_centro(sala_actual)
                                        salas_encontradas = True
                                        break


                            else:
                                for datos in self.ocupacion_sala:
                                    if datos[0] == id_sala:
                                        pelicula = datos[7]
                                        dia = datos[3]
                                        hora = datos[4]
                                        minutos = datos[5]
                                        sala = datos[6]
                                        print(f"\n\nID de Sala: {id_sala}")
                                        print(f"Película: {pelicula}")
                                        print(f"Día: {dia} - Hora: {hora:02}:{minutos:02} - Sala: {sala}")

                                        Funciones.imprimir_sala_centro(Funciones.generar_sala())
                                        salas_encontradas = True
                                        break

                    if not salas_encontradas:
                        Funciones.mostrar_alerta("No hay salas para ese día")

                    if salas_encontradas:
                        print()
                        os.system("pause")

                except ValueError:
                    Funciones.mostrar_error("Error de valor: Ingrese un número válido")

                except TypeError:
                    Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")
    
    def ver_ventas_peliculas(self):
        pass





#######################################################################################



#METODOS PARA EL SISTEMA DE VENTAS CONFITERIA

#######################################################################################





#######################################################################################





#METODOS PARA EL SISTEMA DE INFORMACION Y ESTADISTICAS

#######################################################################################


#METODOS PARA EL MANEJO DE DINERO EN CAJA

    def vaciar_dinero_caja(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        fechayhora = str(fecha) + str(hora)
        datos = [fecha, hora, self.dinero_en_caja, "Se dejo la caja en 0"]
        self.modificaciones_caja[fechayhora] = datos
        self.dinero_en_caja = 0
        Funciones.mostrar_exito("La caja a quedado en $ 0")

    def restar_dinero_caja(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Ver asientos salas")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            print("                           'v' para vaciar caja")

            resta = Funciones.hacer_pregunta("¿Cuanto dinero desea retirar de la caja?: ")
            if resta.lower() == "c":
                Funciones.mostrar_alerta("La operación se ha cancelado")
                break
            if resta.lower() == "v":
                self.vaciar_dinero_caja()
                break
            resta = float(resta)

            if resta < self.dinero_en_caja:
                fecha = datetime.now().strftime("%Y-%m-%d")
                hora = datetime.now().strftime("%H:%M:%S")
                fechayhora = str(fecha) + str(hora)
                datos = [fecha, hora, self.dinero_en_caja, f"Se quitó ${resta:.2f} del dinero en caja"]

                self.modificaciones_caja[fechayhora] = datos
                self.dinero_en_caja -= resta
                Funciones.mostrar_exito(f"La caja quedó en: $ {self.dinero_en_caja:.2f}")
                break
            elif resta == self.dinero_en_caja:
                self.vaciar_dinero_caja()
            else:
                Funciones.mostrar_error("No se puede quitar mas dinero del que hay en caja")
    
    def aumentar_dinero_caja(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Ver asientos salas")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            
            suma = Funciones.hacer_pregunta("¿Cuanto dinero desea sumar a la caja?: ")
            if suma.lower() == "c":
                Funciones.mostrar_alerta("La operación se ha cancelado")
                break
            suma = float(suma)

            if suma > 0:
                fecha = datetime.now().strftime("%Y-%m-%d")
                hora = datetime.now().strftime("%H:%M:%S")
                fechayhora = str(fecha) + str(hora)
                datos = [fecha, hora, self.dinero_en_caja, f"Se sumó ${suma:.2f} a la caja"]
                self.modificaciones_caja[fechayhora] = datos
                self.dinero_en_caja += suma
                Funciones.mostrar_exito(f"La caja quedó en: ${self.dinero_en_caja:.2f}")
                break
    
    def ver_movimientos_caja(self):
        while True:
            if not self.modificaciones_caja:
                Funciones.mostrar_alerta("Aun no hay movimientos de caja")
                break
            else:
                color_headers = Fore.LIGHTYELLOW_EX
                estilo_reset = Style.RESET_ALL
                os.system("cls")
                Funciones.encabezado()
                Funciones.subtitulo("Movimientos de caja")
                headers = [f"{color_headers}Fecha modificación", "Hora", "Caja original", f"Modificación{estilo_reset}"]
                data = []

                for fechayhora, datos in self.modificaciones_caja.items():
                    fecha = datos[0]
                    hora = datos[1]
                    dinero_en_caja = datos[2]
                    descripcion_de_modificacion = datos[3]
                    data.append([fecha, hora, dinero_en_caja, descripcion_de_modificacion])

                table = tabulate(data, headers, tablefmt="fancy_grid")
                print(table)

            print()
            os.system("pause")
            break
            

#METODOS PARA EL MANEJO DE EGRESOS

#--------------------------------------------------------------------------------------

    def registrar_un_egreso(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Registro de un egreso")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            try:
                numero_factura = Funciones.hacer_pregunta("Numero Factura: ")
                if numero_factura.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                
                valor_egreso = Funciones.hacer_pregunta("Valor del pago: ")
                if valor_egreso.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                valor_egreso = float(valor_egreso)

                descripcion_egreso = Funciones.hacer_pregunta("Descripcion del pago: ")
                if descripcion_egreso.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break


                de_donde_sale_el_dinero = Funciones.hacer_pregunta("De donde sa paga: \n\n1.  De la caja\n2.  Otro\n\n: ")

                if de_donde_sale_el_dinero.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break

                de_donde_sale_el_dinero = int(de_donde_sale_el_dinero)
                el_dinero_sale_de = None
                
                while True:
                    if de_donde_sale_el_dinero == 1:
                        if self.dinero_en_caja >= valor_egreso:
                            self.dinero_en_caja -= valor_egreso
                            el_dinero_sale_de = "De la caja"
                            break

                    elif de_donde_sale_el_dinero == 2:
                        el_dinero_sale_de = "otro"
                        break

                fecha_egreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                egreso = DatosEgreso(numero_factura, valor_egreso, descripcion_egreso, el_dinero_sale_de)
                egreso_archivo = [fecha_egreso, numero_factura, valor_egreso, descripcion_egreso, el_dinero_sale_de, "NUEVO"]

                self.egresos[fecha_egreso] = egreso
                self.archivo.archivo_egresos.append(egreso_archivo)

                Funciones.mostrar_exito("Egreso agregado con exito")

            except ValueError:
                    Funciones.mostrar_error("Error de valor: Ingrese un número válido")

            except TypeError:
                Funciones.mostrar_error("Error de tipo: Ingrese un tipo de dato válido")

    def cancelar_un_egreso(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Eliminar un egreso")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")
            if not self.egresos:
                Funciones.mostrar_alerta("No hay egresos registrados")
                break
            else:
                Funciones.mostrar_egresos(self.egresos)
                try:
                    seleccion = Funciones.hacer_pregunta("Seleccione el egreso a eliminar (número): ")
                    if seleccion.lower() == "c":
                        Funciones.mostrar_alerta("La operación se ha cancelado")
                        break
                    seleccion = int(seleccion)

                    #Se va a seleccionar el egreso a eliminar por item
                    if 1 <= seleccion <= len(self.egresos):
                        #La fecha va a ser igual a la seleccion de la lista de claves de egresos
                        fecha_egreso_a_eliminar = list(self.egresos.keys())[seleccion - 1]
                        #Obtenemos el objeto buscado por la fecha
                        egreso_eliminar = self.egresos[fecha_egreso_a_eliminar]
                        #Lo registramos en el archivo como eliminado
                        egreso_eliminar_archivo = [fecha_egreso_a_eliminar, egreso_eliminar.numero_factura, egreso_eliminar.valor_egreso, egreso_eliminar.descripcion_egreso, egreso_eliminar.el_dinero_sale_de, "ELIMINADO"]
                        self.dinero_en_caja += egreso_eliminar.valor_egreso  #Asumiendo que se debe devolver el dinero a la caja
                        self.archivo.archivo_egresos.append(egreso_eliminar_archivo)
                        del self.egresos[fecha_egreso_a_eliminar] #Eliminamos el egreso
                        Funciones.mostrar_exito("Egreso eliminado con éxito")
                        Funciones.mostrar_exito("El dinero se sumó a la caja")
                    else:
                        Funciones.mostrar_alerta("Selección no válida. Intente nuevamente.")

                except ValueError:
                    Funciones.mostrar_error("Error de valor: Ingrese un número válido")

    def ver_egresos(self):
        # Definir colores y estilos
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}I N G R E S O S               |               E G R E S O S            {estilo_reset}"

        ingresos_data = []
        for fecha, datos_ingreso in self.ingresos.items():
            ingresos_data.append([datos_ingreso[0], datos_ingreso[1], datos_ingreso[2], datos_ingreso[3]])

        egresos_data = []
        for fecha, datos_egreso in self.egresos.items():
            egresos_data.append([fecha, datos_egreso.numero_factura, datos_egreso.valor_egreso, datos_egreso.descripcion_egreso, datos_egreso.el_dinero_sale_de])

        headers_ingresos = [f"{color_headers}Fecha", " Numero de Factura", "Total", "Descripcion"]
        headers_egresos = [f"{color_headers}Fecha", "Número de Factura", "Valor", "Descripción", f"De dónde se paga{estilo_reset}"]

        # Obtener la tabla de ingresos y egresos utilizando tabulate sin imprimir
        tabla_ingresos = tabulate(ingresos_data, headers=headers_ingresos, tablefmt="fancy_grid")
        tabla_egresos = tabulate(egresos_data, headers=headers_egresos, tablefmt="fancy_grid")

        # Convertir las tablas en listas de filas
        filas_ingresos = tabla_ingresos.split('\n')
        filas_egresos = tabla_egresos.split('\n')

        # Asegurar que ambas tablas tengan la misma longitud
        max_filas = max(len(filas_ingresos), len(filas_egresos))
        filas_ingresos.extend([''] * (max_filas - len(filas_ingresos)))
        filas_egresos.extend([''] * (max_filas - len(filas_egresos)))

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(filas_ingresos[0]) + len(filas_egresos[0])) + "\n")

        # Imprimir la tabla de ingresos y egresos una al lado de la otra
        for fila_ingresos, fila_egresos in zip(filas_ingresos, filas_egresos):
            print(fila_ingresos + "  " + fila_egresos)

        print()

        os.system("pause")


#######################################################################################