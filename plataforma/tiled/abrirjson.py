import json

if __name__ == '__main__':

    archivo = 'mapa01.json'
    with open(archivo) as archivo_json:
        mapa = json.load(archivo_json)


    info = None
    info = mapa['tilesets'][0]

    '''
    for valor in mapa['tilesets']:
        print valor
        info = valor

    img_nom = ''
    for v in info:
        #print v, ':' , info[v]
        if v == 'image':
            img_nom = info[v]

    print img_nom'''
    print info['image']
