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

        # Resto de la lógica para las otras opciones del menú

# Código principal
club = ClubUdenar()

while True:
    club.mostrar_menu_principal()
    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == '1':
        club.manejar_socios()
        # Implementar lógica para manejar socios

    elif opcion_principal == '2':
        club.manejar_autorizados()
        # Implementar lógica para manejar autorizados

    elif opcion_principal == '3':
        club.manejar_consumos()
        # Implementar lógica para manejar consumos

    elif opcion_principal == '4':
        club.estadisticas()
        # Implementar lógica para estadísticas

    elif opcion_principal == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")