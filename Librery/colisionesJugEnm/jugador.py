import pygame


class Jugador(pygame.sprite.Sprite):

    def __init__(self, alto, ancho, col ):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.ancho = ancho
        self.alto = alto
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.col = col
        self.colision = False
        self.teclado = 0

    def update(self):

        if self.colision == True:
            self.alto = self.alto + 5
            self.ancho = self.ancho + 5
            self.image = pygame.Surface([self.ancho, self.alto])
            self.rect = self.image.get_rect()
            self.image.fill(self.col)
            self.col = False

        if self.teclado == 1:

            pass
