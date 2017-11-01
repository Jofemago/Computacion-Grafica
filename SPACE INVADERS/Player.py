'''
Se crea una clase jugador la cual tendra un movimiento con los teclas
y dispara
'''

import pygame
from configuraciones import *

TIEMPODESTRUCION = 8


class Vida(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()


    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):

    def __init__(self,img, imgdestru, vidas = 3,  col = AZUL):


        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img).convert_alpha()
        self.image = pygame.image.load(img).convert_alpha()
        self.imagedestruida = pygame.image.load(imgdestru).convert_alpha()
        self.rect = self.image.get_rect()
        self.setPos(400,ALTO - 80)
        self.disparo = pygame.mixer.Sound('Sonidos/disparojg.ogg')

        #variables de movimiento
        self.var_x = 0

        self.vidas = vidas

        #tiempo que durara destruida
        self.destrucion = False
        self.tiempodes = TIEMPODESTRUCION

    def disparar(self):
        self.disparo.play()

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
        if self.destrucion:
            self.image = self.imagedestruida
            if self.tiempodes <= 0:
                self.image = self.img
                self.destrucion = False
                self.tiempodes = TIEMPODESTRUCION
            self.tiempodes -= 1
        else:
            self.movX()
