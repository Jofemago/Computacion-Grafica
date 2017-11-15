import json

if __name__ == '__main__':

    archivo = 'mapa01.json'
    with open(archivo) as archivo_json:
        mapa = json.load(archivo_json)

    '''for valor in mapa['layers']:

        print valor'''

    capa1 = mapa['layers'][0]
    capa2 = mapa['layers'][1]
    '''for v in capa1:
        print v
    '''
    #print 'nombre:', capa1['name']
    #print 'datos:', capa1['data']

    num_col = capa2['width']
    num_filas = capa2['height']
    linea = capa2['data']

    #print 'datos:', linea

    m = []
    i = 0
    for f in range(num_filas):
        fila = []
        for c in range(num_col):
            v = linea[i]
            fila.append(v)
            i+=1
        m.append(fila)

    for fila in m:
        print fila
