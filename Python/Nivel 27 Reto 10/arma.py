class Arma:
    def __init__(self, nombre, resistencia, destruccion, categoria=1):
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
        self.categoria = categoria

    def __str__(self):
        return self.nombre

    def elevar_categoria(self):
        self.categoria += 1
        self.resistencia += 2
        self.destruccion += 2
