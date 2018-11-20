import sys, time, pickle
from MapGUI.map_engine import *
from MapGUI.momon import *
from MapGUI.player import *
from MapGUI.GUI import *
from MapGUI.lava import *
from MapGUI.sand import *
from MapGUI.home import *
from MapGUI.houseout import *
from MapGUI.nurse import *

pygame.init()
pygame.mixer.init()

cSec = 0
cFrame = 0
FPS = 0

def save_data(num):
    pickle.dump([player.name,player.hp,player.maxhp,player.xp,player.maxxp,player.attack,player.lv,player.pot,player.job],open("Char{}.sav".format(num),"wb"))

def load_data(num):
     player.name,player.hp,player.maxhp,player.xp,player.maxxp,player.attack,player.lv,player.pot,player.job =pickle.load(open("Char{}.sav".format(num),"rb"))

terrain = Map_Engine.load_map("rpgmap3.map")
houseterrain = Map_Engine.load_map("housemap3.map")

sky = pygame.image.load("tiles/bgcloud.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

wpp = pygame.image.load("wallpaper/dragonwallpp.jpg")
Wpp = pygame.Surface(wpp.get_size(), pygame.HWSURFACE)
Wpp.blit(wpp, (0, 0))
del wpp
lose = pygame.image.load("wallpaper/lose.jpg")
Lose_image = pygame.transform.scale(lose, (1200, 800))
Lose_image.blit(Lose_image, (0, 0))
del lose

win = pygame.image.load("wallpaper/WINNING.jpg")
Win_image = pygame.transform.scale(win, (1200, 800))
Win_image.blit(Win_image, (0, 0))
del win

job = pygame.image.load("wallpaper/backgro.png")
Job_image = pygame.transform.scale(job, (1200, 800))
Job_image.blit(Job_image, (0, 0))
del job

dialog_background = pygame.image.load("wallpaper/dialog1.png")
Dialog_background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
Dialog_background.blit(dialog_background, (0, 0))
Dialog_background_Width, Dialog_background_Height = Dialog_background.get_size()
del dialog_background

dialog_background1 = pygame.image.load("char/dialognurse.png")
Dialog_background1 = pygame.Surface(dialog_background1.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
Dialog_background1.blit(dialog_background1, (0, 0))
Dialog_background1_Width, Dialog_background1_Height = Dialog_background1.get_size()
del dialog_background1

stats = pygame.image.load("wallpaper/statstext.png")
rect = stats.get_rect()
Stats = pygame.transform.scale(stats, (int(rect.width * 0.3), int(rect.height * 0.4)))
del stats

panah = pygame.image.load("buttons/right.png")
rect = panah.get_rect()
Panah = pygame.transform.scale(panah, (int(rect.width * 4), int(rect.height * 4)))
del panah


combatterrain = pygame.image.load("fightpict/combat.jpg")
rect = combatterrain.get_rect()
Combat_Terrain = pygame.transform.scale(combatterrain, (int(rect.width * 1.5), int(rect.height * 1.727861771058315)))
del combatterrain

combattext = pygame.image.load("fightpict/TEXTRED.png")
rect = combattext.get_rect()
CombatTEXT = pygame.transform.scale(combattext, (int(rect.width * 0.5), int(rect.height * 0.5)))
del combattext

attackimage = pygame.image.load("buttons/slash_attack.png")
rect = attackimage.get_rect()
Attackimage = pygame.transform.scale(attackimage, (int(rect.width * 3), int(rect.height * 3)))
del attackimage

attackimage = pygame.image.load("buttons/fireeffect.png")
rect = attackimage.get_rect()
Attackimage1 = pygame.transform.scale(attackimage, (int(rect.width * 0.2), int(rect.height * 0.2)))
del attackimage

attackimage = pygame.image.load("buttons/swordslash.png")
attackimage = pygame.transform.flip(attackimage,True,False)
rect = attackimage.get_rect()
Attackimage2 = pygame.transform.scale(attackimage, (int(rect.width * 0.3), int(rect.height * 0.3)))
del attackimage

bigattack = pygame.image.load("buttons/big_attack.png")
rect = bigattack.get_rect()
Bigattack = pygame.transform.scale(bigattack, (int(rect.width * 3), int(rect.height * 3)))
del bigattack

heal = pygame.image.load("buttons/heal.png")
rect = heal.get_rect()
Heal= pygame.transform.scale(heal, (int(rect.width * 0.2), int(rect.height * 0.2)))
del heal


attbutton = pygame.image.load("buttons/sword1.png")
rect = attbutton.get_rect()
Attbutton = pygame.transform.scale(attbutton, (int(rect.width * 0.3), int(rect.height * 0.3)))
del attbutton

attbutton1 = pygame.image.load("buttons/dagger.png")
rect = attbutton1.get_rect()
Attbutton1 = pygame.transform.scale(attbutton1, (int(rect.width * 0.13), int(rect.height * 0.13)))
del attbutton1

attbutton = pygame.image.load("buttons/fireball.png")
attbutton2 = pygame.transform.flip(attbutton,True,False)
rect = attbutton2.get_rect()
Attbutton2 = pygame.transform.scale(attbutton2, (int(rect.width * 0.06), int(rect.height * 0.06)))
del attbutton2

potbutton = pygame.image.load("buttons/Potion.png")
rect = potbutton.get_rect()
Potbutton = pygame.transform.scale(potbutton, (int(rect.width * 0.7), int(rect.height * 0.7)))
del potbutton

warrior = pygame.image.load("fightpict/charr.png")
rect = warrior.get_rect()
Warrior = pygame.transform.scale(warrior, (int(rect.width * 0.4), int(rect.height * 0.4)))
del warrior

mage = pygame.image.load("fightpict/mage.png")
mage = pygame.transform.flip(mage,True, False)
rect = mage.get_rect()
Mage = pygame.transform.scale(mage, (int(rect.width * 0.57), int(rect.height * 0.57)))
del mage

thief = pygame.image.load("fightpict/thief1.png")
rect = thief.get_rect()
Thiefpict = pygame.transform.scale(thief, (int(rect.width * 0.35), int(rect.height * 0.35)))
del thief

warrior1 = pygame.image.load("fightpict/charr.png")
rect = warrior1.get_rect()
Warrior1 = pygame.transform.scale(warrior1, (int(rect.width * 0.55), int(rect.height * 0.55)))
del warrior1

thief1 = pygame.image.load("fightpict/thief1.png")
rect = thief1.get_rect()
Thief1 = pygame.transform.scale(thief1, (int(rect.width * 0.45), int(rect.height * 0.45)))
del thief1

mage1 = pygame.image.load("fightpict/mage.png")
mage1 = pygame.transform.flip(mage1,True, False)
rect = mage1.get_rect()
Mage1 = pygame.transform.scale(mage1, (int(rect.width * 0.69), int(rect.height * 0.69)))
del mage1

ant_image = pygame.image.load("fightpict/semutt.png")
rect = ant_image.get_rect()
Ant_image = pygame.transform.scale(ant_image, (int(rect.width), int(rect.height)))
del ant_image

snake_image = pygame.image.load("fightpict/snake.png")
rect = snake_image.get_rect()
Snake_image = pygame.transform.scale(snake_image, (int(rect.width * 1.2), int(rect.height * 1.2)))
del snake_image

jellyfish_image = pygame.image.load("fightpict/jellyfish.png")
rect = jellyfish_image.get_rect()
Jellyfish_image = pygame.transform.scale(jellyfish_image, (int(rect.width * 0.3), int(rect.height * 0.3)))
del jellyfish_image

crab_image = pygame.image.load("fightpict/crab.png")
Crab_image = pygame.Surface(crab_image.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
Crab_image.blit(crab_image, (0, 0))
Crab_image_Width, Crab_image_Height = Crab_image.get_size()
del crab_image

deadwood_image = pygame.image.load("fightpict/deadwood.png")
rect = deadwood_image.get_rect()
Deadwood_image = pygame.transform.scale(deadwood_image, (int(rect.width * 0.4), int(rect.height * 0.4)))
del deadwood_image

skeleton_image = pygame.image.load("fightpict/skeleton.png")
rect = skeleton_image.get_rect()
Skeleton_image = pygame.transform.scale(skeleton_image, (int(rect.width * 0.9), int(rect.height * 0.9)))
del skeleton_image

babywyvern_image = pygame.image.load("fightpict/Wyvern.png")
rect = babywyvern_image.get_rect()
Babywyvern_image = pygame.transform.scale(babywyvern_image, (int(rect.width * 0.8), int(rect.height * 0.8)))
del babywyvern_image

greatdragon_image = pygame.image.load("fightpict/Dragon.png")
rect = greatdragon_image.get_rect()
Greatdragon_image = pygame.transform.scale(greatdragon_image, (int(rect.width * 0.8), int(rect.height * 0.8)))
del greatdragon_image

wyvern_image = pygame.image.load("fightpict/boss.png")
Wyvern_image = pygame.Surface(wyvern_image.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
Wyvern_image.blit(wyvern_image, (0, 0))
Wyvern_image_Width, Wyvern_image_Height = Wyvern_image.get_size()
del wyvern_image

fps_font = pygame.font.SysFont("", 20)

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def screen():
    global window, window_height, window_width, window_title
    window_width, window_height = 1200, 800
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)


def count_fps():
    global cSec, cFrame, FPS
    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            Globals.deltatime = 1 / FPS


screen()

OPDialog = Dialog(text=[("      Welcome to", "", "  NIGHTMARE HUNT", "   Cry of the Wyvern",
                         "                                 Made by : Leagrove","            "
                                                                               "                                       "
                                                                               "                                     Press Space to Continue"),

                        ("All You Have to Do Is Kill Kill Kill", "", "", "enjoy :D"), ("", "", "AND DON'T DIE!!!")])
Globals.active_dialog = OPDialog

man1 = Male1(name="Zaky", pos=(800, 600), dialog=Dialog(
    text=[("Villager1", "",
           "        Save me from the Monstrous Wyern!!"), ("Villager1","","     The Wyvern is Located in a Hot Place"), ("Villager1","","       NOW GO!!")]))
man3 = Male2(name="a", pos=(1500, 1500), dialog=Dialog(
    text=[( "Villager2","","     All Hail Mighty Hunter"), ("Villager2","","     Fate of this Town.."), ("Villager2","","        Is in Your Hand!")]))

# initialize Music

pygame.mixer.music.load("Music/Overworld.mp3")
pygame.mixer.music.play(-1)


# initialize GUI
def Play():
    Globals.scene = "Createchar"

btnPlay = Menu.Button(text="LET THE HUNT BEGIN!!", rect=(30, 100, 350, 50),
                      bg=Color.DarkSlateGray, fg=Color.GhostWhite,
                      bgr=Color.Azure, tag=("menu", None))
btnPlay.Command = Play


def Knight():
    global player
    player = Player("Artorias","Knight",575,385,145,30,100,1,0)
    playerSprite.add(player)
    Globals.scene ="game"
    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
    pygame.mixer.music.play(-1)

btnKnight = Menu.Button(text="Artorias", rect=(150, 500, 250, 50),
                      bg=Color.DarkSlateGray, fg=Color.GhostWhite,
                      bgr=Color.Azure, tag=("Createchar", None))

btnKnight.Command = Knight
Knighttext2 = Menu.Text(text="Class : Knight", color=Color.Brown, font=Font.Scanner)
Knighttext2.Left,Knighttext2.Top = 150,570
Knighttext3 = Menu.Text(text="Desc  : High Hp, Low Damage", color=Color.Brown, font=Font.Scanner)
Knighttext3.Left,Knighttext3.Top = 150,590
Knighttext = Menu.Text(text="His Armor is Made out of ", color=Color.Brown, font=Font.Scanner)
Knighttext.Left,Knighttext.Top = 150,620
Knighttext1 = Menu.Text(text="Dragon Skin,Nothing Breaks it", color=Color.Brown, font=Font.Scanner)
Knighttext1.Left,Knighttext1.Top = 150,640
Knighttext4 = Menu.Text(text="\"A knight must never", color=Color.Brown, font=Font.Scanner)
Knighttext4.Left,Knighttext4.Top = 150,680
Knighttext5 = Menu.Text(text="  run away,no matter ", color=Color.Brown, font=Font.Scanner)
Knighttext5.Left,Knighttext5.Top = 150,700
Knighttext6 = Menu.Text(text="  how mighty the enemy\"", color=Color.Brown, font=Font.Scanner)
Knighttext6.Left,Knighttext6.Top = 150,720
Knighttext7 = Menu.Text(text="-Artorias", color=Color.Brown, font=Font.Scanner)
Knighttext7.Left,Knighttext7.Top = 300,740




def Thief():
    global player
    player = Player("Leagrove","Thief",575,385,75,65,100,1,0)
    playerSprite.add(player)
    Globals.scene ="game"
    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
    pygame.mixer.music.play(-1)

btnThief = Menu.Button(text="Leagrove", rect=(470, 500, 250, 50),
                      bg=Color.DarkSlateGray, fg=Color.GhostWhite,
                      bgr=Color.Azure, tag=("Createchar", None))

btnThief.Command = Thief
Thieftext = Menu.Text(text="Class : Thief", color=Color.Brown, font=Font.Scanner)
Thieftext.Left,Thieftext.Top = 470,570
Thieftext1 = Menu.Text(text="Desc : High Damage low Hp", color=Color.Brown, font=Font.Scanner)
Thieftext1.Left,Thieftext1.Top = 470,590
Thieftext2 = Menu.Text(text="Coldblood and Brutal,", color=Color.Brown, font=Font.Scanner)
Thieftext2.Left,Thieftext2.Top = 470,620
Thieftext4 = Menu.Text(text="Nobody Matches His Speed", color=Color.Brown, font=Font.Scanner)
Thieftext4.Left,Thieftext4.Top = 470,640
Thieftext3 = Menu.Text(text="\"Dont Blink, or You'll Miss Me\"", color=Color.Brown, font=Font.Scanner)
Thieftext3.Left,Thieftext3.Top = 470,680
# Thieftext5 = Menu.Text(text=" ", color=Color.Brown, font=Font.Scanner)
# Thieftext5.Left,Thieftext5.Top = 470,700
Thieftext6 = Menu.Text(text="-Leagrove", color=Color.Brown, font=Font.Scanner)
Thieftext6.Left,Thieftext6.Top = 620,700
def Witch():
    global player
    player = Player("Emilia","Witch",575,385,90,40,100,1,2)
    playerSprite.add(player)
    Globals.scene ="game"
    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
    pygame.mixer.music.play(-1)

btnWitch = Menu.Button(text="Emilia", rect=(780, 500, 250, 50),
                      bg=Color.DarkSlateGray, fg=Color.GhostWhite,
                      bgr=Color.Azure, tag=("Createchar", None))

btnWitch.Command = Witch
#
Witchtext1 = Menu.Text(text="Class : Witch", color=Color.Brown, font=Font.Scanner)
Witchtext1.Left,Witchtext1.Top = 780,570
Witchtext = Menu.Text(text="Desc : Balance Hp and Damage", color=Color.Brown, font=Font.Scanner)
Witchtext.Left,Witchtext.Top = 780,590
Witchtext3 = Menu.Text(text="Holy Witch Blessed by", color=Color.Brown, font=Font.Scanner)
Witchtext3.Left,Witchtext3.Top = 780,620
Witchtext4 = Menu.Text(text="the Ancient One, +2 Pots", color=Color.Brown, font=Font.Scanner)
Witchtext4.Left,Witchtext4.Top = 780,640
Witchtext5 = Menu.Text(text="\"I'm Not Resting Till\' " , color=Color.Brown, font=Font.Scanner)
Witchtext5.Left,Witchtext5.Top = 780,680
Witchtext6 = Menu.Text(text=" There's Nothing Left to Burn\"" , color=Color.Brown, font=Font.Scanner)
Witchtext6.Left,Witchtext6.Top = 780,700
Witchtext2 = Menu.Text(text="-Emilia" , color=Color.Brown, font=Font.Scanner)
Witchtext2.Left,Witchtext2.Top = 945,720


def Exit():
    global isrunning
    isrunning = False


btnExit = Menu.Button(text="Nah, I'm Good ^^", rect=(100, 155, 280, 40),
                      bg=Color.DarkSlateGray, fg=Color.GhostWhite,
                      bgr=Color.Azure, tag=("menu", None))
btnExit.Command = Exit

menuTitle = Menu.Text(text="NIGHTMARE HUNT", color=Color.IndianRed, font=Font.Large)
menuVersion = Menu.Text(text="Cry of the Wyvern", color=Color.DarkRed, font=Font.Medium)

menuTitle.Left, menuTitle.Top = 10, 0
menuVersion.Left, menuVersion.Top = 80, 40


def Lose():
    global isrunning
    isrunning = False
    Globals.scene = "lose"


btnLose = Menu.Button(text="You Can't Respawn, just Admit Defeat!!", rect=(300, 600, 600, 100), bg=Color.RedBrown,
                      fg=Color.DarkSlateGray,
                      bgr=Color.BlueViolet, tag=("lose", None))
btnLose.Command = Lose

loseversion = Menu.Text(text="told u not to die", color=Color.BlanchedAlmond, font=Font.Small)

loseversion.Left, loseversion.Top = 900, 700

def Saveslot1():
    save_data(1)
    Globals.scene = "game"
btnSave1 = Menu.Button(text="Slot 1", rect=(200, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Saveslot", None))
btnSave1.Command = Saveslot1

def Saveslot2():
    save_data(2)
    Globals.scene = "game"
btnSave2 = Menu.Button(text="Slot 2", rect=(500, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Saveslot", None))
btnSave2.Command = Saveslot2

def Saveslot3():
    save_data(3)
    Globals.scene = "game"
btnSave3 = Menu.Button(text="Slot 3", rect=(800, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Saveslot", None))
btnSave3.Command = Saveslot3

def Loadslot1():
    load_data(1)
    Globals.scene = "game"
btnLoad1 = Menu.Button(text="Load Char 1", rect=(200, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Loadslot", None))
btnLoad1.Command = Loadslot1

def Loadslot2():
    load_data(2)
    Globals.scene = "game"
btnLoad2 = Menu.Button(text="Load Char 2", rect=(500, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Loadslot", None))
btnLoad2.Command = Loadslot2

def Loadslot3():
    load_data(3)
    Globals.scene = "game"
btnLoad3 = Menu.Button(text="Load Char 3", rect=(800, 300, 200,50), bg=Color.LightCoral,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("Loadslot", None))
btnLoad3.Command = Loadslot3

def How():
    Globals.scene = "how"


howtoplay = Menu.Text(text="How to Play", color=Color.LimeGreen, font=Font.Giga)
howtoplay1 = Menu.Text(text="Kill Monsters to Level Up", color=Color.LightGoldenrodYellow, font=Font.Large)
howtoplay2 = Menu.Text(text="You Beat the Wyvern, You Beat the Game", color=Color.LightGoldenrodYellow, font=Font.Large)
howtoplay3 = Menu.Text(text="You Get 1 Pot when Lvl Up", color=Color.LightGoldenrodYellow, font=Font.Large)
howtoplay4 = Menu.Text(text="And", color=Color.LightGoldenrodYellow, font=Font.Large)
howtoplay5 = Menu.Text(text="Don't Die", color=Color.LightGoldenrodYellow, font=Font.Large)
howtoplay6 = Menu.Text(text="Press Esc to Continue", color=Color.LightGoldenrodYellow, font=Font.Medium)
howtoplay.Left, howtoplay.Top = 100, 100
howtoplay1.Left, howtoplay1.Top = 180, 250
howtoplay2.Left, howtoplay2.Top = 150, 300
howtoplay3.Left, howtoplay3.Top = 200, 350
howtoplay4.Left, howtoplay4.Top = 300, 400
howtoplay5.Left, howtoplay5.Top = 250, 450
howtoplay6.Left, howtoplay6.Top = 850, 600

def House():
    Globals.scene = "house"


housetext = Menu.Text(text="Home Sweet Home", color=Color.Orange, font=Font.Giga)
housetext.Left,housetext.Top = 50,10

def Resume():
    Globals.scene = "game"
btnResume = Menu.Button(text="Continue Hunt", rect=(410, 200, 400,50), bg=Color.Black,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("pause", None))
btnResume.Command = Resume

def Save():
    Globals.scene = "Saveslot"
btnSave = Menu.Button(text="Save Character", rect=(410, 300, 400,50), bg=Color.Black,
                      fg=Color.White,
                      bgr=Color.LightSlateGray, tag=("pause", None))
btnSave.Command = Save

def Load():
    Globals.scene = "Loadslot"
btnLoad = Menu.Button(text="Load Character", rect=(410, 400, 400, 50), bg=Color.Black,
                  fg=Color.White,
                  bgr=Color.LightSlateGray, tag=("pause", None))
btnLoad.Command = Load

def Quit():
    global isrunning
    isrunning = False
    Globals.scene = "pause"
btnQuit = Menu.Button(text="Quit Game", rect=(410, 600, 400, 50), bg=Color.Black,
                  fg=Color.White,
                  bgr=Color.LightSlateGray, tag=("pause", None))
btnQuit.Command = Quit


def HowtoPlay():
    Globals.scene = "how"
btnHow = Menu.Button(text="How to Play", rect=(410, 500, 400, 50), bg=Color.Black,
                  fg=Color.White,
                  bgr=Color.LightSlateGray, tag=("pause", None))
btnHow.Command = HowtoPlay

def Win():
    Globals.scene = "credit"


btnWin = Menu.Button(text="Continue", rect=(450, 500, 300, 50), bg=Color.Gold, fg=Color.DarkSlateGray,
                     bgr=Color.White, tag=("win", None))
btnWin.Command = Win

def Credit():
    global isrunning
    isrunning = False
    Globals.scene = "credit"
credittext = Menu.Text(text="CREDITS", color=Color.DarkOliveGreen, font=Font.Giga)
credittext.Left,credittext.Top = 310,300
credittext1 = Menu.Text(text="Livander Surya as Leagrove", color=Color.DarkOliveGreen, font=Font.Large)
credittext1.Left,credittext1.Top = 300,500
credittext2 = Menu.Text(text="Youtube Meloonatic for References code", color=Color.DarkOliveGreen, font=Font.Large)
credittext2.Left,credittext2.Top = 170,575
credittext11 = Menu.Text(text="Google Image and Pygame.org for All Images", color=Color.DarkOliveGreen, font=Font.Large)
credittext11.Left,credittext11.Top = 120,650
credittext3 = Menu.Text(text="Eris-Kun as References and Personal Teacher", color=Color.DarkOliveGreen, font=Font.Large)
credittext3.Left,credittext3.Top = 120,725
credittext4 = Menu.Text(text="Game Tester : ", color=Color.DarkOliveGreen, font=Font.Large)
credittext4.Left,credittext4.Top = 300,850
credittext5 = Menu.Text(text="Renata", color=Color.DarkOliveGreen, font=Font.Large)
credittext5.Left,credittext5.Top = 610,850
credittext6 = Menu.Text(text="Ricky", color=Color.DarkOliveGreen, font=Font.Large)
credittext6.Left,credittext6.Top = 610,900
credittext7 = Menu.Text(text="Zefanya", color=Color.DarkOliveGreen, font=Font.Large)
credittext7.Left,credittext7.Top = 610,950
credittext8 = Menu.Text(text="Special Thanks to ", color=Color.DarkOliveGreen, font=Font.Giga)
credittext8.Left,credittext8.Top = 50,1200
credittext0 = Menu.Text(text="Sir Minaldy", color=Color.DarkOliveGreen, font=Font.Giga)
credittext0.Left,credittext0.Top = 250,1300
credittext9 = Menu.Text(text="Thanks for Playing :)", color=Color.DarkOliveGreen, font=Font.Large)
credittext9.Left,credittext9.Top = 400,2000
credittext10 = Menu.Text(text="a", color=Color.DarkOliveGreen, font=Font.Large)
credittext10.Left,credittext10.Top = 1300,2000


def Fightsong():
    pygame.mixer.music.load("Music/Fight.mp3")
    pygame.mixer.music.play()


def Bosssong():
    pygame.mixer.music.load("Music/High Action.mp3")
    pygame.mixer.music.play()

def daggersound():
    pygame.mixer.Sound("sound/sword.wav").play()


def swordsound():
    pygame.mixer.Sound("sound/sword.ogg").play()


def firesound():
    pygame.mixer.Sound("sound/fire.ogg").play()

def enemysound():
    pygame.mixer.Sound("sound/bite.wav").play()

def realwarrior():
    window.blit(Warrior, (200, 400))

def realthief():
    window.blit(Thiefpict, (180, 360))

def realwitch():
    window.blit(Mage, (180, 330))

def swordicon():
    window.blit(Attbutton, (455, 700))

def daggericon():
    window.blit(Attbutton1,(455,690))

def fireicon():
    window.blit(Attbutton2,(430,700))

def swordslash():
    window.blit(Attackimage2,(700,500))

def daggerslash():
    window.blit(Attackimage,(820,570))

def fireburnt():
    window.blit(Attackimage1,(720,500))

isrunning = True
while isrunning:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isrunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not Globals.dialog_open and not Globals.combat_open:
                player.walking = True
                player.direction = 1
                Globals.playery = 50
                Globals.camera_moveUp = True
            if event.key == pygame.K_DOWN and not Globals.dialog_open and not Globals.combat_open:
                player.walking = True
                player.direction = 2
                Globals.playery = 50
                Globals.camera_moveDown = True
            if event.key == pygame.K_LEFT and not Globals.dialog_open and not Globals.combat_open:
                player.walking = True
                player.direction = 3
                Globals.playerx = 50
                Globals.camera_moveLeft = True
            if event.key == pygame.K_RIGHT and not Globals.dialog_open and not Globals.combat_open:
                player.walking = True
                player.direction = 4
                Globals.playerx = 50
                Globals.camera_moveRight = True

            if event.key == pygame.K_SPACE:
                if Globals.dialog_open:
                    # TO RENDER NEXT DIALOG
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
                        Globals.active_dialog.Page += 1

                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None

                        for npc in NPC.AllNPC:
                            if not npc.Timer.Active:
                                npc.Timer.Start()




                else:
                    for npc in NPC.AllNPC:
                        npc_x = npc.X / Tiles.Size
                        npc_y = npc.Y / Tiles.Size
                        if player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y - 2 and player_y <= npc_y + 2:
                            Globals.dialog_open = True
                            Globals.active_dialog = npc.Dialog
                            npc.Timer.Pause()
                            npc.walking = False
                            Globals.camera_moveUp = False
                            Globals.camera_moveDown = False
                            Globals.camera_moveLeft = False
                            Globals.camera_moveRight = False


            if event.key == pygame.K_ESCAPE:
                if Globals.scene == "how":
                    Globals.scene = "pause"
                elif Globals.scene == "game" or Globals.scene == "house":
                    Globals.scene = "pause"
                elif Globals.scene == "pause":
                    Globals.scene = "game"
                elif Globals.scene == "Saveslot" or Globals.scene == "Loadslot":
                    Globals.scene = "pause"


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and not Globals.dialog_open and not Globals.combat_open:
                player.walking = False
                Globals.playery = 0
                Globals.camera_moveUp = False
            if event.key == pygame.K_DOWN and not Globals.dialog_open and not Globals.combat_open:
                player.walking = False
                Globals.playery = 0
                Globals.camera_moveDown = False
            if event.key == pygame.K_LEFT and not Globals.dialog_open and not Globals.combat_open:
                player.walking = False
                Globals.playerx = 0
                Globals.camera_moveLeft = False
            if event.key == pygame.K_RIGHT and not Globals.dialog_open and not Globals.combat_open:
                player.walking = False
                Globals.playerx = 0
                Globals.camera_moveRight = False

            # HANDLE BUTTON CLICK EVENTS

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left Click
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()  # Do Button Event
                        btn.Rolling = False
                        break  # Exit loop

    if Globals.scene == "game":


        # LOGIC
        if Globals.camera_moveUp:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))) and not sandmaze and player.job == "Knight":
                Globals.camera_y += 90 * Globals.deltatime


        if Globals.camera_moveLeft:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))) and not sandmaze and player.job == "Knight":
                Globals.camera_x += 90 * Globals.deltatime

        if Globals.camera_moveDown:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))) and not sandmaze and player.job == "Knight":
                Globals.camera_y -= 90 * Globals.deltatime

        if Globals.camera_moveRight:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))) and not sandmaze and player.job == "Knight":
                Globals.camera_x -= 90 * Globals.deltatime

        if Globals.camera_moveUp:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))) and not sandmaze and player.job == "Thief":
                Globals.camera_y += 250 * Globals.deltatime


        if Globals.camera_moveLeft:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))) and not sandmaze and player.job == "Thief":
                Globals.camera_x += 250 * Globals.deltatime

        if Globals.camera_moveDown:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))) and not sandmaze and player.job == "Thief":
                Globals.camera_y -= 250 * Globals.deltatime

        if Globals.camera_moveRight:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))) and not sandmaze and player.job == "Thief":
                Globals.camera_x -= 250 * Globals.deltatime

        if Globals.camera_moveUp:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))) and not sandmaze and player.job == "Witch":
                Globals.camera_y += 160 * Globals.deltatime


        if Globals.camera_moveLeft:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))) and not sandmaze and player.job == "Witch":
                Globals.camera_x += 160 * Globals.deltatime

        if Globals.camera_moveDown:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))) and not sandmaze and player.job == "Witch":
                Globals.camera_y -= 160 * Globals.deltatime

        if Globals.camera_moveRight:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))) and not sandmaze and player.job == "Witch":
                Globals.camera_x -= 160 * Globals.deltatime

        player_x = (window_width / 2 - player.rect.width / 2 - 10 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player.rect.height / 2 - 10 - Globals.camera_y) / Tiles.Size

        # Render Graphic
        window.blit(Sky, (0, 0))
        # terrain.set_alpha(230)
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))




        #MAKE CLASS AGAIN SO THE POSITION DOESN'T GO ERROR
        class Momon(pygame.sprite.Sprite):
            def __init__(self, name, x, y, maxhp, attack, xp, lv):
                pygame.sprite.Sprite.__init__(self, monster)
                self.name = name
                self.maxhp = maxhp
                self.hp = self.maxhp
                self.attack = attack
                self.xp = xp
                self.lv = lv

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
                    self.image = pygame.transform.scale(self.image, (200, 190))
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y

            def update(self):
                self.rect.x += Globals.camera_x
                self.rect.y += Globals.camera_y


        class Lava(pygame.sprite.Sprite):
            def __init__(self, x, y, damage):
                pygame.sprite.Sprite.__init__(self, lava)
                self.damage = damage
                self.x = x
                self.y = y
                self.image = pygame.image.load("tiles/lava.png")
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

            def update(self):
                self.movex = self.x + Globals.camera_x
                self.movey = self.y + Globals.camera_y

                self.rect.x = self.movex
                self.rect.y = self.movey


        class Sand(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self, sand)
                self.x = x
                self.y = y
                self.image = pygame.image.load("tiles/lava.png")
                self.image = pygame.transform.scale(self.image, (1200, 800))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

            def update(self):
                self.movex = self.x + Globals.camera_x
                self.movey = self.y + Globals.camera_y

                self.rect.x = self.movex
                self.rect.y = self.movey

        class Home(pygame.sprite.Sprite):
            def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self,home)
                self.x = x
                self.y = y
                self.image = pygame.image.load("tiles/houseoverworld.png")
                self.image = pygame.transform.scale(self.image,(300,300))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
            def update(self):
                self.movex = self.x + Globals.camera_x
                self.movey = self.y + Globals.camera_y

                self.rect.x = self.movex
                self.rect.y = self.movey

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
        class Nurse(pygame.sprite.Sprite):
            def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self,nurse)
                self.image  = pygame.image.load("nurse.png")
                self.image = pygame.transform.scale(self.image,(32,32))
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

        # DRAW THE MONSTER,PLAYER,COLLISION TILES, AND NPC
        for npc in NPC.AllNPC:
            npc.Render(window)
            if Globals.stats_open:
                window.blit(Stats, (0, (window_height - Dialog_background_Height) + 94))

            if Globals.active_stats != None:
                lines = Globals.active_stats.Text[Globals.active_stats.Page]



        sand.update()
        sand.draw(window)
        lava.update()
        lava.draw(window)
        playerSprite.update()
        playerSprite.draw(window)
        player.anime()
        monster.update()
        monster.draw(window)
        home.update()
        home.draw(window)

        # DRAW PLAYER STATS ON BOTTOM LEFT OF THE SCREEN
        stattext = Dialog(text=[("", "", "Name : {}".format(player.name),"Class : {}".format(player.job),
                                 "Hp : {}/{}".format(player.hp, player.maxhp), "Attack : {}".format(player.attack),
                                 "Xp : {}/{}".format(player.xp, player.maxxp), "Lv : {}".format(player.lv),
                                 "Pots : {}".format(player.pot))])
        Globals.active_stats = stattext
        if Globals.stats_open:
            window.blit(Stats, (0, (window_height - Dialog_background_Height) + 94))

            if Globals.active_stats != None:
                lines = Globals.active_stats.Text[Globals.active_stats.Page]

                for line in lines:
                    # DRAW TEXT TO SCREEN
                    window.blit(Font.Default.render(line, True, Color.Blue),
                                (15, (window_height - Dialog_background_Height) + 94 + lines.index(line) * 18))
        #MAX LEVEL FOR FIGHTING THE WYVERN
        if player.lv == 11:
            MaxDialog = Dialog(text=[(" ","  You Have Awaken the ","", " True Power of Wyvern Hunter  ","",
                                                                               "                                                                                 Press Space to Continue"),

                        (" "," Ancient Wyvern is Waiting for          ",""," Your Presence "), ("", "Bring an End to ","","This Village Misery!")])
            Globals.active_dialog = MaxDialog
            Globals.dialog_open = True
            if Globals.dialog_open:
                window.blit(Dialog_background,
                            (window_width / 2 - Dialog_background_Width / 2, window_height - Dialog_background_Height - 2))

            # DRAW DIALOG TEXt
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                for line in lines:
                    # DRAW TEXT TO SCREEN
                    window.blit(Font.Scanner.render(line, True, Color.Gold),
                                (400, (window_height - Dialog_background_Height) + 94 + lines.index(line) * 18))

            player.maxhp += 200000
            player.hp = player.maxhp
            player.attack += 84000
            player.lv = str('MAX LEVEL')
            player.xp = 0
            player.maxxp = 99999
            player.pot += 1
        # MAKE COLLISION FOR THE PLAYER TOUCHING THE MONSTER
        collision = pygame.sprite.spritecollide(player, monster, False)

        if collision and not Globals.combat_open:

            if collision[0].name != 'Ancient Wyvern(BOSS)':
                Fightsong()
            if collision[0].name == 'Ancient Wyvern(BOSS)':
                Bosssong()

            Globals.combat_open = True
            Globals.camera_moveUp = False
            Globals.camera_moveDown = False
            Globals.camera_moveLeft = False
            Globals.camera_moveRight = False

            #BLIT THE COMBAT TERRAIN AND YOU CAN FIGHT NOW
        if Globals.combat_open:
            window.blit(Combat_Terrain, (0, 0))
            window.blit(CombatTEXT, (100, 50))
            window.blit(CombatTEXT, (700, 50))

            if collision[0].name == 'Fire Ant':
                window.blit(Ant_image, (700, 480))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1

                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"


            elif collision[0].name == 'Poisonous Snake':
                window.blit(Snake_image, (700, 470))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1

                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'StingJellyfish':
                window.blit(Jellyfish_image, (580, 450))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1

                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'Mr.Crab':
                window.blit(Crab_image, (630, 510))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1

                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'DeadWood':
                window.blit(Deadwood_image, (630, 260))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (650, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1

                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'Skelly skelly':
                window.blit(Skeleton_image, (700, 425))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1
                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'Baby wyvern':
                window.blit(Babywyvern_image, (660, 300))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1
                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'Great Red Fire Dragon':
                window.blit(Greatdragon_image, (650, 70))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0 :
                    monster.remove(collision[0])
                    player.xp += collision[0].xp
                    Globals.combat_open = False
                    for npc in NPC.AllNPC:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                    pygame.mixer.music.load("Music/Pleasant Creek.mp3")
                    pygame.mixer.music.play(-1)
                    if player.xp > player.maxxp:
                        player.maxhp += 54
                        player.hp = player.maxhp
                        player.attack += 12
                        xp_current = player.xp - player.maxxp
                        player.xp = xp_current
                        player.maxxp += 200
                        player.lv += 1
                        player.pot += 1
                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            elif collision[0].name == 'Ancient Wyvern(BOSS)':
                window.blit(Wyvern_image, (480, 50))
                if player.job == "Knight":
                    realwarrior()
                    swordicon()
                if player.job == "Thief":
                    realthief()
                    daggericon()
                if player.job == "Witch":
                    realwitch()
                    fireicon()
                window.blit(Potbutton, (640, 680))
                window.blit(Panah,(Globals.i,700))

                if collision[0].hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Enchanted Festival.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "win"
                elif player.hp <= 0:
                    monster.remove(collision[0])
                    pygame.mixer.music.load("Music/Kings Theme.mp3")
                    pygame.mixer.music.play(-1)
                    Globals.scene = "lose"

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        if not Globals.attack :
                            Globals.i = 400

                    if event.key == pygame.K_RIGHT:
                        if not Globals.attack:
                            Globals.i = 600

                    if event.key == pygame.K_RETURN:

                        if Globals.attack == False:
                            Globals.attack = True


                elif event.type == pygame.KEYUP:
                    pass
            if Globals.attack :
                #POSITION OF THE ARROW, 400 IS TO ATTACK
                if Globals.i == 400:
                    #INCREASE TIMER UNTIL 1
                    Globals.timer += 0.045
                    if Globals.timer < 1:
                        if not Globals.turn:
                            collision[0].hp -= player.attack
                            Globals.turn = True
                        if player.job == "Knight":
                            swordslash()

                        if player.job == "Thief":
                            daggerslash()

                        if player.job == "Witch":
                            fireburnt()


                        if not Globals.attacksound:
                            if player.job == "Knight":
                                swordsound()
                            if player.job == "Thief":
                                daggersound()
                            if player.job == "Witch":
                                firesound()

                            Globals.attacksound = True


                        textfight = Dialog(text=[("","{} Deals {} Damage!!".format(player.name,player.attack))])
                        Globals.active_fight = textfight
                        if Globals.active_fight != None:
                            lines = Globals.active_fight.Text[Globals.active_fight.Page]
                            for line in lines:
                                window.blit(Font.Medium.render(line, True, Color.Yellow), (
                                720, (window_height / 2 - Dialog_background_Height ) + 94 + lines.index(line) * 18))

                        if collision[0].hp < 0:
                            Globals.attack = False
                            Globals.timer = 0
                            Globals.attacksound = False
                            Globals.turn = False
                            Globals.turn2 = False

                    if Globals.timer > 1:
                        if collision[0].hp > 0:
                            window.blit(Bigattack,(290,450))
                            enemysound()
                            textfightenemy = Dialog(text=[("","{} Deals {} Damage!!".format(collision[0].name,collision[0].attack))])
                            Globals.active_fight = textfightenemy
                            if Globals.active_fight != None:
                                lines = Globals.active_fight.Text[Globals.active_fight.Page]
                                for line in lines:
                                    window.blit(Font.Medium.render(line, True, Color.Red), (
                                    120, (window_height / 2 - Dialog_background_Height ) + 94 + lines.index(line) * 18))

                            if not Globals.turn2:
                                player.hp -= collision[0].attack
                                Globals.turn2 = True


                    if Globals.timer > 2:
                        Globals.attack = False
                        Globals.timer = 0
                        Globals.attacksound = False
                        Globals.turn = False
                        Globals.turn2 = False
                #POSITION OF THE ARROW NEXT TO THE POT
                if Globals.i == 600:

                    if player.pot <= 0:
                        Globals.attack = False

                    elif player.pot > 0:

                        if not Globals.attacksound:

                            heal = pygame.mixer.Sound("sound/Heal8-Bit.ogg")
                            heal.play()
                            attacksound = True

                        window.blit(Heal,(350,330))

                        Globals.timer += 0.045
                        if Globals.timer >1 :
                            player.hp = player.maxhp
                            player.pot -= 1

                            Globals.timer = 0
                            Globals.attack = False
                            Globals.attacksound = False

            fighttextp = Dialog(text=[("", "{}".format(player.name), "", "Lv : {}".format(player.lv),
                                       "Hp : {}/{}".format(player.hp, player.maxhp),
                                       "Attack : {}".format(player.attack), "Pots : {}".format(player.pot))])
            Globals.active_go = fighttextp
            lines = Globals.active_go.Text[Globals.active_go.Page]
            for line in lines:
                window.blit(Font.Default.render(line, True, Color.White),
                            (120, (window_height / 2 - Dialog_background_Height - 155) + 94 + lines.index(line) * 18))

            fighttextant = Dialog(text=[("", "{}".format(collision[0].name), "", "Lv : {}".format(collision[0].lv),
                                         "Hp : {}/{}".format(collision[0].hp, collision[0].maxhp),
                                         "Attack : {}".format(collision[0].attack))])
            Globals.active_ant = fighttextant
            if Globals.active_ant != None:
                lines = Globals.active_ant.Text[Globals.active_ant.Page]
                for line in lines:
                    window.blit(Font.Default.render(line, True, Color.White), (
                    720, (window_height / 2 - Dialog_background_Height - 155) + 94 + lines.index(line) * 18))

        lavamaze = pygame.sprite.spritecollide(player, lava, False)
        if lavamaze and not Globals.combat_open:
            player.hp -= 3
            if player.hp <= 0:
                bg = pygame.Surface((1200,800))
                bg.fill((20,20,20))
                bg.set_alpha(10)
                window.blit(bg,(0,0))
                pygame.mixer.music.load("Music/Kings Theme.mp3")
                pygame.mixer.music.play(-1)
                Globals.scene = "lose"

        sandmaze = pygame.sprite.spritecollide(player, sand, False)
        if sandmaze and not Globals.combat_open:
            if Globals.camera_moveUp:
                Globals.camera_y += 50 * Globals.deltatime
            if Globals.camera_moveLeft:
                Globals.camera_x += 50 * Globals.deltatime
            if Globals.camera_moveDown:
                Globals.camera_y -= 50 * Globals.deltatime
            if Globals.camera_moveRight:
                Globals.camera_x -= 50 * Globals.deltatime

        homecollide = pygame.sprite.spritecollide(player,home,False)
        if homecollide:
            pygame.mixer.music.load("Music/Town Theme.mp3")
            pygame.mixer.music.play(-1)
            Globals.scene = "house"


        if Globals.dialog_open:
            window.blit(Dialog_background,
                        (window_width / 2 - Dialog_background_Width / 2, window_height - Dialog_background_Height - 2))

            # DRAW DIALOG TEXt
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                for line in lines:
                    # DRAW TEXT TO SCREEN
                    window.blit(Font.Scanner.render(line, True, Color.Gold),
                                (400, (window_height - Dialog_background_Height) + 94 + lines.index(line) * 18))

        # Process Main Menu
    elif Globals.scene == "menu":

        window.blit(Wpp, (0, 0))

        menuTitle.Render(window)
        menuVersion.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)

        btnPlay.Render(window)

    elif Globals.scene == "lose":
        Lose_image.set_alpha(10)

        window.blit(Lose_image, (0, 0))

        loseversion.Render(window)

        btnLose.Render(window)

        pygame.display.flip()

    elif Globals.scene == "win":
        Win_image.set_alpha(50)
        window.blit(Win_image, (0, 0))

        btnWin.Render(window)
    elif Globals.scene == "how":
        bg = pygame.Surface((1200,800))
        bg.fill((180,180,180))
        window.blit(bg,(0,0))
        pygame.display.flip()
        howtoplay.Render(window)
        howtoplay1.Render(window)
        howtoplay2.Render(window)
        howtoplay3.Render(window)
        howtoplay4.Render(window)
        howtoplay5.Render(window)
        howtoplay6.Render(window)


    if Globals.scene == "house":
        if Globals.camera_moveUp:
            if not Tiles.Blocked_At2((round(player_x), math.floor(player_y))) :
                Globals.camera_y += 150 * Globals.deltatime

        if Globals.camera_moveLeft:
            if not Tiles.Blocked_At2((math.floor(player_x), round(player_y))):
                Globals.camera_x += 150 * Globals.deltatime

        if Globals.camera_moveDown:
            if not Tiles.Blocked_At2((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 150 * Globals.deltatime

        if Globals.camera_moveRight:
            if not Tiles.Blocked_At2((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 150 * Globals.deltatime



        player_x = (window_width / 2 - player.rect.width / 2 - 10 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player.rect.height / 2 - 10 - Globals.camera_y) / Tiles.Size

        # Render Graphic
        window.fill((0,0,0))
        window.blit(houseterrain,(Globals.camera_x,Globals.camera_y))
        housetext.Render(window)
        nurse.update()
        nurse.draw(window)
        player.anime()
        playerSprite.update()
        playerSprite.draw(window)
        out.update()
        out.draw(window)
        stattext = Dialog(text=[("", "", "Nickname : {}".format(player.name),
                                 "Hp : {}/{}".format(player.hp, player.maxhp), "Attack : {}".format(player.attack),
                                 "Xp : {}/{}".format(player.xp, player.maxxp), "Lv : {}".format(player.lv),
                                 "Pots : {}".format(player.pot))])
        Globals.active_stats = stattext
        if Globals.stats_open:
            window.blit(Stats, (0, (window_height - Dialog_background_Height) + 94))

            if Globals.active_stats != None:
                lines = Globals.active_stats.Text[Globals.active_stats.Page]

                for line in lines:
                    # DRAW TEXT TO SCREEN
                    window.blit(Font.Default.render(line, True, Color.Blue),
                                (15, (window_height - Dialog_background_Height) + 94 + lines.index(line) * 18))


        outcollide = pygame.sprite.spritecollide(player,out,False)
        if outcollide:
            pygame.mixer.music.load("Music/Pleasant Creek.mp3")
            pygame.mixer.music.play(-1)
            Globals.scene = "game"


        nursedialog = Dialog(text=[("","Heyy Cute Guy~","Need Some Medichal Treatment?","","Here You Go <3")])
        Globals.active_dialog = nursedialog
        nursecollide = pygame.sprite.spritecollide(player,nurse,False)
        if nursecollide:
            if player.hp != player.maxhp:
                heal = pygame.mixer.Sound("sound/Heal8-Bit.ogg")
                heal.play()

            Globals.dialog_open1 = True
            Globals.active_dialog = nursedialog
            if Globals.dialog_open1:
                window.blit(Dialog_background1,
                            (window_width / 2 - Dialog_background1_Width / 2, window_height - Dialog_background1_Height - 500))

                # DRAW DIALOG TEXt
                if Globals.active_dialog != None:
                    lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                    for line in lines:
                        # DRAW TEXT TO SCREEN
                        window.blit(Font.Medium.render(line, True, Color.DeepPink),
                                    (400, (window_height - Dialog_background1_Height - 550) + 94 + lines.index(line) * 24))
                        window.blit(Heal,(650,280))
                        player.hp = player.maxhp



    elif Globals.scene == "pause":
        btnSave.Render(window)
        btnLoad.Render(window)
        btnQuit.Render(window)
        btnResume.Render(window)
        btnHow.Render(window)
        bg = pygame.Surface((1200,800))
        bg.fill((20,20,20))
        bg.set_alpha(10)
        window.blit(bg,(0,0))
        pygame.display.flip()

    elif Globals.scene == "Saveslot":
        window.fill((120,120,120))
        btnSave1.Render(window)
        btnSave2.Render(window)
        btnSave3.Render(window)

    elif Globals.scene == "Loadslot":
        window.fill((120,120,120))
        btnLoad1.Render(window)
        btnLoad2.Render(window)
        btnLoad3.Render(window)


    elif Globals.scene == "Createchar":
        window.blit(Job_image,(0,0))
        window.blit(Warrior1,(110,20))
        window.blit(Thief1,(420,20))
        window.blit(Mage1,(750,-10))
        Thieftext.Render(window)
        Thieftext1.Render(window)
        Thieftext2.Render(window)
        Thieftext3.Render(window)
        Thieftext4.Render(window)
        # Thieftext5.Render(window)
        Thieftext6.Render(window)
        Witchtext.Render(window)
        Witchtext1.Render(window)
        Witchtext2.Render(window)
        Witchtext3.Render(window)
        Witchtext4.Render(window)
        Witchtext5.Render(window)
        Witchtext6.Render(window)
        # Witchtext7.Render(window)
        Knighttext.Render(window)
        Knighttext1.Render(window)
        Knighttext2.Render(window)
        Knighttext3.Render(window)
        Knighttext4.Render(window)
        Knighttext5.Render(window)
        Knighttext6.Render(window)
        Knighttext7.Render(window)
        btnKnight.Render(window)
        btnThief.Render(window)
        btnWitch.Render(window)

    elif Globals.scene == "credit":
        window.fill((0,0,0))
        credittext.Render(window)
        credittext1.Render(window)
        credittext2.Render(window)
        credittext11.Render(window)
        credittext3.Render(window)
        credittext4.Render(window)
        credittext5.Render(window)
        credittext6.Render(window)
        credittext7.Render(window)
        credittext8.Render(window)
        credittext0.Render(window)
        credittext9.Render(window)
        credittext10.Render(window)

        credittext.Top -=2
        credittext1.Top -=2
        credittext2.Top -=2
        credittext11.Top -=2
        credittext3.Top -=2
        credittext4.Top -=2
        credittext5.Top -=2
        credittext6.Top -=2
        credittext7.Top -=2
        credittext8.Top -=2
        credittext0.Top -=2
        credittext9.Top -=2
        credittext10.Top -=2

        if credittext9.Top == 300:
            credittext9.Top += 2
        if credittext10.Top == -250:
            isrunning = False


    show_fps()

    pygame.display.update()

    count_fps()

pygame.quit()
sys.exit()
