#!/usr/bin/python
#coding: utf-8

# Filename  : menu.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/XX
# pep8: 100%

# Importaciones
from packages.operaciones import *
import webbrowser as web

d = []
gotData  = False

def mainMenu(gotData, d, c):	# Menú Main
	opcion = int(input("\nElige una opción:\n\n  +- Estadística\n\n  [01] Obtener Media.\n  [02] Obtener Mediana.\n  [03] Obtener Moda.\n  [04] Obtener Varianza y Desviación Estándar.\n  [05] Obtener Covarianza.\n\n  +- Probabilidad\n\n  [06] Teorema de Chebyshev.\n  [07] Teorema de Bayes.\n  [08] Esperanza Matematica.\n\n  [99] Ir a página web.\n  [00] Salir.\n\n>: "))
	if(opcion == 1):
		mediaMenu(gotData, d, c) 	# Manda al menú para obtener la media
	elif(opcion == 2):
		medianaMenu(gotData, d, c)	# Manda al menú para obtener la mediana
	elif(opcion == 3):
		modaMenu(gotData, d, c)		# Manda al menú para obtener la moda
	elif(opcion == 4):
		varianzaMenu(gotData, d, c)	# Manda al menú para obtener La varianza y desvíación estándar
	elif(opcion == 5):
		covarianzaMenu(gotData, d, c)	# Manda al menú para obtener la covarianza
	elif(opcion == 6):
		chebyshevMenu() 			# Manda al menú para obtener resultado de teorema de chebyshev
	elif(opcion == 7):
		bayesMenu()
	elif(opcion == 8):				# Manda al menú para obtener resultado de teorema de bayes
		esperanzaMenu()
	elif(opcion == 99):
		goToWeb()					# Manda a página web
	elif(opcion == 00):
		print("\n\n			+- Adiós.")
		exit()

def goToWeb(w):
	if(w == 1):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/media')
	elif(w == 2):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/mediana')
	elif(w == 3):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/moda')
	elif(w == 4):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/varianza-y-desviacion-estandar')
	elif(w == 5):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/covarianza')
	elif(w == 6):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/teorema-de-chebyshev')
	elif(w == 7):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/teorema-de-bayes')
	elif(w == 8):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/estadistica/esperanza-matematica')
	elif(w == 99):
		web.open('https://sites.google.com/cesunbc.edu.mx/pypres/home')


def askMain(w):
	op = int(input("\n¿Quieres regresar al menú principal o salir?\n\n[1] Regresar.\n[2] Ver más sobre el tema. (Página Web)\n[3] Salir.\n\n>: "))
	if(op == 1):
		mainMenu(False, [], 0)
	elif(op == 2):
		goToWeb(w)
		askMain(w)
	elif(op == 3):
		print("\n\n			+- Adiós.")
		exit()

def getAnother(d, c, w):
	op = int(input("\n¿Quieres hacer otra operación con estos mismos datos?\n\n[1] Sí.\n[2] No.\n\n>: "))
	if(op == 1):
		gotData = True
		mainMenu(gotData, d, c)
	elif(op == 2):
		gotData = False
		op = 0
		askMain(w)

def mediaMenu(gotData, d, c):
	print("\n+----------------+")
	print("+ Calcular Media +")
	print("+----------------+")
	if(gotData == True):
		print("\nLa lista de datos es: ", d)
		media = Media(d, c)
		print("	+- Media Aritmetica: " , media.getMedia(d, c))
		getAnother(d, c, 1)
	elif(gotData == False):
		c = int(input("\n¿Cuántos valores desea ingresar?\n>: "))
		for i in range(1, c + 1):
			print("Dato No.", i)
			dato = float(input(">: "))
			d.append(dato)
		print("\nLa lista de datos es: ", d)
		media = Media(d, c)
		print("	+- Media Aritmetica: " , media.getMedia(d, c))
		getAnother(d, c, 1)


