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
TIEMPOSEGUNDOMUNDO = 120



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
    EnemigosTipo2 = pygame.sprite.Group() #donde van almacenados los bonus
    Enemigos = pygame.sprite.Group()
    general1 = pygame.sprite.Group()#todos los sprites del nivel1


    #creamos jugador
    jg = Player('imagenes/nave1.png','imagenes/naveDestruida.png',3)
    jugadores.add(jg)
    general1.add(jg)



    #se crean los escudos
    Escudos = CreateEscudos(general1)

    #se crean las vidas del jugador
    vidas = CreateVidas(general1,jg)

    #creamos los enemigos todos fuera de la pantalla para el nivel 1
    EnemigosTipo1 = CreateEnemigos1(general1)
    Enemigos.add(EnemigosTipo1)
    #Enemigos = CreateEnemigos1(general1) #enemigos globales

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

    tiros = False
    #imagenes de inicio
    Inicio1 = True
    inicio2 = False #cuando se active da inicio al nivel 2
    iniciar = False
    recorrer = 95
    Invaders =pygame.font.SysFont("comicsansms", 80)
    Indicaciones =pygame.font.SysFont("comicsansms", 20)
    Pulsacion =pygame.font.SysFont("comicsansms", 40)
    Utp = pygame.image.load('imagenes/inicio.png').convert_alpha()
    gameover = pygame.image.load('imagenes/gameover.jpg').convert_alpha()
    imgvida = pygame.image.load('imagenes/nave1.png').convert_alpha()


    nivel1 = False

    puntos = 0
    Marcador =pygame.font.SysFont("comicsansms", 35)
    Puntuacion =pygame.font.SysFont("comicsansms", 25)
    Tipodejuego =pygame.font.SysFont("comicsansms", 60)
    #Indicaciones =pygame.font.SysFont("comicsansms", 20)
    bonus = True #defino direccion inicial del bonis
    tiempobonus = 1000


    nivel2 = False
    jefe = Jefe(True)


    #Sprites1 = CargarSprites(Enemy1, Colores)
    #Sprites2 = CargarSprites(Enemy2, Colores)
    #Sprites3 = CargarSprites(Enemy3, Colores)
    JuegoPerdido = False
    Gano = False
    pausa = False

    #Manejo de reloj
    t_ini = TIEMPOSEGUNDOMUNDO # dos minutos
    f_con = 0
    f_tasa = 60
    fuentereloj = pygame.font.SysFont("comicsansms",50)


    reloj = pygame.time.Clock()
    fin  = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            if event.type == pygame.KEYDOWN and Inicio1:
                iniciar = True
            if event.type == pygame.KEYDOWN and inicio2:
                iniciar = True
            if event.type == pygame.KEYDOWN and JuegoPerdido:
                fin=True

            if event.type == pygame.KEYDOWN and (nivel1 or nivel2):
                if event.key == pygame.K_a:
                    if not tiros:
                        tiros = not tiros
                        jg.vidas -= 1
                        print tiros
                if event.key == pygame.K_p:
                    #print "pausa"
                    pausa = not pausa
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 4

                if event.key == pygame.K_LEFT:

                    jg.var_x = -4

                if event.key == pygame.K_SPACE:

                    if not tiros:
                        if len(disparosJugador) == 0:
                            #jg.disparar()
                            bala = ProyectilJugador(2)
                            bala.rect.x = jg.rect.x + 22
                            bala.rect.y = jg.rect.y +5
                            disparosJugador.add(bala)
                            disparos.add(bala)
                            general1.add(bala)
                            jg.disparar()
                    else:
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
                #Enemigos.add(EnemigosTipo1)
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

            text1 = Marcador.render("SCORE", True, BLANCO)
            text2 = Puntuacion.render(strpuntos(puntos), True, BLANCO)
            text3 = Tipodejuego.render('PAUSADO', True, BLANCO)
            textoreloj = fuentereloj.render("-- : --",True, BLANCO)

            pantalla.fill(NEGRO)
            pantalla.blit(text1,[25,10])
            pantalla.blit(text2, [50, 35])
            pantalla.blit(text3, [565, 10])
            pantalla.blit(textoreloj,[300,10])


            #general1.update()
            general1.draw(pantalla)
        #nivel1 del juego
        elif Gano:
            pantalla.fill(NEGRO)
            pantalla.blit(Utp,[150,100])
            text1 = Invaders.render("INVADERS", True, BLANCO)
            text2= Indicaciones.render("hecho por JOHAN FELIPE MARIN GONZALEZ, ganaste y recuerda tu puntaje es : "+ str(puntos), True, BLANCO)
            text3 = Pulsacion.render("TE DA LAS GRACIAS, NOS SALVASTE",True, BLANCO)
            pantalla.blit(text3,[50,420])
            pantalla.blit(text1,[400,320])
            pantalla.blit(text2,[0,600])

        elif nivel1:



            #pantalla.draw(l[0][0],[0,0])
            #choque entre muros y enemigos para bordear el area de juego cuando alguno choca con un muro todos cambian de direccion
            col = pygame.sprite.groupcollide(EnemigosTipo1, limitesEnemy, False, False)
            if len(col) > 0:
                EnemigosTipo1.update(False, True)
            #para el segundo mundo redisenar este con un ciclo individual de sprites OJOOOOOOOOOO



            #Choque de balas contra el Escudo y limites
            pygame.sprite.groupcollide(disparos, Escudos, True, True)

            #vvalido que las balas no salgan de los limites
            for bala in disparos:
                ls_col = pygame.sprite.spritecollide(bala, limites, False)
                if len(ls_col) > 0:
                        bala.choque = True





            #cuando un enemigo toque el esucudo lo destruira
            pygame.sprite.groupcollide(EnemigosTipo1, Escudos, False, True)





            #choque de balas con los enemigos
            #col = pygame.sprite.groupcollide(disparosJugador, EnemigosTipo1, True, False)
            #print col
            for b in disparosJugador:
                ls_col = pygame.sprite.spritecollide(b, EnemigosTipo1, False)
                for e in ls_col:
                    b.kill()
                    e.muerto = True
                    puntos += e.points


            #disparos maquina
            #choque de las balas Enemigas con las balas jugadores
            col = pygame.sprite.groupcollide(disparosMaquina, disparosJugador, True, True)
            puntos += len(col)

            #Disparos de la maquina
            for rival in EnemigosTipo1:

                if rival.disparo == True:

                    b = CreateBalaEnemiga()
                    b.rect.x = rival.rect.x+ 25
                    b.rect.y = rival.rect.y + 50
                    disparosMaquina.add(b)
                    disparos.add(b)
                    general1.add(b)
                    rival.disparo = False

            #colision de los disparos maquina con el jugadores
            ls_col = pygame.sprite.spritecollide(jg, disparosMaquina, True)
            for e in ls_col:
                jg.vidas -= 1
                jg.destrucion = True


            #Redibujar vidas
            for v in vidas:
                v.kill()
            vidas = CreateVidas(general1,jg)


            if jg.vidas <= 0:
                JuegoPerdido = True
                nivel1 = False #acabo el nivel 1 ya que perdi

            if len(EnemigosTipo1) == 0:
                nivel1 = False
                inicio2= True

            ls_col = pygame.sprite.spritecollide(jg, EnemigosTipo1, False)
            if len(ls_col) > 0:
                JuegoPerdido = True
                nivel1 = False

            #contador tiempo
            textoreloj = relojAsc(f_con,f_tasa,fuentereloj)

            #manejo del bonus ENEMIGO QUE ES UN BONUS
            if tiempobonus <= 0:
                tiempobonus = 1000
                e = Enemigo2(bonus)
                EnemigosTipo2.add(e)
                Enemigos.add(e)
                general1.add(e)
                bonus = not bonus
            tiempobonus -= 1

            #colision con el bonus
            for b in disparosJugador:
                ls_col = pygame.sprite.spritecollide(b, EnemigosTipo2, True)
                if len(ls_col) > 0:
                    b.kill()
                    for e in ls_col:
                        jg.vidas += 1



            text1 = Marcador.render("SCORE", True, BLANCO)
            text2 = Puntuacion.render(strpuntos(puntos), True, BLANCO)
            text3 = Tipodejuego.render('DESTRUYE', True, BLANCO)

            pantalla.fill(NEGRO)
            pantalla.blit(text1,[25,10])
            pantalla.blit(text2, [50, 35])
            pantalla.blit(text3, [565, 10])
            pantalla.blit(textoreloj,[300,10])

            general1.update()
            general1.draw(pantalla)
            f_con += 1 #aumento el tiempo
        elif inicio2:

            if not iniciar:

                pantalla.fill(NEGRO)
                #text1 = Invaders.render("ESTE ES EL NIVEL 2", True, BLANCO)
                #pantalla.blit(text1, [50, 35])

                for v in range(jg.vidas):

                    pantalla.blit(imgvida, [100 + v * 60 , 200 ])
                    if v == jg.vidas - 1:
                        text3 = Pulsacion.render("+",True, BLANCO)
                        pantalla.blit(text3,[100 + v * 60 + 50,200])
                        pantalla.blit(imgvida, [100 + v * 60 + 70, 200 ])

                text3 = Pulsacion.render("Puntuacion =" + str(puntos),True, BLANCO)
                pantalla.blit(text3,[250,250])


                text1 = Invaders.render("SEGUNDO NIVEL", True, BLANCO)
                text2= Indicaciones.render("Use las flechas <- -> para moverse,  use espacio para disparar, SEGUNDO MUNDO SOBREVIVE", True, BLANCO)
                text3 = Pulsacion.render("PRESIONE CUALQUIER TECLA PARA CONTINUAR",True, BLANCO)
                pantalla.blit(text3,[50,420])
                pantalla.blit(text1,[150,100])
                pantalla.blit(text2,[0,600])

            else:
                pantalla.fill(NEGRO)
                jg.vidas += 1
                nivel2 = True
                inicio2 = False
                general1.empty()
                general1.add(jg)
                general1.add(limites)
                general1.add(limitesEnemy)
                #Escudos.empty()
                #Escudos = CreateEscudos(general1)
                general1.add(Escudos)
                disparos.empty()
                disparosJugador.empty()
                disparosMaquina.empty()
                EnemigosTipo1.empty()
                EnemigosTipo2.empty()
                Enemigos.empty()
                Enemigos.add(EnemigosTipo1)
                Enemigos.add(jefe)
                general1.add(jefe)
                EnemigosTipo2.add(jefe)
                f_con = 0
        elif nivel2:



            #introducir enemigos en el jeugo
            if jefe.introducir:
                jefe.introducir = False
                #jefe.tiempoBase -= 25
                jefe.tiempoIntro = jefe.tiempoBase
                X = jefe.rect.x
                Y = jefe.rect.y
                en = CreateEnemy1(X + 50,Y+ 60, 0, 0)
                en.temporizadormov = 0
                en.tiempoMov = 0
                general1.add(en)
                EnemigosTipo1.add(en)
                Enemigos.add(en)

            #choque entre muros y enemigo para que cuando llegue a la esquina baje
            col = pygame.sprite.groupcollide(EnemigosTipo1, limitesEnemy, False, False)
            for e in col:
                e.update(False, True)

            #Choque de balas contra el Escudo y limites
            pygame.sprite.groupcollide(disparos, Escudos, True, True)

            #vvalido que las balas no salgan de los limites
            for bala in disparos:
                ls_col = pygame.sprite.spritecollide(bala, limites, False)
                if len(ls_col) > 0:
                        bala.choque = True

            #cuando un enemigo toque el esucudo lo destruira
            pygame.sprite.groupcollide(EnemigosTipo1, Escudos, False, True)

            #choque de balas con los enemigos
            #col = pygame.sprite.groupcollide(disparosJugador, EnemigosTipo1, True, False)
            #print col
            for b in disparosJugador:
                ls_col = pygame.sprite.spritecollide(b, Enemigos, False)
                for e in ls_col:
                    b.kill()
                    e.muerto = True
                    puntos += e.points

            #disparos maquina
            #choque de las balas Enemigas con las balas jugadores
            col = pygame.sprite.groupcollide(disparosMaquina, disparosJugador, True, True)
            puntos += len(col)

            #Disparos de la maquina
            for rival in EnemigosTipo1:

                if rival.disparo == True:

                    b = CreateBalaEnemiga()
                    b.rect.x = rival.rect.x+ 25
                    b.rect.y = rival.rect.y + 50
                    disparosMaquina.add(b)
                    disparos.add(b)
                    general1.add(b)
                    rival.disparo = False

            #Redibujar vidas
            for v in vidas:
                v.kill()
            vidas = CreateVidas(general1,jg)


            if jg.vidas <= 0:
                JuegoPerdido = True
                nivel2 = False #acabo el nivel 1 ya que perdi

            #colision de los disparos maquina con el jugador
            ls_col = pygame.sprite.spritecollide(jg, disparosMaquina, True)
            for e in ls_col:
                jg.vidas -= 1
                jg.destrucion = True

            ls_col = pygame.sprite.spritecollide(jg, EnemigosTipo1, True)
            if len(ls_col) > 0:
                JuegoPerdido = True
                nivel2 = False


            #manejo del reloj descendente
            t_segundos = t_ini - (f_con// f_tasa)
            minutos = t_segundos // 60
            segundos = t_segundos % 60
            texto_reloj ='{0:02}:{1:02}'.format(minutos,segundos)
            textoreloj = None
            if t_segundos <= 5:
                textoreloj = fuentereloj.render(texto_reloj,True, ROJO)
            else:
                textoreloj = fuentereloj.render(texto_reloj,True, BLANCO)

            if t_segundos <= 0:
                Gano = True
                nivel2 = False

            text1 = Marcador.render("SCORE", True, BLANCO)
            text2 = Puntuacion.render(strpuntos(puntos), True, BLANCO)
            text3 = Tipodejuego.render('SOBREVIVE', True, BLANCO)

            pantalla.fill(NEGRO)
            pantalla.blit(text1,[25,10])
            pantalla.blit(text2, [50, 35])
            pantalla.blit(text3, [560, 10])
            pantalla.blit(textoreloj,[300,10])




            general1.update()
            general1.draw(pantalla)
            f_con +=1



        elif JuegoPerdido:
            pantalla.fill(NEGRO)
            pantalla.blit(gameover, [250, 150])
            text1 = Invaders.render("la UTP ha sido destruida", True, BLANCO)
            pantalla.blit(text1, [50, 35])
            text2= Indicaciones.render("TU PUNTAJE = "+ str(puntos) , True, BLANCO)
            pantalla.blit(text2,[250,450])



       # pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(f_tasa)
