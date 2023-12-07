from colorama import Fore, init

class Persona:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Estudiante(Persona):
    def __init__(self, nombre, codigo_estudiante):
        super().__init__(nombre, "Estudiante")
        self.codigo_estudiante = codigo_estudiante

class Trabajador(Persona):
    def __init__(self, nombre, codigo_trabajador):
        super().__init__(nombre, "Trabajador")
        self.codigo_trabajador = codigo_trabajador

class Docente(Persona):
    def __init__(self, nombre, codigo_docente):
        super().__init__(nombre, "Docente")
        self.codigo_docente = codigo_docente

class Usuario(Persona):
    def __init__(self, username, password, tipo):
        super().__init__(username, tipo)
        self.username = username
        self.password = password

    def __str__(self):
        return f"{Fore.YELLOW}{self.tipo}{Fore.RESET} - {Fore.CYAN}{self.nombre}{Fore.RESET}"

    def __repr__(self):
        return str(self)
