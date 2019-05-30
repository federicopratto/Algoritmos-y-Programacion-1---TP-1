from datos_prueba         import *
from funciones_validacion import *
from funciones_busqueda   import *
from funciones_carga      import *


#Defino la biblioteca vacia donde se almacenaran los datos de usuario
datos_usuarios = {}

#Esta funcion se encarga de verificar si el usuario desea contestar un mensaje recibido o no
def contestar_mensajes(usuario_actual, usuario, datos_usuarios):
    contestar = input("¿Deseas contestar? (S/N): ").upper()
    if contestar == "S":
        mensajes_anteriores = datos_usuarios[usuario_actual]["Mensajes"][usuario][1]
        nuevo_mensaje = input("Mensaje: ")
        nuevo_mensaje = mensajes_anteriores + "@"+usuario_actual+": "+nuevo_mensaje+"\n"
        datos_usuarios[usuario_actual]["Mensajes"][usuario] = [False, nuevo_mensaje]
        datos_usuarios[usuario]["Mensajes"][usuario_actual] = [True, nuevo_mensaje]


#Esta funcion muestra los mensajes que los usuarios se enviaron entre si cuando hay mensajes nuevos.
def mostrar_mensajes(usuario_actual, datos_usuarios):
    for usuario in datos_usuarios[usuario_actual]["Mensajes"]:
        if datos_usuarios[usuario_actual]["Mensajes"][usuario][0]:
            print("\nTienes mensajes sin leer de @{0}\n".format(usuario))
            print(datos_usuarios[usuario_actual]["Mensajes"][usuario][1])
            datos_usuarios[usuario_actual]["Mensajes"][usuario][0] = False
            contestar_mensajes(usuario_actual, usuario, datos_usuarios)


''' Funciones correspondientes al Menu Principal    '''
# Esta funcion muestra el menu principal cada vez que el usuario finalice una accion
def presentacion_menu_principal():
    print("╔═══════════════════════════════════════════════╗")
    print("║ »»»»»»»»»»»» Bienvenido a Tender «««««««««««« ║")
    print("╠═══════════════════════════════════════════════╣")
    print("║¿Que desea hacer?                              ║")
    print("║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║")
    print("║ 1- Cargar un grupo de personas predeterminado ║")
    print("║ 2- Cargar una nueva persona                   ║")
    print("║ 3- Ingresar al sistema                        ║")
    print("║ 4- Finalizar aplicación                       ║")
    print("║                                               ║")
    print("╚═══════════════════════════════════════════════╝")
    eleccion = int(input("»» Opcion elegida: "))
    return eleccion


#Esta funcion llama a las funciones necesarias para ejecutar el menu principal
def menu_principal():
    seguir = True
    while(seguir):
        eleccion = presentacion_menu_principal()
        seguir = validar_menu_principal(eleccion)
    return eleccion



''' Cuerpo principal del programa   '''
eleccion = menu_principal()
while(eleccion != 4):
    # Carga de usuarios de prueba
    if eleccion == 1:
        datos_usuarios = cargar_usuarios_de_prueba(datos_usuarios)
    # Carga de nuevo usuario.
    elif eleccion == 2:
        cargar_nuevo_usuario(datos_usuarios)
    # Busqueda entre usuarios.
    else:
        if datos_usuarios != {}:
            usuario_actual = ingresar_a_sistema(datos_usuarios)
            coincidencias = realizar_busqueda(usuario_actual, datos_usuarios)
            mostrar_mensajes(usuario_actual, datos_usuarios)
            mostrar_coincidencias(coincidencias, datos_usuarios, usuario_actual)
        else:
            print("No hay usuarios cargados en la base de datos.")
    eleccion = menu_principal()
