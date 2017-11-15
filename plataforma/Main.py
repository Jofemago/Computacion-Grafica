import pygame
import random



from configuraciones import *


if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()



    reloj = pygame.time.Clock()
    fin  = False





    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        reloj.tick(60)
        #f_x -= 1
