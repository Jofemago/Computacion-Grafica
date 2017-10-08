import pygame
from Player import *

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, ANCHO, ALTO , COLOR = ROJO):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Crear la imagen que va ser un bloque que representa el Jugador
        self.image = pygame.Surface([ANCHO, ALTO])
        self.image.fill(COLOR)

        #posiciion del objeto, importante para poder ubicarlo en patanlla
        self.rect = self.image.get_rect()

        self.vel = 3

    def movDown(self):

        self.rect.y += self.vel

    def setPos(self, x, y):


        self.rect.x = x
        self.rect.y = y


    def update(self, jugador):

        if self.rect.y >= 440:
            self.kill()
            jugador.Vidas -=1
        else:
            self.movDown()
