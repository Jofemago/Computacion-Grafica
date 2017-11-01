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
    bloques = pygame.sprite.Group()

    base1 = bloquebase(50,50, AZUL)
    base2 = bloquebase(50,50, VERDE)


    general.add(base1)
    base1.rect.x = 10
    base1.rect.y = 540
    base2.rect.x = 65
    base2.rect.y = 540



    general.add(base2)


    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if base2.rect.collidepoint(event.pos): #si el onbjto choca con el mouse cuando hay click
                    b = bloque(50,50, base2.col)
                    b.rect.x = base2.rect.x
                    b.rect.y = base2.rect.y
                    #b.click = True
                    general.add(b)
                    bloques.add(b)
                if base1.rect.collidepoint(event.pos): #si el onbjto choca con el mouse cuando hay click
                    b = bloque(50,50, base1.col)
                    b.rect.x = base1.rect.x
                    b.rect.y = base1.rect.y
                    #b.click = True
                    general.add(b)
                    bloques.add(b)
                for b in bloques:
                    if b.rect.collidepoint(event.pos):
                        b.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                for b in bloques:
                    b.click = False



        pantalla.fill(BLANCO)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
        #f_x -= 1
