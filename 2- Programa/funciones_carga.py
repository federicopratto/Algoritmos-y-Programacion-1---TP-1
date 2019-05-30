from funciones_validacion import *

#Funcion para cargar usuarios predeterminados.
def cargar_usuarios_de_prueba(datos_usuarios):
    import datos_prueba
    datos_usuarios = datos_prueba.cargar_personas_predeterminadas(datos_usuarios)
    return datos_usuarios


#Esta funcion se encarga de pedir al usuario su sexo
#Esta funcion no se valida, se supone que aca el usuario no se va a equivocar.
def ingresar_sexo():
    print("\n¿Cual es su sexo?\n- Femenino (F)\n- Masculino (M)\n- Otro (O)\n")
    sexo = input("Opcion elegida: ").upper()
    return sexo


#Esta función se encarga de cargar un nuevo pseudonimo de usuario.
def cargar_pseudonimo(datos_usuarios):
    seguir = True
    while(seguir):
        pseudo = input("Ingrese un pseudonimo (Solo minúsculas, números y guiones bajos): ")
        seguir = validar_pseudonimo(pseudo, datos_usuarios)
    return pseudo


#Esta funcion se encarga de solicitar al usuario una contraseña
def cargar_contraseña():
    seguir = True
    while(seguir):
        print("\nIngrese una contraseña. La misma debera tener como minimo:\n")
        print("- Una mayúscula\n- Una minúscula\n- Un dígito decimal\n- Un largo de 5 o mas caracteres\n")
        contraseña = input("Contraseña: ")
        seguir = validar_contraseña(contraseña)
    return contraseña


#Esta función carga y verifica la edad del usuario.
def ingresar_edad():
    seguir = True
    while(seguir):
        edad = int(input("\nIngrese su edad (18 a 99): "))
        if(18<=edad<=99):
            seguir = False
        else:
            print("\n* ¡Edad incorrecta. Intente de nuevo! *")
    return edad


#Esta funcion carga la ubicacion del usuario
def cargar_ubicacion():
    import geopy
    from geopy.geocoders import Nominatim
    geolocator = geopy.Nominatim(user_agent="specify_your_app_name_here")
    print("\nIngrese su dirección actual")
    print("Ej: Avenida Corrientes 600, Buenos Aires\n")
    direccion = geolocator.geocode(input("Direccion: "))
    latitud = direccion.latitude
    longitud = direccion.longitude
    return latitud, longitud


#Esta funcion permite cargar los intereses del usuario.
def cargar_intereses():
    print("\nIngrese sus intereses separados por coma y espacio.")
    print("Ej: futbol, cafe con leche, bailar, queso cheddar")
    intereses = input("\nIntereses: ").replace(" ", "-").split(",-")
    return intereses


#Esta funcion llama a las funciones necesarias para crear un nuevo usuario.
def cargar_nuevo_usuario(datos_usuarios):
    nuevo_usuario = {}
    nuevo_usuario["Nombre"] = input("\nIngrese su nombre: ").capitalize()
    nuevo_usuario["Apellido"] = input("Ingrese su apellido: ").capitalize()
    pseudo = cargar_pseudonimo(datos_usuarios)
    nuevo_usuario["Contraseña"] = cargar_contraseña()
    nuevo_usuario["Sexo"] = ingresar_sexo()
    nuevo_usuario["Edad"] = ingresar_edad()
    nuevo_usuario["Ubicacion"] = cargar_ubicacion()
    nuevo_usuario["Intereses"] = cargar_intereses()
    nuevo_usuario["Likes"] = {}
    nuevo_usuario["Mensajes"] = {}
    datos_usuarios[pseudo] = nuevo_usuario
    print("\n"
          "╔════════════════════════════════════════════════╗")
    print("║ * Ya estas registrado. ¡Bienvenido a Tender! * ║")
    print("╚════════════════════════════════════════════════╝\n")
    return datos_usuarios


#Esta funcion solicita los datos para ingresar al sistema.
def ingresar_a_sistema(datos_usuarios):
    seguir = True
    while(seguir):
        usuario = input("\nIngrese su nombre de usuario: ").lower()
        clave = input("Ingrese su clave: ")
        seguir = validar_datos_de_ingreso(usuario, clave, datos_usuarios)
    return usuario


#Esta funcion carga y verifica que el radio de busqueda sea valido.
def cargar_radio_busqueda():
    seguir = True
    while(seguir):
        distancia = float(input("\nIngrese el radio maximo de busqueda (km): "))
        if(0 > distancia or distancia > 20000):
            print("\n* Distancia invalida, vuelva a intentarlo. *")
        else:
            seguir = False
    return distancia


#Esta funcion carga y verifica que el sexo a buscar sea valido.
def cargar_sexo_busqueda():
    seguir = True
    while(seguir):
        print("\nIngrese el sexo de interes:\n\n1- Hombres\n2- Mujeres\n3- Ambos\n")
        sexo = int(input("Opcion elegida: "))
        if sexo not in [1, 2, 3]:
            print("\n* Opcion invalida, vuelva a intentarlo. *")
        else:
            if sexo == 1: sexo = "M"
            elif sexo == 2: sexo = "F"
            seguir = False
    return sexo