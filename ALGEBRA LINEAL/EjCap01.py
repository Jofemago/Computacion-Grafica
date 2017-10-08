from cap01Lineal import *

def isPerpendicular(A1, A2, B1, B2):
	''' Valida si puntos dados forman vectores perpendiculares
		
		Parametros:

		A1 punto 1 vector 1
		A2 punto 2 vector 1
		B1 punto 1 vector 2
		B2 punto 2 vector 2

	'''
	v = Vector(A1, A2)
	u = Vector(B1, B2)

	ppunto = Punto(v, u)

	if ppunto == 0:
		return True
	else:
		return False


def IsParalelo(A1, A2, B1, B2):
	''' Valida si puntos dados forman vectores paralelos
		
		Parametros:

		A1 punto 1 vector 1
		A2 punto 2 vector 1
		B1 punto 1 vector 2
		B2 punto 2 vector 2

	'''
	v = Vector(A1, A2)
	u = Vector(B1, B2)
	

if __name__ == "__main__":

	print(isPerpendicular([2,1],[5,1],[4,0],[4,4]))