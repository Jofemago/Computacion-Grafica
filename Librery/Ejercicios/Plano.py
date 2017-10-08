#libreria
import pygame
from Algebralineal import *

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)




def triangulo(p, lsp):

    pygame.draw.line(p,ROJO,lsp[0],lsp[1])
    pygame.draw.line(p,ROJO,lsp[1],lsp[2])
    pygame.draw.line(p,ROJO,lsp[2],lsp[0])


class Plano:

    cx = 100
    cy = 100

    def __init__(self,pantalla,ancho, alto , centro = None):

        #self.cx = centro[0]
        #self.cy = centro[1]
        self.p = pantalla

        self.alto = alto
        self.ancho = ancho
        #self.pantalla = p

        if centro != None:

            self.cx = centro[0]
            self.cy = centro[1]
        self.plano()

    def plano(self):

        self.p.fill(BLANCO)
        pygame.draw.line(self.p,NEGRO, [0,self.cy], [self.ancho,self.cy ])
        pygame.draw.line(self.p,NEGRO, [self.cx,0],[ self.cx,self.alto])
        pygame.display.flip()

    def acar(self, punto):
        ''' realia la transformacion lineal de un punto x,y  en un plano con un centro especifico a
            los puntos permitidos en la pantalla'''
        x = self.cx + punto[0]
        y = self.cy - punto[1]
        return [x,y]

    def aplan(self,pto):
        '''Realiza el proceso inverso, de convertir de coordenadas pantalla a un punto en pantalla '''

        x = pto[0] - self.cx
        y = self.cy - pto[1]
        return [x,y]

    def DrawVector(self,punto):
        '''recibe un punto obtenido por clic del mouse y dibuja una recta del origen al punto,
            ademas imprime la ecuacion de la recta '''
        pygame.draw.line(self.p, ROJO,[self.cx, self.cy] , punto, 2 )
        pygame.display.flip()


        pto =  self.aplan(punto)
        m = Pendiente([0,0], pto)
        #print Ecuacion(pto, m)
        pygame.display.flip()

    def DrawRect(self, m,b, xmin = 0, xmax = 10):

        y = Recta(m, b, xmin, xmax)#llamado de la libreria algebra lineal
        x = [j for j in range(xmin, xmax)]
        #print type (y[0])
        for i in range(len(x)):

            self.Punto([x[i],y[i]])
        pygame.display.flip()


    def drawParabola(self, x2, x1, b, xmin = 0, xmax = 20):

        x= []
        y = []
        for i in range(xmin,xmax):

            a = (x2*i)**2 +x1*i + b
            x.append(i)
            y.append(a)

        for i in range(len(y)):

            self.Punto([x[i],y[i]])
        pygame.display.flip()
        #y = [x2 **]

    def DrawTriangulo(self, p1, p2, p3, color  = ROJO ):
        ''' dibuja un triangulo en el plano '''
        p1 = self.acar(p1)
        p2 = self.acar(p2)
        p3 = self.acar(p3)
        pygame.draw.line(self.p,color,p1,p2,2)
        pygame.draw.line(self.p,color,p2,p3,2)
        pygame.draw.line(self .p,color,p3,p1,2)
        pygame.display.flip()

    def DrawTrianguloPant(self, p1, p2, p3, color  = ROJO ):
        ''' dibuja un triangulo en el plano '''

        pygame.draw.line(self.p,color,p1,p2,2)
        pygame.draw.line(self.p,color,p2,p3,2)
        pygame.draw.line(self .p,color,p3,p1,2)
        pygame.display.flip()


    def DrawTrianguloEscalado(self, p1, p2, p3 , color = ROJO, sx = 2, sy =2):

        print p1,p2,p3

        p1 = self.EscalarPuntos(p1,sx,sy)
        p2 = self.EscalarPuntos(p2,sx,sy)
        p3 = self.EscalarPuntos(p3,sx,sy)

        print p1,p2,p3

        p1 = self.acar(p1)
        p2 = self.acar(p2)
        p3 = self.acar(p3)

        pygame.draw.line(self.p,color,p1,p2,2)
        pygame.draw.line(self.p,color,p2,p3,2)
        pygame.draw.line(self.p,color,p3,p1,2)
        pygame.display.flip()


    def EscalarPuntos(self, Pto, sx = 2, sy = 2):

        x = Pto[0]*sx
        y = Pto[1]*sy
        return [x,y]


    def Circle(self, pto1, r):

        self.p.fill(BLANCO)
        self.plano()
        pygame.draw.circle(self.p, ROJO, [400,300] , r, 1)

        pygame.display.flip()

    def Punto(self,pto):

        a = self.acar(pto)
        pygame.draw.circle(self.p, ROJO, a, 2)
        pygame.display.flip()


    def Linea(self,pi, pf):

        cpi = self.acar(pi)
        cpf = self.acar(pf)

        pygame.draw.line(self.p, ROJO, cpi, cpf, 2)
        pygame.display.flip()

    def sum(self, p1, p2):

        return [p1[0] + p2[0], p1[1] + p2[1]]

    def Equilatero(self, a , n):


        b = [a[0]+ n ,a[1]]
        h = math.sqrt((n**2)- (n/2)**2)
        h = int(h)
        c=[a[0]+(n/2), a[1]+h]
        self.DrawTrianguloPant(a,b,c)
        pygame.display.flip()


    def EquilateroCar(self, a , n):


        b = [a[0]+ n ,a[1]]
        h = math.sqrt((n**2)- (n/2)**2)
        h = int(h)
        c=[a[0]+(n/2), a[1]+h]
        self.DrawTriangulo(a,b,c)
        pygame.display.flip()
