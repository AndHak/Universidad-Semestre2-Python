class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin
    def estatnte_A(self):
        return "La bicicleta está en el Estante A"
    def bodega(self):
        return "La bicicleta está en la bodega"
    def pedido(self):
        return "La bicicleta se encuentra en pedido"
    
urbana = Bicicleta("Roja", 2, 27.5)
hibrida = Bicicleta("Gris", 8, 28)

print(f"Bicicleta: Urbana\nColor: {urbana.color}\nCambios: {urbana.cambios}\nRin: {urbana.rin}\nActualmente {urbana.bodega()}")