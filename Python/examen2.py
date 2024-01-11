
class Socio:
    def __init__(self, nombre, id, tipo):
        self.nombre = nombre
        self.id = id
        self.tipo = tipo
        self.autorizados = []

    def obtener_descuento(self):
        if self.tipo == 'platino':
            return 0.15
        elif self.tipo == 'gold':
            return 0.10
        elif self.tipo == 'silver':
            return 0.05
        else:
            raise ValueError("Tipo de socio no válido")

class ClubUdenar:
    def __init__(self):
        self.socios = []
        self.autorizados = []
        self.consumos = []

    def mostrar_menu_principal(self):
        print("Menu Club Udenar")
        print("1. Manejo de Socios")
        print("2. Manejo de Autorizados")
        print("3. Manejo de Consumos")
        print("4. Estadísticas")
        print("5. Salir")

    def manejar_socios(self):
        while True:
            print("\nMenú Manejar Socios")
            print("1. Adicionar Socio")
            print("2. Modificar Socio")
            print("3. Eliminar Socio")
            print("4. Consultar Socio con Autorizados")
            print("5. Regresar")

            opcion_socios = input("Seleccione una opción: ")

            if opcion_socios == '1':
                nombre = input("Ingrese el nombre del socio: ")
                id_socio = input("Ingrese el ID del socio: ")
                tipo_socio = input("Ingrese el tipo de socio (platino, gold, silver): ")

                # Validar tipo de socio
                if tipo_socio not in ['platino', 'gold', 'silver']:
                    raise ValueError("Tipo de socio no válido")

                nuevo_socio = Socio(nombre, id_socio, tipo_socio)
                self.socios.append(nuevo_socio)
                print("Socio añadido correctamente.")

            elif opcion_socios == '2':
                # Implementar lógica para modificar socio
                pass

            elif opcion_socios == '3':
                # Implementar lógica para eliminar socio
                pass

            elif opcion_socios == '4':
                # Implementar lógica para consultar socio con autorizados
                pass

            elif opcion_socios == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def manejar_autorizados(self):
        while True:
            print("\nMenú Manejar Autorizados")
            print("1. Adicionar Autorizado")
            print("2. Modificar Autorizado")
            print("3. Eliminar Autorizado")
            print("4. Consultar Autorizado con Socio")
            print("5. Regresar")

            opcion_autorizados = input("Seleccione una opción: ")

            if opcion_autorizados == '1':
                # Implementar lógica para adicionar autorizado
                pass

            elif opcion_autorizados == '2':
                # Implementar lógica para modificar autorizado
                pass

            elif opcion_autorizados == '3':
                # Implementar lógica para eliminar autorizado
                pass

            elif opcion_autorizados == '4':
                # Implementar lógica para consultar autorizado con socio
                pass

            elif opcion_autorizados == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def manejar_consumos(self):
        while True:
            print("\nMenú Manejar Consumos")
            print("1. Adicionar Consumo")
            print("2. Pagar Consumo")
            print("3. Modificar Consumo")
            print("4. Consultar Consumos Socio")
            print("5. Regresar")

            opcion_consumos = input("Seleccione una opción: ")

            if opcion_consumos == '1':
                # Implementar lógica para adicionar consumo
                pass

            elif opcion_consumos == '2':
                # Implementar lógica para pagar consumo
                pass

            elif opcion_consumos == '3':
                # Implementar lógica para modificar consumo
                pass

            elif opcion_consumos == '4':
                # Implementar lógica para consultar consumos socio
                pass

            elif opcion_consumos == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def estadisticas(self):
        while True:
            print("\nMenú Informes")
            print("1. Total Consumos")
            print("2. Total Consumos por Socio")
            print("3. Socio que más Consumió")
            print("4. Total Consumos por Tipo de Socio")
            print("5. Regresar")

            opcion_informes = input("Seleccione una opción: ")

            if opcion_informes == '1':
                # Implementar lógica para informe de total consumos
                pass

            elif opcion_informes == '2':
                # Implementar lógica para informe de total consumos por socio
                pass

            elif opcion_informes == '3':
                # Implementar lógica para informe de socio que más consumió
                pass

            elif opcion_informes == '4':
                # Implementar lógica para informe de total consumos por tipo de socio
                pass

            elif opcion_informes == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


# Código principal
club = ClubUdenar()

while True:
    club.mostrar_menu_principal()
    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == '1':
        club.manejar_socios()

    elif opcion_principal == '2':
        club.manejar_autorizados()

    elif opcion_principal == '3':
        club.manejar_consumos()

    elif opcion_principal == '4':
        club.estadisticas()

    elif opcion_principal == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

