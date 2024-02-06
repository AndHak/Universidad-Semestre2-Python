class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calle = 1
        self.energy = 15

    def situacion(self):
        return self.nombre, self.calle, self.energy

    def moverse(self, movimiento):
        if movimiento == 1:
            self.calle += 1
        if movimiento == 2:
            self.calle += 2
        else:
            self.calle += 3
        self.energy -= 1


