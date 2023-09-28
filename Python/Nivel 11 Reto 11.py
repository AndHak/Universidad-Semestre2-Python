#Contraseñas más complejas, aceptar nombre de usuario o no, incluso recomendar un nombre de usuario

import random

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

