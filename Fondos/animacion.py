import pygame
#from Plano import *
#from LibPolares import *
#from Images import *
#from Algebralineal import *
import random

ANCHO=640
ALTO=480
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)


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

class Jugador(pygame.sprite.Sprite):

    def __init__(self, img_sprite):

        pygame.sprite.Sprite.__init__(self)
        self.m = img_sprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.var_x = 0
        self.var_y = 0

    def update(self):

        if self.var_y != 0 or self.var_x != 0:
            if self.i < 2 :

                self.i += 1
            else:
                self.i = 0
        self.image = self.m[self.i][self.dir]
        #self.rect = self.image.get_rect()
        self.rect.x += self.var_x
        self.rect.y += self.var_y






if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    anm = recortar('animales.png',12,8)

    '''
    pantalla.blit(anm[0][0],[0,0])
    pygame.display.flip()'''

    jp = Jugador(anm)
    general = pygame.sprite.Group()
    general.add(jp)




    reloj = pygame.time.Clock()
    fin  = False
    puntos = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    jp.dir = 1
                    jp.var_x = -5
                if event.key == pygame.K_RIGHT:
                    jp.dir = 2
                    jp.var_x = 5
                if event.key == pygame.K_UP:
                    jp.dir = 3
                    jp.var_y = -5
                if event.key == pygame.K_DOWN:
                    jp.dir = 0
                    jp.var_y = 5
                if event.key == pygame.K_SPACE:
                    jp.var_y = 0
                    jp.var_x = 0




        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
