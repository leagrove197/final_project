import pygame
from MapGUI.NPC import *



pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self, name,job, x, y, maxhp, attack, maxxp, lv,pot):
        pygame.sprite.Sprite.__init__(self)
        self.job = job
        if self.job == "Knight":
            self.image = pygame.image.load("char/armorman3.png")
        elif self.job =="Thief":
             self.image = pygame.image.load("char/tile004.png")
        elif self.job == "Witch":
            self.image = pygame.image.load("char/witch3.png")
        self.rect = self.image.get_rect()
        self.rect.center = x,y
        self.rect.x += 15
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.attack = attack
        self.maxxp = maxxp
        self.xp = 0
        self.lv = lv
        self.pot = pot
        self.name = name
        self.walking = False
        self.current_frame = 0
        self.lastupdate = 0
        self.direction = 0


    def anime(self):
        if self.job == "Knight":

            self.now = pygame.time.get_ticks()
            self.atas = [pygame.image.load("char/armorman1.png"),pygame.image.load("char/armorman2.png")]
            self.bawah = [pygame.image.load("char/armorman3.png"),pygame.image.load("char/armorman4.png")]
            self.kiri =[pygame.image.load("char/armorman5.png"),pygame.image.load("char/armorman6.png")]
            self.kanan = [pygame.image.load("char/armorman7.png"),pygame.image.load("char/armorman8.png")]
            if self.walking :
                if self.now - self.lastupdate > 100 :
                    self.lastupdate = self.now
                    self.current_frame = (self.current_frame + 1) %len(self.atas)
                    if self.direction == 1:
                        self.image = self.atas[self.current_frame]

                    elif self.direction == 2:
                        self.image = self.bawah[self.current_frame]

                    elif self.direction == 3:
                        self.image = self.kiri[self.current_frame]

                    elif self.direction == 4:
                        self.image = self.kanan[self.current_frame]

        if self.job == "Thief":
            self.now = pygame.time.get_ticks()
            self.atas = [pygame.image.load("char/tile000.png"),pygame.image.load("char/tile001.png")]
            self.bawah = [pygame.image.load("char/tile002.png"),pygame.image.load("char/tile003.png")]
            self.kiri =[pygame.image.load("char/tile004.png"),pygame.image.load("char/tile005.png")]
            self.kanan = [pygame.image.load("char/tile006.png"),pygame.image.load("char/tile007.png")]
            if self.walking :
                if self.now - self.lastupdate > 100 :
                    self.lastupdate = self.now
                    self.current_frame = (self.current_frame + 1) %len(self.atas)
                    if self.direction == 1:
                        self.image = self.atas[self.current_frame]

                    elif self.direction == 2:
                        self.image = self.bawah[self.current_frame]

                    elif self.direction == 3:
                        self.image = self.kiri[self.current_frame]

                    elif self.direction == 4:
                        self.image = self.kanan[self.current_frame]
        if self.job == "Witch":
            self.now = pygame.time.get_ticks()
            self.atas = [pygame.image.load("char/witch1.png"),pygame.image.load("char/witch2.png")]
            self.bawah = [pygame.image.load("char/witch3.png"),pygame.image.load("char/witch4.png")]
            self.kiri =[pygame.image.load("char/witch5.png"),pygame.image.load("char/witch6.png")]
            self.kanan = [pygame.image.load("char/witch7.png"),pygame.image.load("char/witch8.png")]
            if self.walking :
                if self.now - self.lastupdate > 100 :
                    self.lastupdate = self.now
                    self.current_frame = (self.current_frame + 1) %len(self.atas)
                    if self.direction == 1:
                        self.image = self.atas[self.current_frame]

                    elif self.direction == 2:
                        self.image = self.bawah[self.current_frame]

                    elif self.direction == 3:
                        self.image = self.kiri[self.current_frame]

                    elif self.direction == 4:
                        self.image = self.kanan[self.current_frame]





playerSprite = pygame.sprite.Group()


