import json
import os

ruta_del_archivo = "B_D/bd.json" #ruta donde se guardara el json

def cargar_archivo(ruta):
    """Summary
    
    Args:
        ruta (string): Ruta donde se encuentra guardado el archivo ".json"
    
    Returns:
        List: Retorna una lista de diccionarios 
    """

    
    if open(ruta).read() != '':
        with open(ruta) as archivo:
            contenido = json.load(archivo)
        return contenido
    else:
        datos="[]"
        with open(ruta, 'w') as archivo:
            json.dump(ruta, datos)

def sobrescribir_archivo(ruta, diccionario_con_datos_nuevos):
    """Summary
    
    Args:
        ruta (String): Ruta donde se encuentra guardado el archivo ".json"
        diccionario_con_datos_nuevos (dict): Diccionario que tiene datos nuevos para ser agregados al archivo ".json" 
    """

    with open(ruta, 'w') as archivo:
        json.dump(diccionario_con_datos_nuevos, archivo, sort_keys=True, indent=4)

def crear_usuario(nombre_usuario, password,
                nombre, apellido,
                direccion, universidad):
    """Summary
    
    Args:
        nombre_usuario (String): Nombre de usuario de la persona.
        password (String): Contraseña de la persona.
        nombre (String): Nombre real de la persona.
        apellido (String): Apellido de la persona.
        direccion (String): Dirección de la persona.
        universidad (String): Casa de estudio de la persona.
    """
    persona = {
                "Nombre":nombre,
                "Apellido":apellido,
                "Usuario":nombre_usuario,
                "Password":password,
                "Dirrecion":direccion,
                "Casa estudio":universidad,               
                "Bandeja de entrada":[] # o "Bandeja de entrada":[] verificar.{"Fuente":"","Asunto":"","Mensaje":""}.
                }

    nueva_persona = cargar_archivo(ruta_del_archivo)
    nueva_persona.append(persona)
    sobrescribir_archivo(ruta_del_archivo, nueva_persona)

    input("Usuario agregado exitosamente, presione enter para continuar")

def iniciar_sesion(nombre_usuario, contra_usuario, archivo):
    """Summary
    
    Args:
        nombre_usuario (String): Nombre del usuario
        contra_usuario (dict): Contraseña del usuario
        archivo (string): Ruta donde se encuentra guardado el archivo ".json"
    """
    cargardatos = cargar_archivo(archivo)
    for elemento in cargardatos:
        if nombre_usuario == elemento.get("Usuario") and contra_usuario == elemento.get("Password"):
            print("logeo exitoso")
            while True:
                print("Presione 'a' para entrar a la bandeja de entrada")
                print("Presione 'b' para redactar un mensaje")
                print("Presione 'c' para configurar su perfil")
                print("Presione 'd' para salir de la cuenta")
                opt = input("Digite su opcion: ")

                if opt == 'a':
                    print(elemento.get("Bandeja de entrada"))

                elif opt == 'b':
                    print("Ingrese el destinatario")
                    mensaje_destinatario = input("Ingrese el destinatario")
                    for usuarios in cargardatos:
                        if mensaje_destinatario.lower() in usuarios["Usuario"]:
                            indice = cargardatos.index(usuarios)
                            print(indice)
                            mensaje_asunto = input("Ingrese el asunto (opcional)")
                            mensaje_redactato = input("Escriba el mensaje")
                            mensaje = {"Asunto":mensaje_asunto,"Emisor":elemento.get("Usuario"),"Mensaje":mensaje_redactato}
                            cargardatos[indice]["Bandeja de entrada"].append(mensaje)

                            sobrescribir_archivo(ruta_del_archivo, cargardatos)
                            break


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

                            nueva_pass = input("Ingrese su nueva pass")
                            elemento["Password"] = nueva_pass.lower()
                            sobrescribir_archivo(ruta_del_archivo,cargardatos)
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
        iniciar_sesion(nombre_inicio,contra_inicio,ruta_del_archivo)
                

    elif opt == 'b':

#eliminar
       # nombre_usuario = input("Ingrese su nombre de usuario\n")
       # password = input("Ingrese su password de usuario\n")
        #nombre_real = input("Ingrese su nombre\n")
        #apellido = input("Ingrese su apellido\n")
       # direccion = input("Ingrese su dirrecion\n")
        #casa_de_estudio = input("Ingrese su casa de estudio\n")
        
       # crear_usuario(nombre_usuario,password,
        #            nombre_real,apellido,
         #           direccion,casa_de_estudio)
#eliminar/

        cargardatos = cargar_archivo(ruta_del_archivo)
        boleano = bool(1)
        nombre_usuario = input("Ingrese su nombre de usuario\n")
        for elemento in cargardatos:
            if nombre_usuario.lower() == elemento.get("Usuario"):
                print("ese nombre de usuario ya esta utilizado")
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


