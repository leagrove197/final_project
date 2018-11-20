import pygame

from MapGUI.globals import *


out= pygame.sprite.Group()
class Out(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,out)
        self.x = x
        self.y = y
        self.image = pygame.image.load("tiles/stone_interior/out.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey
out1 = Out(640,285)

