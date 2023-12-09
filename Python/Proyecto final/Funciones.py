from colorama import Fore, Back, Style
import time
import os
from tabulate import tabulate

class Funciones:

    color_letras = Fore.LIGHTMAGENTA_EX
    estilo_reset = Style.RESET_ALL
    
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
        time.sleep(2) 

    @staticmethod
    def mostrar_exito(mensaje):
        print(Fore.LIGHTGREEN_EX + f"\nÉxito: {mensaje}" + Fore.RESET)
        time.sleep(2) 

    @staticmethod
    def mostrar_alerta(mensaje):
        print(Fore.LIGHTMAGENTA_EX + f"\nAlerta: {mensaje}" + Fore.RESET)
        time.sleep(2)


    @staticmethod
    def hacer_pregunta(pregunta):
        return input(Fore.LIGHTYELLOW_EX + f"\n{pregunta}" + Fore.RESET + "")
    
    def mostrar_productos(inventario_confiteria):

        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}C O N F I T E R I A{estilo_reset}"
        
        inventario_data = []
        for id_producto, datos_producto in inventario_confiteria.items():
            datos_producto = datos_producto.obtener_datos_producto()
            inventario_data.append([id_producto, datos_producto[1], datos_producto[2],
                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                    datos_producto[5]])

        headers = [f"{color_headers}ID", "Producto", "Categoria", "Compra", "Venta", f"Cantidad{estilo_reset}"]

        # Obtener la tabla del inventario utilizando tabulate sin imprimir
        tabla_inventario = tabulate(inventario_data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_inventario.split('\n')[0])) + "\n")

        # Imprimir la tabla del inventario utilizando tabulate
        print(tabla_inventario)
        print()

    def mostrar_peliculas(cartelera):

        # Definir colores y estilos
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}C A R T E L E R A{estilo_reset}"
        cartelera_data = []
        for titulo_pelicula, datos_pelicula in cartelera.items():
            datos_pelicula = datos_pelicula.obtener_datos_pelicula()
            cartelera_data.append([titulo_pelicula, datos_pelicula[1], datos_pelicula[3],
                                f"{datos_pelicula[2]} min", f"{datos_pelicula[4]}+",
                                f"${datos_pelicula[5]:.2f}"])

        headers = [f"{color_headers}Título", "Sinopsis", "Género", "Duración", "Edad mínima", f"Costo{estilo_reset}"]

        # Obtener la tabla de cartelera utilizando tabulate sin imprimir
        tabla_cartelera = tabulate(cartelera_data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_cartelera.split('\n')[0])) + "\n")
        
        # Imprimir la tabla de cartelera utilizando tabulate
        print(tabla_cartelera)
        print()

    def mostrar_ocupacion_sala(ocupacion_sala, cronograma_dia, dia_cronograma):

        # Definir colores y estilos
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        cronograma_ordenado = sorted(cronograma_dia, key=lambda x: (int(x[6]) if x[6] != "XX" else float('inf'), x[4], x[5])) if not all(x[6:8] == ("XX", "XX") for x in cronograma_dia) else cronograma_dia

        # Obtener la tabla del cronograma utilizando tabulate sin imprimir
        cronograma_data = []
        for datos in cronograma_ordenado:
            pelicula_asignada = datos[7]
            hora_inicio = f"{datos[4]:02}:{datos[5]:02}"
            sala_asignada = datos[6]
            cronograma_data.append([pelicula_asignada, hora_inicio, f"Sala {sala_asignada}"])


        # Modificar los headers con los colores y estilos deseados
        headers_cronograma = [f"{color_headers}Película", "Hora de inicio", f"Sala asignada{estilo_reset}"]

        # Imprimir el título centrado sobre la tabla
        print("\n" + f"{color_titulo}Cronograma del día: {dia_cronograma}{estilo_reset}".center(len(tabulate(cronograma_data, headers=headers_cronograma, tablefmt="fancy_grid").split('\n')[0])) + "\n")

        # Imprimir la tabla del cronograma utilizando tabulate
        print(tabulate(cronograma_data, headers=headers_cronograma, tablefmt="fancy_grid"))
        

    def generar_sala():
        sala = []
        columnas = "ABCDEFGHIJK"
        for i in range(len(columnas)-1, -1, -1):
            fila_actual = []
            for j in range(10):
                numero_asiento = columnas[i] + str(j+1)
                fila_actual.append(numero_asiento)
            sala.append(fila_actual)
        return sala
    
    def imprimir_sala_centro(sala):
        print("\n") 
        print(f"OCUPADO: {Fore.LIGHTRED_EX}XX{Style.RESET_ALL}")
        print(f"DISPONIBLE: {Fore.LIGHTGREEN_EX}LN°{Style.RESET_ALL}")
        print("\n")
        for i, fila in enumerate(sala, start=1):
            print("        ", " ", end="")
            for j, asiento in enumerate(fila, start=1):
                if asiento == "XX":
                    print(f"{Fore.LIGHTRED_EX}{asiento}{Style.RESET_ALL}", end="  ")
                else:
                    print(f"{Fore.LIGHTGREEN_EX}{asiento}{Style.RESET_ALL}", end="  ")
            print("\n")
        print("\n            " + Fore.BLACK + Back.WHITE + "_____________PANTALLA_____________" + Style.RESET_ALL)










