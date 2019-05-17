import json
import os
                                                                           
RUTA_DEL_ARCHIVO = "B_D/bd.json" #ruta donde se encuentra el JSON

def cargar_archivo(ruta):
    """
    Carga todos los datos del archivo JSON en la variable contenido 
    y esta es retornada.
    Argumentos:
        ruta (String): Ruta donde se encuentra guardado el archivo JSON
    
    Retorna:
        lista: Retorna una lista de diccionarios con los datos que 
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
    los datos del diccionario que se le entrega como parámetro.
    
    Argumentos:
        ruta (String): Ruta donde se encuentra guardado el archivo
        JSON.
        diccionario_con_datos_nuevos (dict): Diccionario que tiene
        datos nuevos para ser agregados al archivo JSON.

    """

    with open(ruta, 'w') as archivo:
        json.dump(diccionario_con_datos_nuevos, archivo, indent=4)

def listar_usuarios():
    """
    Crea una lista con todos los nombres de usuarios dentro del
    archivo JSON. 
    Retorna:
        lista: Retorna una lista con todos los nombres de usuarios
        que estén en el archivo JSON.

    """
    lista_usuarios = []
    for elementos in cargar_archivo(RUTA_DEL_ARCHIVO):
        # Busca obtener los elementos del JSON "Usuarios" y pasarcelo
        # a una lista
        lista_usuarios.append(elementos.get("Usuario").lower())
    return lista_usuarios

