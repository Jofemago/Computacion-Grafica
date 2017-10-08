import pygame

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

class Player(pygame.sprite.Sprite):

    def __init__(self, ANCHO, ALTO , COLOR = VERDE):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Crear la imagen que va ser un bloque que representa el Jugador
        self.image = pygame.Surface([ANCHO, ALTO])
        self.image.fill(COLOR)

        #posiciion del objeto, importante para poder ubicarlo en patanlla
        self.rect = self.image.get_rect()

        #defino variable de movimiento que define la direccion
        self.dir = 0

        #defino la velociad con la que se movera
        self.vel = 5

        #defino el numero de vidas que tiene el Jugadores
        self.Vidas = 5


    def setPos(self, x, y):


        self.rect.x = x
        self.rect.y = y

    def movDer(self):

        self.rect.x += self.vel

    def movIzq(self):

        self.rect.x -= self.vel


    def update(self):

        if self.dir == 1:

            if self.rect.x > 0:
                self.movIzq()
            #self.dir = 0

        elif self.dir == 2:

            if self.rect.x  < 350:
                self.movDer()


            #self.dir = 0
