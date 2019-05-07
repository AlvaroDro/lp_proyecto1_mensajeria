import json
import os

file_path = "B_D/bd.json" #ruta donde se guardara el json

def cargar_archivo(path):
    """Summary
    
    Args:
        path (string): Ruta donde se encuentra guardado el archivo ".json"
    
    Returns:
        List: Retorna una lista de diccionarios 
    """

    with open(path) as archivo:
        contenido = json.load(archivo)
    return contenido

def sobrescribir_archivo(path, dictionary):
    """Summary
    
    Args:
        path (String): Ruta donde se encuentra guardado el archivo ".json"
        dictionary (dict): Diccionario que tiene datos nuevos para ser agregados al archivo ".json" 
    """

    with open(path, 'w') as file:
        json.dump(dictionary, file, sort_keys=True, indent=4)

def crear_usuario(nombusu, contr,
                nombr, apell,
                direc, univ):
    """Summary
    
    Args:
        nombusu (String): Nombre de usuario de la persona.
        contr (String): Contraseña de la persona.
        nombr (String): Nombre real de la persona.
        apell (String): Apellido de la persona.
        direc (String): Dirección de la persona.
        univ (String): Casa de estudio de la persona.
    """
    persona = {
                "Nombre":"",
                "Usuario":"",
                "Dirrecion":"",
                "Casa estudio":"",
                "Apellido":"",
                "Password":"",
                "Bandeja de entrada":[{"Fuente":"","Asunto":"","Mensaje":""}] # o "Bandeja de entrada":[] verificar.
                }

    persona["Usuario"] = nombusu
    persona["Password"] = contr
    persona["Nombre"] = nombr
    persona["Apellido"] = apell
    persona["Dirrecion"] = direc
    persona["Casa estudio"] = univ

    data_base = [] 
    if open(file_path).read() == '':
        data_base.append(persona)
        sobrescribir_archivo(file_path, data_base)
    else:
        nueva_persona = cargar_archivo(file_path)
        nueva_persona.append(persona)
        sobrescribir_archivo(file_path, nueva_persona)

    input("Usuario agregado exitosamente, presione enter para continuar")

def iniciar_sesion(nombreu, contrau, file):
    """Summary
    
    Args:
        nombreu (String): Nombre del usuario
        contrau (dict): Contraseña del usuario
        file (string): Ruta donde se encuentra guardado el archivo ".json"
    """
    cargardatos = cargar_archivo(file)
    for elemento in cargardatos:
        if nombreu == elemento.get("Usuario") and contrau == elemento.get("Password"):
            print("logeo exitoso")
            while True:
                print("Presione 'a' para entrar a la bandeja de entrada")
                print("Presione 'b' para redactar un mensaje")
                print("Presione 'c' para configurar su perfil")
                print("Presione 'd' para salir de la cuenta")
                opt = input("Digite su opcion: ")

                if opt == 'a':
                    print("hola")

                elif opt == 'b':
                    print("hola")

                elif opt == 'c':
                    while True:
                        print("Presione 'a' para configurar su password")
                        print("Presione 'b' para configurar su nombre")
                        print("Presione 'c' para configurar su apellido")
                        print("Presione 'd' para configurar su direccion")
                        print("Presione 'e' para configurar su casa de estudio")
                        print("Presione 'f' para salir de la configuracion y volver al menu de usuario")
                        opc = input("Digite su opcion: ")
                        if opc == 'a':
                             print("hola")
                        elif opc == 'b':
                            print("hola")
                        elif opc == 'c':
                            print("hola")
                        elif opc == 'd':
                            print("hola")
                        elif opc == 'e':
                            print("hola")
                        elif opc == 'f':
                	        print("Saliendo al menu de usuario")
                	        break
                        else:
                            print("Opcion no valida, ingrese una de las opciones mostradas")

                elif opt == 'd':
                    print("Saliendo de la cuenta...")
                    return bool('true')
                    break
                    
                else:
                    print("Opcion no valida, ingrese una de las opciones mostradas")

    else:
        print("Error de inicio de sesion, volviendo al menu principal")
    return bool()


continuar = True # condicion para el bucle while True = continuar False = salir



while(continuar):

    print("Bienvenido al servicio de mensajeria")
    print("Presione 'a' si quiere iniciar sesion")
    print("Presione 'b' si quiere crear una nueva cuenta")
    print("Presione 'c' si quiere salir del servicio de mensajeria")

    opt = input("Digite su opcion: ")


    if opt == 'a':

        nombre_inicio = input("Ingrese su nombre de usuario\n")
        contra_inicio = input("ingrese su password de usuario\n")
        iniciar_sesion(nombre_inicio,contra_inicio,file_path)
                

    elif opt == 'b':

        cargardatos = cargar_archivo(file_path)
        boleano = bool(1)
        nombre_usuario = input("Ingrese su nombre de usuario\n")
        for elemento in cargardatos:
            if nombre_usuario == elemento.get("Usuario"):
                print("ese nombre de usuario ya esta utilizado")
                print("si ingreso admin no puedes ingresar este nombre, ya que, solo se le permite a los administradores")
                boleano=bool(0)
        if boleano:
            password = input("Ingrese su password de usuario\n")
            nombre_real = input("Ingrese su nombre\n")
            apellido = input("Ingrese su apellido\n")
            direccion = input("Ingrese su dirrecion\n")
            casa_de_estudio = input("Ingrese su casa de estudio\n")
            crear_usuario(nombre_usuario, password,
                          nombre_real, apellido,
                          direccion, casa_de_estudio) 

        

    elif opt == 'c':

        continuar = False

    else:

        print("Opcion no valida, ingrese una de las opciones mostradas")

        input("Presione enter para continuar")