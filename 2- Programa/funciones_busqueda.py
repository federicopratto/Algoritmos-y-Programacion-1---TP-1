from funciones_carga import *

#Esta funcion carga y verifica los rangos de edad a buscar
def rango_edad_busqueda():
    seguir = True
    i = 0
    rango_edad = [0, 0]
    mensaje = ["minima", "maxima"]
    print("\nIngrese rango de edades:\n")
    while seguir:
        if i == 2:
            seguir = False
        else:
            rango_edad[i] = int(input("-Edad {}: ".format(mensaje[i])))
            if rango_edad[i] < 18 or rango_edad[i] > 99:
                print("\n* Edad invalida, minimo 18 años y maximo 99 años *\n")
            else:
                i += 1
    return rango_edad


#Esta funcion llama a las funciones encargadas de cargar los datos para la busqueda.
def datos_para_busqueda(usuario_actual):
    print("\n¡Hola @{}! Hagamos una busqueda".format(usuario_actual))
    distancia = cargar_radio_busqueda()
    sexo = cargar_sexo_busqueda()
    rango_edad = rango_edad_busqueda()
    return distancia, sexo, rango_edad


#Esta funcion calcula la distancia entre dos usuarios.
def calcular_distancia(coordenadas_1, coordenadas_2):
    import geopy.distance
    distancia = round(geopy.distance.geodesic(coordenadas_1, coordenadas_2).kilometers, 2)
    return distancia


#Esta funcion compara las distancias entre dos usuarios con el rango buscado por el usuario actual
def comparar_distancias(usuario, usuario_actual, datos_usuarios, criterios_de_busqueda):
    coordenadas_1 = datos_usuarios[usuario_actual]["Ubicacion"]
    coordenadas_2 = datos_usuarios[usuario]["Ubicacion"]
    distancia = calcular_distancia(coordenadas_1, coordenadas_2)
    if distancia > criterios_de_busqueda[0]:
        return False, distancia
    return True, distancia


#Esta funcion compara el sexo de un usuario con el sexo buscado por el usuario actual
def comparar_sexos(usuario, datos_usuarios, criterios_de_busqueda):
    sexo = datos_usuarios[usuario]["Sexo"]
    if criterios_de_busqueda[1] == 3 or criterios_de_busqueda[1] == sexo:
        return True
    return False


#Esta funcion compara la edad de un usario con el rango de edades buscado por el usuario actual.
def comparar_edades(usuario, datos_usuarios, criterios_de_busqueda):
    edad = datos_usuarios[usuario]["Edad"]
    edad_min = criterios_de_busqueda[2][0]
    edad_max = criterios_de_busqueda[2][1]
    if edad_min < edad < edad_max:
        return True
    return False


#Esta funcion compara los intereses entre usuarios y calcula el porcentaje de interes.
def comparar_intereses(usuario, usuario_actual, datos_usuarios):
    intereses_en_comun = []
    for interes in datos_usuarios[usuario_actual]["Intereses"]:
        if interes in datos_usuarios[usuario]["Intereses"]:
            intereses_en_comun.append(interes)
    cant_intereses_1 = len(datos_usuarios[usuario_actual]["Intereses"])
    cant_intereses_2 = len(datos_usuarios[usuario]["Intereses"])
    porcentaje_de_interes = round(100*(len(intereses_en_comun)/(cant_intereses_1+cant_intereses_2)))
    return porcentaje_de_interes


#Esta funcion busca entre los usuarios del sistema los que coinciden con los criterios del actual
# y devuelve un listado de coincidencias
def realizar_busqueda(usuario_actual, datos_usuarios):
    criterios_de_busqueda = datos_para_busqueda(usuario_actual)
    coincidencias = []
    for usuario in datos_usuarios:
        if usuario_actual != usuario:
            seguir, distancia = comparar_distancias(usuario, usuario_actual, datos_usuarios, criterios_de_busqueda)
            if seguir:
                if comparar_sexos(usuario, datos_usuarios, criterios_de_busqueda):
                    if comparar_edades(usuario, datos_usuarios, criterios_de_busqueda):
                        intereses = comparar_intereses(usuario, usuario_actual, datos_usuarios)
                        coincidencias.append([usuario, distancia, intereses])
    if coincidencias != []: coincidencias.sort(key=lambda x: x[1])
    return coincidencias


#Esta funcion consulta al usuario si esta interesado o no en un usuario y lo agregar a sus Likes
def tomar_like_user(datos_usuarios, usuario_actual, user):
    interes = input("¿Estas interesado en este perfil?(S/N): ").upper()
    if interes == "S":
        datos_usuarios[usuario_actual]["Likes"][user] = True
    else:
        datos_usuarios[usuario_actual]["Likes"][user] = False


#Esta funcion muestra las coincidencias que hubo al realizar una busqueda.
def mostrar_coincidencias(coincidencias, datos_usuarios, usuario_actual):
    seguir = True
    i = 0
    print("\nResultados de la busqueda:")
    if coincidencias != []:
        while(seguir):
            print("\nUsuario: @{}".format(coincidencias[i][0]))
            print("Edad: {} años".format(datos_usuarios[coincidencias[i][0]]["Edad"]))
            print("Distancia: {} km".format(coincidencias[i][1]))
            print("Porcentaje de coincidencia: {}%\n".format(coincidencias[i][2]))
            tomar_like_user(datos_usuarios, usuario_actual, coincidencias[i][0])
            mandar_primer_mensaje(datos_usuarios, usuario_actual, coincidencias[i][0])
            i, seguir = seguir_viendo_coincidencias(i, seguir)
    else:
        print("\nNingun usuario encontrado. Intente mas tarde.\n")


#Esta funcion pregunta al usuario si desea ver mas coincidencias o salir al menu principal.
def seguir_viendo_coincidencias(i, seguir):
    eleccion = int(input("\n¿Que desea hacer?\n1- Ver mas coincidencias\n2- Salir\n\nOpcion elegida: "))
    if eleccion == 1:
        i += 1
    else:
        seguir = False
    return i, seguir


#Esta funcion verifica si ha habido match entre usuarios, y solicita al actual que mande un mensaje
#a modo de saludo.
def mandar_primer_mensaje(datos_usuarios, usuario_actual, user):
    if usuario_actual in datos_usuarios[user]["Likes"]:
        if datos_usuarios[usuario_actual]["Likes"][user] and datos_usuarios[user]["Likes"][usuario_actual]:
            if user not in datos_usuarios[usuario_actual]["Mensajes"]:
                print("\nFelicidades, @{0} tambien te dio like, enviale un mensaje".format(user))
                mensaje = input("Mensaje: ")
                mensaje = "@"+usuario_actual+": "+mensaje+"\n"
                datos_usuarios[usuario_actual]["Mensajes"][user] = [False, mensaje]
                datos_usuarios[user]["Mensajes"][usuario_actual] = [True, mensaje]
