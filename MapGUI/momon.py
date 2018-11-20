import pygame

from MapGUI.globals import *


monster = pygame.sprite.Group()
class Momon(pygame.sprite.Sprite):
    def __init__(self,name,x,y,maxhp,attack,xp,lv):
        pygame.sprite.Sprite.__init__(self,monster)
        self.name = name
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.attack = attack
        self.xp = xp
        self.lv = lv
        self.x = x
        self.y = y

        if self.name == "Fire Ant":
            self.image = pygame.image.load('tiles/monsters/Ant.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Poisonous Snake':
            self.image = pygame.image.load('tiles/monsters/Snake.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'StingJellyfish':
            self.image = pygame.image.load('tiles/monsters/Jellyfish.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Mr.Crab':
            self.image = pygame.image.load('tiles/monsters/Crab.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'DeadWood':
            self.image = pygame.image.load('tiles/monsters/Angry Tree.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Skelly skelly':
            self.image = pygame.image.load('tiles/monsters/Skeleton.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Baby wyvern':
            self.image = pygame.image.load('tiles/monsters/Dragon.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Great Red Fire Dragon':
            self.image = pygame.image.load('tiles/monsters/Great Dragon.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        if self.name == 'Ancient Wyvern(BOSS)':
            self.image = pygame.image.load('tiles/monsters/bosss.png')
            self.image = pygame.transform.scale(self.image,(200,190))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


    def update(self):
        self.movex = self.x + Globals.camera_x
        self.movey = self.y + Globals.camera_y

        self.rect.x = self.movex
        self.rect.y = self.movey



ant1 = Momon("Fire Ant",1000, 750, 90, 10, 40, 1)
ant2 = Momon("Fire Ant",900, 600, 90, 10, 40, 1)
ant3 = Momon("Fire Ant",1190,450, 90, 10, 40, 1)
ant4 = Momon("Fire Ant",1200, 800, 90, 10, 40, 1)
ant5 = Momon("Fire Ant",900, 800, 90, 10, 40, 1)
ant6 = Momon("Fire Ant",950, 1100, 90, 10, 40, 1)
ant7 = Momon("Fire Ant",1300, 450, 90, 10, 40, 1)
ant8 = Momon("Fire Ant",1200, 1200, 90, 10, 40, 1)


snake1 = Momon("Poisonous Snake",1300,800, 120, 15,61,2,)
snake2 = Momon("Poisonous Snake",1400,600, 120, 15,61,2,)
snake3 = Momon("Poisonous Snake",1350,550, 120, 15,61,2,)
snake4 = Momon("Poisonous Snake",1500,780, 120, 15,61,2,)
snake5 = Momon("Poisonous Snake",1400,1450, 120, 15,61,2,)
snake6 = Momon("Poisonous Snake",1450,1000, 120, 15,61,2,)
snake7 = Momon("Poisonous Snake",1300,1250, 120, 15,61,2,)
snake8 = Momon("Poisonous Snake",1100,1360, 120, 15,61,2,)


jellyfish1 =Momon("StingJellyfish",800,2600, 130, 40,100,4)
jellyfish2 =Momon("StingJellyfish",1020,2190,130, 40,100,4)
jellyfish3 =Momon("StingJellyfish",700,2000, 130, 40,100,4)
jellyfish4 =Momon("StingJellyfish",1400,2120, 130, 40,100,4)
jellyfish5 =Momon("StingJellyfish",632,2432, 130, 40,100,4)
jellyfish6 =Momon("StingJellyfish",1300,2203, 130, 40,100,4)
jellyfish7 =Momon("StingJellyfish",1190,2300, 130, 40,100,4)
jellyfish8 =Momon("StingJellyfish",740,2590, 130, 40,100,4)



crab1=Momon("Mr.Crab",1000,2100,200, 25,120,5)
crab2=Momon("Mr.Crab",1400,2500,200, 25,120,5)
crab3=Momon("Mr.Crab",1320,2323, 200, 25,120,5)
crab4=Momon("Mr.Crab",1403,2320,200, 25,120,5)
crab5=Momon("Mr.Crab",934,2330,200, 25,120,5)
crab6=Momon("Mr.Crab",1323,2012,200, 25,120,5)
crab7=Momon("Mr.Crab",1200,2101,200, 25,120,5)
crab8=Momon("Mr.Crab",1102,2430,200, 25,120,5)


deadwood1 = Momon("DeadWood",2100,780, 400, 40,200,6)
deadwood2 = Momon("DeadWood",1850,1490, 400, 40,200,6)
deadwood3 = Momon("DeadWood",1920,600, 400, 40,200,6)
deadwood4 = Momon("DeadWood",760,730, 400, 40,200,6)
deadwood5 = Momon("DeadWood",2103,1200, 400, 40,200,6)
deadwood6 = Momon("DeadWood",2001,1001, 400, 40,200,6)
deadwood7 = Momon("DeadWood",2403,1120, 400, 40,200,6)
deadwood8 = Momon("DeadWood",2050,1530, 400, 40,200,6)


skeleton1 = Momon("Skelly skelly",1900,500, 290, 60,235,7)
skeleton2 = Momon("Skelly skelly",2504,1700, 290, 60,235,7)
skeleton3 = Momon("Skelly skelly",2001,700, 290, 60,235,7)
skeleton4 = Momon("Skelly skelly",2176,900, 290, 60,235,7)
skeleton5 = Momon("Skelly skelly",2295,1630, 290, 60,235,7)
skeleton6 = Momon("Skelly skelly",2304,1100, 290, 60,235,7)
skeleton7 = Momon("Skelly skelly",1990,1590, 290, 60,235,7)
skeleton8 = Momon("Skelly skelly",2403,1030, 290, 60,235,7)


babywyvern1 = Momon("Baby wyvern",1990,2200, 500, 70,340,9)
babywyvern2 = Momon("Baby wyvern",2040,1900, 500, 70,340,9)
babywyvern3 = Momon("Baby wyvern",2200,2080, 500, 70,340,9)
babywyvern4 = Momon("Baby wyvern",1950,2111, 500, 70,340,9)
babywyvern5 = Momon("Baby wyvern",2330,2102, 500, 70,340,9)
babywyvern6 = Momon("Baby wyvern",2302,2300, 500, 70,340,9)
babywyvern7 = Momon("Baby wyvern",1974,2300, 500, 70,340,9)
babywyvern8 = Momon("Baby wyvern",2420,2100, 500, 70,340,9)



greatdragon1 = Momon("Great Red Fire Dragon",1980,1900, 650, 85,420,10)
greatdragon2 = Momon("Great Red Fire Dragon",2300,2400, 650, 85,420,10)
greatdragon3 = Momon("Great Red Fire Dragon",2403,2032, 650, 85,420,10)
greatdragon4 = Momon("Great Red Fire Dragon",2500,2560, 650, 85,420,10)
greatdragon5 = Momon("Great Red Fire Dragon",2301,1940, 650, 85,420,10)
greatdragon6 = Momon("Great Red Fire Dragon",1990,2200, 650, 85,420,10)
greatdragon7 = Momon("Great Red Fire Dragon",2430,2630, 650, 85,420,10)
greatdragon8 = Momon("Great Red Fire Dragon",2100,2200, 650, 85,420,10)



wyvern = Momon("Ancient Wyvern(BOSS)", 2000,2400,270000,91000,0,999)



