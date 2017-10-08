import pygame
from jugador import *
from Rival import *
#from Plano import *
#from LibPolares import *
#from Images import *
#from Algebralineal import *
import random

ANCHO=400
ALTO= 400
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)


def printPantalla(surface):
    surface.fill(NEGRO)
    rect = pygame.Rect(0,350, 400, 50)
    pygame.draw.rect(surface,BLANCO, rect)
    #pygame.draw.polygon(surface, BLANCO, [(0,350), (ANCHO,350) , (ANCHO,ALTO) ,(0, ALTO) ], 0)



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    #printPantalla(pantalla)
    pantalla.fill(NEGRO)
    #spritep
    jp = Jugador(50,50, AZUL)
    jp.rect.x = 200
    jp.rect.y = 300
    #grupo de sprite
    Jugadores = pygame.sprite.Group()
    Jugadores.add(jp)


    rojos = pygame.sprite.Group()
    n = 10
    for i in range(n):

        nb = Rival(25,25, ROJO)
        nb.rect.x = random.randrange(0, ANCHO)
        nb.rect.y = random.randrange(0, 325)
        rojos.add(nb)

    #bloques.draw(pantalla)

    #pygame.display.flip()
    reloj = pygame.time.Clock()
    fin  = False
    puntos = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        #ciclo de juego
        #pantalla.fill(NEGRO)
        pos = pygame.mouse.get_pos()
        jp.rect.x = pos[0] -20
        jp.rect.y = pos[1] -20


        #colision
        ls_col = pygame.sprite.spritecollide(jp, rojos, False)
        for elemento in ls_col:
            jp.colision= True

        #rojos.update()
        #printPantalla(pantalla)
        #pantalla.fill(NEGRO)
        #rect = pygame.Rect(0,350, 400, 50)
        #pygame.draw.rect(pantalla,BLANCO, rect)
        jp.update()
        Jugadores.draw(pantalla)
        rojos.draw(pantalla)
        pygame.display.flip()
        #reloj.tick(60)