def medianaMenu(gotData, d, c):
	print("\n+------------------+")
	print("+ Calcular Mediana +")
	print("+------------------+")
	if(gotData == True):
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		mediana = Mediana(d, c, dS)
		print("\n	+- Mediana: ", mediana.getMediana(d, c, dS))
		getAnother(d, c, 2)
	elif(gotData == False):
		d = []
		c = int(input("¿Cuántos valores desea ingresar?\n>: "))
		for i in range(1, c + 1):
			print("Dato No.", i)
			dato = float(input(">: "))
			d.append(dato)
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		mediana = Mediana(d, c, dS)
		print("\n	+- Mediana: ", mediana.getMediana(d, c, dS))
		getAnother(d, c, 2)

def modaMenu(gotData, d, c):
	print("\n+---------------+")
	print("+ Calcular Moda +")
	print("+---------------+")
	if(gotData == True):
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		moda = Moda(d, dS)
		print("	+- Moda: ", moda.getModa(d, dS))
		getAnother(d, c, 3)
	elif(gotData == False):
		d = []
		c = int(input("¿Cuántos valores desea ingresar?\n>: "))
		for i in range(1, c + 1):
			print("Dato No.", i)
			dato = float(input(">: "))
			d.append(dato)
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		moda = Moda(d, dS)
		print("	+- Moda: ", moda.getModa(d, dS))
		getAnother(d, c, 3)

def varianzaMenu(gotData, d, c):
	print("\n+-------------------+")
	print("+ Calcular Varianza +")
	print("+-------------------+")
	if(gotData == True):
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		me = Media(d, c)
		m = me.getMedia(d, c)
		varianza = Varianza(d, m, c)
		vP = varianza.getVarianzaPoblacion(d, m, c)
		v = varianza.getVarianzaMuestra(d, m, c)
		desv = varianza.getDesv(v)
		desvP = varianza.getDesv(vP)
		print("\n	+- Varianza de Muestra: ", v)
		print("	+- Desviación Estándar Muestra: ", desv)
		print("\n	+- Varianza de Poblacion: ", vP)
		print("	+- Desviación Estándar Poblacion: ", desvP)
		getAnother(d, c, 4)
	elif(gotData == False):
		d = []
		c = int(input("¿Cuántos valores desea ingresar?\n>: "))
		for i in range(1, c + 1):
			print("Dato No.", i)
			dato = float(input(">: "))
			d.append(dato)
		print("\nLa lista de datos es: ", d)
		dS = sorted(d)
		print("La lista de datos ordenados es: ", dS)
		me = Media(d, c)
		m = me.getMedia(d, c)
		varianza = Varianza(d, m, c)
		vP = varianza.getVarianzaPoblacion(d, m, c)
		v = varianza.getVarianzaMuestra(d, m, c)
		desv = varianza.getDesv(v)
		desvP = varianza.getDesv(vP)
		print("\n	+- Varianza de Muestra: ", v)
		print("	+- Desviación Estándar Muestra: ", desv)
		print("\n	+- Varianza de Poblacion: ", vP)
		print("	+- Desviación Estándar Poblacion: ", desvP)
		getAnother(d, c, 4)

def covarianzaMenu(gotData, d, c):
	print("\n+---------------------+")
	print("+ Calcular Covarianza +")
	print("+---------------------+")
	if(gotData == True):
		dY = []
		print("\nPor favor, ingresa los datos de Y:\n")
		for i in range(1, c + 1):
			print("Dato para Y No.", i)
			dato = float(input(">: "))
			dY.append(dato)

		print("\nLa lista de datos de X es: ", d)
		print("La lista de datos de Y es: ", dY)
		meX = Media(d, c)
		mX = meX.getMedia(d, c)
		meY = Media(dY, c)
		mY = meY.getMedia(dY, c)

		covarianza = Covarianza(d, dY, mX, mY, c)
		print("\n	+- La media de X es: ", mX)
		print("	+- La media de Y es: ", mY)
		print("	+- La covarianza es: ", covarianza.getCovarianza(d, dY, mX, mY, c))
		getAnother(d, c, 5)
	elif(gotData == False):
		d = []
		dY = []
		c = int(input("\n¿Cuántos valores desea ingresar?\n>: "))
		for i in range(1, c + 1):
			print("Dato para X No.", i)
			dato = float(input(">: "))
			d.append(dato)
		print("\nPor favor, ingresa los datos de Y:\n")
		for i in range(1, c + 1):
			print("Dato para Y No.", i)
			dato = float(input(">: "))
			dY.append(dato)

		print("\nLa lista de datos de X es: ", d)
		print("La lista de datos de Y es: ", dY)
		meX = Media(d, c)
		mX = meX.getMedia(d, c)
		meY = Media(dY, c)
		mY = meY.getMedia(dY, c)

		covarianza = Covarianza(d, dY, mX, mY, c)
		print("\n	+- La media de X es: ", mX)
		print("	+- La media de Y es: ", mY)
		print("	+- La covarianza es: ", covarianza.getCovarianza(d, dY, mX, mY, c))
		getAnother(d, c, 5)

