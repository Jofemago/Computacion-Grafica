import pygame
import random


from configuraciones import *
from bloque import *



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()



    reloj = pygame.time.Clock()
    fin  = False

    general = pygame.sprite.Group()

    b = bloque(50,50)
    general.add(b)


    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b.rect.collidepoint(event.pos): #si el onbjto choca con el mouse cuando hay click
                    b.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                b.click = False



        pantalla.fill(BLANCO)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
        #f_x -= 1
