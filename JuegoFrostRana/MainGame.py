import pygame
import random
from pantalla import *
from Player import *
from Cars import *

ANCHO=448
ALTO=512
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

rue = 'spritesRana/'
sprites = ["up.png","left.png", "right.png", "down.png","jup.png","jleft.png", "jright.png", "jdown.png"]


if __name__ =='__main__':

    pygame.init()
    pantalla =  pygame.display.set_mode([ANCHO, ALTO])
    pan = Pantalla(pantalla, [ANCHO, ALTO],'spritesRana/background.png')
    #pan.MakePantalla()
    reloj = pygame.time.Clock()

    #SE CREA EL JUGADOR
    jg = Player([rue + i for i in sprites ])
    jg.setPos(0, 0)


    #grupo para guardar todos los sprites
    general = pygame.sprite.Group()

    #creo un grupo para darle manejo y dibujarlos
    Jugadores = pygame.sprite.Group()
    Jugadores.add(jg)
    general.add(jg)
    Jugadores.draw(pantalla)
    pygame.display.flip()


    #creo los carros rivales
    rivales = pygame.sprite.Group()
    car1 = Car('spritesRana/car-1.png',1,2,50)
    car1.rect.x = 448
    car1.rect.y = 420
    general.add(car1)
    rivales.add(car1)



    fin  = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            #"up.png","left.png", "right.png", "down.png",
            if event.type == pygame.KEYDOWN:
                jg.salto=True
                if event.key == pygame.K_RIGHT:
                    jg.var_x=20
                    jg.dir = 2
                if event.key == pygame.K_LEFT:
                    jg.var_x= -20
                    jg.dir = 1
                if event.key == pygame.K_UP:
                    jg.var_y=-20
                    jg.dir = 0
                if event.key == pygame.K_DOWN:
                    jg.var_y= 20
                    jg.dir = 3

            if event.type == pygame.KEYUP:
                jg.var_x=0
                jg.var_y=0


        Jugadores.update()
        rivales.update()
        pan.MakePantalla()

        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
