class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo == False):
            return "No podemos arrancar, compruebe el estado del coche"
        else:
            return "El coche esta parado"

    def estado(self):
        print(f"El coche tiene: {self.__ruedas} ruedas\nUn ancho de: {self.__anchoChasis}\nUn largo de: {self.__largoChasis}")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False    

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print(miCoche.__chequeo_interno())

print("-------------A continuacion creamos el segundo objeto-----------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
print(miCoche2.__chequeo_interno())