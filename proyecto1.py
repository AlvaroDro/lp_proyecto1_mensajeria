import json
import os
import hashlib
import os.path
import getpass
                                                                           
RUTA_DEL_ARCHIVO = "B_D/bd.json" #ruta donde se encuentra el JSON

def inicializar():
    """
    Busca los archivos y carpetas necesarios para que funcione el
    programa y los crea en el caso de que no esten.
    """
    if not os.path.exists("B_D"):
        os.mkdir("B_D", dir_fd=None)
        datos = []
        with open(RUTA_DEL_ARCHIVO, 'w') as archivo:
            json.dump(datos, archivo)
        crear_administrador()

    elif os.path.exists("B_D"):
        if not os.path.exists(RUTA_DEL_ARCHIVO):
            datos = []
            with open(RUTA_DEL_ARCHIVO, 'w') as archivo:
                json.dump(datos, archivo)
            crear_administrador()

def crear_administrador():
    """
    Funcion que inicializa la creacion del JSON con el administrador.
    """
    administrador = {
                "Usuario":"admin",
                "Password":"8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                "Bandeja de entrada":[] 
                }                       
    nuevo_admin = cargar_archivo()
    nuevo_admin.append(administrador)
    sobrescribir_archivo(nuevo_admin)

def cargar_archivo():
    """
    Carga todos los datos del archivo JSON en la variable contenido 
    y esta es retornada.
    
    Retorna:
        contenido (Lista): Retorna una lista de diccionarios con los datos que 
        contiene el archivo JSON.
        main() (funcion): Retorna a la funcion principal, para 
        desplegar el menu. 
    """ 

    if open(RUTA_DEL_ARCHIVO).read() != '':
        with open(RUTA_DEL_ARCHIVO) as archivo:
            contenido = json.load(archivo)
        return contenido          
    else:
        print("\n[!] base de datos vacia, cree un usuario\n")
        datos = []
        with open(RUTA_DEL_ARCHIVO, 'w') as archivo:
            json.dump(datos, archivo)
        return main() 

def sobrescribir_archivo(diccionario_con_datos_nuevos):
    """
    Abre el archivo JSON y sobrescribe el archivo con 
    los datos del diccionario que se le entrega como parámetro.
    
    Argumentos:
        diccionario_con_datos_nuevos (dict): Diccionario que tiene
        datos nuevos para ser agregados al archivo JSON.
    """

    with open(RUTA_DEL_ARCHIVO, 'w') as archivo:
        json.dump(diccionario_con_datos_nuevos, archivo, indent=4)

