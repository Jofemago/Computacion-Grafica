import pygame
import random
from Escudo import *
from Player import *
from Enemigos import *
from configuraciones import *

RUTAIMG = 'imagenes/'




def recortar(archivo, an , al):
    fondo = pygame.image.load(archivo).convert_alpha()
    info = fondo.get_size()
    img_ancho = info[0]  #alto y ancho de cada sprite
    img_alto = info[1]
    corte_x = img_ancho /an
    corte_y = img_alto/al

    m = []
    for i in range(an):
        fila = []
        for j in range(al):
            cuadro = [i*corte_x,j*corte_y,corte_x,corte_y]
            recorte = fondo.subsurface(cuadro)
            fila.append(recorte)
        m.append(fila)

    return m


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

def SelectSprite(i):

    if i == 0:
        return recortar(Enemy2,3,4)
    elif i >= 1 and i <= 2:
        return recortar(Enemy2,3,4)
    else:
        return recortar(Enemy2,3,4)

def CreateEnemigos1(general):
    Enemigos1 = pygame.sprite.Group()
    Y = -330
    X = 100

    for j in range(0,5):

        for i in range(0,10):

            en = Enemigo1(10 + j * 10, i, SelectSprite(i))
            en.setPos( X + i * 60, Y + j * 55)
            general.add(en)
            Enemigos1.add(en)

    return Enemigos1
