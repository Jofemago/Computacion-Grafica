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
    pulsacion = True
    r = 0
    pulsaciones = []
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pulsacion:

                    pos = pygame.mouse.get_pos()
                    pto = ppol.aplan(pos)
                    r = ppol.DrawCirclePoint(pto)

                    pulsacion = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not pulsacion:

                    ppol.DrawTrinCir2(r)
                    pulsacion = True
