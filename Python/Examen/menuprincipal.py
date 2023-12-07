from colorama import init, Fore
from login import Login
from prestamo import *



def imprimir_menu(opciones):
    for i, opcion in enumerate(opciones, start=1):
        print(f"{Fore.CYAN}{i}. {opcion}{Fore.RESET}")

def menu_principal(login, central_prestamos):
    init(autoreset=True)  

    while True:
        print("\n¡Bienvenido al Sistema de Gestión de Préstamos!")
        imprimir_menu(["Iniciar Sesión", "Registrarse", "Salir"])

        opcion_inicio = input("Seleccione una opción: ")

        if opcion_inicio == "1":
            usuario_actual = login.iniciar_sesion()
            if usuario_actual:
                menu_usuario(login, central_prestamos, usuario_actual)
        elif opcion_inicio == "2":
            login.registrar_usuario()
        elif opcion_inicio == "3":
            print("¡Hasta luego!")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, seleccione una opción válida.{Fore.RESET}")

def menu_usuario(login, central_prestamos, usuario_actual):
    while True:
        print(f"\n¡Bienvenido, {usuario_actual.username} ({usuario_actual.tipo})!")

        print("\nMenú Principal")
        print("1. Manejo de Recursos")
        print("2. Manejo de Usuarios")
        print("3. Manejo de Préstamos y Devoluciones")
        print("4. Cerrar Sesión")

        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1":
            menu_recursos(central_prestamos)
        elif opcion_principal == "2":
            menu_usuarios(login)
        elif opcion_principal == "3":
            menu_prestamos_devoluciones(central_prestamos, usuario_actual) 
        elif opcion_principal == "4":
            login.cerrar_sesion()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def menu_recursos(central_prestamos):
    while True:
        imprimir_menu(["Adicionar recurso", "Consultar recurso", "Modificar recurso", "Mostrar recursos", "Eliminar recurso", "Salir"])
        opcion_recursos = input("Seleccione una opción: ")

        if opcion_recursos == "1":
            central_prestamos.agregar_recurso()
        elif opcion_recursos == "2":
            central_prestamos.consultar_recurso()
        elif opcion_recursos == "3":
            central_prestamos.modificar_recurso()
        elif opcion_recursos == "4":
            central_prestamos.mostrar_recursos()
        elif opcion_recursos == "5":
            central_prestamos.eliminar_recurso()
        elif opcion_recursos == "6":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, seleccione una opción válida.{Fore.RESET}")

def menu_usuarios(login):
    while True:
        imprimir_menu(["Adicionar Usuario", "Consultar Usuario", "Modificar Usuario", "Eliminar Usuario", "Mostrar Usuarios", "Salir"])
        opcion_usuarios = input("Seleccione una opción: ")

        if opcion_usuarios == "1":
            login.agregar_usuario()
        elif opcion_usuarios == "2":
            login.consultar_usuario()
        elif opcion_usuarios == "3":
            login.modificar_usuario()
        elif opcion_usuarios == "4":
            login.eliminar_usuario()
        elif opcion_usuarios == "5":
            login.mostrar_usuarios()
        elif opcion_usuarios == "6":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, seleccione una opción válida.{Fore.RESET}")

def menu_prestamos_devoluciones(central_prestamos, usuario_actual):
    while True:
        print("\nMenú Manejo de Préstamos y Devoluciones")
        print("1. Préstamo de Recurso")
        print("2. Devolución de un recurso")
        print("3. Mostrar préstamo usuario")
        print("4. Mostrar préstamos usuarios")
        print("5. Salir")

        opcion_prestamos_devoluciones = input("Seleccione una opción: ")

        if opcion_prestamos_devoluciones == "1":
            central_prestamos.prestamo_recurso(usuario_actual)
        elif opcion_prestamos_devoluciones == "2":
            central_prestamos.devolucion_recurso()
        elif opcion_prestamos_devoluciones == "3":
            central_prestamos.mostrar_prestamo_usuario()
        elif opcion_prestamos_devoluciones == "4":
            central_prestamos.mostrar_prestamos_usuarios()
        elif opcion_prestamos_devoluciones == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# ... (código posterior)

if __name__ == "__main__":
    central_prestamos = CentralPrestamos()  
    login = Login()
    menu_principal(login, central_prestamos)