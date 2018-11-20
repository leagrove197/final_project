import random
class Globals:
    camera_x = 0
    camera_y = 0
    camera_up = 0
    camera_down = 0
    playerx = 0
    playery = 0
    camera_moveUp = False
    camera_moveDown = False
    camera_moveLeft = False
    camera_moveRight = False
    scene = "menu"
    deltatime = 0

    dialog_open = True
    dialog_open1 = False
    active_dialog = None
    combat_open = False
    image_fight = None

    stats_open = True
    active_stats = None
    active_fight = None
    fight_open = True
    active_go = None
    active_ant = None

    timer = 0
    i = 400
    attack = False
    attacksound = False

    turn = False
    turn2 = False
    lose_open = False
    critical = random.randint(0,2)





