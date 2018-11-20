import pygame
from MapGUI.globals import *


nurse = pygame.sprite.Group()
class Nurse(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,nurse)
        self.image  = pygame.image.load("char/nurse.png")
        self.image = pygame.transform.scale(self.image,(32,42))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey
nurse1 = Nurse(760,150)



