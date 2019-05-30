#Esta funcion verifica si el pseudonimo ingresado para un nuevo usuario es valido.
def validar_pseudonimo(pseudo, datos_usuarios):
    if pseudo in datos_usuarios:
        print("\n* ¡El nombre de usuario ingresado ya se encuentra en uso. Por favor seleccione otro! *\n")
        return True
    else:
        prueba = pseudo.replace("_", "")
        if prueba.islower() and prueba.isalnum():
            return False
        else:
            print("\n* ¡Hay caracteres invalidos en el pseudonimo. Vuelva a intentarlo! *\n")
            return True


#Esta función verifica cuantas mayusculas, minusculas y numeros tiene la contraseña
def contar_caracteres_contraseña(contraseña):
    mayusculas, minusculas, digitos = 0, 0, 0
    for caracter in contraseña:
        if caracter.isdigit():
            digitos += 1
        elif caracter.isalpha():
            if caracter.islower():
                minusculas += 1
            elif caracter.isupper():
                mayusculas += 1
    return mayusculas, minusculas, digitos


#Esta función verifica si la contraseña ingresada es valida
def validar_contraseña(contraseña):
    if len(contraseña) >= 5:
        caracteres = contar_caracteres_contraseña(contraseña)
        if (0 not in caracteres):
            return False
    print("\n* ¡La contraseña ingresada no cumple los requisitos! *")
    return True


#Esta funcion convalida si los datos de ingreso son correctos.
def validar_datos_de_ingreso(usuario, clave, datos_usuarios):
    if usuario not in datos_usuarios:
        print("\n* Usuario invalido, vuelva a ingresar los datos *")
        return True
    elif datos_usuarios[usuario]["Contraseña"] != clave:
        print("\n* Clave invalida, vuelva a ingresar los datos *")
        return True
    else:
        return False


#Esta funcion validara si la eleccion hecha por el usuario en el menu principal es correcta
def validar_menu_principal(eleccion):
    if(eleccion not in [1, 2, 3, 4, 5]):
        print("╔═══════════════════════════════════════════════╗")
        print("║*****Opcion invalida. Vuelva a intentarlo******║")
        print("╚═══════════════════════════════════════════════╝")
        return True
    return False