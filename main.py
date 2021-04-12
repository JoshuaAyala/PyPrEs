#!/usr/bin/python
#coding: utf-8

# Filename  : main.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/XX
# pep8: 100%

# Importaciones
from packages.banners import *
from packages.menus import *
from packages.operaciones import *

import os, time, random
import statistics as stat


randBan = random.randint(1, 2) # Generación de numero aleatorio para diferente banner

# Declaración de variables esenciales
gotData = False 
d = []
c = 0

# Función Main
def main():
	if(randBan == 1):
		banner1()
	elif(randBan == 2):
		banner2()
	mainMenu(gotData, d, c)

main()