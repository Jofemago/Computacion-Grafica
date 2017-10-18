'''
Se crea una clase jugador la cual tendra un movimiento con los teclas
y dispara
'''

import pygame
from configuraciones import *


class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(VERDE)
        self.rect= self.image.get_rect()

class Player(pygame.sprite.Sprite):

    def __init__(self, ancho, alto, col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.setPos(0,0)

        #variables de movimiento
        self.var_x = 0
        self.var_y = 0
        #self.vidas = vidas

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

    def movY(self):


        if self.rect.y >= ALTO -60 and self.var_y >= 0:
            self.var_y = 0

        if self.rect.y <= 100 and self.var_y <= 0:
            self.var_y = 0

        self.rect.y += self.var_y

    def update(self):

        if self.var_y == 0:
            self.var_y = 1
        else:
            self.var_y += 0.35
        self.movX()
        self.movY()
