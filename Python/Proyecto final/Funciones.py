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
        print(Fore.LIGHTRED_EX + f"\n{mensaje}" + Fore.RESET)
        time.sleep(1) 

    @staticmethod
    def mostrar_exito(mensaje):
        print(Fore.LIGHTGREEN_EX + f"\n{mensaje}" + Fore.RESET)
        time.sleep(1) 

    @staticmethod
    def mostrar_alerta(mensaje):
        print(Fore.LIGHTMAGENTA_EX + f"\n{mensaje}" + Fore.RESET)
        time.sleep(1)


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
        columnas = "ABCDFGHIJK"
        for i in range(len(columnas)-1, -1, -1):
            fila_actual = []
            for j in range(10):
                numero_asiento = columnas[i] + str(j+1)
                fila_actual.append(numero_asiento)
            sala.append(fila_actual)
        return sala
    
    def imprimir_sala_centro(sala):
        print(f"OCUPADO: {Fore.LIGHTRED_EX}XX{Style.RESET_ALL}")
        print(f"DISPONIBLE: {Fore.LIGHTGREEN_EX}VERDE{Style.RESET_ALL}")
        print(f"SELECCIONADO: {Fore.LIGHTYELLOW_EX}SELECCIONADO{Style.RESET_ALL}")
        print("\n")
        for i in range(len(sala)):
            print("        ", " ", end="")
            for j in range(len(sala[i])):
                if sala[i][j] == "XX":
                    print(f"{Fore.LIGHTRED_EX}{sala[i][j]}{Style.RESET_ALL}", end="  ")
                elif sala[i][j].startswith("|") and sala[i][j].endswith("|"):
                    print(f"{Fore.LIGHTYELLOW_EX}{sala[i][j]}{Style.RESET_ALL}", end="  ")
                else:
                    print(f"{Fore.LIGHTGREEN_EX}{sala[i][j]}{Style.RESET_ALL}", end="  ")
            print("\n")
        print("\n            " + Fore.BLACK + Back.WHITE + "_____________PANTALLA_____________" + Style.RESET_ALL)

    def comprobar_sala_llena(sala):
        for i, fila in enumerate(sala, start=1):
            for j, asiento in enumerate(fila, start=1):
                if asiento != "XX":
                    return False
        return True
    
    def restablecer_asientos_seleccionados(sala):
        for i in range(len(sala)):
            for j in range(len(sala[i])):
                if sala[i][j].startswith("|") and sala[i][j].endswith("|"):
                    sala[i][j] = sala[i][j][1:-1]

    def confirmar_asientos_seleccionados(sala):
        for i in range(len(sala)):
            for j in range(len(sala[i])):
                if sala[i][j].startswith("|") and sala[i][j].endswith("|"):
                    sala[i][j] = "XX"


    def mostrar_egresos(egresos):
        # Definir colores y estilos
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}E G R E S O S{estilo_reset}"
        egresos_data = []

        for i, (fecha, datos_egreso) in enumerate(egresos.items(), start=1):
            egresos_data.append([i, fecha, datos_egreso.numero_factura, datos_egreso.valor_egreso, datos_egreso.descripcion_egreso, datos_egreso.el_dinero_sale_de])

        headers = [f"{color_headers}Índice", "Fecha", "Número de Factura", "Valor", "Descripción", f"De dónde se paga{estilo_reset}"]
        data = [[fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]] for fila in egresos_data]

        # Obtener la tabla de egresos utilizando tabulate sin imprimir
        tabla_egresos = tabulate(data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_egresos.split('\n')[0])) + "\n")

        # Imprimir la tabla de egresos utilizando tabulate
        print(tabla_egresos)
        print()


    def mostrar_facturas_peliculas(facturas_peliculas):
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}F A C T U R A S     P E L I C U L A S{estilo_reset}"
        facturas_data = []

        for numero_factura, datos_factura in facturas_peliculas.items():
            fecha_venta, cliente, pelicula, asientos, id_sala, dia_compra, hora_compra, minutos_compra, sala_de_compra = datos_factura
            identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()
            titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula = pelicula.obtener_datos_pelicula()
            total_venta = costo_pelicula * len(asientos)
            facturas_data.append([numero_factura, fecha_venta, nombre_cliente, titulo_pelicula, asientos, dia_compra, hora_compra, minutos_compra, sala_de_compra, total_venta])

            headers = [f"{color_headers}Numero Factura", "Fecha de venta", "Cliente", "Pelicula", "Asientos", "Dia", "Hora", "Sala", f"Total Venta{estilo_reset}"]
            data = [[f"{a[0]:04}", a[1], a[2], a[3], " ".join(a[4]), a[5], f"{a[6]:02}:{a[7]:02}", a[8], f"{a[9]:.2f}"] for a in facturas_data]

        tabla_facturas = tabulate(data, headers=headers, tablefmt="fancy_grid")

        print("\n" + titulo.center(len(tabla_facturas.split('\n')[0])) + "\n")
        print(tabla_facturas)


    def mostrar_facturas_confiteria(facturas_confiteria):
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}F A C T U R A S     C O N F I T E R Í A{estilo_reset}"
        
        facturas_data = []
        for factura in facturas_confiteria:
            numero_factura, fecha_venta, cliente, productos_vendidos, cantidad_vendida, total_venta, estado = factura

            # Acceder a los datos del cliente
            identificacion_cliente, nombre_cliente, edad_cliente = cliente.obtener_datos_cliente()

            # Construir información de productos vendidos
            productos_info = ""
            for producto, cantidad in productos_vendidos:
                id_producto, nombre_producto, _, _, precio_venta_producto, _ = producto.obtener_datos_producto()
                productos_info += f"{cantidad}x {nombre_producto} (${precio_venta_producto:.2f})\n"

            facturas_data.append([numero_factura, fecha_venta, nombre_cliente, productos_info, total_venta])

        headers = [f"{color_headers}Numero Factura", "Fecha de venta", "Cliente", "Productos", f"Total Venta{estilo_reset}"]
        data = [[f"{a[0]:04}", a[1], a[2], a[3], f"${a[4]:.2f}"] for a in facturas_data]

        tabla_facturas = tabulate(data, headers=headers, tablefmt="fancy_grid")

        print("\n" + titulo.center(len(tabla_facturas.split('\n')[0])) + "\n")
        print(tabla_facturas)


    @staticmethod
    def mostrar_factura(factura, productos_vendidos):
        # Implementa la lógica para mostrar la factura aquí
        # Puedes utilizar la información de la factura y los productos vendidos

        print("FACTURA:")
        print("Número de factura:", factura[1])
        print("Fecha de venta:", factura[0])
        print("Cliente:", factura[2].nombre_cliente)
        print("Productos vendidos:")

        for producto, cantidad in productos_vendidos:
            print(f"- {cantidad} {producto.nombre_producto} - ${producto.precio_venta_producto:.2f} c/u")

        print("Total venta: ${:.2f}".format(factura[2]))
        print("¡Gracias por su compra!")

    def mostrar_productos_combos(inventario_combos):
        color_titulo = Fore.LIGHTCYAN_EX
        color_headers = Fore.LIGHTYELLOW_EX
        estilo_reset = Style.RESET_ALL

        titulo = f"{color_titulo}C O M B O S{estilo_reset}"
        
        inventario_data = []
        for id_producto, datos_producto in inventario_combos.items():
            datos_producto = datos_producto.obtener_datos_producto()
            lista_elementos = ", ".join(datos_producto[2])  # Convertir la lista a una cadena
            inventario_data.append([id_producto, datos_producto[1], lista_elementos,
                                    f"$ {datos_producto[3]:.2f}", f"$ {datos_producto[4]:.2f}",
                                    datos_producto[5]])

        headers = [f"{color_headers}ID", "Combo", "Incluye", "Compra", "Venta", f"Cantidad{estilo_reset}"]

        # Obtener la tabla del inventario utilizando tabulate sin imprimir
        tabla_inventario = tabulate(inventario_data, headers=headers, tablefmt="fancy_grid")

        # Imprimir el título centrado sobre la tabla
        print("\n" + titulo.center(len(tabla_inventario.split('\n')[0])) + "\n")

        # Imprimir la tabla del inventario utilizando tabulate
        print(tabla_inventario)
        print()