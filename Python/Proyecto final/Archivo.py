from Funciones import *
import os

class Archivo:
    def __init__(self):
        self.archivo_peliculas = []
        self.archivo_productos = []
        self.archivo_combos = []
        self.archivo_ocupacion_sala = []
        self.archivo_facturas_confiteria = []
        self.archivo_factura_peliculas = []
        self.modificaciones_caja = []

    def mostrar_archivo_peliculas(self):
        if not self.archivo_peliculas:
            Funciones.mostrar_alerta("No hay datos en el archivo de películas.")
        else:
            color_titulo = Fore.LIGHTCYAN_EX
            color_headers = Fore.LIGHTYELLOW_EX
            estilo_reset = Style.RESET_ALL

            titulo = f"{color_titulo}A R C H I V O   D E   P E L Í C U L A S{estilo_reset}"

            headers = [f"{color_headers}Título", "Sinopsis", "Duración", "Género", "Edad Mínima", "Costo", f"Caso{estilo_reset}"]
            data = [[fila[0], fila[1], fila[2], fila[3], f"{fila[4]}+", f"$ {fila[5]:.2f}", fila[6]] for fila in self.archivo_peliculas]

            # Obtener la tabla del archivo de películas utilizando tabulate sin imprimir
            tabla_archivo_peliculas = tabulate(data, headers=headers, tablefmt="fancy_grid")

            # Imprimir el título centrado sobre la tabla
            print("\n" + titulo.center(len(tabla_archivo_peliculas.split('\n')[0])) + "\n")

            # Imprimir la tabla del archivo de películas utilizando tabulate
            print(tabla_archivo_peliculas)
            print()
            os.system("pause")


    def mostrar_archivo_productos(self):
        if not self.archivo_productos:
            Funciones.mostrar_alerta("No hay datos en el archivo de productos.")
        else:
            color_titulo = Fore.LIGHTCYAN_EX
            color_headers = Fore.LIGHTYELLOW_EX
            estilo_reset = Style.RESET_ALL

            titulo = f"{color_titulo}A R C H I V O   D E   P R O D U C T O S{estilo_reset}"

            headers = [f"{color_headers}ID Producto", "Nombre", "Categoría", "Precio Compra", "Precio Venta", "Cantidad", f"Caso{estilo_reset}"]
            data = [[fila[0], fila[1], fila[2], f"$ {fila[3]:.2f}", f"$ {fila[4]:.2f}", fila[5], fila[6]] for fila in self.archivo_productos]
            
            # Obtener la tabla del archivo de productos utilizando tabulate sin imprimir
            tabla_archivo_productos = tabulate(data, headers=headers, tablefmt="fancy_grid")

            # Imprimir el título centrado sobre la tabla
            print("\n" + titulo.center(len(tabla_archivo_productos.split('\n')[0])) + "\n")

            # Imprimir la tabla del archivo de productos utilizando tabulate
            print(tabla_archivo_productos)
            print()
            os.system("pause")


    #def mostrar_archivo_combos():
        #pass


    def mostrar_archivo_ocupacion_sala(self):
        if not self.archivo_ocupacion_sala:
            Funciones.mostrar_alerta("No hay datos en el archivo de ocupación de sala.")
        else:
            color_titulo = Fore.LIGHTCYAN_EX
            color_headers = Fore.LIGHTYELLOW_EX
            estilo_reset = Style.RESET_ALL

            titulo = f"{color_titulo}A R C H I V O   D E   O C U P A C I Ó N   D E   S A L A{estilo_reset}"

            headers = [f"{color_headers}ID Asignación", "Año", "Mes", "Día", "Hora", "Minutos", "Sala", "Película", f"Caso{estilo_reset}"]
            data = [[fila[0], fila[1], fila[2], fila[3], f"{fila[4]:02}", f"{fila[5]:02}", fila[6], fila[7], fila[8]] for fila in self.archivo_ocupacion_sala]

            # Obtener la tabla del archivo de ocupación de sala utilizando tabulate sin imprimir
            tabla_archivo_ocupacion_sala = tabulate(data, headers=headers, tablefmt="fancy_grid")

            # Imprimir el título centrado sobre la tabla
            print("\n" + titulo.center(len(tabla_archivo_ocupacion_sala.split('\n')[0])) + "\n")

            # Imprimir la tabla del archivo de ocupación de sala utilizando tabulate
            print(tabla_archivo_ocupacion_sala)
            print()
            os.system("pause")

    def mostrar_archivo_facturas_peliculas(self):
        pass

    