import pygame

from MapGUI.globals import *


lava = pygame.sprite.Group()
class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y,damage):
        pygame.sprite.Sprite.__init__(self,lava)
        self.damage = damage
        self.x = x
        self.y = y
        self.image = pygame.image.load("tiles/lava.png")
        self.image = pygame.transform.scale(self.image,(450,500))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey
lava1 = Lava(2000,2000,20)

