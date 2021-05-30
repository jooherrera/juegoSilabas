import pygame
from math import floor
import sys
from config import *
import os


class menu:
    def __init__(self, width, height):
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
        self.GITHUBcollider = (floor(91.4*self.width/100),floor(89.5*self.height/100))
        self.GITHUBcolliderW_H = (floor(6*self.width/100),floor(7.8*self.height/100))
        self.circle = pygame.Rect(self.GITHUBcollider,self.GITHUBcolliderW_H)
        self.mousePos = ""

    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 255, 255), self.player,1)
        screen.blit(self.menuPrincipal,(0,0))
        screen.blit(self.flechaIMG,self.player)
        if (self.quiereSalir):
            screen.blit(self.menuSalirIMG,(0,0))
            screen.blit(self.flechaUpIMG,self.playerUp)


        #screen = pygame.display.set_mode((self.width, self.height))


    def handelInput(self, input):
        self.mousePos = pygame.mouse.get_pos()
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
                print("Circle",self.circle)
                print("mousePos",self.mousePos)
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
                    print("PLAy")
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
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN and self.menuTitle == "creditos" and self.quiereSalir == False:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    self.menuPrincipal = self.menuIMG
                    self.menuTitle = "principal"
                    self.player.x = floor(29*self.width/100)
                    self.player.y = floor(52.4*self.height/100)

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