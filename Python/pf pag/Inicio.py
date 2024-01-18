from clientes import Cliente
from guardar_y_cargar import guardar, cargar
from servicios import *
from venta import *
import os

def titulo():
    print("""     
        ########### CABAÑAS OASIS ###########
        """)
    

def mostrar_menu():
    print("\n-------- Menú Principal --------")
    print("1. Registrar Cliente")
    print("2. Ofrecer Servicios")
    print("3. Ver Clientes")
    print("4. Ver Ventas")
    print("5. Salir")
    return input("Ingrese el número de la opción deseada: ")

def menu_servicios():
    print("\n-------- Servicios --------")
    print("1. Aregar servicio")
    print("2. Ver servicios")
    print("3. Facturar servicio")
    print("4. Facturar Cabaña")
    print("5. Administrar cabañas")
    print("6. Salir")
    return int(input("Ingrese el número de la opción deseada: "))


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            Cliente.registrar_cliente()
            guardar()
            os.system("pause")
            
        elif opcion == "2":
            while True:
                try:
                    opcion = menu_servicios()

                    if opcion == 1:
                        try:
                            nombre = input("Nombre: ")
                            descripcion = input("Descripcion: ")
                            costo = float(input("Costo: "))
                            
                            Servicio.agregar_servicio(nombre, descripcion, costo)
                            guardar()
                        except ValueError:
                            print("Dato incorrecto")

                    if opcion == 2:
                        Servicio.ver_servicios()
                        seleccion = input("e para eliminar, s para salir: ")

                        if seleccion.lower() == "e":
                            indice_a_eliminar = int(input("Ingrese el número del servicio a eliminar: "))
                            Servicio.eliminar_servicio(indice_a_eliminar)
                        elif seleccion.lower() == "s":
                            continue

                    if opcion == 3:
                        
                        Servicio.ver_servicios()

                        escoger = int(input("\nIngrese el numero del servicio a escoger: "))

                        boleto = Venta.hacer_venta(escoger)

                        Venta.imprimir_boleto(boleto)
                        guardar()

                        os.system("pause")

                    if opcion == 4:
                        Cabaña.ver_cabañas()
                        seleccionar = int(input("Seleccione una cabaña: "))

                        cabaña_seleccionada = Cabaña.seleccionar_cabaña(seleccionar)

                        if cabaña_seleccionada:
                            if not cabaña_seleccionada.ocupada:
                                boleto = Venta.hacer_venta_cabana(cabaña_seleccionada)
                                Venta.imprimir_boleto(boleto)
                                guardar()
                            else:
                                print("La cabaña seleccionada está ocupada.")



                    if opcion == 5:
                        Cabaña.ver_cabañas()
                        seleccionar = int(input("Seleccione una cabaña: "))

                        cabaña_seleccionada = Cabaña.seleccionar_cabaña(seleccionar)

                        if cabaña_seleccionada:
                            Cabaña.mostrar_cabaña(cabaña_seleccionada)

                            while True:
                                print("\ne para eliminar")
                                print("s para salir")
                                print("d para marcar como disponible")
                                accion = input("> ")

                                if accion.lower() == "d":
                                    Cabaña.marcar_como_disponible(cabaña_seleccionada)

                                if accion.lower() == "e":
                                    Cabaña.eliminar_cabaña(cabaña_seleccionada)

                                if accion.lower() == "s":
                                    break
                            
                    if opcion == 6:
                        break
                except ValueError:
                    continue

        elif opcion == "3":
            Cliente.ver_clientes()
            try:
                buscando = True
                while buscando:
                    buscar_cedula = int(input("Buscar por cedula: "))
                    Cliente.gestionar_cliente(buscar_cedula)
                    guardar()
                    break    
            except (ValueError, TypeError):
                print("Error: Ingrese valores válidos.")

        elif opcion == "4":
            while True:
                try:
                    Venta.ver_ventas()
                    print("\n (s) para salir")
                    print("e para eliminar, s para cancelar")
                    print("vc ver ventas por cliente")
                    print("vt ver ventas por categoria")
                    print("vn ver ventas por servicio")

                    numero_factura = input("Numero Factura: ")

                    if numero_factura.isalpha():
                        accion = str(numero_factura)
                        if accion == "s":
                            break

                        if accion.lower() == "c":
                            continue

                        elif accion.lower() == "e":
                            while True:
                                numero_factura_eliminar = int(input("Numero de factura: "))

                                for objeto in Venta.registro_ventas:
                                    if numero_factura_eliminar == objeto.numero_factura:
                                        venta = objeto
                                        if isinstance(venta.servicio, Cabaña):
                                            Cabaña.marcar_como_disponible(venta.servicio)
                                        
                                        Venta.registro_ventas.remove(venta)
                                        print("Venta eliminada")
                                        break
                                    else:
                                        print("El numero de factura no existe")

                        elif accion.lower() == "vc":
                            cc_cliente = int(input("Cedula del cliente: "))
                            Venta.ver_ventas_cliente(cc_cliente)
                        elif accion.lower() == "vt":
                            categoria = input("Categoria de servicio: ")
                            Venta.ver_ventas_categoria(categoria)
                        elif accion.lower() == "vn":
                            nombre_servicio = input("Nombre de servicio: ")
                            Venta.ver_ventas_servicio(nombre_servicio)
                        
                    if numero_factura.isnumeric():
                        numero_factura = int(numero_factura)
                        venta = None

                        for objeto in Venta.registro_ventas:
                            if numero_factura == objeto.numero_factura:
                                venta = objeto

                        if venta:
                            Venta.imprimir_boleto(venta)
                            os.system("pause")
                        else:
                            print("No existe la factura")

                except ValueError:
                    continue
                
        elif opcion == "5":
            guardar()
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    cargar()
    titulo()
    main()