def chebyshevMenu():
	print("\n+-------------------+")
	print("+ Teorema Chebyshev +")
	print("+-------------------+")
	lI = int(input("\nIntroduce el límite Inferior: \n>: "))
	lS = int(input("Introduce el límite Superior: \n>: "))
	d.append(lI)
	d.append(lS)
	me = Media(d, 2)
	m = me.getMedia(d, 2)
	yi = [lI, m]
	ys = [lS, m]
	mI = Media(yi, 2)
	meI = mI.getMedia(yi,2)
	mS = Media(ys, 2)
	meS = mS.getMedia(ys,2)
	varI = Varianza(yi, meI, 2)
	varS = Varianza(ys, meS, 2)
	vI = varI.getVarianzaPoblacion(yi, meI, 2)
	vS = varS.getVarianzaPoblacion(ys, meS, 2)
	desI = varI.getDesv(vI)
	desS = varS.getDesv(vS)
	xi = (lI-m) / desI
	xs = (lS-m) / desS
	r = TeoremaChebyshev(xs)
	print("\n	+- La probabilidad es de: ", r.getTotal(xs), "%\n	+- Limite inferior de: ", lI, "\n	+- Limite superior de: ", lS)

	# m = float(input("\nIntroduce el valor de la media:\n>: "))
	# desv = float(input("\nIntroduce el valor de la desviación:\n>: "))
	# k = float(input("\nIntroduce el valor de k:\n>: "))
	# r = TeoremaChebyshev(m, desv, k)
	# lS = m + (2*desv)
	# lI = m - (2*desv)
	# print("\n	+- La probabilidad es de: ", r.getTotal(m, desv, k), "%\n	+- Limite inferior de: ", lI, "\n	+- Limite superior de: ", lS)

	askMain(6)

def bayesMenu():
	print("\n+---------------+")
	print("+ Teorema Bayes +")
	print("+---------------+")
	A = float(input("\nIntroduce el valor de A:\n>: "))
	B = float(input("Introduce el valor de B:\n>: "))
	Da = float(input("Introduce el valor de Da:\n>: "))
	Db = float(input("Introduce el valor de Db:\n>: "))
	pab = TeoremaBayes(A, B, Da, Db)
	pba = TeoremaBayes(A, B, Da, Db)
	print("\n	+- P(A|B) = ", pab.getTotalAB(A, B, Da, Db))
	print("	+- P(B|A) = ", pab.getTotalBA(A, B, Da, Db))
	askMain(7)

def esperanzaMenu():
	print("\n+----------------------+")
	print("+ Esperanza Matemática +")
	print("+----------------------+")
	c = int(input("\n¿Cuántos datos desea ingresar?: "))
	for i in range(c):
		print("Dato no.", i + 1)
		d.append(float(input(">: ")))
	if(sum(d)>1):
		print("Los datos no son aceptados, su suma es mayor a 1.")
		askMain()
	elif(sum(d)<1):
		print("Los datos no son aceptados, su suma es menor a 1.")
		askMain()
	else:
		p = EsperanzaMatematica(d)
		print("\n	+- Esperanza Matemática: ", p.getEsperanza(d))

	askMain(8)