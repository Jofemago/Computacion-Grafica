import pygame
from Plano import *
#from LibPolares import *
#from Images import *
from Algebralineal import *

ANCHO=800
ALTO=600
if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(NEGRO)
    pygame.display.flip()



    Pcar = Plano(pantalla,ANCHO,ALTO,[400,300])
    Pcar.plano()


    fin  = False
    n = 40 # tamano del triagulo rectangulo
    k = 0 #pulsaciones hechas hasa el momento
    pulsaciones = []
    r = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN and k == 3:

                if event.key == pygame.K_UP:
                    r += 5
                    Pcar.plano()
                    Pcar.Circle([400,300],r)

                if event.key == pygame.K_DOWN:
                    Pcar.plano()

                    if( r > 0):
                        r -= 5
                    if r <= 2:
                        r = 10

                    print r
                    Pcar.Circle([400,300],r)



            #oprimir dos click hacer linea, mostrar puntos carteasianos
            if event.type == pygame.MOUSEBUTTONDOWN and k < 3:
                #print 'tecla del raton', pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                pulsaciones.append(pos)
                r = DistEntrePuntos([400,300],pulsaciones[0])
                print r
                Pcar.Circle([400,300],r)

                k = 3
