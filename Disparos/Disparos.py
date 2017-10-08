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

class Bloque(pygame.sprite.Sprite):

    def __init__(self, alto, ancho, col = AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ALTO - self.rect.height
        self.var_x = 0

    def update(self):

        self.rect.x += self.var_x



class Proyectil(pygame.sprite.Sprite):

    def __init__(self, dir, col = VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 10])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.dir = dir
        self.var_y = 4

    def update(self):
        if self.dir == 1:

            self.rect.y  -= self.var_y

        if self.dir == 2:

            self.rect.y  += self.var_y



class Enemy(pygame.sprite.Sprite):

    def __init__(self, alto, ancho, timeAct,col = AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.dir = 1
        self.var_x = 3
        self.timeAc = timeAct
        self.temporizador = timeAct
        self.disparo = False

    def update(self):
        if self.rect.x < ANCHO - self.rect.height and self.dir == 1:
            self.rect.x += self.var_x
        else:
            self.dir = 2
            self.rect.x  -=  self.var_x
        if self.rect.x <= 0 and self.dir == 2:
            self.dir = 1
            #self.var_x+= 2
        if self.temporizador < 0:

            self.temporizador = self.timeAc
            self.disparo = True

        self.temporizador -= 1



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    #sprite
    jg = Bloque(70, 50)

    #grupo de sprite
    balas = pygame.sprite.Group()
    balasEnemigas = pygame.sprite.Group()

    general = pygame.sprite.Group()

    bloques = pygame.sprite.Group()

    bloques.add(jg)
    general.add(jg)


    rojos = pygame.sprite.Group()
    n = 10
    for i in range(n):
        temp = random.randrange(100, 500)
        nb = Enemy(20,20,temp ,ROJO)
        nb.rect.x = random.randrange(0, ANCHO)
        nb.rect.y = random.randrange(0, ALTO- 100)
        rojos.add(nb)
        general.add(nb)

    #bloques.draw(pantalla)

    #pygame.display.flip()
    reloj = pygame.time.Clock()
    fin  = False
    puntos = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jg.var_x = 5
                    #print 'derecha'
                if event.key == pygame.K_LEFT:
                    jg.var_x = -5
                    #print 'izquierda'
                if event.key == pygame.K_SPACE:

                    b= Proyectil(1)
                    b.rect.x = jg.rect.x
                    b.rect.y = jg.rect.y
                    balas.add(b)
                    general.add(b)


            if event.type == pygame.KEYUP:
                jg.var_x = 0


        for b in balas:
            ls_col = pygame.sprite.spritecollide(b, rojos, True)

            for e in ls_col:
                general.remove(e)
                rojos.remove(e)
            if len(ls_col):
                general.remove(b)
                balas.remove(e)

        for rival in rojos:

            if rival.disparo == True:
                b= Proyectil(2)
                b.rect.x = rival.rect.x
                b.rect.y = rival.rect.y
                balasEnemigas.add(b)
                general.add(b)
                rival.disparo = False




        pantalla.fill(NEGRO)
        general.update()
        general.draw(pantalla)

        pygame.display.flip()
        reloj.tick(60)
