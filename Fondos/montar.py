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
    fondo = pygame.image.load(archivo).convert()
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





if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    #fondo = pygame.image.load('terrenogen.png').convert()

    #info = fondo.get_size() #puedo optener ancho y alto de la imagen
    #img_ancho = info[0]
    #img_alto = info[1]




    #cuadro= [20*32,0,32,32]
    #recorte = fondo.subsurface(cuadro) #recorte de la superficie

    recortes  = recortar('terrenogen.png',32,12)
    '''for i in range(32):
        for j in range(12):
            pantalla.blit(recortes[i][j],[0,0])'''

    pantalla.blit(recortes[10][0],[0,0])
    pygame.display.flip()




    fin  = False
    puntos = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
