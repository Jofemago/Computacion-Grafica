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


    jg = Player(50,50)
    #jg.rect.x = 0
    #jg.rect.y = 0

    jugadores.add(jg)
    general.add(jg)

    reloj = pygame.time.Clock()
    fin  = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYUP:

                jg.var_y = 0
                jg.var_x = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 5

                if event.key == pygame.K_LEFT:

                    jg.var_x = -5

        pantalla.fill(NEGRO)

        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
