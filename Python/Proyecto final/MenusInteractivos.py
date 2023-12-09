from colorama import init
from datetime import datetime, timedelta
from Funciones import *
from Datos import *
from tabulate import *
import os

init(autoreset=True)

class Menus:

    def __init__(self):
        self.cartelera = {}
        self.ventas_peliculas = {}
        self.ventas_confiteria = {}
        self.clientes = {}
        self.ocupacion_sala = []
        self.inventario_confiteria = {}
        self.salas = {}
        self.cargar_datos()
    
    def salir(self):
        self.guardar_datos()

    def guardar_datos(self):
        ruta_cartelera = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\cartelera.txt"
        with open(ruta_cartelera, "w", encoding="utf-8") as file:
            for titulo, pelicula in self.cartelera.items():
                file.write(f"{titulo},{pelicula.sinopsis},{pelicula.duracion},{pelicula.genero},{pelicula.edad_minima},{pelicula.costo_pelicula}\n")

        ruta_confiteria = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\confiteria.txt"
        with open(ruta_confiteria, "w", encoding="utf-8") as file:
            for id_producto, datos_producto in self.inventario_confiteria.items():
                file.write(f"{id_producto},{datos_producto.nombre_producto},{datos_producto.categoria_producto},{datos_producto.precio_compra_producto},{datos_producto.precio_venta_producto},{datos_producto.cantidad_producto}\n")

        ruta_ocupacion_sala = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\ocupacion_sala.txt"
        with open(ruta_ocupacion_sala, "w", encoding="utf-8") as file:
            for datos_asignacion in self.ocupacion_sala:
                datos_asignacion[3] = str(datos_asignacion[3])
                datos_asignacion[4] = str(datos_asignacion[4])
                datos_asignacion[5] = str(datos_asignacion[5])
                file.write(','.join(map(str, datos_asignacion)) + '\n')

    def cargar_datos(self):
        try:
            ruta_cartelera = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\cartelera.txt"
            with open(ruta_cartelera, "r", encoding="utf-8") as file:
                for line in file:
                    datos_pelicula = line.strip().split(',')
                    titulo_pelicula = datos_pelicula[0]
                    sinopsis = datos_pelicula[1]
                    duracion = int(datos_pelicula[2])
                    genero = datos_pelicula[3]
                    edad_minima = int(datos_pelicula[4])
                    costo_pelicula = float(datos_pelicula[5])

                    pelicula = DatosPelicula(titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula)
                    self.cartelera[titulo_pelicula] = pelicula

        except FileNotFoundError:
            print("El archivo 'cartelera.txt' no fue encontrado. Se creará por primera vez al agregar una película.")
        except Exception as e:
            print(f"Error al leer 'cartelera.txt': {e}")

        try:
            ruta_confiteria = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\confiteria.txt"
            with open(ruta_confiteria, "r", encoding="utf-8") as file:
                for line in file:
                    datos_producto = line.strip().split(',')
                    id_producto = datos_producto[0]
                    nombre_producto = datos_producto[1]
                    categoria_producto = datos_producto[2]
                    precio_compra_producto = float(datos_producto[3])
                    precio_venta_producto = float(datos_producto[4])
                    cantidad_producto = int(datos_producto[5])

                    producto = DatosConfiteria(id_producto, nombre_producto, categoria_producto, precio_compra_producto, precio_venta_producto, cantidad_producto)
                    self.inventario_confiteria[id_producto] = producto
        except FileNotFoundError:
            print("El archivo 'confiteria.txt' no fue encontrado. Se creará por primera vez al agregar productos.")
        except Exception as e:
            print(f"Error al leer 'confiteria.txt': {e}")

        try:
            ruta_ocupacion_sala = r"C:\Programacion Universidad\Semestre 2\Python\Proyecto final\datos_cine\ocupacion_sala.txt"
            with open(ruta_ocupacion_sala, "r", encoding="utf-8") as file:
                for line in file:
                    datos_asignacion = line.strip().split(',')
                    asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_asignada = datos_asignacion

                    if sala.upper() == "XX":
                        mes, año, dia = map(int, [mes, año, dia])
                        self.ocupacion_sala.append([asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_asignada])
                    else:
                        dia, mes, año, hora, minutos, sala = map(int, [dia, mes, año, hora, minutos, sala])
                        self.ocupacion_sala.append([asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_asignada])

        except FileNotFoundError:
            print("El archivo 'ocupacion_sala.txt' no fue encontrado. Se creará por primera vez al asignar salas.")
        except Exception as e:
            print(f"Error al leer 'ocupacion_sala.txt': {e}")


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

                #La agregamos al diccionario con la clave id_pelicula
                self.cartelera[titulo_pelicula] = pelicula_a_agregar
                Funciones.mostrar_exito("La película ha sido agregada a la cartelera")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")

