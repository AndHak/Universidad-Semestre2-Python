

class Cliente:
    clientes = {}

    def __init__(self, cliente_id, nombre, num_acompanantes, telefono):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.num_acompanantes = num_acompanantes
        self.telefono = telefono

    def obtener_nivel_acceso(self):
        return "N/A"
    
    def obtener_tarifa_base(self):
        return 0  

    def __str__(self):
        nivel_acceso = self.obtener_nivel_acceso()
        return f"ID: {self.cliente_id}, Nombre: {self.nombre}, Acompañantes: {self.num_acompanantes}, Teléfono: {self.telefono}, Nivel de Acceso: {nivel_acceso}"

    @classmethod
    def registrar_cliente(cls):
        try:
            cc_cliente = int(input("\nCédula: "))
            nombre_cliente = input("Nombre: ")

            nivel_acceso = cls.seleccionar_nivel_acceso()

            num_acompanantes = int(input("Número de acompañantes: "))
            telefono = input("Celular: ")

            cliente = cls.cliente_tipo(cc_cliente, nombre_cliente, num_acompanantes, telefono, nivel_acceso)

            cls.clientes[cc_cliente] = cliente
            print(f"\nCliente {nombre_cliente} registrado con éxito.")

            factura = FacturaCliente(cliente, num_acompanantes)
            total_factura = factura.factura_cliente()

            print(f"\nFactura generada:")
            print(f"Cliente: {cliente.nombre}")
            print(f"Número de Acompañantes: {num_acompanantes}")
            print(f"Total a Pagar: ${total_factura:.2f}")

        except (ValueError, TypeError):
            print("Error: Ingrese valores válidos.")

    
    @classmethod
    def modificar_cliente_datos(cls):
        try:
            cc_cliente = int(input("\nCédula: "))
            nombre_cliente = input("Nombre: ")
            num_acompanantes = int(input("Número de acompañantes: "))
            telefono = input("Celular: ")

            nivel_acceso = cls.seleccionar_nivel_acceso()

            cliente = cls.cliente_tipo(cc_cliente, nombre_cliente, num_acompanantes, telefono, nivel_acceso)

            cls.clientes[cc_cliente] = cliente

            return cc_cliente

        except (ValueError, TypeError):
            print("Error: Ingrese valores válidos.")

    @classmethod
    def seleccionar_nivel_acceso(cls):
        while True:
            print("\nNiveles de Acceso:")
            print("1. Básico    -   Tarifa: 8000")
            print("   Beneficios:")
            print("   - Sin descuento en servicios solo entrada.")

            print("2. Premium   -   Tarifa: 50000")
            print("   Beneficios:")
            print("   - Descuento del 20% en servicios de Piscina.")
            print("   - Descuento del 20% en servicios de Restaurante.")
            print("   - Descuento del 20% en servicios de Juegos.")
            print("   - Descuento del 20% en servicios de cabañas.")
            print("   - Reservas prioritarias.")

            print("3. Diamond   -   Tarifa: 300000")
            print("   Beneficios:")
            print("   - Descuento del 100% en servicios de Piscina.")
            print("   - Descuento del 100% en servicios de Restaurante.")
            print("   - Descuento del 100% en servicios de Juegos.")
            print("   - Descuento del 50% en servicios de cabañas.")
            print("   - Acceso a todas las áreas, incluyendo exclusivas.")
            print("   - Reservas prioritarias.")
            print("   - Servicio de mayordomo.")
            print("   - Transporte VIP.")

            nivel_acceso = int(input("\nSeleccione el nivel de acceso: "))
            if nivel_acceso in [1, 2, 3]:
                return nivel_acceso
            else:
                print("Opción no válida. Por favor, seleccione un nivel de acceso válido.")

    @classmethod
    def cliente_tipo(cls, cc_cliente, nombre_cliente, num_acompanantes, telefono, nivel_acceso):
        if nivel_acceso == 1:
            return ClienteBasic(cc_cliente, nombre_cliente, num_acompanantes, telefono)
        elif nivel_acceso == 2:
            return ClientePremium(cc_cliente, nombre_cliente, num_acompanantes, telefono)
        else:
            return ClienteDiamond(cc_cliente, nombre_cliente, num_acompanantes, telefono)
    
    @classmethod
    def ver_clientes(cls):
        print("\nClientes Registrados:")
        for cedula, cliente in cls.clientes.items():
            print(cliente)

    @classmethod
    def buscar_cliente(cls, cedula):
        for cedula_cliente, cliente in cls.clientes.items():
            if cedula_cliente == cedula:
                return cliente
        return None

    @classmethod
    def gestionar_cliente(cls, cedula):
        cliente = cls.buscar_cliente(cedula)
        if cliente:
            print(f"\nCliente encontrado con cédula {cedula}:")
            print(cliente)

            while True:
                accion = input("\nE para eliminar, M para modificar, S para salir: ").upper()

                if accion == "E":
                    cls.eliminar_cliente(cedula)
                    print("Cliente eliminado.")
                    break
                elif accion == "M":
                    cls.modificar_cliente(cedula)
                    print("Cliente modificado.")
                    break
                elif accion == "S":
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
        else:
            print(f"\nCliente con cédula {cedula} no encontrado.")

    @classmethod
    def eliminar_cliente(cls, cedula):
        del cls.clientes[cedula]

    @classmethod
    def modificar_cliente(cls, cedula):
        cliente = cls.buscar_cliente(cedula)
        if cliente:
            print(f"\nModificando cliente con cédula {cedula}:")
            nueva_cedula = cls.modificar_cliente_datos()
            print(f"\nCliente con cédula {cedula} modificada a {nueva_cedula} con éxito.")
            cls.eliminar_cliente(cedula)
        else:
            print(f"\nCliente con cédula {cedula} no encontrado.")

class ClienteBasic(Cliente):
    def obtener_nivel_acceso(self):
        return "Básico"
    
    def obtener_tarifa_base(self):
        return 8000

class ClientePremium(Cliente):
    def obtener_nivel_acceso(self):
        return "Premium"
    
    def obtener_tarifa_base(self):
        return 50000

class ClienteDiamond(Cliente):
    def obtener_nivel_acceso(self):
        return "Diamond"
    
    def obtener_tarifa_base(self,):
        return 300000

class FacturaCliente:
    def __init__(self, cliente, num_acompanantes):
        self.cliente = cliente
        self.num_acompanantes = num_acompanantes

    def factura_cliente(self):
        tarifa_base = self.cliente.obtener_tarifa_base()
        tarifa_total = tarifa_base
        if self.num_acompanantes > 2:
            aumento = self.num_acompanantes - 2
            contador = 0
            while contador < aumento:
                tarifa_total += tarifa_base/2
                contador += 1
            return tarifa_total
        else:
            return tarifa_base
