import json
import os

ruta_del_archivo = "B_D/bd.json" #ruta donde se guardara el json

def cargar_archivo(ruta):
    """Comprueba si la ruta de JSON no esta vacia cargando sus datos en esta y si lo esta comprueba que tenga almenos [] en este
    
    Argumentos:
        ruta (string): Ruta donde se encuentra guardado el archivo ".json"
    
    Retorna:
        Lista: Retorna una lista de diccionarios 
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
    """Busca sobrescribir el JSON antiguo con un nuevo, con los mismos valores pero agrengando, ademas, los datos del nuevo usuario
    
    Argumentos:
        ruta (String): Ruta donde se encuentra guardado el archivo ".json"
        diccionario_con_datos_nuevos (dict): Diccionario que tiene datos nuevos para ser agregados al archivo ".json" 
    """

    with open(ruta, 'w') as archivo:
        json.dump(diccionario_con_datos_nuevos, archivo, sort_keys=True, indent=4)

def listar_usuarios():
    """Crea nueva lista, llama a la funcion cargar_archivos y los deja relacionado con una variable elemento donde mas tarde la 
    lista_usuarios se llena con los elementos de la clave del JSON 'usuarios'

    Retorna:
        Lista: Retorna una lista ya con todos los nombres de usuarios en el JSON

    """
    lista_usuarios = []
    for elementos in cargar_archivo(ruta_del_archivo):
        lista_usuarios.append(elementos.get("Usuario"))
    return lista_usuarios

def crear_usuario(nombre_usuario, password,
                nombre, apellido,
                direccion, universidad):
    """Realiza la obtecion de los datos para la creacion y la sobreescritura del JSON con el nuevo usuario, llamando a la funcion
    sobrescribir_archivo obteniendo el parametro nueva_persona que obtiene en si el diccionario persona ordenado con los datos del nuevo usuario
    
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


def vista_de_sesion(indice_cuenta):
    """Muestra el menu de usuario con las diferentes opciones que se pueden realizar en este, ademas recargarga los datos ya exisitentes en el 
    JSON con cargar_archivo, guardandolo en cargar_datos y permitiendo obtenerlos con indice_cuenta especificando que dato a obtener, al igual, 
    este brinda la modificacion del usuario ya encontrado con la funcion sobrescribir_archivo que guarda en la ruta del JSON junto a la variable cargar_datos
    ya modificado
    
    Args:
        indice_cuenta (String): 
    """
    cargar_datos = cargar_archivo(ruta_del_archivo)
    while True:
        print("Presione 'a' para entrar a la bandeja de entrada")
        print("Presione 'b' para redactar un mensaje")
        print("Presione 'c' para configurar su perfil") 
        print("Presione 'd' para salir de la cuenta")
        opcion = input("Digite su opcion: ")

        if opcion == 'a': # Restriccion faltante de posicion ingresada sea una letra
            bandeja = cargar_datos[indice_cuenta].get("Bandeja de entrada")
            while True:
                if len(bandeja) == 0:
                    print("No tiene, ningun nuevo mensaje, volviendo al menu de usuario")
                    break
                else:
                    i = 1
                    print("\nMensajes recibidos")
                    for elementos in bandeja:
                        print("Mensaje nº",i,"\nFuente: "+elementos.get("Emisor")+"\tAsunto: "+elementos.get("Asunto"),
                                "\n\nMensaje:\n"+elementos.get("Mensaje")+"\n")
                        i = i + 1
                    break
            if len(bandeja) != 0:
                while True:
                    print("a.-Eliminar mensaje")
                    print("b.-Responder")
                    print("c.-Salir al menu de usuario")
                    opcion = input("")
                    opcion = opcion.lower()
                    if opcion == "a":

                        eliminar_mensaje = input("Ingrese el numero del mensaje a eliminar: ")

                        if not eliminar_mensaje.isdigit():
                            print("Ingreso una letra y no un numero")
                            continue
                    
                        if int(eliminar_mensaje) <= 0 or int(eliminar_mensaje) > len(bandeja):
                            print("ingrese valores correctos para eliminar")
                            continue
                        else:
                            eliminar_mensaje = int(eliminar_mensaje) - 1
                            cargar_datos[indice_cuenta]["Bandeja de entrada"].pop(int(eliminar_mensaje))
                            print("Mensaje eliminado correctamente")
                            sobrescribir_archivo(ruta_del_archivo, cargar_datos)   

                    elif opcion =="b":

                        responder_mensaje = input("Ingrese el numero del mensaje a responder: ")
                        if int(responder_mensaje) <= 0 or int(responder_mensaje) > len(bandeja):
                            print("ingrese valores correctos para responder un mensaje")
                            continue
                        responder_mensaje = int(responder_mensaje) - 1 
                        persona_a_responder = bandeja[int(responder_mensaje)].get("Emisor")
                        if persona_a_responder in listar_usuarios():
                            indice = listar_usuarios().index(persona_a_responder)
                        mensaje_asunto = input("Ingrese el asunto (opcional): ")
                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,"Emisor":cargar_datos[indice_cuenta].get("Usuario"),"Mensaje":mensaje_redactato}
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
            lista = []
            lista = listar_usuarios()
            lista = [item.lower() for item in lista]
            mensaje_destinatario = input("Ingrese el destinatario: ")
            if mensaje_destinatario in lista:
                for usuarios in cargar_datos:
                    if mensaje_destinatario in usuarios["Usuario"].lower():

                        indice= cargar_datos.index(usuarios)
                        mensaje_asunto = input("Ingrese el asunto (opcional): ")
                        mensaje_redactato = input("Escriba el mensaje: ")
                        mensaje = {"Asunto":mensaje_asunto,"Emisor":cargar_datos[indice_cuenta].get("Usuario"),"Mensaje":mensaje_redactato}
                        cargar_datos[indice]["Bandeja de entrada"].append(mensaje)

                        sobrescribir_archivo(ruta_del_archivo, cargar_datos)  
            else:
                print("Destinatario no existente")


        elif opcion == 'c':
            while True:
                print("Presione 'a' para configurar su password")
                print("Presione 'b' para configurar su nombre")
                print("Presione 'c' para configurar su apellido")
                print("Presione 'd' para configurar su direccion")
                print("Presione 'e' para configurar su casa de estudio")
                print("Presione 'f' para salir de la configuracion y volver al menu de usuario")
                opcion = input("Digite su opcion: ")

                if opcion == 'a':
                    while True:
                        nueva_pass = input("Ingrese su nueva password: ")
                        nueva_pass_confirmacion = input("Ingrese nuevamente la password a cambiar: ")
                        if nueva_pass != nueva_pass_confirmacion:
                            print("No son iguales las password")
                            continue
                        break
                    cargar_datos[indice_cuenta]["Password"] = nueva_pass.lower()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de password realizada")

                elif opcion == 'b':
                    while True:
                        nuevo_nombre = input("Ingrese su nuevo nombre: ")
                        if not nuevo_nombre.isalpha():
                            print("El nombre debe ser alfabético")
                            continue
                        break
                    cargar_datos[indice_cuenta]["Nombre"] = nuevo_nombre.lower()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de nombre realizada")                             

                elif opcion == 'c':
                    while True:
                        nuevo_apellido = input("Ingrese su apellido nombre: ")
                        if not nuevo_apellido.isalpha():
                            print("El nombre debe ser alfabético")
                            continue
                        break
                    cargar_datos[indice_cuenta]["Apellido"] = nuevo_apellido.lower()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de apellido realizada")

                elif opcion == 'd':

                    nueva_dirreccion = input("Ingrese su nueva dirrecion: ")
                    cargar_datos[indice_cuenta]["Dirrecion"] = nueva_dirreccion.lower()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de direccion realizada")

                elif opcion == 'e':

                    nueva_casa_de_estudio = input("Ingrese su nueva casa de estudio: ")
                    cargar_datos[indice_cuenta]["Casa estudio"] = nueva_casa_de_estudio.lower()
                    sobrescribir_archivo(ruta_del_archivo,cargar_datos)
                    print("Cambio de casa de estudio realizada")

                elif opcion == 'f':

                    print("Saliendo al menu de usuario")
                    break
                else:
                    print("Opcion no valida, ingrese una de las opciones mostradas")

        elif opcion == 'd':
            print("Saliendo de la cuenta...")
            break
                
        else:
            print("Opcion no valida, ingrese una de las opciones mostradas")


