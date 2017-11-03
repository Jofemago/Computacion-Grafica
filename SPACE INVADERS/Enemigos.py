import random
import pygame
from configuraciones import *
from funciones import *


class Jefe(pygame.sprite.Sprite):

    def __init__(self,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/EnemyCasual/EnemyBonus.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.dir = dir
        self.rect.y = 70
        self.var_x = 3
        '''if self.dir:
            self.rect.x = ANCHO
        else:
            self.rect.x = 0'''
        self.rect.x = 100
        self.points = 50
        self.introducir = False
        self.tiempoBase = 200
        self.tiempoIntro = self.tiempoBase



    def MovX(self):
        if self.dir:
            self.rect.x -= self.var_x
        else:
            self.rect.x += self.var_x



    def update(self):

        #self.rect.x += self.var_x
        if self.dir:
            if self.rect.x <= 0:
                self.rect.x = 0
                self.dir = not self.dir
        else:
            if self.rect.x > ANCHO - self.rect.width:
                self.rect.x = ANCHO - self.rect.width
                self.dir = not self.dir
        self.MovX()
        if self.tiempoIntro <= 0:

            self.tiempoIntro = self.tiempoBase
            self.introducir = True
        self.tiempoIntro -= 1

class Enemigo2(pygame.sprite.Sprite):

    def __init__(self,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/EnemyCasual/EnemyBonus.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.dir = dir
        self.rect.y = 70
        self.var_x = 0
        if self.dir :
            self.rect.x = ANCHO
            self.var_x = -3
        else:
            self.rect.x = 0 - self.rect.width
            self.var_x = 3

    def update(self):

        self.rect.x += self.var_x
        if self.dir:
            if self.rect.x < 0 - self.rect.width:
                self.kill()
        else:
            if self.rect.x > ANCHO:
                self.kill()


#def EnemigoNivel2()

class Enemigo1(pygame.sprite.Sprite):



    def __init__(self,timeAct,row,sprites, puntos, tiempo,col = ROJO):
        pygame.sprite.Sprite.__init__(self)

        self.row = row
        self.sprites = sprites
        #self.Sprites = self.setImages()
        #primer casilla del arreglo para moverse entre el mismo color
        #segunda casilla para moverse entre colores distintos
        self.mov = 0#movimiento del sprite la posicion 2 indica que el sprite ha muerto
        self.color = 3# posicion de los sprites dependiendo de la pos que se encuentre en un momento determinado
        self.image = self.sprites[self.mov][self.color]

        self.rect = self.image.get_rect()
        self.var_y = 0
        self.var_x = 8
        self.m = 0
        self.movs = [pygame.mixer.Sound('Sonidos/movimiento1.wav'),pygame.mixer.Sound('Sonidos/movimiento2.wav'),pygame.mixer.Sound('Sonidos/movimiento3.wav'),pygame.mixer.Sound('Sonidos/movimiento4.wav')]
        self.movimiento = self.movs[0] #diferentes sonidos

        self.TiempoMov = tiempo # tiempo de movimiento
        #self.TiempoMov = 35
        self.temporizadormov = timeAct# temporizador que va disminuyedo con el tiempo
        self.dir  = True #indica la posicion de izquierda a derecha


        self.bajar = False
        self.Bajo = False
        self.contbajar = 0

        #momento en que muere y tiempo que tiene que esperar para desaparecer
        self.muerto = False
        self.conteoMuerto = 20

        self.points = puntos

        self.timeDisparo = random.randrange(100, 500) #tiempo para disparar
        self.disparo = False





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

    def MovX(self):

        if self.temporizadormov <= 0:
            #self.ValidarDir()
            if self.dir:
                self.rect.x += self.var_x
            else:
                self.rect.x -= self.var_x
            self.temporizadormov = self.TiempoMov
            #self.moverse() #sonido
            if self.mov > 1:
                self.mov = 0
            if self.muerto:
                self.image = self.sprites[2][self.color]
            else:
                self.image = self.sprites[self.mov][self.color]
            self.mov += 1
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
        if self.muerto:
            self.image = self.sprites[2][3]
            if self.conteoMuerto < 0:
                self.kill()
            else:
                self.conteoMuerto -= 1
        else:
            #calculo el disparo en caso tal que no este muerto  y vuelvo y calculo un nuevo tiempo aleatorio para disparar
            if self.timeDisparo <= 0:
                self.disparo = True
                #self.timeDisparo = random.randrange(200, 1000) #tiempo para disparar
                self.timeDisparo = 500


        if coli:
            self.CambiarDir()
            if self.bajar:
                self.movY()
                self.bajar = False
                self.contbajar = 0
                #apenas bajo reinicion contadpr em 0 para que los otros no bajen

                if self.TiempoMov <= 10: #aumentar la velociadad del enemigo conforme va bajando
                    self.TiempoMov -=2
                    self.conteoMuerto -=1
                else:
                    self.TiempoMov -= 10

        elif iniciar:
            #self.moverse()
            self.var_y = 5
            self.movY()
        else:
            self.MovX()
            if self.contbajar > 100:
                #despues de 100 movmientos en X se activa la opcion de bajar
                #para que cuando llegue un elemento a la esquiva los movimientos de los otros
                #sprites no hagan bajar mas de un cuadro
                self.bajar = True
            else:
                self.contbajar+=1
        self.timeDisparo -= 1 #disminuyo el tiempo de disparo
