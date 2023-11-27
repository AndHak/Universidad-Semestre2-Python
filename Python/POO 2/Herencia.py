class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca {self.marca}\nModelo {self.modelo}\nEn marcha {self.enmarcha}\nAcelerando {self.acelera}\nFrenando {self.frena}")


class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print(f"Marca {self.marca}\nModelo {self.modelo}\nEn marcha {self.enmarcha}\nAcelerando {self.acelera}\nFrenando {self.frena}\n{self.hcaballito}")

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furoneta no esta cargada"
        
class VehiculosElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True


MiMoto = Moto("Yamaha", "R3")

MiMoto.caballito()

MiMoto.estado()

print()

MiFurgoneta = Furgoneta("Renault", "Kong")

MiFurgoneta.arrancar()

MiFurgoneta.estado()

print(MiFurgoneta.carga(True))

class BicicletaElectrica(VehiculosElectricos, Vehiculos):
    pass

MiBicicleta = BicicletaElectrica()