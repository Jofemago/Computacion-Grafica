import pygame

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Player(pygame.sprite.Sprite):

    def __init__(self, archivos):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Crear la imagen que va ser un bloque que representa el Jugador
        self.sprites = archivos
        self.image = None
        self.SetImage(0)


        #posiciion del objeto, importante para poder ubicarlo en patanlla
        self.rect = self.image.get_rect()

        #defino variable de movimiento que define la direccion va de 1 a 4
        self.dir = 0
        self.pos = 0 # que pos del sprite se usara
        self.timeSalto = 20
        #defino la velociad con la que se movera
        self.var_x =0
        self.var_y = 0
        self.salto = False

        #defino el numero de vidas que tiene el Jugadores
        self.Vidas = 5

    def SetImage(self,pos):

        self.image =  pygame.image.load(self.sprites[pos]).convert_alpha()

    def setPos(self, x, y):


        self.rect.x = x
        self.rect.y = y

    def movDer(self):

        self.rect.x += self.vel

    def movIzq(self):

        self.rect.x -= self.vel


    def update(self):

        '''if self.dir == 1:

            if self.rect.x > 0:
                self.movIzq()
            #self.dir = 0

        elif self.dir == 2:

            if self.rect.x  < 350:
                self.movDer()


            #self.dir = 0'''
        if self.salto:
            self.timeSalto = 20
            self.rect.x += self.var_x
            self.rect.y += self.var_y
            self.salto=False
            self.SetImage(self.dir + 4)
        self.timeSalto -= 1
        if self.timeSalto < 0:

            self.timeSalto = 10
            self.SetImage(self.dir)