def iniciar_sesion(nombre_usuario, contra_usuario, archivo):
    """Comprueba que el nnombre y contraseña del usuario sean las correspondientes
    
    Args:
        nombre_usuario (String): Nombre del usuario
        contra_usuario (dict): Contraseña del usuario
        archivo (string): Ruta donde se encuentra guardado el archivo ".json"
    """
    cargar_datos = cargar_archivo(archivo)
    while True:
        if  nombre_usuario in listar_usuarios():
            indice = listar_usuarios().index(nombre_usuario)
            if  cargar_datos[indice]["Password"] == contra_usuario:
                print("logeo exitoso")
                return vista_de_sesion(indice)
            else:
                print("Error de inicio de sesion, volviendo al menu principal")
                break
        else:
            print("Error de inicio de sesion, volviendo al menu principal")
            break


def main():
    """Menu principal al cual se va manejar todo el programa, obtenendo los datos del usuario a crear y entregandoselos a la funcion (crear_usuario), 
    por otro lado ayuda a entregar los valores que inicia la sesion del usuario a la funcion (iniciar_sesion) y finalmente el termino del programa
    """
    while True:

        print("Bienvenido al servicio de mensajeria")
        print("Presione 'a' si quiere iniciar sesion")
        print("Presione 'b' si quiere crear una nueva cuenta")
        print("Presione 'c' si quiere salir del servicio de mensajeria")

        opcion = input("Digite su opcion: ")


        if opcion == 'a':       

            nombre_inicio = input("Ingrese su nombre de usuario\n")
            contra_inicio = input("ingrese su password de usuario\n")

            iniciar_sesion(nombre_inicio,contra_inicio,ruta_del_archivo)

        elif opcion == 'b':

            while True:
                lista = []
                lista = listar_usuarios()
                lista = [item.lower() for item in lista]
                nombre_usuario = input("Ingrese su nombre de usuario\n")
                if nombre_usuario.lower() in lista:
                    print("Ese nombre de ususario ya existe")
                    continue
                while True:    
                    password = input("Ingrese su password de usuario\n")
                    password_confirmacion = input("Ingrese nuevamente su password de usuario\n")
                    if password != password_confirmacion:
                        print("No son iguales las password")
                        continue
                    break
                while True:
                    nombre_real = input("Ingrese su nombre\n")
                    if not nombre_real.isalpha():
                        print("El nombre debe ser alfabético")
                        continue
                    break
                while True:
                    apellido = input("Ingrese su apellido\n")
                    if not apellido.isalpha():
                        print("El apellido debe ser alfabético")
                        continue
                    break
                direccion = input("Ingrese su dirrecion\n")
                casa_de_estudio = input("Ingrese su casa de estudio\n")
                break
            crear_usuario(nombre_usuario, password,
                          nombre_real, apellido,
                          direccion, casa_de_estudio) 

        elif opcion == 'c':

            break

        else:

            print("Opcion no valida, ingrese una de las opciones mostradas")

main()