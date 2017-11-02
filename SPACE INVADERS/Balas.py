import pygame
from configuraciones import *


class ProyectilJugador(pygame.sprite.Sprite):

    def __init__(self, dir, col = VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.imgdestr = pygame.image.load('imagenes/destrbala.png').convert()
        self.image = pygame.Surface([3, 10])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.dir = dir
        self.var_y = 10

        self.choque = False
        self.TiempoDesaparece = 10

    def update(self):

        if self.choque:
            self.image = self.imgdestr
            self.rect.y = 70
            if self.TiempoDesaparece <= 0:
                self.kill()
            self.TiempoDesaparece -= 1
        elif self.dir == 2: #abajo arriba

            self.rect.y  -= self.var_y

        elif self.dir == 1:#arriba a abajo

            self.rect.y  += self.var_y


class ProyectilEnemigo(pygame.sprite.Sprite):

    def __init__(self, dir, sprites):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = sprites
        self.mov = 0#movimiento del sprite la posicion 2 indica que el sprite ha muerto
        self.color = 3# posicion de los sprites dependiendo de la pos que se encuentre en un momento determinado
        self.image = self.sprites[self.mov][self.color]
        self.imgdestr = pygame.image.load('imagenes/destrbala.png').convert()
        #traje la imagen ya estan los sprites aca falta generar el mov y cambiar el sprite cada que se mueve y hacer las pruebas
        #respectivas con esto


        self.rect = self.image.get_rect()
        self.dir = dir
        self.var_y = 10

        self.choque = False
        self.TiempoDesaparece = 10


        self.color = 0

    def calcularColor(self):
        if self.rect.y < 100:
            self.color = 1
        elif self.rect.y >= 100 and self.rect.y <= 225:
            self.color = 2
        elif self.rect.y > 225 and self.rect.y <= 350:
            self.color = 3

        elif self.rect.y > 350:
            self.color = 0

    def movY(self):
        self.calcularColor() #calculo el color de bajada con el que los sprites se deben presentar
        self.rect.y += self.var_y
        if self.mov > 1:
            self.mov = 0
        self.image = self.sprites[self.mov][self.color]
        self.mov +=1

    def update(self):

        if self.choque:
            self.image = self.imgdestr
            self.rect.y = 608
            if self.TiempoDesaparece <= 0:
                self.kill()
            self.TiempoDesaparece -= 1

        else:
            self.movY()
