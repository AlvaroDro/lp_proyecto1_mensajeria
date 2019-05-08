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

def sobreescribir_archivo(path, dictionary):
    """Summary
    
    Args:
        path (String): Ruta donde se encuentra guardado el archivo ".json"
        dictionary (dict): Diccionario que tiene datos nuevos para ser agregados al archivo ".json" 
    """

    with open(path,'w') as file:
        json.dump(dictionary, file, sort_keys=True, indent=4)

def crearusuario(nombusu,contr,
                nombr,apell,
                direc,univ):
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
                "Apellido":"",
                "Dirrecion":"",
                "Casa estudio":"",
                "Usuario":"",
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
        sobreescribir_archivo(file_path, data_base)
    else:
        nueva_persona = cargar_archivo(file_path)
        nueva_persona.append(persona)
        sobreescribir_archivo(file_path, nueva_persona)

    input("Usuario agregado exitosamente, presione enter para continuar")


continuar = True # condicion para el bucle while True = continuar False = salir

while(continuar):

    print("Bienvenido al servicio de mensajeria")
    print("Presione 'a' si quiere iniciar sesion")
    print("Presione 'b' si quiere crear una nueva cuenta")
    print("Presione 'c' si quiere salir del servicio de mensajeria")

    opt = input("Digite su opcion: ")


    if opt == 'a':

        nombreini = input("ingrese su nombre de usuario")

        contraini = input("ingrese su password de usuario")

    elif opt == 'b':

        nombreusu = input("Ingrese su nombre de usuario\n")
        password = input("Ingrese su password de usuario\n")
        nombrereal = input("Ingrese su nombre\n")
        apellido = input("Ingrese su apellido\n")
        direccion = input("Ingrese su dirrecion\n")
        casaestudio = input("Ingrese su casa de estudio\n")
        
        crearusuario(nombreusu,password,
                    nombrereal,apellido,
                    direccion,casaestudio)

    elif opt == 'c':

        continuar = False

    else:

        print("Opcion no valida, ingrese una de las opciones mostradas")

        input("Presione enter para continuar")