#--------------------------------------------------------------------------------------

    def eliminar_peliculas(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Eliminar pelicula")
            #Opcion siempre disponibe
            print("Opción siempre disponible: 'c' para cancelar")
            año = datetime.now().strftime("%Y")
            mes = datetime.now().strftime("%m")
            print(f"\n\nAño: {año}   mes: {mes}\n\n")

            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")
            else:
                Funciones.mostrar_peliculas(self.cartelera)

            try:

                #Código de pelicula
                titulo_pelicula = Funciones.hacer_pregunta("Ingrese el Titulo de la pelicula: ")
                if titulo_pelicula.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                titulo_pelicula = titulo_pelicula.title()
                #Buscar código de pelicula en cartelera
                if titulo_pelicula in self.cartelera:
                    #Eliminar pelicula de la cartelera
                    del self.cartelera[titulo_pelicula]
                    
                    for datos in self.ocupacion_sala:
                        if datos[7] == titulo_pelicula:
                            datos[7] = f"{titulo_pelicula} CANCELADA"
                            datos[4] = "XX"
                            datos[5] = "XX"
                            datos[6] = "XX"
                    Funciones.mostrar_exito(f"La pelicula ha sido eliminada")
                else:
                    Funciones.mostrar_error("La pelicula no existe en cartelera")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")

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

                pelicula_a_asignar_sala = Funciones.hacer_pregunta("¿A qué película se le va a asignar sala?\n\nTítulo de la película:  ")
                if pelicula_a_asignar_sala.lower() == "c":
                    Funciones.mostrar_alerta("La operación se ha cancelado")
                    break
                pelicula_a_asignar_sala = pelicula_a_asignar_sala.title()

                if pelicula_a_asignar_sala not in self.cartelera:
                    Funciones.mostrar_error("La película no existe en cartelera")
                else:

                    dia = Funciones.hacer_pregunta("Ingrese el día: ")
                    if dia.lower() == "c":
                        Funciones.mostrar_alerta("La operación se ha cancelado")
                        break
                    dia = int(dia)

                    if 0 < dia < 31:

                        cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia]

                        if not cronograma_dia:
                            Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia}")
                        else:
                            Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia)

                        hora = Funciones.hacer_pregunta("Ingrese la hora en formato 24h: ")
                        if hora.lower() == "c":
                            Funciones.mostrar_alerta("La operación se ha cancelado")
                            break
                        hora = int(hora)

                        if 8 <= hora < 21:
                            minutos = Funciones.hacer_pregunta("Ingrese los minutos: ")
                            if minutos.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            minutos = int(minutos)

                            if 0 <= minutos < 60:
                                sala = Funciones.hacer_pregunta("Ingrese el número de sala: ")
                                if sala.lower() == "c":
                                    Funciones.mostrar_alerta("La operación se ha cancelado")
                                    break
                                sala = int(sala)

                                if 0 < sala < 4:

                                    asignacion_id = str(dia) + str(hora) + str(minutos) + str(sala)
                                    datos = [asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala]

                                    esta_ocupada = self.verificar_disponibilidad_sala(asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala)
                                    if not esta_ocupada:
                                        self.ocupacion_sala.append(datos)
                                        Funciones.mostrar_exito(f"\nLa película {pelicula_a_asignar_sala} Se presentara en la Sala {sala}\nPara el día {dia} a las {hora:02}:{minutos:02}")
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
                Funciones.mostrar_error("Ingrese una opción válida")

    def verificar_disponibilidad_sala(self, asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala):
        intervalo_tiempo = timedelta(hours=3)
        hora_nueva_datetime = datetime(int(año), int(mes), int(dia), int(hora), int(minutos))

        for datos in self.ocupacion_sala:
            asignacion_id_existente, año_existente, mes_existente, dia_existente, hora_existente, minutos_existente, sala_existente, pelicula_a_asignar_sala = datos

            if asignacion_id_existente != asignacion_id and sala_existente == sala:
                hora_asignada_datetime = datetime(int(año_existente), int(mes_existente), int(dia_existente), int(hora_existente), int(minutos_existente))
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
                    self.eliminar_salas_canceladas()
                    Funciones.mostrar_exito("Se eliminaron las funciones canceladas")
                    break
                dia_cronograma = int(dia_cronograma)

                if 0 < dia_cronograma < 31:
                    cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_cronograma]

                    if not cronograma_dia:
                        Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia_cronograma}")
                    else:
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
                        
                        se_puede_eliminar_asignacion = False
                        for datos in self.ocupacion_sala:
                            if datos[3] == dia_cronograma and datos[4] == hora_asignacion_a_eliminar and datos[5] == minutos_asignacion_a_eliminar and datos[6] == sala_asignacion_a_eliminar:
                                asignacion_a_eliminar = datos
                                id_asignacion_a_eliminar = datos[0]
                                se_puede_eliminar_asignacion = True

                        if se_puede_eliminar_asignacion:
                            
                            eliminar_de_salas = False
                            if self.salas:
                                for id_sala, sala in self.salas.items():
                                    if id_sala == id_asignacion_a_eliminar:
                                        eliminar_de_salas = True
                            
                            if eliminar_de_salas:
                                del self.salas[id_asignacion_a_eliminar]

                            self.ocupacion_sala.remove(asignacion_a_eliminar)
                            Funciones.mostrar_exito("La Asignacion de sala ha sido eliminada")
                        else:
                            Funciones.mostrar_alerta("No existe una asignacion de sala con los datos especificados")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")
    
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
                    cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_cronograma]

                    if not cronograma_dia:
                        Funciones.mostrar_alerta(f"No hay funciones programadas para el día {dia_cronograma}")
                    else:
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

                        se_puede_modificar_asignacion = False
                        for datos in self.ocupacion_sala:
                            if datos[3] == dia_cronograma and datos[4] == hora_asignacion_a_modificar and datos[5] == minutos_asignacion_a_modificar and datos[6] == sala_asignacion_a_modificar:
                                asignacion_a_modificar = datos
                                id_asignacion_vieja = datos[0]
                                se_puede_modificar_asignacion = True
                            
                        if se_puede_modificar_asignacion:
                            Funciones.mostrar_exito("Sala encontrada")
                            
                            cumple_requisitos_para_modificarse = False

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

                            sala_modificada = Funciones.hacer_pregunta("Nueva sala: ")
                            if sala_modificada.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            sala_modificada = int(sala_modificada)

                            if 0 < sala_modificada <= 4:

                                id_asignacion_nueva = str(dia_cronograma) + str(hora_modificada) + str(minutos_modificados) + str(sala_modificada)
                            
                                nueva_fecha_hora = datetime(int(año), int(mes), dia_cronograma, hora_modificada, minutos_modificados)
                                intervalo_tiempo = timedelta(hours=3)

                                fecha_hora_asignada = datetime(int(año), int(mes), asignacion_a_modificar[3], asignacion_a_modificar[4], asignacion_a_modificar[5])
                                if not (nueva_fecha_hora >= fecha_hora_asignada + intervalo_tiempo or nueva_fecha_hora + intervalo_tiempo <= fecha_hora_asignada):
                                    cumple_requisitos_para_modificarse = True

                                if cumple_requisitos_para_modificarse:
                                    asignacion_a_modificar[4] = hora_modificada
                                    asignacion_a_modificar[5] = minutos_modificados
                                    asignacion_a_modificar[6] = sala_modificada
                                    asignacion_a_modificar[0] = id_asignacion_nueva

                                    if self.salas and id_asignacion_vieja in self.salas:
                                        self.salas[id_asignacion_nueva] = self.salas.pop(id_asignacion_vieja, None)

                                    Funciones.mostrar_exito("La modificación ha sido exitosa")
                                else:
                                    Funciones.mostrar_error(f"La sala {sala_modificada} no está disponible en el horario especificado")

                        else:
                            Funciones.mostrar_alerta("No existe una asignación de sala con los datos especificados")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")
     
