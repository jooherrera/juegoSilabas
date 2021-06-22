#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      joo
#
# Created:     29/05/2021
# Copyright:   (c) joo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import sys
import menu
#import principal
from configuracion import *

class main:
    def __init__(self,width,height):
        pygame.init()
        pygame.mixer.music.load('sound/music.mp3') # Carga la musica de la pantalla inicial.
        pygame.mixer.music.play(-1) #Reproduce la musica infinitas veces.
        pygame.display.set_caption("Sí-la-bas...") #Titulo de la ventana.
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.BackGround = pygame.image.load("image/inicio/background.jpg") # Carga imagen de fondo de la pantalla inicial.
        self.BackGround = pygame.transform.scale(self.BackGround, (width, height))
        self.Github = pygame.image.load("image/inicio/github.png") # Carga imagen de GITHUB
        self.Github = pygame.transform.scale(self.Github, (width, height))
        self.menu = menu.menu(self.width, self.height) #Instancia al objeto MENU.
        self.bg_letras = pygame.image.load("image/inicio/bg-letras1.png") # Carga imagen de las letras en la pantalla de inicio.
        self.bg_letras = pygame.transform.scale(self.bg_letras, (width, height))
        self.pos = 0

    def draw(self):
        if not (pygame.display.get_init()):
            run = main(self.menu.width,self.menu.height)
            run.run()

        self.screen.fill((30, 30, 30))
        self.screen.blit(self.BackGround, (0, 0))
        self.screen.blit(self.bg_letras,(0,self.pos))
        self.screen.blit(self.bg_letras,(0,self.pos - self.height))
        self.screen.blit(self.Github, (0, 0))
        self.menu.draw(self.screen)
        pygame.display.flip()

    def handleInput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.menu.handelInput(input,self.screen)

    def run(self):
        while True:

            self.clock.tick(60)
           # self.framCrounter += 1
            self.handleInput()
            self.draw()
            if self.pos >= self.height:
                self.pos = 0
            self.pos += 1




run = main(Width, Height)
run.run()