import json
import os

file_path = "B_D/bd.json" #ruta donde se guardara el json 

def crearusuario(nombusu,contr,nombr,apell,direc,univ):

	diccionario={}

	diccionario["Usuario"]=nombusu

	diccionario["Password"]=contr

	diccionario["Nombre"]=nombr

	diccionario["Apellido"]=apell

	diccionario["Dirrecion"]=direc

	diccionario["Casa estudio"]=univ

	#datosguardados = json.dumps(diccionario)

	with open((file_path), 'a') as file:
		json.dump(diccionario, file)



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

		

		crearusuario(nombreusu,password,nombrereal,apellido,direccion,casaestudio)



	elif opt == 'c':



		continuar = False



	else:



		print("Opcion no valida, ingrese una de las opciones mostradas")

		input("Presione enter para continuar")