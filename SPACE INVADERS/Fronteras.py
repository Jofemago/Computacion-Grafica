
import pygame
from configuraciones import *

class limite(pygame.sprite.Sprite):
    al = 800
    an = 2
    def __init__(self, cl = ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.al,self.an])
        self.cl = cl
        self.image.fill(self.cl)
        self.rect= self.image.get_rect()

    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y
