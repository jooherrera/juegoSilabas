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
from config import *

class main:
    def __init__(self,width,height):
        pygame.init()
        pygame.mixer.music.load('sound/music.mp3')
        pygame.mixer.music.play(-1)
        self.width = width
        self.height = height
        #self.framCrounter = 0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.BackGround = pygame.image.load("image/inicio/background.jpg")
        self.BackGround = pygame.transform.scale(self.BackGround, (width, height))
        self.Github = pygame.image.load("image/inicio/github.png")
        self.Github = pygame.transform.scale(self.Github, (width, height))
        self.menu = menu.menu(self.width, self.height)

        self.bg_letras = pygame.image.load("image/inicio/bg-letras1.png")
        self.bg_letras = pygame.transform.scale(self.bg_letras, (width, height))
        self.pos = 0
        #mousePos = (pygame.mouse.get_pos())
    #    self.circle = pygame.Rect(GITHUBcollider,GITHUBcolliderW_H)


    pass


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
        #circle2 = pygame.draw.rect(self.screen,(255,0,0),(GITHUBcollider,GITHUBcolliderW_H))

        #self.player.drawBullets(self.screen)
        #self.player.draw(self.screen)
        #self.drawAlien()
        pygame.display.flip()

    def handleInput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.menu.handelInput(input)

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
#run = main(600, 400)
run.run()