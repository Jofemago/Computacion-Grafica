import pygame

from configuraciones import *


class bloque(pygame.sprite.Sprite):

    def __init__(self, ancho,alto,  col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)

        self.rect = self.image.get_rect()
        #self.setPos(100,400)
        self.rect.x = 200
        self.rect.y = 200
        self.click = False #indicarle si se ha dado click sobre el


    def update(self):
        #self.rect.y += 1
        if self.click:
            self.rect.center = pygame.mouse.get_pos() #cada que doy click actulizo

class bloquebase(pygame.sprite.Sprite):

    def __init__(self, ancho,alto,  col = AZUL):

        self.col = col
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)

        self.rect = self.image.get_rect()
        #self.setPos(100,400)
        self.rect.x = 200
        self.rect.y = 200
        self.click = False #indicarle si se ha dado click sobre el


    def update(self):
        #self.rect.y += 1
        if self.click:
            pass