#--------------------------------------------------------------------------------------

    def mostrar_cartelera_y_cronograma(self):
        os.system("cls")
        Funciones.encabezado()
        Funciones.subtitulo("Cartelera y cronograma")
        print("Opción siempre disponible: 's' para salir")
        año = datetime.now().strftime("%Y")
        mes = datetime.now().strftime("%m")
        print(f"\n\nAño: {año}   mes: {mes}\n\n")

        if not self.cartelera:
            Funciones.mostrar_alerta("No hay películas disponibles")
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
                        else:
                            Funciones.mostrar_alerta("La cantida no es valida")

                    else:
                        Funciones.mostrar_alerta("El precio digitado no es valido")

                else:
                    Funciones.mostrar_alerta("El precio digitado no es valido")
                    
            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")

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
                    try:
                        eliminar_pregunta = Funciones.hacer_pregunta("Esta seguro que desea eliminar si/no: ")
                        if eliminar_pregunta.lower() == "c":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                            break
                        if eliminar_pregunta.lower() == "no":
                            Funciones.mostrar_alerta("No se ha eliminado el producto")
                        if eliminar_pregunta.lower() == "si":
                            del self.inventario_confiteria[id_producto_buscar]
                            Funciones.mostrar_exito("Se ha eliminado el producto")
                            
                    except ValueError:
                        Funciones.mostrar_error("Ingrese una opción válida")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")

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
                    try:
                        modificar_pregunta = Funciones.hacer_pregunta("Esta seguro que desea modificar si/no: ")
                        if modificar_pregunta.lower() == "c":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                            break  
                        if modificar_pregunta.lower() == "no":
                            Funciones.mostrar_alerta("La operacón se ha cancelado")
                        if modificar_pregunta.lower() == "si":
                            try:
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
                                        else:
                                            Funciones.mostrar_alerta("La cantidad no es válida")

                                    else:
                                        Funciones.mostrar_alerta("El precio digitado no es válido")

                                else:
                                    Funciones.mostrar_alerta("El precio digitado no es válido")

                            except ValueError:
                                Funciones.mostrar_error("Ingrese una opción válida")
                                    
                    except ValueError:
                        Funciones.mostrar_error("Ingrese una opción válida")

            except ValueError:
                Funciones.mostrar_error("Ingrese una opción válida")

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
                Funciones.mostrar_error("Ingrese una opción válida")



