
import pygame

from configuraciones import *


class player(pygame.sprite.Sprite):

    def __init__(self, ancho, alto,img, col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()

        self.rect = self.image.get_rect()
        #self.setPos(100,400)
        self.rect.x = 100
        self.rect.y = 400
