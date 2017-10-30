import pygame
import random
from Escudo import *
from Player import *
from Enemigos import *

RUTAIMG = 'imagenes/'
Enemy1 = 'Enemy1/'
Enemy2 = 'Enemy2/'
Enemy3 = 'Enemy3/'

Colores = [['verde1.png','verde2.png'],
            ['violeta1.png','violeta2.png'],
            ['azul1.png','azul2.png'],
            ['amarillo1.png','amarillo2.png']]


def CreateEscudos(general):
    Escudos = pygame.sprite.Group()
    Y = 490
    for i in range(0,20):
        for j in range(0,12):

            es = Escudo()
            es.setPos(75 + i*5,Y + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(250 + i*5,Y + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(425 + i*5,Y + j* 5)
            general.add(es)
            Escudos.add(es)

            es = Escudo()
            es.setPos(600 + i*5,Y + j* 5)
            general.add(es)
            Escudos.add(es)
    return Escudos


def CreateVidas(general,jg):
    vidas = pygame.sprite.Group()
    for vida in range(jg.vidas - 1):
        v = Vida('imagenes/nave1.png')
        v.rect.x = 5 + vida * 75
        v.rect.y = ALTO - jg.rect.height
        vidas.add(v)
        general.add(v)
    return vidas

def CreateEnemigos1(general):
    Enemigos1 = pygame.sprite.Group()
    Y = -330
    X = 100

    for j in range(0,5):

        for i in range(0,10):

            en = Enemigo1(10 + j * 10, i)
            en.setPos( X + i * 60, Y + j * 55)
            general.add(en)
            Enemigos1.add(en)

    return Enemigos1