def crear_usuario(nombre_usuario, password,
                  nombre, apellido,
                  direccion, universidad):
    """
    Toma los parámetros y crea un diccionario con esos datos
    que se guardan en la variable persona, la cual es añadida
    a la lista de diccionarios del archivo JSON en la variable
    nueva_persona y sobrescribe el archivo con estos datos.
    
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

    nueva_persona = cargar_archivo(RUTA_DEL_ARCHIVO)
    nueva_persona.append(persona)
    sobrescribir_archivo(RUTA_DEL_ARCHIVO, nueva_persona)

    print("Usuario agregado exitosamente, presione Enter para continuar")


def vista_de_sesion(indice_cuenta):
    """
    Muestra todas las opciones para la cuenta que inicio sesión
    utilizando su índice como referencia, las opciones que se despliegan
    son las siguientes:  

    a) Bandeja de entrada: Opción para visualizar los mensajes 
        recibidos, los cuales puede responder o eliminar.

    b) Redactar un mensaje: Envió de mensajes a los usuarios
        de la aplicación.

    c) Configurar perfil: Opción para cambiar la información
        de la cuenta del usuario.

    d) Salir de la cuenta y volver al menu principal.

    Argumentos:
        indice_cuenta (String): índice del nombre de usuario con el que
                                inicio sesión.

    """
    cargar_datos = cargar_archivo(RUTA_DEL_ARCHIVO)
    while True:
        print("Presione 'a' para entrar a la bandeja de entrada")
        print("Presione 'b' para redactar un mensaje")
        print("Presione 'c' para configurar su perfil") 
        print("Presione 'd' para salir de la cuenta")
        opcion = input("Digite su opción: ").lower()

        if opcion == 'a':
            bandeja = cargar_datos[indice_cuenta].get("Bandeja de entrada")

            while True:
                if len(bandeja) == 0:
                    print(
                        "No tiene ningún nuevo mensaje, volviendo al menú "+
                        "de usuario...")
                    break

                else:

                    i = 1
                    print("\nMensajes recibidos")

                    for elementos in bandeja:
                        # Busca imprimir por pantalla de forma ordenada
                        # lo que contiene la bandeja de entrada de este usuario

                        print("Mensaje nº",i,"\nFuente: "+elementos.get(
                            "Emisor")+"\tAsunto: "+elementos.get("Asunto"),
                        "\n\nMensaje:\n"+elementos.get("Mensaje")+"\n")

                        i = i + 1 

                    break

            if len(bandeja) != 0:

                while True:

                    print("a.-Eliminar mensaje")
                    print("b.-Responder")
                    print("c.-Salir al menú de usuario")
                    opcion = input("")
                    opcion = opcion.lower()

                    if opcion == "a":

                        eliminar_mensaje = input("Ingrese el número del"
                            +" mensaje a eliminar: ")

                        if not eliminar_mensaje.isdigit():
                            print("ingrese valores correctos para eliminar")
                            continue

                        elif (int(eliminar_mensaje) <= 0 or 
                             int(eliminar_mensaje) > len(bandeja)):

                            print("ingrese valores correctos para eliminar")
                            continue

                        else:
                            eliminar_mensaje = int(eliminar_mensaje) - 1
                            cargar_datos[indice_cuenta][
                            "Bandeja de entrada"].pop(int(eliminar_mensaje))

                            print("Mensaje eliminado correctamente")
                            sobrescribir_archivo(RUTA_DEL_ARCHIVO,
                                                 cargar_datos)   

                    elif opcion =="b":

                        responder_mensaje = input("Ingrese el número del "+
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
                        remitente = bandeja[responder_mensaje].get("Emisor")

                        if bandeja[responder_mensaje].get(
                                                "Emisor") == 'Administrador':
                            print("No puedes responder mensajes de aun"+
                            " administrador")
                            continue

                        elif remitente in listar_usuarios():
                            indice = listar_usuarios().index(remitente)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional): ")

                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,
                                    "Emisor":cargar_datos[
                                                          indice_cuenta
                                                         ].get("Usuario"),
                                    "Mensaje":mensaje_redactato
                                  }
                        cargar_datos[indice][
                                        "Bandeja de entrada"].append(mensaje)
                        sobrescribir_archivo(RUTA_DEL_ARCHIVO, cargar_datos)
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
                    # Realiza una operacion para buscar en cargar_datos
                    # si el usuario al que se quiere enviar el mensaje
                    # existe y asi poder manejar los datos de la 
                    # Bandeja de entrada de este

                    if mensaje_destinatario.lower() in usuarios[
                                                       "Usuario"].lower():

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

                        sobrescribir_archivo(RUTA_DEL_ARCHIVO, cargar_datos) 
            else:
                print("Destinatario no existente, volviendo al menú de"+
                " usuario...")


        elif opcion == 'c':

            while True:
                print("Presione 'a' para configurar su password")
                print("Presione 'b' para configurar su nombre")
                print("Presione 'c' para configurar su apellido")
                print("Presione 'd' para configurar su dirección")
                print("Presione 'e' para configurar su casa de "+
                    "estudio")
                print("Presione 'f' para salir de la configuración "+
                    "y volver al menú de usuario")
                opcion = input("Digite su opción: ").lower()

                if opcion == 'a':
                    while True:

                        nueva_pass = input("Ingrese su nueva password: ")
                        nueva_pass_confirmacion = input("Ingrese nuevamente"+
                        " la password a cambiar: ")


                        if nueva_pass != nueva_pass_confirmacion:
                            print("No son iguales las password")
                            continue

                        break

                    cargar_datos[indice_cuenta][
                                                "Password"
                                               ] = nueva_pass

                    sobrescribir_archivo(RUTA_DEL_ARCHIVO,cargar_datos)
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
                    sobrescribir_archivo(RUTA_DEL_ARCHIVO,cargar_datos)
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
                    sobrescribir_archivo(RUTA_DEL_ARCHIVO,cargar_datos)
                    print("Cambio de apellido realizada")

                elif opcion == 'd':

                    nueva_dirreccion = input("Ingrese su nueva dirección: ")
                    cargar_datos[indice_cuenta][
                                                "Dirrecion"
                                               ] = nueva_dirreccion
                    sobrescribir_archivo(RUTA_DEL_ARCHIVO,cargar_datos)
                    print("Cambio de dirección realizada")

                elif opcion == 'e':


                    nueva_casa_de_estudio = input("Ingrese su nueva casa de"+
                        " estudio: ")
                    cargar_datos[
                                indice_cuenta
                                ][
                                "Casa estudio"
                                ] = nueva_casa_de_estudio.capitalize()


                    sobrescribir_archivo(RUTA_DEL_ARCHIVO,cargar_datos)
                    print("Cambio de casa de estudio realizada")

                elif opcion == 'f':

                    print("Saliendo al menú de usuario...")
                    break

                else:

                    print("Opción no valida, ingrese una de las opciones"+
                        " mostradas")


        elif opcion == 'd':
            print("Saliendo de la cuenta...")
            break
                
        else:
            print("Opción no valida, ingrese una de las opciones mostradas")

def vista_de_administrador():
    """
    Muestra todas las opciones para el administrador, las opciones que se 
    despliegan son las siguientes:  

    a) Eliminar un usuario: Opción para visualizar los usuarios
        creados, los cuales pueden ser eliminados.

    b) Eliminar un mensaje: Opción que visualiza los usuarios
        de la aplicacion y permite la eliminacion de los mensajes
        recibidos por este usuario

    c) Redactar un mensaje: Envió de mensajes a los usuarios
        de la aplicación.

    d) Salir del administrador y volver al menu principal.

