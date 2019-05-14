import json
import os
                                                                           
ruta_del_archivo = "B_D/bd.json" #ruta donde se encuentra el JSON

def cargar_archivo(ruta):
    """
    Carga todos los datos del archivo JSON en la variable contenido 
    y esta es retornada.


    Argumentos:
        ruta (string): Ruta donde se encuentra guardado el archivo JSON
    
    Retorna:
        list: Retorna una lista de diccionarios con los datos que 
        contiene el archivo JSON.

    """ 
    if len(ruta) != 0:
        with open(ruta) as archivo:
            contenido = json.load(archivo)
        return contenido
    else:
        datos = "[]"
        with open(ruta, 'w') as archivo:
            json.dump(ruta, datos)


def sobrescribir_archivo(ruta, diccionario_con_datos_nuevos):
    """
    Abre el archivo JSON y sobrescribe el archivo con 
    los datos del diccionario que se le entrega como parametro.
    
    Argumentos:
        ruta (String): Ruta donde se encuentra guardado el archivo
        JSON.

        diccionario_con_datos_nuevos (dict): Diccionario que tiene
        datos nuevos para ser agregados al archivo JSON.

    """

    with open(ruta, 'w') as archivo:
        json.dump(diccionario_con_datos_nuevos, archivo, indent=4)

def listar_usuarios():
    """Crea una lista con todos los nombres de usuarios dentro del
    archivo JSON. 

    Retorna:
        list: Retorna una lista con todos los nombres de usuarios
        que esten en el archivo JSON.

    """
    lista_usuarios = []
    for elementos in cargar_archivo(ruta_del_archivo):
        lista_usuarios.append(elementos.get("Usuario").lower())
    return lista_usuarios

