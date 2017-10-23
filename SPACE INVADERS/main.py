import pygame
import random

from Player import *
from configuraciones import *
#from Proyectil import *
#from Enemys import *


if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    #fondo = pygame.image.load('imagenes/fondo.jpg')
    #creamos  grupos 
    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()


    #creamos jugador
    jg = Player('imagenes/nave1.png',10)
    jugadores.add(jg)
    general.add(jg)

    reloj = pygame.time.Clock()
    fin  = False


    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYUP:
            	if event.key == pygame.K_RIGHT:
            		jg.var_x = 0
            	if event.key == pygame.K_LEFT:

                    jg.var_x = 0
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 5

                if event.key == pygame.K_LEFT:

                    jg.var_x = -5


		pantalla.fill(NEGRO)
		general.update()
		general.draw(pantalla)
       
       # pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(60)