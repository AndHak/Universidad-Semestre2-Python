from recurso import Recurso  
from registro import RegistroPrestamo
from persona import *

class CentralPrestamos:
    def __init__(self):
        self.recursos = []
        self.prestamos = []
        self.historial_prestamos = [] 
        self.usuarios = []  

    def agregar_recurso(self):
        codigo = input("Ingrese el código del recurso: ")
        nombre = input("Ingrese el nombre del recurso: ")
        nuevo_recurso = Recurso(codigo, nombre)
        self.recursos.append(nuevo_recurso)
        print("Recurso agregado correctamente.")

    def consultar_recurso(self):
        codigo = input("Ingrese el código del recurso a consultar: ")
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                print(f"Código: {recurso.codigo}, Nombre: {recurso.nombre}, Estado: {recurso.estado}")
                return
        print("Recurso no encontrado.")

    def modificar_recurso(self):
        codigo = input("Ingrese el código del recurso a modificar: ")
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                nuevo_nombre = input("Ingrese el nuevo nombre del recurso: ")
                recurso.nombre = nuevo_nombre
                print("Recurso modificado correctamente.")
                return
        print("Recurso no encontrado.")

    def mostrar_recursos(self):
        print("Recursos disponibles:")
        for recurso in self.recursos:
            print(f"Código: {recurso.codigo}, Nombre: {recurso.nombre}, Estado: {recurso.estado}")

    def eliminar_recurso(self):
        codigo = input("Ingrese el código del recurso a eliminar: ")
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                confirmacion = input(f"¿Está seguro de eliminar el recurso {recurso.nombre}? (S/N): ")
                if confirmacion.lower() == "s":
                    self.recursos.remove(recurso)
                    print("Recurso eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
                return
        print("Recurso no encontrado.")

    def prestamo_recurso(self, usuario_actual):
        codigo_recurso = input("Ingrese el código del recurso a prestar: ")
        nombre_destinatario = input("Ingrese el nombre de la persona a quien se le prestará el recurso: ")

        recurso_prestamo = None
        for recurso in self.recursos:
            if recurso.codigo == codigo_recurso and recurso.estado == "Disponible":
                recurso_prestamo = recurso
                break

        if recurso_prestamo:
            registro_prestamo = RegistroPrestamo(recurso_prestamo, usuario_actual, nombre_destinatario)
            self.prestamos.append(registro_prestamo)
            self.historial_prestamos.append(registro_prestamo)
            recurso_prestamo.estado = "Prestado"
            print(f"Préstamo realizado correctamente a {nombre_destinatario}.")
        else:
            print("No se pudo realizar el préstamo. Verifique el código del recurso.")



    def devolucion_recurso(self):
        codigo_recurso_devolucion = input("Ingrese el código del recurso a devolver: ")

        for prestamo in self.historial_prestamos:
            if prestamo.recurso.codigo == codigo_recurso_devolucion:
                prestamo.recurso.estado = "Disponible"
                self.historial_prestamos.remove(prestamo)
                print(f"Devolución realizada correctamente del recurso {codigo_recurso_devolucion}.")
                return

        print("No se pudo realizar la devolución. Verifique el código del recurso o si existe un préstamo asociado en el historial.")


    def mostrar_prestamo_usuario(self):
        nombre_usuario = input("Ingrese el nombre del usuario a consultar: ")

        for prestamo in self.historial_prestamos:
            if isinstance(prestamo.usuario, str):
                usuario_nombre = prestamo.usuario
            else:
                usuario_nombre = getattr(prestamo.usuario, 'nombre', 'N/A')

            if isinstance(prestamo.recurso, str):
                recurso_nombre = prestamo.recurso
            else:
                recurso_nombre = getattr(prestamo.recurso, 'nombre', 'N/A')

            if isinstance(prestamo.destinatario, str):
                destinatario_nombre = prestamo.destinatario
            else:
                destinatario_nombre = getattr(prestamo.destinatario, 'nombre_destinatario', 'N/A')

            print(f"Usuario: {usuario_nombre}, Recurso prestado: {recurso_nombre}, Prestado a: {destinatario_nombre}")

        print("No se encontraron préstamos asociados al usuario especificado en el historial.")



    def mostrar_prestamos_usuarios(self):
        print("Historial completo de préstamos:")
        print("{:<20} {:<20} {:<20} {:<20}".format("Usuario", "Recurso prestado", "Prestado a", "Fecha de préstamo"))

        for prestamo in self.historial_prestamos:
            usuario_nombre = getattr(prestamo.usuario, 'nombre', 'N/A')
            recurso_nombre = getattr(prestamo.recurso, 'nombre', 'N/A')
            nombre_destinatario = getattr(prestamo.destinatario, 'nombre_destinatario', 'N/A')

            print("{:<20} {:<20} {:<20}".format(usuario_nombre, recurso_nombre, nombre_destinatario))

        if not self.historial_prestamos:
            print("No hay registros de préstamos.")



