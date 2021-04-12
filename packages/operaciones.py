#!/usr/bin/python
#coding: utf-8

# Filename  : operaciones.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/XX
# pep8: 100%

# Importaciones

import statistics as stat
import math

class Operaciones(object):


	def __init__(self, d):
		self.datos = d


class Media(Operaciones):


	def __init__(self, d, c):
		super().__init__(d)
		self.cantidad = c


	def getMedia(self, d, c):
		return sum(self.datos) / self.cantidad

class Mediana(Operaciones):


	def __init__(self, d, c, dS):
		super().__init__(d)
		self.cantidad = c
		self.dataSorted = dS


	def getMediana(self, d, c, dS):
		if(self.cantidad % 2 == 0):
			return (self.dataSorted[(self.cantidad//2)-2] + self.dataSorted[(self.cantidad//2)+1])/2
		else:
			y = self.cantidad//2
			return self.dataSorted[y]
		
class Moda(Operaciones):


	def __init__(self, d, dS):
		super().__init__(d)
		self.dataSorted = dS


	def getModa(self, d, dS):
		return stat.mode(self.dataSorted)
		
class Varianza(Operaciones):


	def __init__(self, d, m, c):
		super().__init__(d)
		self.media = m
		self.cantidad = c


	def getVarianzaMuestra(self, d, m, c):
		s = 0
		for i in d:
			s += (i - self.media)**2

		return s / (c - 1)


	def getVarianzaPoblacion(self, d, m, c):
		s = 0
		for i in d:
			s += (i - self.media)**2

		return s / (c)


	def getDesv(self, v):
		self.varianza = v
		return math.sqrt(v)

class Covarianza(Operaciones):


	def __init__(self, d, dY, mX, mY, c):
		super().__init__(d)
		self.datosY = dY
		self.mediaX = mX
		self.mediaY = mY
		self.cantidad = c


	def getCovarianza(self, d, dY, mX, mY, c):
		sumaXY = 0
		for x in range(self.cantidad):
			sumaXY = sumaXY + ((self.datos[x] - self.mediaX)*(self.datosY[x] - self.mediaY))

		return sumaXY / self.cantidad

class EsperanzaMatematica(Operaciones):


	def __init__(self, d):
		super().__init__(d)


	def getEsperanza(self, d):
		x = 0
		r = 0
		for i in d:
			r += x * i
			x +=1

		return round(r,2)

class TeoremaChebyshev(object):


	def __init__(self, k):
		self.k = k


	def getTotal(self, k):
		return (1 - (1 / (self.k)**2)) * 100

class TeoremaBayes(object):


	def __init__(self, A, B, Da, Db):
		self.A = A
		self.B = B
		self.Da = Da
		self.Db = Db


	def getTotalAB(self, A, B, Da, Db):
		return (self.Da * self.A) / ((self.A * self.Da) + (self.B * self.Db))


	def getTotalBA(self, A, B, Da, Db):
		return (self.Db * self.B) / ((self.B * self.Db) + (self.A * self.Da))