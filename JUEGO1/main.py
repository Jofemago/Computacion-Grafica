import pygame
import random
from pantalla import *
from Player import *
from Enemy import *


ANCHO=400
ALTO=550
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

if __name__ =='__main__':

        pygame.init()
        pantalla=pygame.display.set_mode([ANCHO, ALTO])
        pan = Pantalla(pantalla, [ANCHO, ALTO])
        pan.MakePantalla()
        reloj = pygame.time.Clock()

        #SE CREA EL JUGADOR
        jg = Player(50, 50)
        jg.setPos(155, 400)

        #creo un grupo para darle manejo y dibujarlos
        Jugadores = pygame.sprite.Group()
        Jugadores.add(jg)
        Jugadores.draw(pantalla)


        #creo los rivales
        n = 10
        j = 50
        enemigos =  pygame.sprite.Group()
        for i in range(n):

            rival = Enemy(10,10)
            rival.rect.x = random.randrange(0, ANCHO)
            rival.rect.y = random.randrange(0, j) * -1
            j += 100
            enemigos.add(rival)

        enemigos.draw(pantalla)
        pygame.display.flip()

        fin  = False
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True


                #DECLARO LAS RUTINAS DEL TECLADO PARA EL MOV DEL JUGADOR
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        jg.dir = 1
                    if event.key == pygame.K_RIGHT:
                        jg.dir = 2
                    if event.key == pygame.K_UP:
                        jg.dir = 0

            ls_col = pygame.sprite.spritecollide(jg, enemigos, True)


            print jg.Vidas

            if jg.Vidas > 0 :
                pan.MakePantalla()

                jg.update()
                Jugadores.draw(pantalla)
                enemigos.update(jg)
                enemigos.draw(pantalla)


            else:
                print 'GAME OVER PUTO'
            pan.DrawVidas(jg)
            pygame.display.flip()
            reloj.tick(60)
