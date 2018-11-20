import pygame, random,math
from MapGUI.Timer import Timer
from MapGUI.globals import Globals
from MapGUI.textures import Tiles

pygame.init()


def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[1]/ 2), int(size[0] / 2))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (tile_size[1],0,tile_size[0],tile_size[1]))
    faces["++"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (0,0, tile_size [0], tile_size[1]))
    faces["-+"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], tile_size[0],tile_size[1],tile_size[1]))
    faces["+-"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0 ,tile_size[0], tile_size[0], tile_size[1]))
    faces["--"] = west


    return faces

def MoveNPC(npc):
    npc.facing = random.choice(("++","-+","+-","--"))
    npc.walking = random.choice((True, False))

class Dialog:
    def __init__(self, text):
        self.Page = 0
        self.Text = text #[("Behold!! Praise the Mighty Hunter!"), ("A Hunter Must Never Run Away, No Matter How Strong the Monster"),("Save us From the Monstrous Terrifying Wyvern")]

class NPC:
    AllNPC = []
    def __init__(self, name, pos, dialog, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.heigh = sprite.get_height()
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()

        self.LastLocation = [0, 0]

        #get NPC faces
        self.facing = "++"
        self.faces = get_faces(sprite)

        #PUBLISH
        NPC.AllNPC.append(self)

    def Render(self, surface):
        self.Timer.Update()
        if self.walking :
            move_speed = 50 * Globals.deltatime
            if self.facing == "+-" :
                if not Tiles.Blocked_At((round(self.X), math.floor(self.Y))):
                    self.Y -= move_speed
            elif self.facing == "--"  :
                if not Tiles.Blocked_At ((math.floor(self.X), round(self.Y))):
                    self.X += move_speed
            elif self.facing == "-+"  :
                if not Tiles.Blocked_At((round(self.X), math.ceil(self.Y))):
                    self.Y += move_speed
            elif self.facing == "++":
                if not Tiles.Blocked_At((math.ceil(self.X), round(self.Y))):
                    self.X -= move_speed

            #BLOCK TILE NPC IS STANDING ON
            location = [round(self.X / Tiles.Size), round(self.Y / Tiles.Size)]
            if self.LastLocation in Tiles.Blocked:
                Tiles.Blocked.remove(self.LastLocation)

            if not location in Tiles.Blocked:
                Tiles.Blocked.append(location)
                self.LastLocation = location

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))



class Male1(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("char/player.png"))
        self.walking = False
class Male2(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("char/male1.png"))




