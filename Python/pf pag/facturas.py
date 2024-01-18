from clientes import *

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente

    def aplicar_descuento(self):
        return 0

class FacturaPiscina(Factura):
    def __init__(self, cliente):
        super().__init__(cliente)

    def aplicar_descuento(self):
        nivel_acceso = self.cliente.obtener_nivel_acceso()
        if nivel_acceso == "Diamond":
            return 1
        elif nivel_acceso == "Premium":
            return 0.2
        else:
            return 0

class FacturaRestaurante(Factura):
    def __init__(self, cliente):
        super().__init__(cliente)

    def aplicar_descuento(self):
        nivel_acceso = self.cliente.obtener_nivel_acceso()
        if nivel_acceso == "Diamond":
            return 1
        elif nivel_acceso == "Premium":
            return 0.2
        else:
            return 0

class FacturaJuegos(Factura):
    def __init__(self, cliente):
        super().__init__(cliente)

    def aplicar_descuento(self):
        nivel_acceso = self.cliente.obtener_nivel_acceso()
        if nivel_acceso == "Diamond":
            return 1
        elif nivel_acceso == "Premium":
            return 0.2
        else:
            return 0

class FacturaCabana(Factura):
    def __init__(self, cliente):
        super().__init__(cliente)

    def aplicar_descuento(self):
        nivel_acceso = self.cliente.obtener_nivel_acceso()
        if nivel_acceso == "Diamond":
            return 0.5
        elif nivel_acceso == "Premium":
            return 0.2
        else:
            return 0
