#Objetos pasan mensajes

class Persona():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}. ¿Cómo te llamas?.")

    def responder(self, otro):
        print(f"Hola {otro.nombre}, me llamo {self.nombre}")

    def preguntar_edad(self, otro):
        print(f"¿Cuantos años tienes {otro.nombre}?")

    def responder_edad(self, otro):
        print(f"Tengo {self.edad} años {otro.nombre}")

    def felicitar(self, otro):
        print(f"{otro}, Felicidades por tu cumpleaños numero {otro.edad+1}")

jorge = Persona("Jorge", 23)
maria = Persona("Maria", 24)

jorge.presentarse()
maria.responder(jorge)
jorge.preguntar_edad(maria)
maria.responder_edad(jorge)
jorge.felicitar(maria)