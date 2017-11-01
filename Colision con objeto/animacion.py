import pygame
import random

ANCHO=700
ALTO=550
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

posmuro = [[50,150],[100,150],[100,450],[150,250],[300,300],[200,350],[400,250],[400,350],[450,250],[550,250]]
tammuros = [[50,350],[500,50],[400,50],[200,50],[50,100],[100,50],[50,100],[100,50],[50,50],[50,250]]


def recortar(archivo, an , al):
    fondo = pygame.image.load(archivo).convert_alpha()
    info = fondo.get_size()
    img_ancho = info[0]  #alto y ancho de cada sprite
    img_alto = info[1]
    corte_x = img_ancho /an
    corte_y = img_alto/al

    m = []
    for i in range(an):
        fila = []
        for j in range(al):
            cuadro = [i*corte_x,j*corte_y,corte_x,corte_y]
            recorte = fondo.subsurface(cuadro)
            fila.append(recorte)
        m.append(fila)

    return m

class Jugador(pygame.sprite.Sprite):

    def __init__(self, img_sprite):

        pygame.sprite.Sprite.__init__(self)
        self.m = img_sprite
        self.image = self.m[6][4]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.var_x = 0
        self.var_y = 0
        self.muros = None

    def update(self):
        #Actualizacion de sprite genera movimiento
        if self.var_y != 0 or self.var_x != 0:
            if self.i < 2 :

                self.i += 1
            else:
                self.i = 0
        self.image = self.m[6+ self.i][4 +self.dir]
        #self.rect = self.image.get_rect()
        self.rect.x += self.var_x


        #colisiones
        ls_bl = pygame.sprite.spritecollide(self,self.muros, False)
        for m in ls_bl:
            if self.var_x > 0:
                self.rect.right = m.rect.left
            if self.var_x < 0:
                self.rect.left  = m.rect.right

        self.rect.y += self.var_y
        ls_bl = pygame.sprite.spritecollide(self,self.muros, False)
        for m in ls_bl:
            if self.var_y > 0:
                self.rect.bottom = m.rect.top
            if self.var_y < 0:
                self.rect.top  = m.rect.bottom

class Muro(pygame.sprite.Sprite):


    def __init__(self, x, y , ANCHO, ALTO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ANCHO, ALTO])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y






if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    anm = recortar('animales.png',12,8)

    '''
    pantalla.blit(anm[0][0],[0,0])
    pygame.display.flip()'''

    jp = Jugador(anm)

    general = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    general.add(jp)
    '''
    m = Muro(150,150, 50,50)
    general.add(m)
    muros.add(m)

    m = Muro(350,250, 20,20)
    general.add(m)
    muros.add(m)'''

    for i in range(len(tammuros)):

        m = Muro(posmuro[i][0],posmuro[i][1],tammuros[i][0],tammuros[i][1])
        general.add(m)
        muros.add(m)

    jp.muros = muros





    reloj = pygame.time.Clock()
    fin  = False
    puntos = 0


    f_con = 0
    f_tasa = 30
    fuente = pygame.font.Font(None,36)
    t_ini = 60
    fin_juego = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    jp.dir = 1
                    jp.var_x = -5
                if event.key == pygame.K_RIGHT:
                    jp.dir = 2
                    jp.var_x = 5
                if event.key == pygame.K_UP:
                    jp.dir = 3
                    jp.var_y = -5
                if event.key == pygame.K_DOWN:
                    jp.dir = 0
                    jp.var_y = 5
                if event.key == pygame.K_SPACE:
                    jp.var_y = 0
                    jp.var_x = 0
            if event.type == pygame.KEYUP:
                jp.var_y = 0
                jp.var_x = 0


        t_segundos = f_con// f_tasa
        minutos = t_segundos // 60
        segundos = t_segundos % 60
        texto_reloj ='{0:02}:{1:02}'.format(minutos,segundos)
        texto = fuente.render(texto_reloj,True, BLANCO)

        t_segundos = t_ini - (f_con// f_tasa)
        minutos = t_segundos // 60
        segundos = t_segundos % 60
        texto_reloj ='{0:02}:{1:02}'.format(minutos,segundos)

        if t_segundos <= 5:
            texto1 = fuente.render(texto_reloj,True, ROJO)
        else:
            texto1 = fuente.render(texto_reloj,True, BLANCO)

        if t_segundos <= 0:
            fin_juego = True

        if fin_juego:

            pantalla.fill(NEGRO)

            texto1 = fuente.render("FIN JUEGO",True, ROJO)
            pantalla.blit(texto1,[250,100])
            pygame.display.flip()
        else:

            general.update()
            pantalla.fill(NEGRO)
            general.draw(pantalla)
            pantalla.blit(texto,[10,10])
            pantalla.blit(texto1,[500,10])
            pygame.display.flip()
            reloj.tick(f_tasa)
            f_con += 1
