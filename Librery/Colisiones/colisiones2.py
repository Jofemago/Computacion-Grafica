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

class Jugador(pygame.sprite.Sprite):

    def __init__(self,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        #self.image.fill(col)
        self.rect = self.image.get_rect()

class Rival(pygame.sprite.Sprite):

    def __init__(self,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        #self.image.fill(col)
        self.rect = self.image.get_rect()
        self.var_x = 2
        self.dir = 1

    def update(self):
        if self.rect.x < ANCHO - self.rect.width and self.dir == 1:
            self.rect.x += self.var_x
        else:

            self.dir = 2
            self.rect.x  -=  self.var_x
        if self.rect.x <= 0 and self.dir == 2:

            self.dir = 1
            #self.var_x+= 2



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    #spritep
    jp = Jugador('pokebols.png')
    jp.rect.x = 100
    jp.rect.y = 100
    #grupo de sprite
    Jugadores = pygame.sprite.Group()
    Jugadores.add(jp)


    rojos = pygame.sprite.Group()
    n = 10
    for i in range(n):

        nb = Rival('pikapika.png')
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
        jp.rect.x = pos[0] -20
        jp.rect.y = pos[1] -20


        #colision
        ls_col = pygame.sprite.spritecollide(jp, rojos, True)
        for elemento in ls_col:
            puntos += 1
            print puntos

        rojos.update()
        Jugadores.draw(pantalla)
        rojos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
