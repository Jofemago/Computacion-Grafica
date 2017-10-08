import pygame
from Player import *


BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Pantalla:

    def __init__(self, pantalla, AnAl):

        self.p = pantalla
        self.AnAl = AnAl

    def MakePantalla(self):

        self.p.fill(NEGRO)
        rect = pygame.Rect(0,450, 400, 100)
        pygame.draw.rect(self.p,BLANCO, rect)
        pygame.display.flip()


    def DrawVidas(self, Jugador):

        rect = pygame.Rect(25,500, Jugador.Vidas * 10, 25)
        pygame.draw.rect(self.p,ROJO, rect)
