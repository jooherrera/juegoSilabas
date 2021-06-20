import pygame
#from math import floor
#import sys
from config import *
#import os

import os, random, sys, math
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesRESUELTO import *
from collections import OrderedDict



class Game:
    def __init__(self, width, height,screen,listaJugadoresPuntaje,nombre):

        self.width = width
        self.height = height
        #Centrar la ventana y despues inicializar pygame
        #os.environ["SDL_VIDEO_CENTERED"] = "1"
        #pygame.init()
        #pygame.mixer.init()
        name = ""
        #Preparar la ventana
        #pygame.display.set_caption("Rapido...")
        #screen = screen
        self.screen = screen
        #tiempo total del juego

        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        silabasEnPantalla=[]
        posiciones=[]
        listaDeSilabas=[]
        lemario=[]
        top = []


        #randomY = 0


        archivo3= open("top.txt","r")
        lectura2(archivo3, top)
        archivo3.close()


        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)
        archivo.close()


        archivo2= open("lemario.txt","r")
        lectura(archivo2, lemario)
        archivo2.close()

        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos,self.width,self.height)

        last = TIEMPO_MAX - 1

        inicio = pygame.time.get_ticks()/1000


        while segundos > fps/1000:


        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 50

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    #return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:

                        puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario)
                        candidata = ""
                        e.key=""


            segundos = inicio + TIEMPO_MAX - pygame.time.get_ticks()/1000
            #segundos = inicio+TIEMPO_MAX - gameClock.get_time()/1000
            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            #print(silabasEnPantalla)


            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos,self.width,self.height)

            pygame.display.flip()


            #actualizar(silabasEnPantalla, posiciones, listaDeSilabas)

            if last > segundos + .4:

                actualizar(silabasEnPantalla, posiciones, listaDeSilabas,width,height)
                last = segundos




        #if self.mensajePuntuacion():

            #print(self.pedirNombre())
        listaJugadoresPuntaje.append((puntos,nombre))

        #listaJugadoresPuntaje[nombre] = puntos
        return None
        while 1:
            #print(puntos)

            #Guardar nombre en array
            #Menu principal


            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()








class menu:

    def __init__(self, width, height):
        self.listaJugadores = []
        self.listaJugadoresPuntaje = []
        self.candidata = ""
        self.width = width
        self.height = height

        self.menuIMG = pygame.image.load("image/inicio/menu.png")
        self.menuIMG = pygame.transform.scale(self.menuIMG,(self.width,self.height))

        self.menuPrincipal = self.menuIMG
        self.menuPrincipal = pygame.transform.scale(self.menuPrincipal,(self.width,self.height))

        self.click_sound = pygame.mixer.Sound("sound/click.mp3")
        self.flechaIMG = pygame.image.load("image/inicio/arrow.png")
        self.menuTitle = "principal"
        #self.flechaIMG = pygame.transform.scale(self.flechaIMG, (floor(6.9*self.width/100),floor(6.7*self.width/100)))

        self.player = pygame.Rect(floor(29*width/100), floor(31.9*height/100),floor(6.9*self.width/100), floor(6.7*self.width/100))
        self.flechaIMG = pygame.transform.scale(self.flechaIMG,(self.player.width,self.player.height))

        #OPCIONES
        self.menuOpcionesIMG = pygame.image.load("image/inicio/menuOptions.png")
        self.menuOpcionesIMG = pygame.transform.scale(self.menuOpcionesIMG,(self.width,self.height))

        #NOMBRE
        self.menuNombreIMG = pygame.image.load("image/inicio/nombre.png")
        self.menuNombreIMG = pygame.transform.scale(self.menuNombreIMG,(self.width,self.height))


        self.menuTop3 = pygame.image.load("image/inicio/top3.png")
        self.menuTop3 = pygame.transform.scale(self.menuTop3,(self.width,self.height))


        #CREDITS
        self.menuCreditsIMG = pygame.image.load("image/inicio/menuCredits.png")
        self.menuCreditsIMG = pygame.transform.scale(self.menuCreditsIMG,(self.width,self.height))

        #Quiere Salir?
        self.menuSalirIMG = pygame.image.load("image/inicio/menuSalir.png")
        self.menuSalirIMG = pygame.transform.scale(self.menuSalirIMG,(self.width,self.height))

        self.flechaUpIMG = pygame.image.load("image/inicio/arrowUp.png")
        self.playerUp = pygame.Rect(floor(25*width/100), floor(53*height/100),floor(6.7*self.width/100), floor(6.9*self.width/100)) #SI UP
        self.flechaUpIMG = pygame.transform.scale(self.flechaUpIMG,(self.playerUp.width,self.playerUp.height))



        self.quiereSalir = False
        self.nombre = False
        self.GITHUBcollider = (floor(91.4*self.width/100),floor(89.5*self.height/100))
        self.GITHUBcolliderW_H = (floor(6*self.width/100),floor(7.8*self.height/100))
        self.circle = pygame.Rect(self.GITHUBcollider,self.GITHUBcolliderW_H)
        self.mousePos = ""
        self.ren1 = ""
        self.defaultFont = pygame.font.Font( pygame.font.get_default_font(), floor(3*self.width/100))
        self.principal = True
        self.puntaje = False
        self.puntos = []




    def draw(self, screen):

        if (self.principal):
            screen.blit(self.menuPrincipal,(0,0))
            self.ren1 = self.defaultFont.render(self.candidata, 1, (0,0,0))
            screen.blit(self.ren1,(floor(27*self.width/100),floor(24.8*self.height/100)))
            screen.blit(self.flechaIMG,self.player)

        if(self.puntaje):
            screen.blit(self.menuPrincipal,(0,0))
            self.puntos = sorted(self.listaJugadoresPuntaje, key=lambda x: x[0],reverse=True)
            #print(self.puntos)
            for cantJugadores in range(len(self.puntos)):
