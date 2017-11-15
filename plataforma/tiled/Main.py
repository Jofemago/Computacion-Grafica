import pygame
import random
import json



from configuraciones import *


if __name__ =='__main__':
    #pygame.init()
    #pantalla=pygame.display.set_mode([ANCHO, ALTO])
    #pygame.display.flip()

    import json

    print "Leer archivos"
    mapajson = json.loads(open('mapa01.json').read())
    #print mapajson


    print mapajson['layers'][0]
    print '----------------------------------------------------------------'
    print type(mapajson['layers'][1])
    print '----------------------------------------------------------------'
    print type(mapajson['tilesets'][0])
    #print type(mapajson['layers'][0]['data'][0])
    reloj = pygame.time.Clock()
    fin  = False
    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha
    '''while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        reloj.tick(60)
        #f_x -= 1'''
