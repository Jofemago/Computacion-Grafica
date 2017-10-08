import pygame
import random

from Player import *
from configuraciones import *
from Proyectil import *
from Enemys import *


if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    paqueteEnemy = 5 #cantidad de enemigos que apareceran cada tanto
    #Grupos de Sprites
    jugadores = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    balasjg = pygame.sprite.Group()
    balasEnemigas = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    general = pygame.sprite.Group()

    #jugador
    jg = Player(50,50,10)


    jugadores.add(jg)
    general.add(jg)

    #se crean las vidas del jugador
    for vida in range(jg.vidas):
        v = Vida()
        v.rect.x = 5 + vida * 45
        v.rect.y = 35
        vidas.add(v)

    #se generan los rivales
    for rival in range(paqueteEnemy):
        temp = random.randrange(100, 500)
        r = Enemy(temp)
        r.rect.x = random.randrange(ANCHO, ANCHO * 2)
        r.rect.y = random.randrange(100, (ALTO - 25) )
        general.add(r)
        enemigos.add(r)

    puntos = 0
    fin_Juego = False
    recrearEnemy = 100 # variable que decrecera para crear mas enemigos cuando sea 0
    reloj = pygame.time.Clock()
    fin  = False
    puntos = 0

    fuente=pygame.font.Font(None, 36)
    points=pygame.font.Font(None, 15)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYUP:

                jg.var_y = 0
                jg.var_x = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    jg.var_x = 5

                if event.key == pygame.K_LEFT:

                    jg.var_x = -5


                if event.key == pygame.K_UP:

                    jg.var_y = -5

                if event.key == pygame.K_DOWN:

                    jg.var_y = 5

                if event.key == pygame.K_SPACE:

                    bala = Proyectil(1)
                    bala.rect.x = jg.rect.x + 50
                    bala.rect.y = jg.rect.y + 25
                    balasjg.add(bala)
                    general.add(bala)


        #processo para crear enemigos infitos
        recrearEnemy -= 1
        if recrearEnemy < 0:
            for rival in range(paqueteEnemy):
                temp = random.randrange(100, 500)
                r = Enemy(temp)
                r.rect.x = random.randrange(ANCHO, ANCHO * 2)
                r.rect.y = random.randrange(100, (ALTO - 25) )
                general.add(r)
                enemigos.add(r)

                if rival == 3:

                    nr = EnemyDos(temp)
                    nr.rect.x = random.randrange(ANCHO, ANCHO * 2)
                    nr.rect.y = random.randrange(100, (ALTO - 25) )
                    general.add(nr)
                    enemigos.add(nr)

                recrearEnemy = 100
                #paqueteEnemy += 1

        #Balasjg contra enemigos
        for b in balasjg:
            ls_col = pygame.sprite.spritecollide(b, enemigos, False)

            for e in ls_col:

                general.remove(e)
                enemigos.remove(e)
                puntos += 1
                if puntos == 30:
                    fin_Juego = True #se acaba el jueg cuando llega  a 30 puntos
            if len(ls_col):
                general.remove(b)
                balasjg.remove(b)

        #BalasMaquina vs jugadores
        '''for b in balasEnemigas:
            col = pygame.sprite.spritecollide(b, jugadores, False)
            jg.vidas -= 1
            if len(col):
                general.remove(b)
                balasjg.remove(b)'''

        col = pygame.sprite.spritecollide(jg, balasEnemigas, True)
        for e in col:
            jg.vidas -=1
            if jg.vidas ==0 : fin_Juego = True
            balasEnemigas.remove(e)
            general.remove(e)

        #balascontrabala

        col3 = pygame.sprite.groupcollide(balasEnemigas, balasjg, True, True)



        #choque enemigos contra jugadores
        col = pygame.sprite.spritecollide(jg, enemigos, True)
        for e in col:
            jg.vidas -=1
            if jg.vidas ==0 : fin_Juego = True
            balasEnemigas.remove(e)
            general.remove(e)



        #Disparos de la maquina
        for rival in enemigos:

            if rival.disparo == True:

                b = Proyectil(2)
                b.rect.x = rival.rect.x
                b.rect.y = rival.rect.y + 12
                balasEnemigas.add(b)
                general.add(b)
                rival.disparo = False


        #REdibujar vidas
        vidas.empty()
        for vida in range(jg.vidas):
            v = Vida()
            v.rect.x = 5 + vida * 45
            v.rect.y = 35
            vidas.add(v)


        text = points.render( "Points " + str(puntos), True, BLANCO)
        pantalla.fill(NEGRO)
        pantalla.blit(text, [700, 30])

        if fin_Juego and jg.vidas == 0:
            salida = fuente.render( 'TU A PERDU', True, BLANCO)
            pantalla.blit(salida, [200, 200])

        elif fin_Juego and puntos == 30:
            salida = fuente.render( 'VOUS AVEZ GAGNE', True, BLANCO)
            pantalla.blit(salida, [200, 200])
            vidas.draw(pantalla)


        else:

            general.update()
            vidas.update()
            vidas.draw(pantalla)
            general.draw(pantalla)
            pygame.draw.line(pantalla, BLANCO, [0,100], [ANCHO,100], 5)

        pygame.display.flip()
        reloj.tick(60)
