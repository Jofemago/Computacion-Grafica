import pygame
from Plano import *
from LibPolares import *
from Images import *

ANCHO=640
ALTO=480
if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(NEGRO)
    pygame.display.flip()

    #PRUEBAS PLANO
    #Pcar = Plano(pantalla,ANCHO,ALTO,[400,300])
    #Pcar.plano()
    #Pcar.Punto([20,-10])
    #pygame.display.flip()
    #Pcar.DrawRect(3,20,-100,100)
    #Pcar.drawParabola(1,5,10,-100,100)
    #Pcar.DrawTriangulo([-5,-5],[-5,5],[5, 5])
    #Pcar.DrawTrianguloEscalado([-5,-5],[-5,5],[5, 5])


    #Pruebas Polares
    #centro = [400,300]
    #ppol = Polar(centro, ANCHO, ALTO, pantalla)
    #ppol.Point(200,20)
    #ppol.Line(200,10)
    #ppol.DrawRosaDelay(100,3)


    #prueba imagenes

    #img = Img(pantalla,'tux.png', 100, 100, [ANCHO, ALTO],'fondo.png')

    #img.HiddenMouse()


    fin  = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            #Movimientos con tecclado de imagen
            #if event.type == pygame.KEYDOWN:
            #    img.MovTeclImg( event.key , True)
        #img.MovWhithMouse()
