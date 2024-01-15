import pickle
import datetime

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.autorizados = []

class Factura:
    def __init__(self):
        self.numero_factura=0
        self.facturas=[]


class Socio(Persona):
    def __init__(self, nombre, cedula,tipo):
        super().__init__(nombre, cedula)
        self.tipo=tipo
        self.socios={}

    def registrar_socio(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        if self.socios:
            for socio in self.socios:
                if socio.cedula == cedula_socio:
                    print("El socio ya está en la base de datos")
                else:
                    nombre_socio = input("Digite el nombre del Socio-> ")
                    tipo_socio = input("Digite el tipo del Socio (platino/gold/silver)-> ")

                    socio = Socio(nombre_socio, cedula_socio, tipo_socio)

                    autorizados = []

                    self.socios[socio] = autorizados
                    print("-Socio registrado exitosamente-")
        else:
            nombre_socio = input("Digite el nombre del Socio-> ")
            tipo_socio = input("Digite el tipo del Socio (platino/gold/silver)-> ")

            socio = Socio(nombre_socio, cedula_socio, tipo_socio)

            autorizados = []

            self.socios[socio] = autorizados
            print("-Socio registrado exitosamente-")

    def listar_socios(self):
        print("\nListado de Socios:")
        for i, socio in enumerate(self.socios, start=1):
            print(f"{i}. {socio.nombre} - {socio.cedula} - {socio.tipo}")

    def modificar_socio(self):
        cedula_socio = input("Digite la cedula del Socio a modificar-> ")
        encontrado = False

        for socio in self.socios:
            if socio.cedula == cedula_socio:
                nuevo_nombre = input("Digite el nuevo nombre del Socio-> ")
                nuevo_tipo = input("Digite el nuevo tipo del Socio (platino/gold/silver)-> ")

                socio.nombre = nuevo_nombre
                socio.tipo = nuevo_tipo
                encontrado = True
                print("Socio modificado exitosamente.")
                break

        if not encontrado:
            print("No se encontró un socio con la cédula proporcionada.")

    def eliminar_socio(self):
        cedula_socio = input("Digite la cedula del Socio a eliminar-> ")
        encontrado = False

        for socio, autorizados in self.socios.items():
            if socio.cedula == cedula_socio:
                socio_delete = socio
                encontrado = True
                break
        if not encontrado:
            print("No se encontró un socio con la cédula proporcionada.")
        if encontrado:
            del self.socios[socio_delete]
            print("-Socio eliminado con exito-")

    def comprobar_socio(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio in self.socios:
            if socio.cedula == cedula_socio:
                print("El socio ya está en la base de datos.") 
            else:
                print(f"""
                    El socio no está en la base de datos.
                    Ingrese nuevo socio-> """) 
                self.registrar_socio()

    def limite_socio(self):
        if self.tipo == 'platino':
            return float("inf"),0.15
        elif self.tipo == 'gold':
            return 10,0.10
        elif self.tipo == 'silver':
            return 5,0.05
        
class ClubUdenar:
    def __init__(self):
        self.metsocio = Socio("","","")
        self.cargar()
        factura = factura()

    def cargar(self):
        try:
            with open("socios.pkl", "rb") as file:
                self.metsocio.socios = pickle.load(file)
        except (FileNotFoundError, EOFError):
            # Si el archivo no existe o está vacío, se inicia con un diccionario vacío.
            self.metsocio.socios = {}

    def guardar(self):
        with open("socios.pkl", "wb") as file:
            pickle.dump(self.metsocio.socios, file)

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
                self.metsocio.registrar_socio()
                self.guardar()
            elif opcion_socios == '2':
                self.metsocio.modificar_socio()
                self.guardar()
            elif opcion_socios == '3':
                self.metsocio.eliminar_socio()
                self.guardar()
            elif opcion_socios == '4':
                self.metsocio.listar_socios()
                self.guardar()
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
                self.agregar_autorizado()
                self.guardar()
            elif opcion_autorizados == '2':
                self.modificar_autorizado()
                self.guardar()

            elif opcion_autorizados == '3':
                self.eliminar_autorizado()
                self.guardar()
            elif opcion_autorizados == '4':
                self.consultar_autorizado_con_socio()
                self.guardar()
            elif opcion_autorizados == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def agregar_autorizado(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                nombre_autorizado = input("Digite el nombre del usuario autorizado-> ")
                cedula_autorizado = input("Digite la cedula del usuario autorizado-> ")
                autorizado=Persona(nombre_autorizado,cedula_autorizado)
                autorizados.append(autorizado)
                print("-Usuario autorizado registrado exitosamente-")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def modificar_autorizado(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if autorizados:
                    nombre_autorizado = input("Digite el nombre del usuario autorizado a modificar-> ")
                    for autorizado in autorizados:
                        if autorizado.nombre == nombre_autorizado:
                            nuevo_nombre = input("Digite el nuevo nombre del usuario autorizado-> ")
                            nuevo_cedula = input("Digite la nueva cedula del usuario autorizado-> ")
                            autorizado.nombre = nuevo_nombre
                            autorizado.cedula = nuevo_cedula
                            print("-Usuario autorizado modificado exitosamente-")
                            break
                    else:
                        print("No se encontró un usuario autorizado con el nombre proporcionado.")
                else:
                    print("No hay usuarios autorizados para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def eliminar_autorizado(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if autorizados:
                    nombre_autorizado = input("Digite el nombre del usuario autorizado a eliminar-> ")
                    for autorizado in autorizados:
                        if autorizado.nombre == nombre_autorizado:
                            autorizados.remove(autorizado)
                            print("-Usuario autorizado eliminado exitosamente-")
                            break
                    else:
                        print("No se encontró un usuario autorizado con el nombre proporcionado.")
                else:
                    print("No hay usuarios autorizados para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def consultar_autorizado_con_socio(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if autorizados:
                    nombre_autorizado = input("Digite el nombre del usuario autorizado a consultar-> ")
                    for autorizado in autorizados:
                        if autorizado.nombre == nombre_autorizado:
                            print("Información del Usuario Autorizado:")
                            print(f"Nombre: {autorizado.nombre}")
                            print(f"Cédula: {autorizado.cedula}")
                            break
                    else:
                        print("No se encontró un usuario autorizado con el nombre proporcionado.")
                else:
                    print("No hay usuarios autorizados para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")


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
                self.adicionar_consumo()
                self.guardar()

            elif opcion_consumos == '2':
                self.pagar_consumo()
                self.guardar()

            elif opcion_consumos == '3':
                self.modificar_consumo()
                self.guardar()

            elif opcion_consumos == '4':
                self.consultar_consumos_socio()

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
                self.informe_total_consumos()

            elif opcion_informes == '2':
                self.informe_total_consumos_por_socio()

            elif opcion_informes == '3':
                self.informe_socio_mas_consumio()

            elif opcion_informes == '4':
                self.informe_total_consumos_por_tipo_socio()

            elif opcion_informes == '5':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def adicionar_consumo(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                monto = float(input("Digite el monto del consumo-> "))
                fecha = datetime.now()
                consumo = (fecha, monto)
                socio.consumos.append(consumo)
                print("-Consumo registrado exitosamente-")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def pagar_consumo(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if socio.consumos:
                    print("Consumos Pendientes:")
                    for i, (fecha, monto) in enumerate(socio.consumos, start=1):
                        print(f"{i}. Fecha: {fecha} - Monto: {monto}")
                    seleccion = int(input("Seleccione el número de consumo a pagar-> "))
                    if 1 <= seleccion <= len(socio.consumos):
                        fecha, monto = socio.consumos.pop(seleccion - 1)
                        factura = factura.Factura(len(socio.facturas) + 1, monto, 0, socio)
                        socio.facturas.append(factura)
                        print("-Consumo pagado exitosamente-")
                    else:
                        print("Selección no válida.")
                else:
                    print("No hay consumos pendientes para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def modificar_consumo(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if socio.consumos:
                    print("Consumos Registrados:")
                    for i, (fecha, monto) in enumerate(socio.consumos, start=1):
                        print(f"{i}. Fecha: {fecha} - Monto: {monto}")
                    seleccion = int(input("Seleccione el número de consumo a modificar-> "))
                    if 1 <= seleccion <= len(socio.consumos):
                        nuevo_monto = float(input("Digite el nuevo monto del consumo-> "))
                        socio.consumos[seleccion - 1] = (socio.consumos[seleccion - 1][0], nuevo_monto)
                        print("-Consumo modificado exitosamente-")
                    else:
                        print("Selección no válida.")
                else:
                    print("No hay consumos registrados para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def consultar_consumos_socio(self):
        cedula_socio = input("Digite la cedula del Socio-> ")
        for socio, autorizados in self.metsocio.socios.items():
            if socio.cedula == cedula_socio:
                print(f"Socio: {socio.nombre} C.C: {socio.cedula}")
                if socio.consumos:
                    print("Consumos Registrados:")
                    for i, (fecha, monto) in enumerate(socio.consumos, start=1):
                        print(f"{i}. Fecha: {fecha} - Monto: {monto}")
                else:
                    print("No hay consumos registrados para este socio.")
                break
        else:
            print("No se encontró un socio con la cédula proporcionada.")

    def informe_total_consumos(self):
        total_consumos = sum(monto for socio in self.metsocio.socios.values() for fecha, monto in socio.consumos)
        print(f"Total Consumos: ${total_consumos:.2f}")

    def informe_total_consumos_por_socio(self):
        for socio, autorizados in self.metsocio.socios.items():
            total_consumos_socio = sum(monto for fecha, monto in socio.consumos)
            print(f"Socio: {socio.nombre} C.C: {socio.cedula} - Total Consumos: ${total_consumos_socio:.2f}")

    def informe_socio_mas_consumio(self):
        socio_mas_consumio = max(self.metsocio.socios.values(), key=lambda socio: sum(monto for fecha, monto in socio.consumos))
        total_consumos_mas_consumio = sum(monto for fecha, monto in socio_mas_consumio.consumos)
        print(f"Socio que más consumió: {socio_mas_consumio.nombre} C.C: {socio_mas_consumio.cedula} - Total Consumos: ${total_consumos_mas_consumio:.2f}")

    def informe_total_consumos_por_tipo_socio(self):
        total_consumos_por_tipo = {tipo: 0 for tipo in ['platino', 'gold', 'silver']}
        for socio in self.metsocio.socios.values():
            total_consumos_por_tipo[socio.tipo] += sum(monto for fecha, monto in socio.consumos)

        for tipo, total_consumo in total_consumos_por_tipo.items():
            print(f"Tipo de Socio: {tipo} - Total Consumos: ${total_consumo:.2f}")
    
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