#######################################################################################




#METODOS PARA EL SISTEMA DE VENTAS

#######################################################################################

    def realizar_venta(self):
        while True:
            os.system("cls")
            Funciones.encabezado()
            Funciones.subtitulo("Venta")
            # Opción siempre disponible
            print("Opción siempre disponible: 'c' para cancelar")

            if not self.cartelera:
                Funciones.mostrar_alerta("No hay películas disponibles")
            else:
                Funciones.mostrar_peliculas(self.cartelera)
                pelicula_a_comprar = Funciones.hacer_pregunta("Película: ")

                if pelicula_a_comprar.lower() == "c":
                    Funciones.mostrar_alerta("La venta se ha cancelado")
                    break
                pelicula_a_comprar = pelicula_a_comprar.title()

                if pelicula_a_comprar in self.cartelera:

                    dias = []
                    for datos in self.ocupacion_sala:
                        if datos[7] == pelicula_a_comprar:
                            dias.append(int(datos[3]))
                    
                    if not dias:
                        Funciones.mostrar_alerta(f"No hay salas asignadas para {pelicula_a_comprar}")
                    else:
                        print(f"\nHay funciones disponibles para los días {dias}")
                        
                        dia_de_compra = Funciones.hacer_pregunta("Seleccione un día: ")
                        if dia_de_compra.lower() == "c":
                            Funciones.mostrar_alerta("La venta se ha cancelado")
                            break
                        dia_de_compra = int(dia_de_compra)

                        if dia_de_compra in dias:
                            cronograma_dia = [datos for datos in self.ocupacion_sala if datos[3] == dia_de_compra and datos[7] == pelicula_a_comprar]
                            Funciones.mostrar_ocupacion_sala(self.ocupacion_sala, cronograma_dia, dia_de_compra)

                            hora_de_compra = Funciones.hacer_pregunta("hora: ")
                            if hora_de_compra.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            hora_de_compra = int(hora_de_compra)

                            minutos_de_compra = Funciones.hacer_pregunta("minutos: ")
                            if minutos_de_compra.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            minutos_de_compra = int(minutos_de_compra)

                            sala_de_compra = Funciones.hacer_pregunta("sala: ")
                            if sala_de_compra.lower() == "c":
                                Funciones.mostrar_alerta("La operación se ha cancelado")
                                break
                            sala_de_compra = int(sala_de_compra)

                            id_identificacion_sala = str(dia_de_compra) + str(hora_de_compra) + str(minutos_de_compra) + str(sala_de_compra)
                            primera_compra_de_sala = False

                            if id_identificacion_sala in self.salas:
                                print(f"\nAsignacion: {id_identificacion_sala}")
                                print(f"\nPelicula: {pelicula_a_comprar}")
                                print(f"dia: {dia_de_compra} - hora: {hora_de_compra:02}:{minutos_de_compra:02}")
                                for id_sala, sala_a_modificar in self.salas.items():
                                    if id_sala == id_identificacion_sala:
                                        sala = sala_a_modificar
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

                                        if asiento_a_comprar != "XX":

                                            for i in range(len(sala)):
                                                for j in range(len(sala[i])):
                                                    if sala[i][j] == asiento_a_comprar:
                                                        if sala[i][j] not in validos:
                                                            validos.append(sala[i][j])
                                                            sala[i][j] = "XX"
                                                            asientos_validos += 1
                                                            break         
                                                        else:
                                                            Funciones.mostrar_error("Este asiento ya ha sido seleccionado")
                                                            break
                                                else:
                                                    continue
                                                break     
                                            else:
                                                Funciones.mostrar_error("Este asiento no es válido")
                                        else:
                                            Funciones.mostrar_error("Este asiento ya ha sido vendido")

                                                    
                                    if cancelacion_compra:
                                        break

                                    if asientos_validos == cuantos_boletos_compra:
                                        self.salas[id_identificacion_sala] = sala
                                        Funciones.mostrar_exito("La compra se ha realizado correctamente")
                         
                            else:
                                for datos in self.ocupacion_sala:
                                    if id_identificacion_sala == datos[0] and dia_de_compra == datos[3] and hora_de_compra == datos[4] and minutos_de_compra == datos[5] \
                                        and sala_de_compra == datos[6] and pelicula_a_comprar == datos[7]:
                                        primera_compra_de_sala = True

                                if primera_compra_de_sala:
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
                                                            sala[i][j] = "XX"
                                                            asientos_validos += 1
                                                            break         
                                                        else:
                                                            Funciones.mostrar_error("Este asiento ya ha sido seleccionado")
                                                            break
                                                else:
                                                    continue
                                                break     
                                            else:
                                                Funciones.mostrar_error("Este asiento no es válido")          
                                                        
                                        if cancelacion_compra:
                                            break

                                        if asientos_validos == cuantos_boletos_compra:
                                            self.salas[id_identificacion_sala] = sala
                                            Funciones.mostrar_exito("La compra se ha realizado correctamente")
            
                                else:
                                    Funciones.mostrar_alerta("horario incorrecto y/o sala incorrectaa")

                        else:
                            Funciones.mostrar_alerta(f"No hay funciones para el dia {dia_de_compra}")
                        
    def administracion_de_salas(self):
        for id_sala, sala in self.salas.items():
            print(f"\nID de Sala: {id_sala}")

            for datos in self.ocupacion_sala:
                if datos[0] == id_sala:
                    pelicula = datos[7]
                    dia = datos[3]
                    hora = datos[4]
                    minutos = datos[5]

                    print(f"Película: {pelicula}")
                    print(f"Día: {dia} - Hora: {hora:02}:{minutos:02}")

            Funciones.imprimir_sala_centro(sala)

        input()







#######################################################################################




#METODOS PARA EL SISTEMA DE INFORMACION Y ESTADISTICAS

#######################################################################################



#######################################################################################





                    

        
