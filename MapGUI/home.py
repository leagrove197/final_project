import pygame

from MapGUI.globals import *


home = pygame.sprite.Group()
class Home(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,home)
        self.x = x
        self.y = y
        self.image = pygame.image.load("tiles/houseoverworld.png")
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey
home1 = Home(580,75)
