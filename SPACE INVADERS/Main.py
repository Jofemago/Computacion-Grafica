import pygame
import random

from Player import *
from configuraciones import *
from Fronteras import *
from Escudo import *
from Balas import *
from funciones import *
from Enemigos import *
#from Enemys import *

LIMITESUPERIOR = 68
LIMITEINFERIOR= 610




if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    #fondo = pygame.image.load('imagenes/fondo.jpg')
    #creamos  grupos
    jugadores = pygame.sprite.Group()
    limites = pygame.sprite.Group()
    limitesEnemy = pygame.sprite.Group()
    Escudos = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    disparosMaquina = pygame.sprite.Group()
    disparosJugador = pygame.sprite.Group()
    EnemigosTipo1 = pygame.sprite.Group()
    general1 = pygame.sprite.Group()#todos los sprites del nivel1


    #creamos jugador
    jg = Player('imagenes/nave1.png',3)
    jugadores.add(jg)
    general1.add(jg)



    #se crean los escudos
    Escudos = CreateEscudos(general1)

    #se crean las vidas del jugador
    vidas = CreateVidas(general1,jg)

    #creamos los enemigos todos fuera de la pantalla para el nivel 1
    EnemigosTipo1 = CreateEnemigos1(general1)

    #se crea y ubica el limite superior y inferior
    superior =limite(NEGRO)
    inferior = limite()
    superior.setPos(0,LIMITESUPERIOR)
    inferior.setPos(0,LIMITEINFERIOR)
    limites.add(superior)
    limites.add(inferior)
    general1.add(superior)
    general1.add(inferior)

    derecha = limiteEnemigo(NEGRO)#estas fronteras estan hechas para que los enemigos se mantengan dentro de patnalla y se muevan de manera adecuada
    derecha.setPos(799,0)
    limitesEnemy.add(derecha)
    general1.add(derecha)

    izquierda = limiteEnemigo(NEGRO)
    izquierda.setPos(-1,0)
    limitesEnemy.add(izquierda)
    general1.add(izquierda)



    reloj = pygame.time.Clock()
    fin  = False

    #imagenes de inicio
    Inicio1 = True
    iniciar = False
    recorrer = 95
    Invaders =pygame.font.SysFont("comicsansms", 80)
    Indicaciones =pygame.font.SysFont("comicsansms", 20)
    Pulsacion =pygame.font.SysFont("comicsansms", 40)
    Utp = pygame.image.load('imagenes/inicio.png').convert_alpha()


    nivel1 = False
    puntos = 0
    Marcador =pygame.font.SysFont("comicsansms", 35)
    Puntuacion =pygame.font.SysFont("comicsansms", 25)
    Tipodejuego =pygame.font.SysFont("comicsansms", 60)
    #Indicaciones =pygame.font.SysFont("comicsansms", 20)


    #Sprites1 = CargarSprites(Enemy1, Colores)
    #Sprites2 = CargarSprites(Enemy2, Colores)
    #Sprites3 = CargarSprites(Enemy3, Colores)
    pausa = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            if event.type == pygame.KEYDOWN and Inicio1:
                iniciar = True

            if event.type == pygame.KEYDOWN and nivel1:
                if event.key == pygame.K_p:
                    print "pausa"
                    pausa = not pausa
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 4

                if event.key == pygame.K_LEFT:

                    jg.var_x = -4

                if event.key == pygame.K_SPACE:

                    if len(disparosJugador) == 0:
                        #jg.disparar()
                        bala = ProyectilJugador(2)
                        bala.rect.x = jg.rect.x + 22
                        bala.rect.y = jg.rect.y +5
                        disparosJugador.add(bala)
                        disparos.add(bala)
                        general1.add(bala)
                        jg.disparar()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and jg.var_x > 0:

                    jg.var_x = 0

                if event.key == pygame.K_LEFT and jg.var_x < 0:

                    jg.var_x = 0

        #inicio de juego
        if Inicio1:
            pantalla.fill(NEGRO)
            if not iniciar:

                pantalla.blit(Utp,[150,100])
                text1 = Invaders.render("INVADERS", True, BLANCO)
                text2= Indicaciones.render("Use las flechas <- -> para moverse,  use espacio para disparar, PRIMER MUNDO DESRUYE", True, BLANCO)
                text3 = Pulsacion.render("PRESIONE CUALQUIER TECLA PARA CONTINUAR",True, BLANCO)
                pantalla.blit(text3,[50,420])
                pantalla.blit(text1,[400,320])
                pantalla.blit(text2,[0,600])

            else:
                pantalla.fill(NEGRO)

                EnemigosTipo1.update(iniciar)
                general1.update()
                general1.draw(pantalla)
                if recorrer == 0:
                    Inicio1 =False
                    iniciar = False
                    nivel1 = True
                recorrer-=1

                #Se consigue comunicacion entre aliados
                '''for e in EnemigosTipo1:
                    for e2 in EnemigosTipo1:
                        if e != e2:
                            e.aliados.append(e2)'''


        elif pausa:

            text1 = Marcador.render("STORE", True, BLANCO)
            text2 = Puntuacion.render(strpuntos(puntos), True, BLANCO)
            text3 = Tipodejuego.render('PAUSADO', True, BLANCO)

            pantalla.fill(NEGRO)
            pantalla.blit(text1,[25,10])
            pantalla.blit(text2, [50, 35])
            pantalla.blit(text3, [565, 10])

            #general1.update()
            general1.draw(pantalla)
        elif nivel1:
            #Choque de balas contra el Escudo y limites
            pygame.sprite.groupcollide(disparos, Escudos, True, True)
            pygame.sprite.groupcollide(disparos, limites, True, False)
            #pantalla.draw(l[0][0],[0,0])
            #choque entre muros y enemigos para bordear el area de juego cuando alguno choca con un muro todos cambian de direccion
            col = pygame.sprite.groupcollide(EnemigosTipo1, limitesEnemy, False, False)
            if len(col) > 0:
                EnemigosTipo1.update(False, True)

            #choque de balas con los enemigos
            #col = pygame.sprite.groupcollide(disparosJugador, EnemigosTipo1, True, False)
            #print col
            for b in disparosJugador:
                ls_col = pygame.sprite.spritecollide(b, EnemigosTipo1, False)
                for e in ls_col:
                    b.kill()
                    e.muerto = True
                    puntos += e.points

            '''for e in EnemigosTipo1:
                if e.muerto:
                    if e.conteoMuerto <= 0:
                        e.kill()'''



            text1 = Marcador.render("STORE", True, BLANCO)
            text2 = Puntuacion.render(strpuntos(puntos), True, BLANCO)
            text3 = Tipodejuego.render('DESTRUYE', True, BLANCO)

            pantalla.fill(NEGRO)
            pantalla.blit(text1,[25,10])
            pantalla.blit(text2, [50, 35])
            pantalla.blit(text3, [565, 10])

            general1.update()
            general1.draw(pantalla)



       # pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(60)
