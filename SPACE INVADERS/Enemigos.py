import random
import pygame
from configuraciones import *

class Enemigo1(pygame.sprite.Sprite):

    def __init__(self,timeAct,row, col = ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.var_y = 0
        self.var_x = 10
        self.m = 0
        self.movs = [pygame.mixer.Sound('Sonidos/movimiento1.wav'),pygame.mixer.Sound('Sonidos/movimiento2.wav'),pygame.mixer.Sound('Sonidos/movimiento3.wav'),pygame.mixer.Sound('Sonidos/movimiento4.wav')]
        self.movimiento = self.movs[0]

        self.TiempoMov = 50
        self.temporizadormov = timeAct
        self.dir  = True
        self.row = row

        self.bajar = False
        self.Bajo = False
        self.contbajar = 0

        self.aliados = []
    def moverse(self):


        if self.temporizadormov > 0:
            self.movimiento = self.movs[self.m]
            self.movimiento.play()
            self.m += 1
            if self.m == 4:
                self.m = 0

    def Setdir(self):
        self.dir = not self.dir


    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def movY(self):

        self.rect.y += self.var_y

    def MovX(self):

        if self.temporizadormov <= 0:
            #self.ValidarDir()
            if self.dir:
                self.rect.x += self.var_x
            else:
                self.rect.x -= self.var_x
            self.temporizadormov = self.TiempoMov
            self.moverse()
        else:
            self.temporizadormov -= 1

    def ValidarDir(self):

        if self.rect.x >  ANCHO - self.rect.width :
            self.dir = not self.dir
            self.NotificarAliador(self.dir)


    def CambiarDir(self):

        self.dir = not self.dir





    def update(self, iniciar = False, coli = False):


        self.var_y = 10
        if coli:
            self.CambiarDir()
            if self.bajar:
                self.movY()
                self.bajar = False
                #self.Bajo = True
                self.contbajar = 0

                if self.TiempoMov <= 10: #aumentar la velociadad del enemigo conforme va bajando
                    self.TiempoMov -=2
                else:
                    self.TiempoMov -= 10

        elif iniciar:
            self.moverse()
            self.var_y = 5
            self.movY()
        else:
            self.MovX()
            if self.contbajar > 100:
                self.bajar = True
            else:
                self.contbajar+=1
