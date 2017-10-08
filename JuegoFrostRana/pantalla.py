import pygame
from Player import *


BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Pantalla:

    def __init__(self, pantalla, AnAl, fondo):

        self.p = pantalla
        self.AnAl = AnAl
        self.fondo = pygame.image.load(fondo)

    def MakePantalla(self):

        self.p.fill(NEGRO)
        self.p.blit(self.fondo,[0,0])


        pygame.display.flip()
