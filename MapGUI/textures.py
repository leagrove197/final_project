import pygame

pygame.init()

class Tiles:
    Size = 32
    SIZE = 150

    Blocked = []
    Blocked_Types = ["2", "5", "7", "4", "3","10","0","17","18","13","19","21","20","14"]




    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else :
            return False

    Blocked2 = []
    Blocked_Types2 = ["23","25","26","27","28","29","30","31","32","33","36"]


    def Blocked_At2(pos):
        if list(pos) in Tiles.Blocked2:
            return True
        else :
            return False


    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size,Size))
        surface = pygame.Surface((Size,Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface
    def Load_Texture2(file, SIZE):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (SIZE,SIZE))
        surface = pygame.Surface((SIZE,SIZE), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface

    Grass = Load_Texture("tiles/grass1.png", Size)
    Stone = Load_Texture("tiles/underground/rock.png", Size)
    Water = Load_Texture("tiles/water/water.png", Size)
    Tree1 = Load_Texture("tiles/tree.png", Size)
    Tree2 = Load_Texture("tiles/tree2.png", Size)
    ug = Load_Texture("tiles/underground/dirt.png", Size)
    gunung = Load_Texture("tiles/hills/gunung.png",Size)
    desert = Load_Texture("tiles/desert/desertt.png", Size)
    lava = Load_Texture("tiles/lava.png", Size)
    garden = Load_Texture("tiles/garden.png", Size)
    house = Load_Texture2("tiles/houseoverworld.png", SIZE)
    castleevil = Load_Texture2("tiles/evilcastle.png", SIZE)
    town = Load_Texture("tiles/town.png", Size)
    towns = Load_Texture("tiles/town_demolished.png",Size)
    dor = Load_Texture("tiles/dor.png", Size)
    door = Load_Texture("tiles/castledoor.png", Size)
    enddoor = Load_Texture("tiles/endor.png", Size)
    endtown = Load_Texture("tiles/road/end_town.png", Size)
    bwater = Load_Texture("tiles/water/water_e.png", Size)
    watera = Load_Texture("tiles/water_hills/watera.png", Size)
    wateraa = Load_Texture("tiles/water_hills/wateraa.png", Size)
    gunung1 = Load_Texture("tiles/hills/gunung1.png", Size)
    rumah = Load_Texture("tiles/stone_interior/fireplace.png", Size)
    rumah1 = Load_Texture("tiles/stone_interior/flagstone.png", Size)
    rumah2 = Load_Texture("tiles/stone_interior/drawers.png", Size)
    rumah3 = Load_Texture("tiles/stone_interior/fireplace_burnt_out.png", Size)
    rumah4 = Load_Texture("tiles/stone_interior/armor.png", Size)
    rumah5 = Load_Texture("tiles/stone_interior/swords.png", Size)
    rumah6 = Load_Texture("tiles/stone_interior/shields2.png", Size)
    rumah7 = Load_Texture("tiles/stone_interior/wallup.png", Size)
    rumah8 = Load_Texture("tiles/stone_interior/wallright.png", Size)
    rumah9 = Load_Texture("tiles/stone_interior/wallleft.png", Size)
    rumah10 = Load_Texture("tiles/stone_interior/wall_floor.png", Size)
    rumah11 = Load_Texture("tiles/stone_interior/rug.png", Size)
    rumah12 = Load_Texture("tiles/stone_interior/rug2.png", Size)
    rumah13 = Load_Texture("tiles/stone_interior/bed.png", Size)







    Texture_Tags = {"1" : Grass, "2" : Stone, "3" : Water, "4" : Tree1, "5" : Tree2, "6" : ug,
                    "7" : gunung, "8" : desert,"9" : lava, "0" : house, "10" : castleevil,
                    "12": garden,"13": town, "14": towns, "15" : dor,"16" : door,
                    "17" : enddoor,"18":endtown,"19" : bwater,"20" : watera,"21" : wateraa,"22": gunung1,"23":rumah,"24":rumah1,"25":rumah2,"26":rumah3,"27":rumah4,
                    "28":rumah5,"29":rumah6,"30":rumah7,"31":rumah8,"32":rumah9,"33":rumah10,"34":rumah11,"35":rumah12,"36":rumah13}
