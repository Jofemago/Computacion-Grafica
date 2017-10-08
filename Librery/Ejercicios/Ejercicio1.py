import pygame
from Plano import *
from LibPolares import *
from Images import *


ANCHO=800
ALTO=600
if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(NEGRO)
    pygame.display.flip()



    Pcar = Plano(pantalla,ANCHO,ALTO,[400,300])
    Pcar.plano()
    Pcar.EquilateroCar([-100,100],40)

    fin  = False
    n = 40 # tamano del triagulo rectangulo
    k = 0 #pulsaciones hechas hasa el momento
    pulsaciones = []
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    n += 5
                    Pcar.plano()
                    Pcar.EquilateroCar([-100,100],n)

                if event.key == pygame.K_DOWN:
                    Pcar.plano()

                    if( n > 0):
                        n -= 5
                        Pcar.EquilateroCar([-100,100],n)


            #oprimir dos click hacer linea, mostrar puntos carteasianos
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print 'tecla del raton', pygame.mouse.get_pressed()
                k += 1
                pos = pygame.mouse.get_pos()
                pulsaciones.append(Pcar.aplan(pos))

                print pulsaciones
                if k == 2:

                    #pygame.draw.line(pantalla,NEGRO,pulsaciones[0],pulsaciones[1])
                    Pcar.Linea(pulsaciones[0],pulsaciones[1])
                    pygame.display.flip()
                    pulsaciones = []
                    k = 0