def crear_usuario(nombre_usuario, password,
                  nombre, apellido,
                  direccion, universidad):
    """
    Toma los parametros y crea un diccionario con esos datos
    que se guardan en la variable persona , la cual es añadida
    a la lista de diccionarios del archivo JSON en la variable
    nueva_persona  y sobrescribe el archivo JSON con estos datos.
    
    Argumentos:

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
                "Bandeja de entrada":[] 
                }                       
                						
    nueva_persona = cargar_archivo(ruta_del_archivo)
    nueva_persona.append(persona)
    sobrescribir_archivo(ruta_del_archivo, nueva_persona)

    print("Usuario agregado exitosamente, presione enter para continuar")


def vista_de_sesion(indice_cuenta):
    """Muestra todas las opciones para la cuenta que inicio sesion
    utilizando su indice como referncia, las opciones que se despligan
    son las siguientes:  

    a) Bandeja de entrada: Opcion para visualizar los mensajes 
        recibidos, los cuales puede responder o eliminar.

    b) Redactar un mensaje: Envio de mensajes a los usuarios
        de la aplicacion.

    c) Configurar perfil: Opcion para cambiar la informacion
        de la cuenta del usuario.

    d) salir de la cuenta.

    Argumentos:
        indice_cuenta (String): indice del nombre de usuario con el que
                                inicio sesion.

    """
    cargar_datos = cargar_archivo(ruta_del_archivo)
    while True:
        print("Presione 'a' para entrar a la bandeja de entrada")
        print("Presione 'b' para redactar un mensaje")
        print("Presione 'c' para configurar su perfil") 
        print("Presione 'd' para salir de la cuenta")
        opcion = input("Digite su opcion: ")

        if opcion == 'a':
            bandeja = cargar_datos[indice_cuenta].get("Bandeja de entrada")

            while True:
                if len(bandeja) == 0:
                    print(
                        "No tiene, ningun nuevo mensaje, volviendo al menu "+
                        "de usuario...")
                    break

                else:

                    i = 1
                    print("\nMensajes recibidos")

                    for elementos in bandeja:

                    	print("Mensaje nº",i,"\nFuente: "+elementos.get(
                    		"Emisor")+"\tAsunto: "+elementos.get("Asunto"),
                    	"\n\nMensaje:\n"+elementos.get("Mensaje")+"\n")

                    	i=i+1

                    break

            if len(bandeja) != 0:

                while True:

                    print("a.-Eliminar mensaje")
                    print("b.-Responder")
                    print("c.-Salir al menu de usuario")
                    opcion = input("")
                    opcion = opcion.lower()

                    if opcion == "a":

                        eliminar_mensaje = input("Ingrese el numero del"+" mensaje a eliminar: ")

                        if not eliminar_mensaje.isdigit():
                            print("ingrese valores correctos para eliminar")
                            continue

                        elif (int(eliminar_mensaje) <= 0 or 
                             int(eliminar_mensaje) > len(bandeja)):

                            print("ingrese valores correctos para eliminar")
                            continue

                        else:
                            eliminar_mensaje = int(eliminar_mensaje) - 1
                            cargar_datos[indice_cuenta]["Bandeja de"+
                            " entrada"].pop(int(eliminar_mensaje))

                            print("Mensaje eliminado correctamente")
                            sobrescribir_archivo(ruta_del_archivo,
                            					 cargar_datos)   

                    elif opcion =="b":

                        responder_mensaje = input("Ingrese el numero del "+
                        	"mensaje a responder: ")
                        if not responder_mensaje.isdigit():
                            print("ingrese valores correctos para responder"+
                            " un mensaje")
                            continue

                        if (int(responder_mensaje) <= 0 or 
                            int(responder_mensaje) > len(bandeja)):

                            print("ingrese valores correctos para responder"+
                            " un mensaje")
                            continue

                        responder_mensaje = int(responder_mensaje) - 1
                        persona_a_responder = bandeja[
                                                      int(responder_mensaje)
                                                     ].get("Emisor")

                        if persona_a_responder in listar_usuarios():
                            indice = listar_usuarios().index(
                        	                             persona_a_responder)
                        mensaje_asunto = input("Ingrese el asunto "+
                        	"(opcional): ")

                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,
                                    "Emisor":cargar_datos[
                                                          indice_cuenta
                                                         ].get("Usuario"),
                                    "Mensaje":mensaje_redactato
                                  }
                        cargar_datos[indice]["Bandeja de entrada"].append(mensaje)
                        sobrescribir_archivo(ruta_del_archivo, cargar_datos)
                    elif opcion == "c":
                        break
                    else:
                        print("No ingreso ninguna opcion valida")
                        continue

                    break

        elif opcion == 'b': 
            print("Posibles destinatarios: ",listar_usuarios())

            lista = listar_usuarios()

            mensaje_destinatario = input("Ingrese el destinatario: ")

            if mensaje_destinatario.lower() in lista:

                for usuarios in cargar_datos:

                    if mensaje_destinatario in usuarios["Usuario"]:

                        indice = cargar_datos.index(usuarios)
                        mensaje_asunto = input("Ingrese el asunto "+
                        	"(opcional): ")
                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,
                                   "Emisor":cargar_datos[
                                                         indice_cuenta
                                                        ].get("Usuario"),
                                   "Mensaje":mensaje_redactato
                                   }
                        cargar_datos[indice]["Bandeja de entrada"].append(
                        	mensaje)

                        sobrescribir_archivo(ruta_del_archivo, cargar_datos)  
            else:
                print("Destinatario no existente, volviendo al menu de"+
                " usuario...")


        elif opcion == 'c':

            while True:
                print("Presione 'a' para configurar su password")
                print("Presione 'b' para configurar su nombre")
                print("Presione 'c' para configurar su apellido")
                print("Presione 'd' para configurar su direccion")
                print("Presione 'e' para configurar su casa de "+
                	"estudio")
                print("Presione 'f' para salir de la configuracion "+
                	"y volver al menu de usuario")
                opcion = input("Digite su opcion: ")

                if opcion == 'a':
                    while True:

                        nueva_pass = input("Ingrese su nueva password: ")
                        nueva_pass_confirmacion = input("Ingrese nuevamente"+                      " la password a cambiar: ")


                        if nueva_pass != nueva_pass_confirmacion:
                            print("No son iguales las password")
                            continue

                        break

                    cargar_datos[indice_cuenta][
                                                "Password"
                                               ] = nueva_pass

                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de password realizada")

                elif opcion == 'b':

                    while True:
                        nuevo_nombre = input("Ingrese su nuevo nombre: ")
                        if not nuevo_nombre.isalpha():
                            print("El nombre debe ser alfabético")
                            continue

                        break
                    cargar_datos[indice_cuenta][
                                                "Nombre"
                                                ] = nuevo_nombre.capitalize()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de nombre realizada")                             

                elif opcion == 'c':
                    while True:

                        nuevo_apellido = input(
                            "Ingrese su nuevo apellido: ").capitalize()

                        if not nuevo_apellido.isalpha():
                            print("El nombre debe ser alfabético")
                            continue

                        break
                    cargar_datos[indice_cuenta][
                                                "Apellido"
                                               ] = nuevo_apellido
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de apellido realizada")

                elif opcion == 'd':

                    nueva_dirreccion = input("Ingrese su nueva dirrecion: ")
                    cargar_datos[indice_cuenta][
                                                    "Dirrecion"
                                               ] = nueva_dirreccion
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de direccion realizada")

                elif opcion == 'e':


                    nueva_casa_de_estudio = input("Ingrese su nueva casa de"+" estudio: ")
                    cargar_datos[
                                    indice_cuenta
                                ][
                                    "Casa estudio"
                                ] = nueva_casa_de_estudio.capitalize()


                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de casa de estudio realizada")

                elif opcion == 'f':

                    print("Saliendo al menu de usuario...")
                    break

                else:

                    print("Opcion no valida, ingrese una de las opciones"+
                        " mostradas")


        elif opcion == 'd':
            print("Saliendo de la cuenta...")
            break
                
        else:
            print("Opcion no valida, ingrese una de las opciones mostradas")


def iniciar_sesion(nombre_usuario, 
                   contra_usuario,
                   archivo):
    """
    Comprueba que el nombre y contraseña del usuario sean las
    correspondientes y le pasa el indice del usuario que esta 
    iniciando sesion  a la funcion vista_de_sesion. 
    
    Argumentos:
        nombre_usuario (String): Nombre del usuario.
        contra_usuario (String): Contraseña del usuario.
        archivo (String): Ruta donde se encuentra guardado el archivo 
        JSON.

    """
    cargar_datos = cargar_archivo(archivo)

    while True:
        if  nombre_usuario in listar_usuarios():
            indice = listar_usuarios().index(nombre_usuario)
            if  cargar_datos[indice]["Password"] == contra_usuario:
                print("Inicio de sesion exitosamente")

                return vista_de_sesion(indice)
            else:
                print("Error de inicio de sesion, volviendo al menu"+
                " principal...")
                break
        else:
            print("Error de inicio de sesion, volviendo al menu "+          
                "principal...")
            break


def main():
    """
    Menu principal en el cual se maneja todo el programa, obteniendo
    los datos del usuario.

    """
    while True:

        print("Bienvenido al servicio de mensajeria")
        print("Presione 'a' si quiere iniciar sesion")
        print("Presione 'b' si quiere crear una nueva cuenta")
        print("Presione 'c' si quiere salir del servicio "+
        	"de mensajeria")

        opcion = input("Digite su opcion: ")


        if opcion == 'a':       

            nombre_inicio = input("Ingrese su nombre de usuario\n").lower()
            contra_inicio = input("ingrese su password de usuario\n")


            iniciar_sesion(nombre_inicio, contra_inicio, ruta_del_archivo)


        elif opcion == 'b':

            while True:
                lista = listar_usuarios()
                nombre_usuario = input("Ingrese su nombre de usuario\n")

                if nombre_usuario.lower() in lista:
                    print("Ese nombre de ususario ya existe")
                    continue

                while True:    
                    password = input("Ingrese su password de usuario\n")
                    password_confirmacion = input("Ingrese nuevamente su "+
                        "password de usuario\n")

                    if password != password_confirmacion:
                        print("No son iguales las password")
                        continue

                    break

                while True:

                    nombre_real = input("Ingrese su nombre\n").capitalize()

                    if not nombre_real.isalpha():
                        print("El nombre debe ser alfabético")
                        continue

                    break

                while True:

                    apellido = input("Ingrese su apellido\n").capitalize()

                    if not apellido.isalpha():

                        print("El apellido debe ser alfabético")
                        continue

                    break

                direccion = input("Ingrese su direción\n")

                while True:

                    casa_de_estudio = input(
                        "Ingrese su casa de estudio\n").capitalize()

                    if not casa_de_estudio.isalpha():
                        print("La casa de estudio debe ser alfabético")
                        continue

                    break

                break

            crear_usuario(nombre_usuario, password, 
                            nombre_real, apellido,
                            direccion, casa_de_estudio)

        elif opcion == 'c':

            break

        else:

            print("Opcion no valida, ingrese una de las opciones mostradas")

main()