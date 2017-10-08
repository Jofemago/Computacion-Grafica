import math

def b(p,m):

	''' Retorna la constante b.

	b = mx + y

	parametros
	p -- lista con valores x,y del punto
	m -- pendiente de la recta
	'''

	res = -(m*p[0]) + p[1]
	return res

def Ecuacion(p,m):
	''' Retorna ecuacion de la recta
	y = mx+b

	Parametros:
	p -- lista con valores x,y del punto
	m -- pendiente de la recta
	'''

	c = b(p,m)
	ecuacion = 'y=' + str(m) + 'x'

	if (c < 0):
		ecuacion = ecuacion + str(c)
	else:
		ecuacion = ecuacion + '+' + str(c)

	return ecuacion


def Recta(m, b, xmin = 0, xmax = 10, inc = 1):
	''' Retorna valores de y para la ecuacion de la recta
		y = mx+b

		Parametros:
		m-- pendiente de la recta
		b-- constante de desplazamiento
		xmin -- Valor minimo de x
		xmax -- valor maximo de x
		inc -- Incremento o razon de cambio
	'''

	y = []
	if xmin > xmax:
		aux = xmin
		xmin = xmax
		xmax = aux

	i = xmin
	while i < xmax:

		val = (m*i)+b
		y.append(val)
		i+=inc
	return y

def Pendiente(p1, p2):
	''' Retorna la pendiente de una recta
 	m = (y2 -y1)/(x2 -x1)

 	Parametros;
 	p1 -- lista de valores x,y del punto 1
 	p2 -- lista de vallores x,y del punto 2

 	Excepciones:
 	Error division por cero si x2-x1 = 0
	'''

	num = p2[1] - p1[1]
	den = p2[0] - p1[0]

	try:
		val = num/den
		return val
	except ZeroDivisionError:
		return float('Inf')


def Vector(p1, p2): #arreglar excepcion para numero de elementos

	''' Retorna el vector canonico

	v = (p2[0] - p1[0]),..., p2[n] - p1[n])

	Parametros
	p1 -- punto incial
	p2 -- punto final

	'''
	r = len(p1)
	v = []
	for i in range(r):
		val = p2[i] - p1[i]
		v.append(val)
	return v

def Norma(v):
	'''Retorna la norma de un vector

	v = raiz ((vi*v1)+ ... + (vn*vn))
	Parametros:
	v-- vector
	'''
	r = len(v)
	suma = 0
	for i in range(r):
		suma += v[i]**2
	res = math.sqrt(suma)
	return res

def Unitario(v):
	''' Retorna el vector unitario de v

		w= v / norma(V)

		parametros:

		v -- vecotr

		Excepciones:
		Error de division por cer si Norma = 0
	'''
	u = []
	r = len(v)
	n = Norma(v)
	try:
		for i in range(r):
			val = v[i] / n
			u.append(val)
		return u
	except ZeroDivisionError:
		return float('inf')


def Punto(u,v , k = 1):

	''' Producto punto entre vectores u y v
		u vecetor
		v vector
		k escalar'''


	lon_u = len(u)
	try:
		suma = 0
		for i in range(lon_u):
			suma += k*(u[i]*v[i])
		return suma
	except Exception:
	#except Exception, ex:
		print (ex)

def Ec_Parametrica(p, v, t=1, ver = 0):
	'''Retorna ecuacio parametrica dado un punto y un vector
	x = x0-t.vx
	y = y0 -t.vy

	Parametros:
	p -- punto P de la rectaa
	v --vector
	t parametro por defeco 1
	ver -- ver ecuacion 0:no 1:si
	'''
	if ver == 0:
		x = p[0] + (t * v[0])
		y = p[1] +(t * v[1])
		return [x,y]

	else:
		s_x = 'x='+ str(p[0])+'+ (' + str(v[0]) + ')t'
		s_y = 'y='+ str(p[1])+'+ (' + str(v[1]) + ')t'
		com = 'para t =' + str(t)
		return[s_x,s_y,com]


def EcRecta_Cartesiana(p, v):
	''' Rertorna la ecuacion cartesiana de la recta

	Ax + By + C = 0
	A =v2
	B = v1
	c = xoV2 + yoV1

	Parametros:
	p --- punto P de la recta
	v --- vetor director

	'''

	c = -(p[0] * v[1]) + (p[1] * v[0])
	ec = str(v[1]) + 'x + '+ str(-v[0]) + 'y + ' +str(c) +' = 0'
	return ec

if __name__ == "__main__":

	#print (b([5,5],3))
	#print(Ecuacion([4,0],-4))
	#print(Recta(3,-1))
	#v= Vector([1,3,3],[2,-1,5])
	#print(Norma([2.0, -2.0]))
	#print(Unitario([4.0,3.0]))
	#print (Punto([4,-1],[3,3],2))
	#print(Vector([-1,2],[2,4]))
	#print(Ec_Parametrica([-1,2],[3,2]))
	print(EcRecta_Cartesiana([-1,2], [3,2]))
