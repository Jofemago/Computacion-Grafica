import pygame
import random

from Player import *
from configuraciones import *
from Fronteras import *
from Escudo import *
from Balas import *
#from Enemys import *


if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    #fondo = pygame.image.load('imagenes/fondo.jpg')
    #creamos  grupos
    jugadores = pygame.sprite.Group()
    limites = pygame.sprite.Group()
    Escudos = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    disparosMaquina = pygame.sprite.Group()
    disparosJugador = pygame.sprite.Group()
    general = pygame.sprite.Group()


    #creamos jugador
    jg = Player('imagenes/nave1.png',3)
    jugadores.add(jg)
    general.add(jg)


    #se crea y ubica el limite superior y inferior
    superior =limite()
    inferior = limite()
    superior.setPos(0,68)
    inferior.setPos(0,598)
    limites.add(superior)
    limites.add(inferior)
    general.add(superior)
    general.add(inferior)


    #se crean los escudos
    for i in range(0,20):
        for j in range(0,15):

            es = Escudo()
            es.setPos(75 + i*5,450 + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(250 + i*5,450 + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(425 + i*5,450 + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(600 + i*5,450 + j* 5)
            general.add(es)
            Escudos.add(es)


    #se crean las vidas del jugador
    for vida in range(jg.vidas - 1):
        v = Vida('imagenes/nave1.png')
        v.rect.x = 5 + vida * 75
        v.rect.y = ALTO - jg.rect.height
        vidas.add(v)
        general.add(v)


    reloj = pygame.time.Clock()
    fin  = False

    print jg.rect.height
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 5

                if event.key == pygame.K_LEFT:

                    jg.var_x = -5

                if event.key == pygame.K_SPACE:

                    if len(disparosJugador) == 0:
                        bala = ProyectilJugador(2)
                        bala.rect.x = jg.rect.x + 22
                        bala.rect.y = jg.rect.y +5
                        disparosJugador.add(bala)
                        general.add(bala)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and jg.var_x > 0:

                    jg.var_x = 0

                if event.key == pygame.K_LEFT and jg.var_x < 0:

                    jg.var_x = 0


        pantalla.fill(NEGRO)
        general.update()
        general.draw(pantalla)

       # pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(60)