##
                if cantJugadores < 3 :
##                  #PUNTAJE
                    self.ren1 = self.defaultFont.render(str(self.puntos[cantJugadores][0]), 1, (0,0,0))
                    screen.blit(self.ren1,(floor(81.5*self.width/100),floor(35.15*self.height/100) + floor((cantJugadores *10 ) *self.height/100)))

                    #NOMBRE
                    self.ren1 = self.defaultFont.render(str(self.puntos[cantJugadores][1]), 1, (0,0,0))

                    screen.blit(self.ren1,(floor(16*self.width/100),floor(35.15*self.height/100) + floor((cantJugadores *10 ) *self.height/100)))

##                #print()



            screen.blit(self.flechaIMG,self.player)
        # pygame.draw.rect(screen, (255, 255, 255), self.player,1)

        if (self.quiereSalir):
            screen.blit(self.menuSalirIMG,(0,0))
            screen.blit(self.flechaUpIMG,self.playerUp)



        #screen = pygame.display.set_mode((self.width, self.height))


    def handelInput(self, input,screen):
        self.mousePos = pygame.mouse.get_pos()
        self.xx= ""


        for event in input:



            if event.type == pygame.KEYDOWN and self.quiereSalir == True:
                if event.key == pygame.K_LEFT and  self.playerUp.x > floor(25*self.width/100) :
                    self.click_sound.play()
                    self.playerUp.x -= floor(44*self.width/100)
                if event.key == pygame.K_RIGHT and  self.playerUp.x < floor(69*self.width/100) :
                    self.click_sound.play()
                    self.playerUp.x += floor(44*self.width/100)
                if event.key == pygame.K_RETURN and  self.playerUp.x == floor(25*self.width/100): #SI
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and  self.playerUp.x == floor(69*self.width/100): #NO
                    self.quiereSalir = False
                    event.key = ""
                if event.key == pygame.K_ESCAPE: #NO
                    self.quiereSalir = False
                    event.key = ""

            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("Circle",self.circle)
                #print("mousePos",self.mousePos)
                #print(self.circle)
                if (self.circle.collidepoint(self.mousePos)) :
                    os.system("start \"\" https://github.com/jooherrera/juegoSilabas")

            if event.type == pygame.KEYDOWN and self.menuTitle == "principal" and self.quiereSalir == False:

##                    if (circle.collidepoint(mousePos)) :
##                        os.system("start \"\" https://github.com/jooherrera/juegoSilabas")
                if event.key == pygame.K_ESCAPE:
##                    pygame.quit()
##                    sys.exit()
                    self.quiereSalir = True
                if event.key == pygame.K_DOWN and self.player.y < floor(62.7*self.height/100):
                    self.click_sound.play()
                    self.player.y += floor(10.41*self.height/100)
                if event.key == pygame.K_UP and self.player.y != floor(31.9*self.height/100):
                    self.click_sound.play()
                    self.player.y -= floor(10.41*self.height/100)
                if event.key == pygame.K_RETURN and self.player.y == floor(31.9*self.height/100): # PLAY
                    self.menuTitle = "play"
                    self.nombre = True
                    event.key =""
                    #self.menuPrincipal = self.menuIMG


                    #Game(self.width, self.height,screen)
                    #self.xx = input("Ingreese su nombre")

