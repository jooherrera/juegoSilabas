import pygame
import os, random, sys, math
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesRESUELTO import *
from collections import OrderedDict

class Sound: # Objeto que tiene el metodo para reproducir los sonidos.
    def __init__(self):
        pass


    def play(self,nombre):
        archivo = "sound/"+ nombre + ".mp3"
        pygame.mixer.Sound(archivo).play()

class Game: #Objeto Game.. Contiene el juego.
    def __init__(self, width, height,screen,listaJugadoresPuntaje,nombre):
        reproducirSonido = Sound() #Instancia el objeto Sonido
        self.width = width
        self.height = height
        name = ""
        self.screen = screen

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

        coloresSilabas=[]

        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)
        archivo.close()


        archivo2= open("lemario.txt","r")
        lectura(archivo2, lemario)
        archivo2.close()

        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos,self.width,self.height,coloresSilabas)

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
                    if e.key == K_RETURN and candidata != "":


                        resp =  procesar(candidata, silabasEnPantalla, posiciones, lemario, coloresSilabas,reproducirSonido)
                        #puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario, coloresSilabas,reproducirSonido)
                        if resp != None:
                            puntos += resp
                            candidata = ""
                            e.key=""
                        else:
                            return None

            segundos = inicio + TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos,self.width,self.height,coloresSilabas)
            pygame.display.flip()

            actualizar(silabasEnPantalla, posiciones, listaDeSilabas,width,height,segundos,coloresSilabas)

        listaJugadoresPuntaje.append((puntos,nombre))
        return None

        while 1:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()

class menu: #Objeto Menu -- Contiene todos los menu.. y sus funcionalidades.

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
        pygame.mixer.music.play(-1) #Reproduce la musica infinitas veces.


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
            for cantJugadores in range(len(self.puntos)):
                if cantJugadores < 3 :
##                  #PUNTAJE
                    self.ren1 = self.defaultFont.render(str(self.puntos[cantJugadores][0]), 1, (0,0,0))
                    screen.blit(self.ren1,(floor(81.5*self.width/100),floor(35.15*self.height/100) + floor((cantJugadores *10 ) *self.height/100)))

                    #NOMBRE
                    self.ren1 = self.defaultFont.render(str(self.puntos[cantJugadores][1]), 1, (0,0,0))
                    screen.blit(self.ren1,(floor(16*self.width/100),floor(35.15*self.height/100) + floor((cantJugadores *10 ) *self.height/100)))

            screen.blit(self.flechaIMG,self.player)

        if (self.quiereSalir):
            screen.blit(self.menuSalirIMG,(0,0))
            screen.blit(self.flechaUpIMG,self.playerUp)


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
                if (self.circle.collidepoint(self.mousePos)) :
                    os.system("start \"\" https://github.com/jooherrera/juegoSilabas")

            if event.type == pygame.KEYDOWN and self.menuTitle == "principal" and self.quiereSalir == False:
                if event.key == pygame.K_ESCAPE:
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
                if event.key == pygame.K_RETURN and self.player.y == floor(42.1*self.height/100): # Options

                    self.menuTitle = "opciones"
                    self.menuPrincipal = self.menuOpcionesIMG
                    self.player.x = floor(29*self.height/100)
                    self.player.y = floor(37*self.height/100)
                    event.key =""
                if event.key == pygame.K_RETURN and self.player.y == floor(52.4*self.height/100): # Credits

                    self.menuTitle = "creditos"
                    self.menuPrincipal = self.menuCreditsIMG
                    self.player.y = floor(71*self.height/100)
                    event.key =""
                if event.key == pygame.K_RETURN and self.player.y == floor(62.7*self.height/100): # EXIT
                    self.quiereSalir = True

            if self.menuTitle == "play" and self.quiereSalir == False:

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
                if event.key == pygame.K_ESCAPE:
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(31.9*self.height/100)
                    self.candidata = ""

                if  event.key == pygame.K_RETURN and self.candidata != "":
                    pygame.mixer.music.stop() #Para la musica infinitas veces.
                    Game(self.width, self.height,screen,self.listaJugadoresPuntaje,self.candidata)
                    self.candidata = ""
                    event.key =""
                    self.principal = False
                    self.puntaje = True
                    self.menuPrincipal = self.menuTop3
                    self.menuTitle = "top3"
                    self.player.x = floor(33*self.width/100)
                    self.player.y = floor(83*self.height/100)
                if event.type == pygame.KEYDOWN:
                    letra = dameLetraApretada(event.key)
                    self.candidata += letra
                    if event.key == K_BACKSPACE:
                        self.candidata = self.candidata[0:len(self.candidata)-1]

            if event.type == pygame.KEYDOWN and self.menuTitle == "top3" and self.quiereSalir == False :

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN :
                    pygame.mixer.music.play(-1) #Reproduce la musica infinitas veces.
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
                if event.key == pygame.K_DOWN and self.player.y != floor(67.9*self.height/100): #67.9
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
                    pygame.display.quit()
                if event.key == pygame.K_RETURN and self.player.y == floor(47.3*self.height/100): #800*600
                    self.width = 824
                    self.height = 614
                    pygame.display.quit()
                if event.key == pygame.K_RETURN and self.player.y == floor(57.6*self.height/100): #1024*768
                    self.width = 1024
                    self.height = 768
                    pygame.display.quit()
                if event.key == pygame.K_RETURN and self.player.y == floor(67.9*self.height/100): # EXIT
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(42.1*self.height/100)
