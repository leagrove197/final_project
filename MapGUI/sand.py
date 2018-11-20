import pygame

from MapGUI.globals import *


sand = pygame.sprite.Group()
class Sand(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,sand)
        self.x = x
        self.y = y
        self.image = pygame.image.load("tiles/monsters/generic.png")
        self.image = pygame.transform.scale(self.image,(1183,832))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey
sand1 = Sand(610,1885)
