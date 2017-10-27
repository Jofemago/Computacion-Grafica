import pygame
#import ConfigParser
from jugador import *
from rival import *

import configuraciones
#import random

ANCHO=700
ALTO=700
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)


if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    general = pygame.sprite.Group()
    rivales = pygame.sprite.Group()

    rival = enemigo(50,50,'recursos/target.png',ROJO)
    jg = player(50,50,'recursos/mira.png')


    general.add(rival)
    general.add(jg)
    rivales.add(rival)

    fondo = pygame.image.load('recursos/fondo.jpeg')

    pygame.display.flip()
    pygame.mouse.set_visible(0)
    fin  = False
    puntos = 0

    punt = 0#puntos
    bal = 3#balas disponibles

    f_x = -500 #pos del fondo en x
    f_varx = 0 #variacion del fondo en x
    balas=pygame.font.Font(None, 15)
    points=pygame.font.Font(None, 15)
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True



            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    bal -= 1
                    for r in rivales:
                        if r.rect.collidepoint(jg.rect.center):#dectete que el jugador esta encima de el

                            #if mouse[0] and bal > 0:#si tiene presiionado click izquierdo
                            r.kill()#que lo elimine
                            #bal -= 1
                            punt += 1


        mov_mouse = pygame.mouse.get_pos()#movimiento con el mouse
        jg.rect.x = mov_mouse[0] - 25
        jg.rect.y = mov_mouse[1] - 25

        if jg.rect.x > 700 - jg.rect.width:#movimiento de la pantalla
            jg.rect.x = 700 - jg.rect.width
            if f_x <= (2060-ANCHO)*-1:
                f_varx = 0
                #f_x = -2060
            else:
                f_varx = -5
        elif jg.rect.x < 20:
            jg.rect.x = 20
            if f_x > 0:
                f_varx = 0
            else:
                f_varx = 5
        else:
            f_varx = 0
        for r in rivales:
            r.rect.x += f_varx
        f_x = f_x + f_varx


        salida = points.render( 'Puntos: '+str(punt), True, BLANCO)
        salida2 = balas.render( 'Balas: '+str(bal), True, BLANCO)

        pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_x,-800])
        pantalla.blit(salida, [100, 650])
        pantalla.blit(salida2, [500, 650])
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
