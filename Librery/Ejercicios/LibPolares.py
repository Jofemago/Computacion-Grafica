'''  clase para la gestion de coordenadas polares'''


import pygame
import math
from Plano import *
from Algebralineal import *


class Polar(Plano):

    def __init__(self, pantalla, ancho, alto ,centro):
        Plano.__init__( self,centro, ancho, alto, pantalla)
        self.reloj = pygame.time.Clock()


    def Polares(self,r, an):

        x = r * math.cos(math.radians(an))
        y = r * math.sin(math.radians(an))

        return [int(x), int(y)]


    def Point(self, r, an):

        pto = self.Polares(r,an)
        self.Punto(pto)
        pygame.display.flip()

    def Line(self, r, an):

        pto = self.Polares(r,an)
        self.Linea([0,0], pto)
        pygame.display.flip()

    def ImgFlor(self,img,r, an):

        pto = self.Polares(r,an)
        pto = self.Cart(pto)
        self.p.blit(img, pto)
        pygame.display.flip()

    def DrawRosaDelay(self, a, b):
        """dibuja ecuacuones de la forma a sin( b teta ) con un delay"""


        for i in range(361):
            r =  a*math.sin(b*math.radians(i))
            self.Line(r,i)
            self.reloj.tick(20)

    def DrawCirclePoint(self, pto):
        ''' Recibe un punto cartesiano y dibuja una circunferencia con radio de el al centro'''
        r = Norma(pto)

        self.p.fill(BLANCO)
        self.plano()
        centro = self.acar([0,0])
        pygame.draw.circle(self.p, ROJO, centro, int(r),1)
        pygame.display.flip()
        return r

    def DrawTrinCir2(self, r):

        pto1 = self.Polares(r, 225)
        pto2 = self.Polares(r, 315)
        pto3 = self.Polares(r, 90)
        self.DrawTriangulo(pto1, pto2, pto3)


    def DrawTrinCir(self, r):

        pto1 = self.Polares(r, 225)
        pto2 = self.Polares(r, 315)
        n = DistEntrePuntos(pto1, pto2)
        print pto1
        print pto2
        self.EquilateroCar(pto1, n)