def listar_usuarios():
    """
    Crea una lista con todos los nombres de usuarios dentro del
    archivo JSON. 
    Retorna:
        lista_usuarios (Lista): Retorna una lista con todos los nombres de usuarios
        que estén en el archivo JSON.
    """
    lista_usuarios = []
    for elementos in cargar_archivo():
        """ 
        Busca obtener los elementos del JSON "Usuarios" y pasarcelo
         a una lista
        """ 
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

    nueva_persona = cargar_archivo()
    nueva_persona.append(persona)
    sobrescribir_archivo(nueva_persona)

    print("\n[+] Usuario agregado exitosamente, presione "+
        "Enter para continuar\n")


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
    cargar_datos = cargar_archivo()
    while True:
        print("****************************************************")
        print("\t|Bienvenid@ : "+cargar_datos[indice_cuenta].get("Usuario")+
            "|")
        print("****************************************************")
        print("Presione 'a' para entrar a la bandeja de entrada")
        print("Presione 'b' para redactar un mensaje")
        print("Presione 'c' para configurar su perfil") 
        print("Presione 'd' para salir de la cuenta")
        print("****************************************************")
        print("****************************************************\n")
        opcion = input("Digite su opción: ").lower()

        if opcion == 'a':
            bandeja = cargar_datos[indice_cuenta].get("Bandeja de entrada")

            while True:
                if len(bandeja) == 0:
                    print(
                        "\n[*] No tiene ningún nuevo mensaje, volviendo al"+
                        " menú  de usuario...\n")
                    break

                else:

                    i = 1
                    print("***********************************")
                    print("\n\tMensajes recibidos")
                    print("***********************************")
                    for elementos in bandeja:
                        """
                        Busca imprimir por pantalla de forma ordenada
                        lo que contiene la bandeja de entrada de este usuario.
                        """

                        print("Mensaje nº",i,"\nFuente: "+elementos.get(
                            "Emisor")+"\tAsunto: "+elementos.get("Asunto"),
                        "\n\nMensaje:\n"+elementos.get("Mensaje")+"\n")

                        i = i + 1 
                    #print("***********************************")
                    print("***********************************\n")
                    break

            if len(bandeja) != 0:

                while True:
                    print("*****************************")
                    print("\tOpciones")
                    print("*****************************")
                    print("a.-Eliminar mensaje")
                    print("b.-Responder")
                    print("c.-Salir al menú de usuario")
                    print("*****************************")
                    print("*****************************\n")
                    opcion = input("")
                    opcion = opcion.lower()

                    if opcion == "a":

                        eliminar_mensaje = input("Ingrese el número del"
                            +" mensaje a eliminar:\n")

                        if not eliminar_mensaje.isdigit():
                            print("\n[!] Ingrese valores correctos para eliminar\n")
                            continue

                        elif (int(eliminar_mensaje) <= 0 or 
                             int(eliminar_mensaje) > len(bandeja)):

                            print("\n[!] Ingrese valores correctos para eliminar\n")
                            continue

                        else:
                            eliminar_mensaje = int(eliminar_mensaje) - 1
                            cargar_datos[indice_cuenta][
                            "Bandeja de entrada"].pop(int(eliminar_mensaje))

                            print("\n[+] Mensaje eliminado correctamente\n")
                            sobrescribir_archivo(cargar_datos)   

                    elif opcion =="b":

                        responder_mensaje = input("Ingrese el número del "+
                            "mensaje a responder:\n")

                        if not responder_mensaje.isdigit():
                            print("\n[!]Ingrese valores correctos para "+
                                "responder un mensaje\n")
                            continue

                        if (int(responder_mensaje) <= 0 or 
                            int(responder_mensaje) > len(bandeja)):

                            print("\n[!] Ingrese valores correctos para "+
                                "responder un mensaje\n")
                            continue

                        responder_mensaje = int(responder_mensaje) - 1
                        remitente = bandeja[responder_mensaje].get("Emisor")

                        if bandeja[responder_mensaje].get(
                                                "Emisor") == 'Administrador':
                            print("\n[!] No puedes responder mensajes de aun"+
                            " administrador\n")
                            continue

                        elif remitente in listar_usuarios():
                            indice = listar_usuarios().index(remitente)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional):\n")

                        mensaje_redactato = input("Escriba el mensaje:\n")
                        mensaje = {"Asunto":mensaje_asunto,
                                    "Emisor":cargar_datos[
                                                          indice_cuenta
                                                         ].get("Usuario"),
                                    "Mensaje":mensaje_redactato
                                  }
                        cargar_datos[indice][
                                        "Bandeja de entrada"].append(mensaje)
                        sobrescribir_archivo(cargar_datos)
                        print("\n[+] Mensaje enviado exitosamente\n ")
                    elif opcion == "c":
                        break
                    else:
                        print("\n[!] No ingreso ninguna opcion valida\n")
                        continue

                    break

        elif opcion == 'b': 
            print("Posibles destinatarios:\n",listar_usuarios())

            lista = listar_usuarios()

            mensaje_destinatario = input("Ingrese el destinatario:\n")

            if mensaje_destinatario.lower() in lista:

                for usuarios in cargar_datos:
                    """
                     Realiza una operacion para buscar en cargar_datos
                     si el usuario al que se quiere enviar el mensaje
                     existe y asi poder manejar los datos de la 
                     Bandeja de entrada de este 
                    """

                    if mensaje_destinatario.lower() in usuarios[
                                                       "Usuario"].lower():

                        indice = cargar_datos.index(usuarios)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional):\n")
                        mensaje_redactato = input("Escriba el mensaje:\n")
                        mensaje = {"Asunto":mensaje_asunto,
                                   "Emisor":cargar_datos[
                                                         indice_cuenta
                                                        ].get("Usuario"),
                                   "Mensaje":mensaje_redactato
                                   }
                        cargar_datos[indice]["Bandeja de entrada"].append(
                            mensaje)

                        sobrescribir_archivo(cargar_datos)
                        print("\n[+] Mensaje enviado exitosamente\n ")
            else:
                print("\n[!] Destinatario no existente, volviendo al menú de"+
                " usuario...\n")


        elif opcion == 'c':

            while True:
                print("*****************************************************")
                print("\tConfiguración de la cuenta")
                print("*****************************************************")
                print("Presione 'a' para configurar su password")
                print("Presione 'b' para configurar su nombre")
                print("Presione 'c' para configurar su apellido")
                print("Presione 'd' para configurar su dirección")
                print("Presione 'e' para configurar su casa de "+
                    "estudio")
                print("Presione 'f' para salir de la configuración "+
                    "y volver al menú de usuario")
                print("*****************************************************")
                print("*****************************************************\n")
                opcion = input("Digite su opción: \n").lower()

                if opcion == 'a':
                    while True:

                        nueva_pass = getpass.getpass("Ingrese su nueva"+
                            " password:\n")
                        nueva_pass_confirmacion = getpass.getpass("Ingrese "+
                            "nuevamente la password a cambiar:\n")


                        if nueva_pass != nueva_pass_confirmacion:
                            print("\n[!] No son iguales las password\n")
                            continue

                        encriptacion = nueva_pass.encode("UTF-8")
                        nueva_pass = hashlib.sha256(encriptacion)
                        break

                    cargar_datos[indice_cuenta][
                                                "Password"
                                               ] = nueva_pass.hexdigest()

                    sobrescribir_archivo(cargar_datos)
                    print("\n[+] Cambio de password realizada\n")

                elif opcion == 'b':

                    while True:
                        nuevo_nombre = input("Ingrese su nuevo nombre:\n")
                        if not nuevo_nombre.isalpha():
                            print("\n[!] El nombre debe ser alfabético\n")
                            continue

                        break
                    cargar_datos[indice_cuenta][
                                                "Nombre"
                                                ] = nuevo_nombre.capitalize()
                    sobrescribir_archivo(cargar_datos)
                    print("\n[+] Cambio de nombre realizada\n")

                elif opcion == 'c':
                    while True:

                        nuevo_apellido = input(
                            "Ingrese su nuevo apellido:\n").capitalize()

                        if not nuevo_apellido.isalpha():
                            print("\n[!] El nombre debe ser alfabético\n")
                            continue

                        break
                    cargar_datos[indice_cuenta][
                                                "Apellido"
                                               ] = nuevo_apellido
                    sobrescribir_archivo(cargar_datos)
                    print("\n[+] Cambio de apellido realizada\n")

                elif opcion == 'd':

                    nueva_dirreccion = input("Ingrese su nueva dirección:\n")
                    cargar_datos[indice_cuenta][
                                                "Dirrecion"
                                               ] = nueva_dirreccion
                    sobrescribir_archivo(cargar_datos)
                    print("\n[+] Cambio de dirección realizada\n")

                elif opcion == 'e':


                    nueva_casa_de_estudio = input("Ingrese su nueva casa de"+
                        " estudio:\n")
                    cargar_datos[
                                indice_cuenta
                                ][
                                "Casa estudio"
                                ] = nueva_casa_de_estudio.capitalize()


                    sobrescribir_archivo(cargar_datos)
                    print("\n[+] Cambio de casa de estudio realizada\n")

                elif opcion == 'f':

                    print("Saliendo al menú de usuario...")
                    break

                else:

                    print("\n[!]Opción no valida, ingrese una de las opciones"+
                        " mostradas\n")


        elif opcion == 'd':
            print("\n[*] Saliendo de la cuenta...\n")
            break
                
        else:
            print("\n[!] Opción no valida, ingrese una de las opciones mostradas\n")

