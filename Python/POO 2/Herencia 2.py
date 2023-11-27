class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}\nEdad {self.edad}\nResidencia {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, salario, antiguedad, a, b, c):
        super().__init__(a, b, c)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario {self.salario}\nAntiguedad {self.antiguedad}")


Antonio = Persona("Andres", 22, "Colombia")

Antonio.descripcion()

print(isinstance(Antonio, Empleado))

