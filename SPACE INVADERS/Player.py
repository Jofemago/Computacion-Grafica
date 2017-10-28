'''
Se crea una clase jugador la cual tendra un movimiento con los teclas
y dispara
'''

import pygame
from configuraciones import *


class Vida(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()


    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):

    def __init__(self,img, vidas = 3,  col = AZUL):


        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.setPos(400,ALTO - 100)

        #variables de movimiento
        self.var_x = 0

        self.vidas = vidas

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def setX(self, x):

        self.rect.x = x

    def setX(self, y):

        self.rect.x = y

    def movX(self):

        if self.rect.x >= ANCHO -50 and self.var_x >= 0:
            self.var_x = 0

        if self.rect.x <= 0 and self.var_x <= 0:
            self.var_x = 0


        self.rect.x += self.var_x



    def update(self):

        self.movX()