def vista_de_administrador(indice_cuenta):
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
    d)	Bandeja de entrada: Opción para visualizar los mensajes 
        recibidos, los cuales puede responder o eliminar.
    e) Salir del administrador y volver al menu principal.
    Argumentos:
        indice_cuenta (String): índice que ayudaa a manejar
        los datos de la posicion del administrador.
"""

    cargar_datos = cargar_archivo()
    while True:
        print("*********************************************************")
        print("\tBienvenido al panel de administrador")
        print("*********************************************************")
        print("Presione 'a' para eliminar un usuario")
        print("Presione 'b' para eliminar un mensaje de un usuario")
        print("Presione 'c' para redactar un mensaje")
        print("Presione 'd' para entrar bandeja de entrada") 
        print("Presione 'e' para salir del administrador")
        print("*********************************************************")
        print("*********************************************************\n")
        opcion = input("Digite su opción:\n").lower()

        if opcion == 'a':
            print("Posibles usuarios a eliminar:\n", listar_usuarios())
            lista = listar_usuarios()

            usuario_eliminar = input("Ingrese al usuario:\n").lower()
            if usuario_eliminar == 'admin' or usuario_eliminar == 'administrador':
            	print("No puedes eliminarme...")
            	continue

            elif usuario_eliminar in lista:
                indice = lista.index(usuario_eliminar)
                cargar_datos.pop(indice)

                sobrescribir_archivo(cargar_datos)
                print("\n[+] Usuario eliminado correctamente\n")
            else:
                print("\n[!] Usuario no existente, volviendo al menú de"+
                    " administrador...\n")
                continue

        elif opcion == 'b':
            lista = listar_usuarios()
            print(lista)
            usuario_elegido = input("Ingrese a cual usuario quiere ver "+
                "los mensajes:\n").lower()
            if usuario_elegido in listar_usuarios():

                for  elementos in cargar_datos:
                    """
                    Ayuda a cargar los datos del JSON para entregar
                    la bandeja de entrada de este usuario ingresado.
                    """
                    indice = listar_usuarios().index(usuario_elegido)

                    bandeja = cargar_datos[indice].get("Bandeja de entrada")

                    while True:
                        if len(bandeja) == 0:
                            print(
                                "\n[!] No tiene ningún mensaje este usuario, "+
                                "volviendo al menú de administrador...\n")
                            break

                        else:
                            i = 1
                            print("\nMensajes recibidos:\n")

                            for elementos in bandeja:
                                """
                                Ayuda a la impresion ordenada de los
                                 datos de la bandeja de entrada del
                                 usuario.
                                """
                                print("Mensaje nº",i,"\nFuente: "+
                                    elementos.get("Emisor")+"\tAsunto: "+
                                    elementos.get("Asunto"),
                                    "\n\nMensaje:\n"+elementos.get("Mensaje")+
                                    "\n")
                                i = i + 1 
                        break

                    if len(bandeja) != 0:

                        while True:
                            eliminar_mensaje = input("\nIngrese el número del"
                            +" mensaje a eliminar:\n")

                            if not eliminar_mensaje.isdigit():
                                print("\n[!] ingrese valores correctos para "+
                                    "eliminar\n")
                                continue

                            elif (int(eliminar_mensaje) <= 0 or 
                                 int(eliminar_mensaje) > len(bandeja)):

                                print("\n[!] ingrese valores correctos para "+
                                    "eliminar\n")
                                continue

                            else:
                                eliminar_mensaje = int(eliminar_mensaje) - 1
                                cargar_datos[indice][
                                "Bandeja de entrada"].pop(int(
                                                            eliminar_mensaje))

                                print("\n[+] Mensaje eliminado correctame\n")
                                sobrescribir_archivo(cargar_datos)
                            break
                    break    
            else:
                print("\n[!] Usuario no existente, volviendo al menú de"+
                        " administrador...\n")

        elif opcion == 'd':
            bandeja = cargar_datos[indice_cuenta].get("Bandeja de entrada")

            while True:
                if len(bandeja) == 0:
                    print(
                        "\n[*] No tiene ningún nuevo mensaje, volviendo al"+
                        " menú  de administrador...\n")
                    break

                else:

                    i = 1
                    print("***********************************")
                    print("\n\tMensajes recibidos")
                    print("***********************************")
                    for elementos in bandeja:
                        """
                        Busca imprimir por pantalla de forma ordenada
                        lo que contiene la bandeja de entrada de este usuario.
                        """

                        print("Mensaje nº",i,"\nFuente: "+elementos.get(
                            "Emisor")+"\tAsunto: "+elementos.get("Asunto"),
                        "\n\nMensaje:\n"+elementos.get("Mensaje")+"\n")

                        i = i + 1 
                    #print("***********************************")
                    print("***********************************\n")
                    break

            if len(bandeja) != 0:

                while True:
                    print("*****************************")
                    print("\tOpciones")
                    print("*****************************")
                    print("a.-Eliminar mensaje")
                    print("b.-Responder")
                    print("c.-Salir al menú de administrador")
                    print("*****************************")
                    print("*****************************\n")
                    opcion = input("")
                    opcion = opcion.lower()

                    if opcion == "a":

                        eliminar_mensaje = input("Ingrese el número del"
                            +" mensaje a eliminar:\n")

                        if not eliminar_mensaje.isdigit():
                            print("\n[!] Ingrese valores correctos para eliminar\n")
                            continue

                        elif (int(eliminar_mensaje) <= 0 or 
                             int(eliminar_mensaje) > len(bandeja)):

                            print("\n[!] Ingrese valores correctos para eliminar\n")
                            continue

                        else:
                            eliminar_mensaje = int(eliminar_mensaje) - 1
                            cargar_datos[indice_cuenta][
                            "Bandeja de entrada"].pop(int(eliminar_mensaje))

                            print("\n[+] Mensaje eliminado correctamente\n")
                            sobrescribir_archivo(cargar_datos)   

                    elif opcion =="b":

                        responder_mensaje = input("Ingrese el número del "+
                            "mensaje a responder:\n")

                        if not responder_mensaje.isdigit():
                            print("\n[!]Ingrese valores correctos para "+
                                "responder un mensaje\n")
                            continue

                        if (int(responder_mensaje) <= 0 or 
                            int(responder_mensaje) > len(bandeja)):

                            print("\n[!] Ingrese valores correctos para "+
                                "responder un mensaje\n")
                            continue

                        responder_mensaje = int(responder_mensaje) - 1
                        remitente = bandeja[responder_mensaje].get("Emisor")

                        if bandeja[responder_mensaje].get(
                                                "Emisor") == 'Administrador':
                            print("\n[!] No puedes responder mensajes de aun"+
                            " administrador\n")
                            continue

                        elif remitente in listar_usuarios():
                            indice = listar_usuarios().index(remitente)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional):\n")

                        mensaje_redactato = input("Escriba el mensaje:\n")
                        mensaje = {"Asunto":mensaje_asunto,
                                    "Emisor":cargar_datos[
                                                          indice_cuenta
                                                         ].get("Usuario"),
                                    "Mensaje":mensaje_redactato
                                  }
                        cargar_datos[indice][
                                        "Bandeja de entrada"].append(mensaje)
                        sobrescribir_archivo(cargar_datos)
                        print("\n[+] Mensaje enviado exitosamente\n ")
                    elif opcion == "c":
                        break
                    else:
                        print("\n[!] No ingreso ninguna opcion valida\n")
                        continue

                    break

        elif opcion == 'c':
            print("Posibles destinatarios:\n",listar_usuarios())

            lista = listar_usuarios()

            mensaje_destinatario = input("Ingrese el destinatario:\n")

            if mensaje_destinatario.lower() in lista:

                for usuarios in cargar_datos:
                    """
                    carga los datos del JSON 
                    para saber si el destinatario 
                    existe y poder manejar los datos de
                    la bandeja de entrada de este.
                    """

                    if mensaje_destinatario.lower() in usuarios[
                                                       "Usuario"].lower():

                        indice = cargar_datos.index(usuarios)
                        mensaje_asunto = input("Ingrese el asunto "+
                            "(opcional):\n")
                        mensaje_redactato = input("Escriba el mensaje:\n")
                        mensaje = {"Asunto":mensaje_asunto,
                                   "Emisor":cargar_datos[
                                                          indice_cuenta
                                                         ].get("Usuario"),
                                   "Mensaje":mensaje_redactato
                                   }
                        cargar_datos[indice]["Bandeja de entrada"].append(
                            mensaje)

                        sobrescribir_archivo(cargar_datos)
                        print("\n[+] Mensaje enviado exitosamente\n ") 
            else:
                print("\n[!] Destinatario no existente, volviendo al menú de"+
                " administrador...\n")

        elif opcion == 'e':
            print("\n[*] Saliendo del panel de administrador...\n")
            break
                
        else:
            print("\n[!] Opción no valida, ingrese una de las opciones"+
                " mostradas\n")

def iniciar_sesion(nombre_usuario, 
                   contra_usuario):
    """
    Comprueba que el nombre y contraseña del usuario sean las
    correspondientes y le pasa el índice del usuario que esta 
    iniciando sesión a la función vista_de_sesion. 
    
    Argumentos:
        nombre_usuario (String): Nombre del usuario.
        contra_usuario (String): Contraseña del usuario.
        JSON.
    """
    cargar_datos = cargar_archivo()

    while True:
        if  nombre_usuario in listar_usuarios():
            indice = listar_usuarios().index(nombre_usuario)

            if nombre_usuario.lower() == 'admin':
                if contra_usuario == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918": #dejar asi 
                    return vista_de_administrador(indice)

            elif  cargar_datos[indice]["Password"] == contra_usuario:
                print("\n[+] Inicio de sesión exitosa\n")

                return vista_de_sesion(indice)
            else:
                print("\n[!] Error de inicio de sesión, volviendo al menú"+
                " principal...\n")
                break
        else:
            print("\n[!] Error de inicio de sesión, volviendo al menú "+
                "principal...\n")
            break


def main():
    """
    Menú principal en el cual se maneja todo el programa, obteniendo
    los datos del usuario o el registro de este.
    """
    inicializar()

    while True:
        print("************************************************************")
        print("\tBienvenido al servicio de mensajería")
        print("************************************************************")
        print("Presione 'a' si quiere iniciar sesión")
        print("Presione 'b' si quiere crear una nueva cuenta")
        print("Presione 'c' si quiere salir del servicio "+
            "de mensajería")
        print("************************************************************")
        print("************************************************************\n")
        opcion = input("Digite su opción: ").lower()


        if opcion == 'a':

            nombre_inicio = input("Nombre de usuario\n").lower()
            contra_inicio = getpass.getpass("Password\n")

            encriptacion =contra_inicio.encode("UTF-8")
            contra_inicio = hashlib.sha256(encriptacion)

            iniciar_sesion(nombre_inicio, contra_inicio.hexdigest())



        elif opcion == 'b':

            print("***********************************************")  
            print("\tFormulario para crear una cuenta")
            print("***********************************************\n")

            while True:
                lista = listar_usuarios()
                nombre_usuario = input("Ingrese su nombre de usuario:\n")

                if nombre_usuario.lower() in lista:
                    print("\n[!] Ese nombre de usuario ya existe\n")
                    continue
                elif nombre_usuario.lower() == 'admin':
                    print("\n[!] Ese nombre de usuario no esta permitido\n")

                while True:    
                    password = getpass.getpass("Ingrese su password de usuario\n")
                    password_confirmacion = getpass.getpass("Ingrese "+
                        "nuevamente su password de usuario\n")

                    if password != password_confirmacion:
                        print("\n[!] No son iguales las password\n")
                        continue
                    encriptacion = password.encode("UTF-8")
                    password = hashlib.sha256(encriptacion)
                    break

                while True:

                    nombre_real = input("Ingrese su nombre\n").capitalize()

                    if not nombre_real.isalpha():
                        print("\n[!] El nombre debe ser alfabético\n")
                        continue

                    break

                while True:

                    apellido = input("Ingrese su apellido\n").capitalize()

                    if not apellido.isalpha():

                        print("\n[!] El apellido debe ser alfabético\n")
                        continue

                    break

                direccion = input("Ingrese su dirección\n")

                casa_de_estudio = input(
                        "Ingrese su casa de estudio\n").capitalize()

                break

            crear_usuario(nombre_usuario, password.hexdigest(), 
                            nombre_real, apellido,
                            direccion, casa_de_estudio)

        elif opcion == 'c':

            print("\n[*] Saliendo del programa...\n")
            break

        else:

            print("\n[!] Opción no valida, ingrese una de las opciones mostradas\n")

main()