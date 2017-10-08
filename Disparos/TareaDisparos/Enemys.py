import random
import pygame
from configuraciones import *

class EnemyDos(pygame.sprite.Sprite):

    def __init__(self,timeAct,col = ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO
        self.dir = 1
        self.var_x = 3
        self.timeAc = timeAct
        self.temporizador = timeAct
        self.disparo = False

    def update(self):


        if self.rect.x < ANCHO /2:

            self.var_x = 0


            #self.var_x+= 2
        if self.temporizador < 0:

            self.temporizador = self.timeAc
            self.disparo = True

        self.temporizador -= 1
        self.rect.x -= self.var_x


class Enemy(pygame.sprite.Sprite):

    def __init__(self,timeAct,col = ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO
        self.dir = 1
        self.var_x = 3
        self.timeAc = timeAct
        self.temporizador = timeAct
        self.disparo = False




    def update(self):


        if self.rect.x < -25:

            self.kill()


            #self.var_x+= 2
        if self.temporizador < 0:

            self.temporizador = self.timeAc
            self.disparo = True

        self.temporizador -= 1
        self.rect.x -= self.var_x
