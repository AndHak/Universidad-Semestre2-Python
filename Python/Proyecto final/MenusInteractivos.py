from colorama import *
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

        pelicula1 = DatosPelicula("El Padrino", "Historia de la mafia en Nueva York", 180, "Drama", 18, 6000)
        pelicula2 = DatosPelicula("Titanic", "Historia de amor a bordo de un barco", 195, "Romance", 12, 5000)
        pelicula3 = DatosPelicula("El Señor De Los Anillos", "Aventuras en la Tierra Media", 201, "Fantasía", 14, 8000)
        pelicula4 = DatosPelicula("Interestelar", "Viaje interestelar para salvar la Tierra", 169, "Ciencia Ficción", 10, 9000)
        pelicula5 = DatosPelicula("Avatar", "Aventura en Pandora", 178, "Ciencia Ficción", 16, 7500)
        pelicula6 = DatosPelicula("Jurassic Park", "Parque de dinosaurios", 127, "Aventura", 12, 5500)
        pelicula7 = DatosPelicula("Inception", "Mundo de los sueños", 148, "Ciencia Ficción", 14, 8500)

        self.agregar_pelicula_al_cartelera(pelicula1)
        self.agregar_pelicula_al_cartelera(pelicula2)
        self.agregar_pelicula_al_cartelera(pelicula3)
        self.agregar_pelicula_al_cartelera(pelicula4)
        self.agregar_pelicula_al_cartelera(pelicula5)
        self.agregar_pelicula_al_cartelera(pelicula6)
        self.agregar_pelicula_al_cartelera(pelicula7)

        self.agregar_asignaciones_prueba()

        producto1 = DatosConfiteria(1, "Palomitas - Caja Grande", "Snacks", 2000, 10000, 20)
        producto2 = DatosConfiteria(2, "Palomitas - Caja Mediana", "Snacks", 1000, 5000, 20)
        producto3 = DatosConfiteria(3, "Palomitas - Personal", "Snacks", 500, 4000, 20)
        producto4 = DatosConfiteria(4, "Gaseosa - Grande", "Bebidas", 2000, 5000, 50)
        producto5 = DatosConfiteria(5, "Gaseosa - Mediana", "Bebidas", 3000, 7000, 35)
        producto6 = DatosConfiteria(6, "Perro Caliente", "Comida Rápida", 1200, 8000, 30)
        producto7 = DatosConfiteria(7, "Nachos con Queso", "Snacks", 2000, 5000, 40)
        producto8 = DatosConfiteria(8, "Caramelos", "Snacks", 200, 900, 200)

        self.inventario_confiteria[producto1.id_producto] = producto1
        self.inventario_confiteria[producto2.id_producto] = producto2
        self.inventario_confiteria[producto3.id_producto] = producto3
        self.inventario_confiteria[producto4.id_producto] = producto4
        self.inventario_confiteria[producto5.id_producto] = producto5
        self.inventario_confiteria[producto6.id_producto] = producto6
        self.inventario_confiteria[producto7.id_producto] = producto7
        self.inventario_confiteria[producto8.id_producto] = producto8


    def agregar_pelicula_al_cartelera(self, pelicula):
        self.cartelera[pelicula.titulo_pelicula] = pelicula

    def agregar_asignaciones_prueba(self):
        asignacion2 = [2321301, "2023", "12", 23, 21, 30, 1, "El Señor De Los Anillos"]
        asignacion3 = [23902, "2023", "12", 23, 9, 0, 2, "Interestelar"]
        asignacion4 = [231202, "2023", "12", 23, 12, 0, 2, "Avatar"]
        asignacion5 = [231401, "2023", "12", 23, 14, 0, 1, "Jurassic Park"]
        asignacion6 = [231602, "2023", "12", 23, 16, 0, 2, "Inception"]

        self.ocupacion_sala.extend([asignacion2, asignacion3, asignacion4, asignacion5, asignacion6])

    

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
                titulo_pelicula = titulo_pelicula.capitalize()
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

                                asignacion_id = str(dia) + str(hora) + str(minutos) + str(sala)
                                datos = [asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala]

                                esta_ocupada = self.verificar_disponibilidad_sala(asignacion_id, año, mes, dia, hora, minutos, sala, pelicula_a_asignar_sala)
                                if not esta_ocupada:
                                    self.ocupacion_sala.append(datos)
                                    Funciones.mostrar_exito(f"\nLa película {pelicula_a_asignar_sala} Se presentara en la Sala {sala}\nPara el día {dia} a las {hora:02}:{minutos:02}")
                                else:
                                    Funciones.mostrar_alerta(f"La sala {sala} no está disponible")
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
                                se_puede_eliminar_asignacion = True

                        if se_puede_eliminar_asignacion:
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
                            
                            nueva_fecha_hora = datetime(int(año), int(mes), dia_cronograma, hora_modificada, minutos_modificados)
                            intervalo_tiempo = timedelta(hours=3)

                            fecha_hora_asignada = datetime(int(año), int(mes), asignacion_a_modificar[3], asignacion_a_modificar[4], asignacion_a_modificar[5])
                            if not (nueva_fecha_hora >= fecha_hora_asignada + intervalo_tiempo or nueva_fecha_hora + intervalo_tiempo <= fecha_hora_asignada):
                                cumple_requisitos_para_modificarse = True

                            if cumple_requisitos_para_modificarse:
                                asignacion_a_modificar[4] = hora_modificada
                                asignacion_a_modificar[5] = minutos_modificados
                                asignacion_a_modificar[6] = sala_modificada
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
                
                categoria_producto = Funciones.hacer_pregunta("Categoria: ")
                if categoria_producto.lower() == "c":
                    Funciones.mostrar_alerta("La operacón se ha cancelado")
                    break

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
        pass

    def mostrar_productos(self):
        pass



#######################################################################################




#METODOS PARA EL SISTEMA DE VENTAS

#######################################################################################

#######################################################################################




#METODOS PARA EL SISTEMA DE INFORMACION Y ESTADISTICAS

#######################################################################################

#######################################################################################





                    

        
