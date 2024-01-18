from datetime import datetime
from servicios import *
from clientes import Cliente
from facturas import *

class Venta:
    registro_ventas = []
    numero_factura = 0

    def __init__(self, numero_factura, servicio, cliente, fecha, total_servicio, descuento, total_total, cantidad):
        self.servicio = servicio
        self.cliente = cliente
        self.fecha_emision = fecha
        self.total_servicio = total_servicio
        self.descuento = descuento
        self.total_total = total_total
        self.numero_factura = numero_factura
        self.cantidad = cantidad

    @classmethod
    def hacer_venta_cabana(cls, cabaña):
        fecha = datetime.now()

        cc_cliente = int(input("Cedula usuario: "))

        if cc_cliente in Cliente.clientes:
            cliente_venta = Cliente.clientes[cc_cliente]
        else:
            print("El cliente no existe")
            return None

        cantidad = 1
        total_servicio = cabaña.costo

        factura_cabana = FacturaCabana(cliente_venta)
        descuento = factura_cabana.aplicar_descuento()

        if descuento:
            total_total = total_servicio - (total_servicio * descuento)
        else:
            total_total = total_servicio

        numero_factura = cls.numero_factura + 1
        cls.numero_factura += 1

        objeto_venta = Venta(numero_factura, cabaña, cliente_venta, fecha, total_servicio, descuento, total_total, cantidad)
        cls.registro_ventas.append(objeto_venta)

        cabaña.ocupada = True

        return objeto_venta

    @classmethod
    def hacer_venta(cls, servicio):
        fecha = datetime.now()
        if 0 <= servicio - 1 < len(Servicio.servicios):
            servicio_encontrado = Servicio.servicios[servicio - 1]
        else:
            print("Índice de servicio no válido.")
            return None

        cc_cliente = int(input("Cedula usuario: "))

        if cc_cliente in Cliente.clientes:
            cliente_venta = Cliente.clientes[cc_cliente]
        else:
            print("El cliente no existe")
            return None
        
        while True:
            cantidad = int(input("Numero personas: "))

            if 0 < cantidad <= cliente_venta.num_acompanantes:
                total_servicio = servicio_encontrado.costo * cantidad
                break
            else:
                print("El numero de acompañantes es mayor al registrado")

        tipo_factura = servicio_encontrado.descripcion

        if tipo_factura == "Piscina":
            factura_cliente = FacturaPiscina(cliente_venta)
        elif tipo_factura == "Restaurante":
            factura_cliente = FacturaRestaurante(cliente_venta)
        elif tipo_factura == "Juegos":
            factura_cliente = FacturaJuegos(cliente_venta)
        else:
            factura_cliente = Factura()

        descuento = factura_cliente.aplicar_descuento()

        if descuento:
            total_total = total_servicio - (total_servicio * descuento)
        else:
            total_total = total_servicio

        numero_factura = cls.numero_factura + 1
        cls.numero_factura += 1

        objeto_venta = Venta(numero_factura, servicio_encontrado, cliente_venta, fecha, total_servicio, descuento, total_total, cantidad)
        cls.registro_ventas.append(objeto_venta)

        return objeto_venta

    def imprimir_boleto(self):
        boleto = f"""
                    Factura N° {self.numero_factura}
            Fecha: {self.fecha_emision.strftime("%Y-%m-%d %H:%M:%S")}  Nivel acceso: {self.cliente.obtener_nivel_acceso()}
            Cliente: {self.cliente.nombre} C.C {self.cliente.cliente_id}
            ---------------------------------------------------------
            Servicio:
            {self.servicio.nombre} - {self.servicio.descripcion} - {self.servicio.costo} * {self.cantidad} = {self.total_servicio}
            Descuento: {self.descuento*100}%      Total: ${self.total_total}
            """
        print(boleto)

    @classmethod
    def ver_ventas(cls):
        print("\n-------- Ventas Registradas --------")
        for venta in cls.registro_ventas:
            print(f"Factura N° {venta.numero_factura}")
            print(f"Fecha: {venta.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Cliente: {venta.cliente.nombre} C.C {venta.cliente.cliente_id}")
            print(f"Servicio: {venta.servicio.nombre} - {venta.servicio.descripcion} - {venta.servicio.costo} * {venta.cantidad} = {venta.total_servicio}")
            print(f"Descuento: {venta.descuento*100}%")
            print(f"Total a Pagar: ${venta.total_total:.2f}")
            print("---------------------------------------------------------")

    @classmethod
    def ver_ventas_cliente(cls, cedula_cliente):
        print("\n-------- Ventas por Cliente --------")
        for venta in cls.registro_ventas:
            if venta.cliente.cliente_id == cedula_cliente:
                cls.imprimir_boleto(venta)

    @classmethod
    def ver_ventas_categoria(cls, categoria_servicio):
        print(f"\n-------- Ventas por Categoría: {categoria_servicio} --------")
        for venta in cls.registro_ventas:
            if venta.servicio.descripcion.lower() == categoria_servicio.lower():
                cls.imprimir_boleto(venta)

    @classmethod
    def ver_ventas_servicio(cls, nombre_servicio):
        print(f"\n-------- Ventas por Servicio: {nombre_servicio} --------")
        for venta in cls.registro_ventas:
            if venta.servicio.nombre.lower() == nombre_servicio.lower():
                cls.imprimir_boleto(venta)