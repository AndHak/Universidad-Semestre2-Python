from string import punctuation

def password_valid(password):

    if len(password) < 6 or len(password) > 12:
        print("La contraseña debe tener entre 6 y 12 carácteres")
    elif not any([letra.isdigit() for letra in password]):
        print("La contraseña debe tener al menos un dígito")
    elif not any([letra.islower() for letra in password]):
        print("La contraseña debe tener al menos una letra minúscula")
    elif not any([letra.isupper() for letra in password]):
        print("La contraseña debe tener al menos una letra mayúscula")
    elif not any([True if letra in punctuation else False for letra in password]):
        print("La contraseña debe tener al menos un carácter especial")
    else:
        print("La contraseña se ha establecido correctamente")
        return True
    return False


password = input("Contraeña: ")
password_valid(password)