import pygame

NEGRO =(0,0,0 )
class Img:

    def __init__ (self, pantalla, img, x, y, Tampantalla ,fondo = None ):

        self.img = pygame.image.load(img)
        self.fondo = None
        if fondo is not None:
            self.fondo = pygame.image.load(fondo)
        self.p = pantalla
        self.x = x
        self.y = y
        self.AnAl = Tampantalla

        self.DrawImg()



    def DrawImg(self, Dx = 0, Dy = 0, pintar = False):

        if(pintar):
            self.p.fill(NEGRO)

        if self.fondo is not None:
            self.p.blit(self.fondo, [0,0])
        self.x += Dx
        self.y += Dy

        self.ValidarLimites()

        self.p.blit(self.img,[self.x , self.y ])
        pygame.display.flip()

    def ValidarLimites(self):
        if self.y > self.AnAl[1]:
            self.y = 0

        if self.x >  self.AnAl[0]:
            self.x = 0

        if self.y < 0:
            self.y = self.AnAl[1]

        if self.x <  0:
            self.x = self.AnAl[0]


    def MovTeclImg(self, event, pintar = False):

        if event == pygame.K_DOWN:
            self.DrawImg(0,10,pintar)
            print 'abajo'

        elif event == pygame.K_UP:
            self.DrawImg(0, -10, pintar)
            print 'arriba'

        elif event == pygame.K_LEFT:
            self.DrawImg(-10,0,pintar)
            print 'izquierda'

        elif event == pygame.K_RIGHT:
            self.DrawImg(10, 0, pintar)
            print 'derecha'

    def HiddenMouse(self):

        pygame.mouse.set_visible(False)

    def ShowMouse(self):

        pygame.mouse.set_visible(False)

    def MovWhithMouse(self, pintar = False):

        tam = self.img.get_rect()#obtengo ancho y alto de  la imagen
        pos = pygame.mouse.get_pos()
        pos = [ pos[0] - tam[2]/2, pos[1] - tam[3]/2]
        if(pintar):
            self.p.fill(NEGRO)

        if self.fondo is not None:
            self.p.blit(self.fondo, [0,0])

        self.p.blit(self.img,pos)
        pygame.display.flip()
