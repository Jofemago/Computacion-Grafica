import pygame
import random

from player import *
from configuraciones import *

if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()

    pl = plataforma()
    pl.rect.x = 300
    pl.rect.y= 450

    pl1 = plataforma()
    pl1.rect.x = 500
    pl1.rect.y= 350


    pl2 = plataforma()
    pl2.rect.x = 300
    pl2.rect.y= 450

    fondo = pygame.image.load('fondo.jpg')

    jg = Player(50,50)

    print fondo.get_rect()
    #lim_img =
    #jg.rect.x = 0
    #jg.rect.y = 0

    jugadores.add(jg)

    general.add(pl)
    general.add(pl1)
    plataformas.add(pl)
    plataformas.add(pl1)
    plataformas.add(pl2)
    general.add(jg)
    jg.plataformas = plataformas

    reloj = pygame.time.Clock()
    fin  = False

    lim_der = 700
    f_x = 0
    f_varx = 0
    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 5


                if event.key == pygame.K_LEFT:

                    jg.var_x = -5

                if event.key == pygame.K_UP:
                    #jg.gritar()
                    jg.salto()
                    #jg.var_y = -10

            if event.type == pygame.KEYUP:

                #jg.var_y = 0
                if event.key == pygame.K_RIGHT  :
                    jg.var_x = 0
                if event.key == pygame.K_LEFT   :

                    jg.var_x = 0

        #ciclo de juego


        #esto define el movimiento de la imagen, cuando corro hacia la izquierda
        if jg.rect.x > lim_der - jg.rect.width:#si esta en la parte que quiero que se empiece a desplazar la pantalla
            jg.rect.x = lim_der - jg.rect.width #dejelo en la misma pos
            f_varx = -5 #varie la pos del fondo el fondo para que aparentar moviendo
        elif jg.rect.x < jg.rect.width:
            jg.rect.x = jg.rect.width
            f_varx = 5
        else:
            f_varx = 0

        f_x += f_varx
        for e in plataformas:
            print e.rect.x
            e.rect.x += f_varx

        pantalla.fill(NEGRO)
        pantalla.blit(fondo,[f_x,0])
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
        #f_x -= 1
