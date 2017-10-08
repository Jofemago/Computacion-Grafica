import pygame
from configuraciones import *


class Proyectil(pygame.sprite.Sprite):

    def __init__(self, dir, col = VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.dir = dir
        self.var_x = 10

    def update(self):
        if self.dir == 2: #derecha a izquierda

            self.rect.x  -= self.var_x

        if self.dir == 1:#izquierda a derecha

            self.rect.x  += self.var_x

        if self.dir == 1 and self.rect.x > ANCHO:
            self.kill()
        if self.dir == 2 and self.rect.x < 0:
            self.kill()
