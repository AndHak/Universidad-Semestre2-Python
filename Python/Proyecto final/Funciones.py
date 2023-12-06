from colorama import init, Fore
import os
import time
from datetime import datetime
from tabulate import tabulate

class Funciones:
    
    @staticmethod
    def subtitulo(titulo):

        separador = "=" * 50
        
        print(f"\n {titulo.upper()} ")
        print(separador)

    @staticmethod
    def encabezado():
        print(Fore.LIGHTRED_EX + """
 ▄████████  ▄█  ███▄▄▄▄      ▄████████      ███    █▄  ████████▄     ▄████████ ███▄▄▄▄      ▄████████    ▄████████ 
███    ███ ███  ███▀▀▀██▄   ███    ███      ███    ███ ███   ▀███   ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ 
███    █▀  ███▌ ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀  ███   ███   ███    ███   ███    ███ 
███        ███▌ ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄     ███   ███   ███    ███  ▄███▄▄▄▄██▀ 
███        ███▌ ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ███   ███ ▀███████████ ▀▀███▀▀▀▀▀   
███    █▄  ███  ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ███   ███   ███    ███ ▀███████████ 
███    ███ ███  ███   ███   ███    ███      ███    ███ ███   ▄███   ███    ███ ███   ███   ███    ███   ███    ███ 
████████▀  █▀    ▀█   █▀    ██████████      ████████▀  ████████▀    ██████████  ▀█   █▀    ███    █▀    ███    ███ 
                                                                                                        ███    ███ 
""" + Fore.RESET)
        
    @staticmethod
    def mostrar_error(mensaje):
        print(Fore.LIGHTRED_EX + f"\nError: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def mostrar_exito(mensaje):
        print(Fore.LIGHTGREEN_EX + f"\nÉxito: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def mostrar_alerta(mensaje):
        print(Fore.LIGHTMAGENTA_EX + f"\nAlerta: {mensaje}" + Fore.RESET)
        os.system("sleep 1")

    @staticmethod
    def hacer_pregunta(pregunta):
        return input(Fore.LIGHTYELLOW_EX + f"\n{pregunta}" + Fore.RESET + "")
    
    def mostrar_productos(inventario_confiteria):
        titulo = "C O N F I T E R I A"
        
        inventario_data = []
        for id_producto, datos_producto in inventario_confiteria.items():
            datos_producto = datos_producto.obtener_datos_producto()
            inventario_data.append([id_producto, datos_producto[1], datos_producto[2],
                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                    datos_producto[5]])

        headers = ["ID", "Producto", "Categoria", "Compra", "Venta", "Cantidad"]

        # Obtener la tabla del inventario utilizando tabulate sin imprimir
        tabla_inventario = tabulate(inventario_data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_inventario.split('\n')[0])) + "\n")

        # Imprimir la tabla del inventario utilizando tabulate
        print(tabla_inventario)
        print()

    def mostrar_peliculas(cartelera):
        titulo = "C A R T E L E R A"
        cartelera_data = []
        for titulo_pelicula, datos_pelicula in cartelera.items():
            datos_pelicula = datos_pelicula.obtener_datos_pelicula()
            cartelera_data.append([titulo_pelicula, datos_pelicula[1], datos_pelicula[3],
                                f"{datos_pelicula[2]} min", f"{datos_pelicula[4]}+",
                                f"${datos_pelicula[5]:.2f}"])

        headers = ["Título", "Sinopsis", "Género", "Duración", "Edad mínima", "Costo"]

        # Obtener la tabla de cartelera utilizando tabulate sin imprimir
        tabla_cartelera = tabulate(cartelera_data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_cartelera.split('\n')[0])) + "\n")
        
        # Imprimir la tabla de cartelera utilizando tabulate
        print(tabla_cartelera)
        print()
    
    def mostrar_ocupacion_sala(ocupacion_sala, cronograma_dia, dia_cronograma):
        cronograma_ordenado = sorted(cronograma_dia, key=lambda x: (int(x[6]) if x[6] != "XX" else float('inf'), x[4], x[5])) if not all(x[6:8] == ("XX", "XX") for x in cronograma_dia) else cronograma_dia

        # Obtener la tabla del cronograma utilizando tabulate sin imprimir
        cronograma_data = []
        for datos in cronograma_ordenado:
            pelicula_asignada = datos[7]
            hora_inicio = f"{datos[4]:02}:{datos[5]:02}"
            sala_asignada = datos[6]
            cronograma_data.append([pelicula_asignada, hora_inicio, f"Sala {sala_asignada}"])

        headers_cronograma = ["Película", "Hora de inicio", "Sala asignada"]

        # Imprimir el título centrado sobre la tabla
        print("\n" + f"Cronograma del día {dia_cronograma}".center(len(tabulate(cronograma_data, headers=headers_cronograma, tablefmt="fancy_grid").split('\n')[0])) + "\n")

        # Imprimir la tabla del cronograma utilizando tabulate
        print(tabulate(cronograma_data, headers=headers_cronograma, tablefmt="fancy_grid"))





