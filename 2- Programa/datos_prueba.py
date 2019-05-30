# Esta función carga en un diccionario los usuarios de prueba
def cargar_personas_predeterminadas(datos_usuarios):
    if "agustinaf19" not in datos_usuarios:
        # Cargo persona de prueba 1
        datos_usuarios["agustinaf19"] = {"Nombre": "Agustina",
                                         "Apellido": "Fernandez",
                                         "Contraseña": "Agus18",
                                         "Sexo": "F",
                                         "Edad": 19,
                                         "Ubicacion": (-34.591059, -58.396550),
                                         "Intereses": ["leer", "star-wars", "rock", "autos", "breaking-bad"],
                                         "Likes": {},
                                         "Mensajes": {}}

        # Cargo persona de prueba 2
        datos_usuarios["aidagomez26"] = {"Nombre": "Adriana",
                                         "Apellido": "Gomez",
                                         "Contraseña": "Volar09",
                                         "Sexo": "F",
                                         "Edad": 26,
                                         "Ubicacion": (-34.601629, -58.387618),
                                         "Intereses": ["motos", "gym", "crossfit"],
                                         "Likes": {},
                                         "Mensajes": {}}

        # Cargo persona de prueba 3
        datos_usuarios["ale_canalla22"] = {"Nombre": "Alejandro",
                                           "Apellido": "Castillo",
                                           "Contraseña": "Fulbo5",
                                           "Sexo": "M",
                                           "Edad": 45,
                                           "Ubicacion": (-34.615338, -58.370698),
                                           "Intereses": ["paulo-cohelo", "lectura-infantil", "cuentos-de-niños"],
                                           "Likes": {},
                                           "Mensajes": {}}

        # Cargo persona de prueba 4
        datos_usuarios["natu325"] = {"Nombre": "Natalia",
                                     "Apellido": "Acosta",
                                     "Contraseña": "natuCapa5",
                                     "Sexo": "F",
                                     "Edad": 32,
                                     "Ubicacion": (-34.619295, -58.387451),
                                     "Intereses": ["gym", "crossfit", "leer", "computacion", "deportes"],
                                     "Likes": {},
                                     "Mensajes": {}}

        # Cargo persona de prueba 5
        datos_usuarios["marce_blanco"] = {"Nombre": "Marcelo",
                                          "Apellido": "Blanco",
                                          "Contraseña": "d4ygAe3",
                                          "Sexo": "M",
                                          "Edad": 26,
                                          "Ubicacion": (-34.611784, -58.388969),
                                          "Intereses": ["star-wars", "buenos-aires", "python", "C"],
                                          "Likes": {},
                                          "Mensajes": {}}

        # Cargo persona de prueba 6
        datos_usuarios["angellucho25"] = {"Nombre": "Angel",
                                          "Apellido": "Rodriguez",
                                          "Contraseña": "Contraseña123",
                                          "Sexo": "M",
                                          "Edad": 18,
                                          "Ubicacion": (-34.590444, -58.434735),
                                          "Intereses": ["dibujar", "arte", "pintura", "van-gogh"],
                                          "Likes": {},
                                          "Mensajes": {}}

        # Cargo persona de prueba 7
        datos_usuarios["ariel_river_89"] = {"Nombre": "Ariel",
                                            "Apellido": "Ramirez",
                                            "Contraseña": "Ari178",
                                            "Sexo": "M",
                                            "Edad": 38,
                                            "Ubicacion": (-34.599387, -58.441578),
                                            "Intereses": ["deportes", "river", "futbol", "carp"],
                                            "Likes": {},
                                            "Mensajes": {}}

        # Cargo persona de prueba 8
        datos_usuarios["bobesponjacuadrada"] = {"Nombre": "Patricio",
                                                "Apellido": "Gordillo",
                                                "Contraseña": "Nick59",
                                                "Sexo": "M",
                                                "Edad": 27,
                                                "Ubicacion": (-34.609448, -58.432638),
                                                "Intereses": ["tomar-agua", "caracoles", "reir", "hacer-hamburguesas"],
                                                "Likes": {},
                                                "Mensajes": {}}

        # Cargo persona de prueba 9
        datos_usuarios["cardomili"] = {"Nombre": "Milagros",
                                       "Apellido": "Cardoso",
                                       "Contraseña": "MiliC08",
                                       "Sexo": "F",
                                       "Edad": 37,
                                       "Ubicacion": (-34.615566, -58.361128),
                                       "Intereses": ["game-of-thrones", "netflix", "breaking-bad", "south-park"],
                                       "Likes": {},
                                       "Mensajes": {}}

        # Cargo persona de prueba 10
        datos_usuarios["emiliagot"] = {"Nombre": "Emilia",
                                       "Apellido": "Cardoso",
                                       "Contraseña": "Got2019",
                                       "Sexo": "F",
                                       "Edad": 27,
                                       "Ubicacion": (-34.570926, -58.430834),
                                       "Intereses": ["porno-checo", "hemoerotismo-interracial", "fisting", "asiatico"],
                                       "Likes": {},
                                       "Mensajes": {}}
        print("\n"
              "╔═══════════════════════════════════════════════╗")
        print("║ »»»»»» Usuarios cargados correctamente «««««« ║")
        print("╚═══════════════════════════════════════════════╝")
    else:
        print("\n"
              "╔═══════════════════════════════════════════════╗")
        print("║ »»»»» Los usuarios ya estaban cargados «««««« ║")
        print("╚═══════════════════════════════════════════════╝")
    return datos_usuarios