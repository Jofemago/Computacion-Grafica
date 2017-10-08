import pygame

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)


class Car(pygame.sprite.Sprite):

    def __init__(self, img, dir, timeb, arranque):

        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.arranque = arranque #determina cuando debe arrancar el sprite
        self.dir = dir
        self.timebase = timeb
        self.tiempo = timeb
        self.var_x = 5

    def setPos(self, x, y):


        self.rect.x = x
        self.rect.y = y

    def movDer(self):

        self.rect.x += self.vel

    def movIzq(self):

        self.rect.x -= self.vel

    def update(self):
        if self.dir == 1 : # va de izquierda a derecha

            if self.rect.x < 0- self.rect[2] and self.arranque<= 0:
                self.rect.x = 448
            else:
                if self.tiempo < 0:
                    self.tiempo = self.timebase
                    self.var_x = 5
                self.rect.x -= self.var_x
                self.var_x = 0
                self.tiempo -= 1
        else:
            if self.rect.x > 640 and self.arranque<= 0: #va de derecha a izquierda
                self.rect.x = 0
            else:
                if self.tiempo < 0:
                    self.tiempo = 10
                    self.var_x = 5
                self.rect.x += self.var_x
                self.var_x = 0
                self.tiempo -= 1

        self.arranque -=1
