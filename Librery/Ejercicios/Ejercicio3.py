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

    centro = [400,300]
    ppol = Polar(centro, ANCHO, ALTO, pantalla)
    #ppol.DrawCirclePoint([10,10])

    #Pcar = Plano(pantalla,ANCHO,ALTO,[400,300])
    #Pcar.plano()
    #Pcar.EquilateroCar([-100,100],40)

    fin  = False
    n = 0
    p1 = None
    p2 = None

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if n == 0:
                    pos = pygame.mouse.get_pos()
                    pto = ppol.aplan(pos)
                    ppol.DrawVector(pos)
                    p1 = pto
                    n += 1
                elif n == 1:
                    pos = pygame.mouse.get_pos()
                    pto = ppol.aplan(pos)
                    ppol.DrawVector(pos)
                    p2 = pto
                    n += 1

                if n == 2:

                    p3 = ppol.sum(p1,p2)

                    ppol.Linea(p1, p3 )
                    ppol.Linea( p2, p3)
                    ppol.Linea( [0,0], p3)
                    print p1, '+', p2, '=', p3

                    n = 0
