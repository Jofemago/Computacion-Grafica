import pygame
from Plano import *
#from LibPolares import *
#from Images import *
from Algebralineal import *
import random

ANCHO=640
ALTO=480
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Bloque(pygame.sprite.Sprite):

    def __init__(self, alto, ancho, col = AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)
        self.rect = self.image.get_rect()



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    #sprite
    b = Bloque(70, 50)
    b.rect.x = 100
    b.rect.y = 100
    #grupo de sprite
    bloques = pygame.sprite.Group()
    bloques.add(b)


    rojos = pygame.sprite.Group()
    n = 10
    for i in range(n):

        nb = Bloque(20,20, ROJO)
        nb.rect.x = random.randrange(0, ANCHO)
        nb.rect.y = random.randrange(0, ALTO)
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
        pantalla.fill(NEGRO)
        pos = pygame.mouse.get_pos()
        b.rect.x = pos[0]
        b.rect.y = pos[1]


        #colision
        ls_col = pygame.sprite.spritecollide(b, rojos, True)
        for elemento in ls_col:
            puntos += 1
            print puntos

        bloques.draw(pantalla)
        rojos.draw(pantalla)
        pygame.display.flip()