#run = main(600, 400)
                    #runGame.run()
                if event.key == pygame.K_RETURN and self.player.y == floor(42.1*self.height/100): # Options
                    print("Options")
                    self.menuTitle = "opciones"
                    self.menuPrincipal = self.menuOpcionesIMG
                    self.player.x = floor(29*self.height/100)
                    self.player.y = floor(37*self.height/100)
                    event.key =""
                elif event.key == pygame.K_RETURN and self.player.y == floor(42.1*self.height/100)+1: # Options
                    print("Options 800*600")
                    self.menuTitle = "opciones"
                    self.menuPrincipal = self.menuOpcionesIMG
                    self.player.x = floor(29*self.height/100)
                    self.player.y = floor(37*self.height/100)
                    event.key =""

                if event.key == pygame.K_RETURN and self.player.y == floor(52.4*self.height/100): # Credits
                    print("Credits")
                    self.menuTitle = "creditos"
                    self.menuPrincipal = self.menuCreditsIMG
                    self.player.y = floor(71*self.height/100)
                    event.key =""
                elif event.key == pygame.K_RETURN and self.player.y == floor(52.4*self.height/100)+1: # Credits
                    print("Credits")
                    self.menuTitle = "creditos"
                    self.menuPrincipal = self.menuCreditsIMG
                    self.player.y = floor(71*self.height/100)
                    event.key =""



                if event.key == pygame.K_RETURN and self.player.y == floor(62.7*self.height/100): # EXIT
                    #pygame.quit()
                    #sys.exit()
                    self.quiereSalir = True


            if self.menuTitle == "play" and self.quiereSalir == False:
                    print("NOMBRE")
                    self.menuTitle = "nombre"
                    self.menuPrincipal = self.menuNombreIMG
                    self.player.y = floor(49*self.height/100)
                    event.key =""

            if event.type == pygame.KEYDOWN and self.menuTitle == "creditos" and self.quiereSalir == False:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(52.4*self.height/100)


            if event.type == pygame.KEYDOWN and self.menuTitle == "nombre" and self.quiereSalir == False:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN and self.candidata != "":
                    #self.menuPrincipal = self.menuIMG
                    #self.menuTitle = "principal"
                    #self.player.x = floor(29*self.width/100)
                    #self.player.y = floor(62.7*self.height/100)

                    #self.listaJugadores.append(self.candidata)

                    #print(self.listaJugadores)
                    Game(self.width, self.height,screen,self.listaJugadoresPuntaje,self.candidata)
                    self.candidata = ""
                    event.key =""
                    self.principal = False
                    self.puntaje = True
                    self.menuPrincipal = self.menuTop3
                    self.menuTitle = "top3"
                    self.player.x = floor(33*self.width/100)
                    self.player.y = floor(83*self.height/100)
                    #print(self.listaJugadores)
                if event.type == pygame.KEYDOWN:
                    letra = dameLetraApretada(event.key)
                    self.candidata += letra
                    #print(self.candidata)
                    if event.key == K_BACKSPACE:
                        self.candidata = self.candidata[0:len(self.candidata)-1]
                    #ren1 = defaultFont.render(self.candidata, 1, (0,0,0))
                    #screen.blit(ren1, (floor(23.75*self.width/100), floor(92*self.height/100)))#190-570
                    #screen.blit(ren1, (0,0))#190-570

            if event.type == pygame.KEYDOWN and self.menuTitle == "top3" and self.quiereSalir == False :

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN :
                    print("principal")
                    self.principal = True
                    self.puntaje = False
                    self.menuTitle = "principal"
                    self.menuPrincipal = self.menuIMG
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(31.9*self.height/100)


            if event.type == pygame.KEYDOWN and self.menuTitle == "opciones" and self.quiereSalir == False:
                if event.key == pygame.K_ESCAPE:
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(42.1*self.height/100)
                if event.key == pygame.K_DOWN and self.player.y != floor(67.9*self.height/100):
                    self.click_sound.play()
                    self.player.y += floor(10.41*self.height/100)
                if event.key == pygame.K_UP and self.player.y != floor(37*self.height/100):
                    self.click_sound.play()
                    self.player.y -= floor(10.41*self.height/100)
                if event.key == pygame.K_RETURN and self.player.y == floor(37*self.height/100): #600*400

                    self.width = 600
                    self.height = 400
                    self.GITHUBcollider = (floor(91.4*self.width/100),floor(89.5*self.height/100))
                    self.GITHUBcolliderW_H = (floor(6*self.width/100),floor(7.8*self.height/100))
                    self.circle = pygame.Rect(self.GITHUBcollider,self.GITHUBcolliderW_H)

                    #pygame.display.set_mode((600, 400))
                    pygame.display.quit()

                if event.key == pygame.K_RETURN and self.player.y == floor(47.3*self.height/100): #800*600

                    self.width = 800
                    self.height = 600

                    #pygame.display.set_mode((600, 400))
                    pygame.display.quit()
                elif event.key == pygame.K_RETURN and self.player.y == floor(47.3*self.height/100) +1: #800*600 x2

                    self.width = 800
                    self.height = 600

                    #pygame.display.set_mode((600, 400))
                    pygame.display.quit()
                if event.key == pygame.K_RETURN and self.player.y == floor(57.6*self.height/100): #1024*768

                    self.width = 1024
                    self.height = 768

                    #pygame.display.set_mode((600, 400))
                    pygame.display.quit()
                elif event.key == pygame.K_RETURN and self.player.y == floor(57.6*self.height/100)+1: #1024*768

                    self.width = 1024
                    self.height = 768

                    #pygame.display.set_mode((600, 400))
                    pygame.display.quit()

                if event.key == pygame.K_RETURN and self.player.y == floor(67.9*self.height/100): # EXIT
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(42.1*self.height/100)
                elif event.key == pygame.K_RETURN and self.player.y == floor(67.9*self.height/100) +1 : # EXIT
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(42.1*self.height/100)








       #print(self.playerUp.x)
        #print( floor(69*self.width/100))
        pass
