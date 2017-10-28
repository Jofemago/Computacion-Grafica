import pygame
from configuraciones import *


class ProyectilJugador(pygame.sprite.Sprite):

    def __init__(self, dir, col = VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 10])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.dir = dir
        self.var_y = 10

    def update(self):
        if self.dir == 2: #abajo arriba

            self.rect.y  -= self.var_y

        if self.dir == 1:#arriba a abajo

            self.rect.y  += self.var_y

        if self.dir == 1 and self.rect.y > ALTO:
            self.kill()
        if self.dir == 2 and self.rect.y < 0:
            self.kill()
