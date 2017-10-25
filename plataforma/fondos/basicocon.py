import ConfigParser

archivo = 'map.map'
interprete = ConfigParser.ConfigParser()
interprete.read(archivo)
print interprete.sections()

"""
print interprete.get('nivel1','fuente') #en la etiqueta nivel 1 qe hay en fuente
print interprete.get('.','tipo'), interprete.get('.','x'), interprete.get('.','y')#en la etiqueta punto que tipo es
print interprete.get('nivel1','mapa')#en la etique muestreme el mapa
"""

for s in interprete.sections():#muestreme todas las secciones que existen
    print s


#tomar el mapa
mapa = interprete.get('nivel1','mapa')
print mapa
'''print '==================================='
for f in mapa:#muesta todo con saltos de linea
    print f'''
print '==================================='
mapa = mapa.split('\n') #dividame el mapa por filas cada fila en una lista y todas las listas en otra lista
print mapa

nf = 0

for f in mapa:
    print nf, f[2]#de cada fila muestreme el tercer elemento
    nf += 1

print '==================================='

fila_ejemplo = mapa[1]#muestreme la segunda fila
print fila_ejemplo

for e in fila_ejemplo: #por cada elemento que exista en la fila 2 muestreme que tipo es y cual es su pos en x y y
    print e, interprete.get(e,'tipo'), interprete.get('.','x'), interprete.get('.','y')

print '==================================='
#manejarlo como un diccionario
print interprete.items('.')
dic_sec = dict( interprete.items('.'))
print dic_sec['tipo']
