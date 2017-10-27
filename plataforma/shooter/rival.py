
import pygame

from configuraciones import *


class enemigo(pygame.sprite.Sprite):

    def __init__(self, ancho, alto,img,  col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        #self.setPos(100,400)
        self.rect.x = 200
        self.rect.y = 200
        self.dir = 0


    def update1(self):#movimiento de izquierda a derecha del mouse

        if self.dir:#direccion igual a 1

            if self.rect.x + self.rect.width > ANCHO:
                self.rect.x = ANCHO -  self.rect.width
                self.dir = 0
            else:
                self.rect.x += 5
        else:
            if self.rect.x <= 0:
                self.dir = 1
            else:
                self.rect.x -= 5
