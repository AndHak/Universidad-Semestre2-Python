from persona import Estudiante, Trabajador, Docente
from prestamo import RegistroPrestamo

class Login:
    def __init__(self):
        self.usuarios = []

    def iniciar_sesion(self):
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                print(f"Inicio de sesión exitoso. ¡Bienvenido, {usuario.username} ({usuario.tipo})!")
                return usuario

        print("Nombre de usuario o contraseña incorrectos.")
        return None

    def registrar_usuario(self):
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        tipo_usuario = input("Ingrese el tipo de usuario (Estudiante/Trabajador/Docente): ").lower()

        if tipo_usuario not in ["estudiante", "trabajador", "docente"]:
            print("Tipo de usuario no válido.")
            return

        nombre = input("Ingrese el nombre del usuario: ")
        if tipo_usuario == "estudiante":
            codigo_estudiante = input("Ingrese el código de estudiante: ")
            nuevo_usuario = Estudiante(nombre, codigo_estudiante)
        elif tipo_usuario == "trabajador":
            codigo_trabajador = input("Ingrese el código de trabajador: ")
            nuevo_usuario = Trabajador(nombre, codigo_trabajador)
        elif tipo_usuario == "docente":
            codigo_docente = input("Ingrese el código de docente: ")
            nuevo_usuario = Docente(nombre, codigo_docente)

        nuevo_usuario.username = username
        nuevo_usuario.password = password
        nuevo_usuario.tipo = tipo_usuario

        self.usuarios.append(nuevo_usuario)
        print("Usuario registrado correctamente.")

    def validar_datos(self, user, password):
        for usuario in self.usuarios:
            if usuario.username == user and usuario.password == password:
                return True
        return False
    
    def consultar_usuario(self):
        username_consultar = input("Ingrese el nombre de usuario a consultar: ")
        for usuario in self.usuarios:
            if usuario.username == username_consultar:
                print(f"Nombre: {usuario.nombre}, Tipo: {usuario.tipo}")
                return
        print(f"Usuario {username_consultar} no encontrado.")

    def eliminar_usuario(self):
        username = input("Digite el nombre de usuario que desea eliminar: ")
        for usuario in self.usuarios:
            if usuario.username == username:
                self.usuarios.remove(usuario)
                print(f"Usuario {username} eliminado correctamente")
                return
        print(f"El usuario {username} no existe")

    def modificar_usuario(self):
        username = input("Ingrese el nombre de usuario a modificar: ")
        for usuario in self.usuarios:
            if usuario.username == username:
                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                usuario.nombre = nuevo_nombre
                print("Usuario modificado correctamente.")
                return
        print("Usuario no encontrado.")

    def agregar_usuario(self):
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")

        tipo = input("Ingrese el tipo de usuario (Estudiante/Trabajador/Docente): ")
        if tipo.lower() == "estudiante":
            codigo_estudiante = input("Ingrese el código de estudiante: ")
            nuevo_usuario = Estudiante("", codigo_estudiante)
        elif tipo.lower() == "trabajador":
            codigo_trabajador = input("Ingrese el código de trabajador: ")
            nuevo_usuario = Trabajador("", codigo_trabajador)
        elif tipo.lower() == "docente":
            codigo_docente = input("Ingrese el código de docente: ")
            nuevo_usuario = Docente("", codigo_docente)
        else:
            print("Tipo de usuario no válido.")
            return

        nuevo_usuario.username = username
        nuevo_usuario.password = password
        nuevo_usuario.tipo = tipo

        self.usuarios.append(nuevo_usuario)
        print("Usuario agregado correctamente.")

    def mostrar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Tipo: {usuario.tipo}")