"""

    cargar_datos = cargar_archivo(RUTA_DEL_ARCHIVO)
    while True:
        print("Bienvenido administrador")
        print("Presione 'a' para eliminar un usuario")
        print("Presione 'b' para eliminar un mensaje de un usuario")
        print("Presione 'c' para redactar un mensaje") 
        print("Presione 'd' para salir del administrador")
        opcion = input("Digite su opción: ").lower()

        if opcion == 'a':
            print("Posibles usuarios a eliminar: ", listar_usuarios())
            lista = listar_usuarios()

            usuario_eliminar = input("Ingrese al usuario: ").lower()

            if usuario_eliminar in lista:
                indice = lista.index(usuario_eliminar)
                cargar_datos.pop(indice)

                sobrescribir_archivo(RUTA_DEL_ARCHIVO, cargar_datos)
                print("Usuario eliminado correctamente")
            else:
                print("Usuario no existente, volviendo al menú de"+
                    " administrador...")
                continue

        elif opcion == 'b':
            lista = listar_usuarios()
            print(lista)
            usuario_elegido = input("Ingrese a cual usuario quiere ver "+
                "los mensajes: ").lower()
            if usuario_elegido in listar_usuarios():

                for  elementos in cargar_datos:
                    # Ayuda a cargar los datos del JSON para entregar
                    # la bandeja de entrada de este usuario ingresado
                    indice = listar_usuarios().index(usuario_elegido)

                    bandeja = cargar_datos[indice].get("Bandeja de entrada")

                    while True:
                        if len(bandeja) == 0:
                            print(
                                "No tiene ningún mensaje este usuario, "+
                                "volviendo al menú de administrador...")
                            break

                        else:
                            i = 1
                            print("\nMensajes recibidos")

                            for elementos in bandeja:
                                # Ayuda a la impresion ordenada de los
                                # datos de la bandeja de entrada del
                                # usuario pedido
                                print("Mensaje nº",i,"\nFuente: "+
                                    elementos.get("Emisor")+"\tAsunto: "+
                                    elementos.get("Asunto"),
                                    "\n\nMensaje:\n"+elementos.get("Mensaje")+
                                    "\n")
                                i = i + 1 
                        break

                    if len(bandeja) != 0:

                        while True:
                            eliminar_mensaje = input("Ingrese el número del"
                            +" mensaje a eliminar: ")

                            if not eliminar_mensaje.isdigit():
                                print("ingrese valores correctos para "+
                                    "eliminar")
                                continue

                            elif (int(eliminar_mensaje) <= 0 or 
                                 int(eliminar_mensaje) > len(bandeja)):

                                print("ingrese valores correctos para "+
                                    "eliminar")
                                continue

                            else:
                                eliminar_mensaje = int(eliminar_mensaje) - 1
                                cargar_datos[indice][
                                "Bandeja de entrada"].pop(int(
                                                            eliminar_mensaje))

                                print("Mensaje eliminado correctame")
                                sobrescribir_archivo(RUTA_DEL_ARCHIVO,
                                                 cargar_datos)
                            break
                    break    
            else:
                print("Usuario no existente, volviendo al menú de"+
                        " administrador...")

        elif opcion == 'c':
            print("Posibles destinatarios: ",listar_usuarios())

            lista = listar_usuarios()

            mensaje_destinatario = input("Ingrese el destinatario: ")

            if mensaje_destinatario.lower() in lista:

                for usuarios in cargar_datos:
                    # Ayuda a cargar los datos del JSON 
                    # para saber si el destinatario 
                    # existe y poder manejar los datos de
                    # la bandeja de entrada de este

                    if mensaje_destinatario.lower() in usuarios[
                                                       "Usuario"].lower():

                        indice = cargar_datos.index(usuarios)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional): ")
                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,
                                   "Emisor":"Administrador",
                                   "Mensaje":mensaje_redactato
                                   }
                        cargar_datos[indice]["Bandeja de entrada"].append(
                            mensaje)

                        sobrescribir_archivo(RUTA_DEL_ARCHIVO, cargar_datos) 
            else:
                print("Destinatario no existente, volviendo al menú de"+
                " administrador...")

        elif opcion == 'd':
            print("Saliendo del administrador...")
            break
                
        else:
            print("Opción no valida, ingrese una de las opciones mostradas")

def iniciar_sesion(nombre_usuario, 
                   contra_usuario,
                   archivo):
    """
    Comprueba que el nombre y contraseña del usuario sean las
    correspondientes y le pasa el índice del usuario que esta 
    iniciando sesión a la función vista_de_sesion. 
    
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
                print("Inicio de sesión exitosamente")

                return vista_de_sesion(indice)
            else:
                print("Error de inicio de sesión, volviendo al menú"+
                " principal...")
                break
        elif nombre_usuario.lower() == 'admin':
            if contra_usuario == 'admin':

                return vista_de_administrador()
            else:
                print("Error de inicio de sesión,volviendo al menú"+
                    " principal")
                break

        else:
            print("Error de inicio de sesión, volviendo al menú "+
                "principal...")
            break


def main():
    """
    Menú principal en el cual se maneja todo el programa, obteniendo
    los datos del usuario o el registro de este.

    """
    while True:

        print("Bienvenido al servicio de mensajería")
        print("Presione 'a' si quiere iniciar sesión")
        print("Presione 'b' si quiere crear una nueva cuenta")
        print("Presione 'c' si quiere salir del servicio "+
            "de mensajería")

        opcion = input("Digite su opción: ").lower()


        if opcion == 'a':       

            nombre_inicio = input("Ingrese su nombre de usuario\n").lower()
            contra_inicio = input("ingrese su password de usuario\n")


            iniciar_sesion(nombre_inicio, contra_inicio, RUTA_DEL_ARCHIVO)


        elif opcion == 'b':

            while True:
                lista = listar_usuarios()
                nombre_usuario = input("Ingrese su nombre de usuario\n")

                if nombre_usuario.lower() in lista:
                    print("Ese nombre de usuario ya existe")
                    continue
                elif nombre_usuario.lower() == 'admin':
                    print("Ese nombre de usuario no esta permitido")

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

                direccion = input("Ingrese su dirección\n")

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

            print("Saliendo del programa...")
            break

        else:

            print("Opción no valida, ingrese una de las opciones mostradas")

main()
