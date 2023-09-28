#Contraseñas más complejas, aceptar nombre de usuario o no, incluso recomendar un nombre de usuario
#SE AGREGA EN LAS MEJORAS
#Menu para sign up and sign in
#Acceso al usuario con la contraña creada y bienvenida al sistema
#Numero de intentos maximos en caso de que el usuario sea correcto
#Mensajes de usuario no existe en caso de que el usuario no exista

import random

datos_usuario = []

def sistema():
    print("Bienvenido al sistema")

def menu():
    global datos_usuario
    while True:
        try:
            print("""******* Bievenido a nuestro blog *******

            1. Sign up
            2. Log in
            3. Salir
            
            """)
            menu_reply = int(input("Escoja una opción del menú: "))
            if menu_reply == 1:
                def sign_up():
                    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    lowercase = "abcdefghijklmnopqrstuvwxyz"
                    numbers = "1234567890"

                    user_try = None
                    user = None
                    tries = 0
                    sign_up = True

                    while sign_up:
                        tries += 1
                        user_try = input("Escribe un nombre de usuario: ")
                        length_valid = False
                        lowercase_valid = False
                        numbers_valid = False
                        capital_valid = False

                        if len(user_try) > 7 and len(user_try) < 16:
                            length_valid = True

                        for letter in user_try:
                            if letter in capital:
                                capital_valid = True
                            if letter in lowercase:
                                lowercase_valid = True
                        for number in user_try:
                            if number in numbers:
                                numbers_valid = True

                        if length_valid and capital_valid and lowercase_valid and numbers_valid:
                            print(f"El nombre de usuario {user_try} es valido")
                            user = user_try
                            datos_usuario.append(user)
                            sign_up = False
                        else:
                            if not length_valid:
                                if len(user_try) < 7:
                                    print("El nombre de usuario es demasiado corto, intente con uno más largo")
                                if len(user_try) > 16:
                                    print("El nombre de usuario es demasiado largo, intente con uno más corto")
                            elif not capital_valid:
                                print("El nombre de usuario debe tener por lo menos una letra mayúscula")
                            elif not lowercase_valid:
                                print("El nombre usuario debe tener por lo menos una letra minúscula")
                            if length_valid and capital_valid and lowercase_valid and not numbers_valid:
                                print("El nombre de usuario debe tener por lo menos un numero")
                                print(f"Intente con {user_try}{random.randint(1,100)}")
                        if tries > 5:
                            sign_up = False

                    if user:
                        print("Su nombre de usuario se ha establecido como: {}".format(user))
                        creating_password = True
                        tries = 0
                        password = None
                        print(f"\nPor favor {user} ahora establesca una contraseña:")
                        while creating_password:
                            tries += 1
                            password_try = input("Ingrese una contraseña: ")
                            capital_valid = False
                            lowercase_valid = False
                            numbers_valid = False
                            length_valid = False
                            
                            if len(password_try) > 7 and len(password_try) < 16:
                                length_valid = True
                            for letter in password_try:
                                if letter in capital:
                                    capital_valid = True
                                if letter in lowercase:
                                    lowercase_valid = True
                            for number in password_try:
                                if number in numbers:
                                    numbers_valid = True
                            if length_valid and capital_valid and lowercase_valid and numbers_valid:
                                password = password_try
                                print(f"La contraseña es valida, {password} se ha establecido como contraseña del usuario {user}")
                                datos_usuario.append(password)
                                creating_password = False
                            else:
                                if not length_valid:
                                    if len(password_try) < 7:
                                        print("La contraseña es demasiado corta, intente con una más larga")
                                    if len(password_try) > 16:
                                        print("La contraseña es demasiado larga, intente con una más corta")
                                elif not capital_valid:
                                    print("La contraseña debe tener por lo menos una letra mayúscula")
                                elif not lowercase_valid:
                                    print("La contraseña debe tener por lo menos una letra minúscula")
                                elif not numbers_valid:
                                    print("La contraseña debe tener por lo menos un numero")
                            if tries > 5:
                                print("Se ha bloqueado el sistema, no se ha podido establecer la contraseña")
                    else:
                        print("No se ha podido establecer el nombre de usuario por demasiados intentos")
                sign_up()
            if menu_reply == 2:
                def log_in():
                    log_in_user_try = True
                    tries = 0
                    while log_in_user_try:
                        print("Inicio de sesión: ")
                        print(datos_usuario)
                        print()
                        log_in_user = input("Ingrese el usuario:   ")
                        if log_in_user == datos_usuario[0]:
                            log_in_password = input("Ingrese su contraseña:  ")
                            if log_in_password == datos_usuario[1]:
                                sistema()
                                return
                            else:
                                tries += 1
                                print("Contraseña incorrecta")
                        else:
                            print("El usuario no existe, intente con otro")
                        if tries > 5:
                            print("Bloqueo por demasiados intentos, hemos mandado un correo de recuperación")
                log_in()
            if menu_reply == 3:
                print("Salio del sistema")
                return
        except ValueError or int(menu_reply) > 3:
            print("Escoja una opción del menú validad")
menu()