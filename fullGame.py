# mainGame
from pygame import *
from math import *
from random import *
from datetime import datetime

# basic colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

init()
# load pictures
mainMenu = image.load("FSE-Assets/mainscreen.jpg")
credMenu = image.load("FSE-Assets/credits.jpg")
instructMenu = image.load("FSE-Assets/instructions.jpg")
levelSelectMenu = image.load("FSE-Assets/levelSelect.jpg")
cross = image.load("FSE-Assets/cross.png")
hudimg = image.load("FSE-Assets/hud.jpg")
hudRect = image.load("FSE-Assets/hudRect.png")
readyPic = image.load("FSE-Assets/readyRect.jpg")
quitP = image.load("FSE-Assets/quitRect.png")
dialogueP = image.load("FSE-Assets/dialogueRect.png")
cancelPic = image.load("FSE-Assets/cancelRect.png")
deletePic = image.load("FSE-Assets/deleteRect.png")
mutePic = image.load("FSE-Assets/musicPicMUTE.png")
eigthNote = image.load("FSE-Assets/musicPic.png")
blackHeart = image.load("FSE-Assets/blackHeart.png")
loseRect = image.load("FSE-Assets/loseRect.png")
pressToStart = image.load("FSE-Assets/previews/pushtostart.png")
muzzleFlash = image.load("FSE-Assets/muzzleFlash.png")
wreck = image.load("FSE-Assets/wreckage.png")
dead = image.load("FSE-Assets/enemies/dead.png")
victoryRect = image.load("FSE-Assets/victoryRect.png")
sureRect = image.load("FSE-Assets/sureRect.png")
finalLevel = image.load("FSE-Assets/finalLevel.png")

txtFont = font.SysFont("FSE-Assets/fonts/kremlin.ttf", 25)
txtFont2 = font.SysFont("Stencil", 17)
txtFont3 = font.SysFont("Stencil", 20)

# loading map previews
pr1 = image.load("FSE-Assets/previews/lvl1prev.jpg")
pr2 = image.load("FSE-Assets/previews/lvl2prev.jpg")
pr3 = image.load("FSE-Assets/previews/lvl3prev.jpg")
pr4 = image.load("FSE-Assets/previews/lvl4prev.jpg")
pr5 = image.load("FSE-Assets/previews/lvl5prev.jpg")

# loading maps
map1 = image.load("FSE-Assets/Maps/map1.jpg")
map2 = image.load("FSE-Assets/Maps/map2.jpg")
map3 = image.load("FSE-Assets/Maps/map3.jpg")
map4 = image.load("FSE-Assets/Maps/map4.jpg")
map5 = image.load("FSE-Assets/Maps/map5.jpg")

# transform pictures
hud = transform.scale(hudimg, (500, 75))
hudRects = transform.scale(hudRect, (200, 95))
quitPic = transform.scale(quitP, (150, 40))
crossPic = transform.scale(cross, (30, 30))
dialoguePic = transform.scale(dialogueP, (400, 110))
blackHeart = transform.scale(blackHeart, (25, 25))
mutePic = transform.scale(mutePic, (37, 35))
eigthNote = transform.scale(eigthNote, (37, 35))

# sounds
mixer.init()
place_sound = mixer.Sound("FSE-Assets/sound/placeSound.wav")
gun_sound = mixer.Sound("FSE-Assets/sound/gunShot.wav")
cannon_sound = mixer.Sound("FSE-Assets/sound/gunShotCannon.wav")

money = 0  # starting variable for how much money you have
score = 0  # the score
pause = False  # if the music is plating or not


class enemyType:  # this is the first class which defines all the properties of all the enemies

    def __init__(self, name, speed, health, damage, prize):
        self.name = name  # name of the enemy (ie. heavyTank)
        self.speed = speed  # the speed at which the enemies travel down the path
        self.health = health  # health of each type of the enemy
        self.damage = damage  # damage that each enemy does to the base when it reaches the end of the path
        self.prize = prize  # money you get if you kill the enemy
        self.filename = "FSE-Assets/Enemies/" + name + ".png"  # filename of each enemy to load in the picture


infantry = enemyType('infantry', 1.5, 100, 5, 100)  # the next ones are all the attributes for each class
transport = enemyType('transport', 1.7, 400, 10, 175)   # for example, 'transport' would have a speed of 1.7, # 400 health, 10 damage to the base, 175 dollars back if you kill it.
motorcycle = enemyType('motorcycle', 2, 250, 5, 150)
lightTank = enemyType('lightTank', 1, 700, 15, 200)
heavyTank = enemyType('heavyTank', 1, 1000, 20, 250)
tankDestroyer = enemyType('tankDestroyer', 0.8, 1100, 25, 300)


class towerType:    # this is all the classes that defines all the properties for the towers

    def __init__(self, name, damage, price, uCost, refund, delay):
        self.name = name    # name of the tower (ie
        self.damage = damage    #
        self.price = price
        self.uCost = uCost
        self.refund = refund
        self.delay = delay
        self.filename = "FSE-Assets/Defenses/" + name + ".png"


antiTank = towerType('antiTank', 80, 800, 350, 400, 60)
bunker = towerType('bunker', 100, 1000, 450, 500, 10)
fortress = towerType('fortress', 150, 1250, 600, 625, 50)
heavyGun = towerType('heavyGun', 200, 1500, 700, 750, 60)
heavyMG = towerType('heavyMG', 5, 500, 200, 250, 5)
soldier = towerType('soldier', 25, 250, 100, 125, 25)


def genEnemies(enemy):
    global pics
    global deadPics
    pics = []
    deadPics = []
    for i in enemy:
        img = []
        img.append(image.load(i[3].filename))
        img.append(transform.rotate(image.load(i[3].filename), -90))
        img.append(transform.rotate(image.load(i[3].filename), -270))
        img.append(transform.rotate(image.load(i[3].filename), -180))
        pics.append(img)
    '''
    for i in enemy:
        img=[]
        if i[3]==infantry:
            img.append(dead)
            img.append(transform.rotate(dead,-90))
            img.append(transform.rotate(dead,-270))
            img.append(transform.rotate(dead,-180))
            deadPics.append(img)
        else:
            img.append(wreck)
            img.append(transform.rotate(wreck,-90))
            img.append(transform.rotate(wreck,-270))
            img.append(transform.rotate(wreck,-180))
            deadPics.append(img)
    '''
    return pics


def healthBars(enemy):
    for i in enemy:
        if i[5] == False:
            draw.rect(screen, BLACK, (i[0] + 14, i[1] - 11, i[3].health / 10 + 2, 9), 0)
            draw.rect(screen, GREEN, (i[0] + 15, i[1] - 10, i[4] / 10, 7), 0)


def moneyScore(screen):
    global money
    global activeDefenses
    global score
    txtMoney = txtFont.render("$" + str(money), True, RED)
    txtScore = txtFont.render(str(score), True, RED)
    screen.blit(txtMoney, (100, 30))
    screen.blit(txtScore, (110, 84))


def baseHealth(enemy):
    global gameOver
    screen.blit(blackHeart, (940, 350))
    bars = 100
    count = 0
    draw.rect(screen, BLACK, (944, 374, 102, 12), 0)
    for i in enemy:
        if i[0] >= 900:
            if i[5] == False:
                bars -= i[3].damage
            if bars <= 0:
                bars = 0

    baseHealth = txtFont3.render(str(bars), True, BLACK)
    screen.blit(baseHealth, (965, 353))
    draw.rect(screen, RED, (1044, 375, bars - 100, 10), 0)
    draw.rect(screen, GREEN, (945, 375, bars, 10), 0)

    if bars == 0:
        gameOver = True


def music(state):
    global pause
    global current
    if current == "main":
        muteRect = Rect(870, 650, 50, 50)
        screen.blit(eigthNote, (875, 655))
    else:
        muteRect = Rect(420, 25, 40, 40)
        screen.blit(eigthNote, (420, 27))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if state is not None:

        if state:
            if muteRect.collidepoint(mx, my) and pause == False:
                pause = True
                mixer.music.pause()
            elif muteRect.collidepoint(mx, my) and pause == True:
                pause = False
                mixer.music.unpause()

    if pause:
        if current == "main":
            screen.blit(mutePic, (875, 655))
        else:
            screen.blit(mutePic, (421, 27))

    if muteRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, muteRect, 3)
    else:
        draw.rect(screen, RED, muteRect, 3)


def moveEnemy(screen, enemy):
    count = -1
    for i in enemy:
        if i[0] < 220:
            i[0] += i[3].speed
            i[2] = 0
        if i[0] >= 220 and i[1] < 420:
            i[1] += i[3].speed
            i[2] = 1
        if i[1] >= 410:
            i[0] += i[3].speed
            i[2] = 0
        count += 1
        if i[5] == False:
            screen.blit(pics[count][i[2]], i[:2])
        '''    
        if i[5]==True:
            screen.blit(deadPics[count][i[2]],i[:2])
        '''


def moveEnemy2(screen, enemy):
    count = -1

    check1 = Rect(300, 220, 65, 350)
    check2 = Rect(300, 155, 365, 65)
    check3 = Rect(665, 210, 65, 230)
    check4 = Rect(665, 440, 900, 65)

    for i in enemy:
        if i[5] == False:
            if i[0] < 300:
                i[0] += i[3].speed
                i[2] = 0
            if check1.collidepoint(i[0], i[1]):
                i[1] -= i[3].speed
                i[2] = 2
            if check2.collidepoint(i[0], i[1]):
                i[0] += i[3].speed
                i[2] = 0
            if check3.collidepoint(i[0], i[1]):
                i[1] += i[3].speed
                i[2] = 1
            if check4.collidepoint(i[0], i[1]):
                i[0] += i[3].speed
                i[2] = 0

        count += 1
        screen.blit(pics[count][i[2]], i[:2])


def moveEnemy3(screen, enemy):
    count = -1
    for i in enemy:
        if i[0] < 370:
            i[0] += i[3].speed
            i[2] = 0
        if i[0] >= 370 and i[1] >= 220:
            i[1] -= i[3].speed
            i[2] = 2
        if i[1] <= 220:
            i[0] += i[3].speed
            i[2] = 0

        count += 1
        screen.blit(pics[count][i[2]], i[:2])


def moveEnemy4(screen, enemy):
    count = -1

    check1 = Rect(230, 280, 60, 280)
    check2 = Rect(230, 560, 360, 60)
    check3 = Rect(590, 330, 60, 300)
    check4 = Rect(590, 270, 900, 60)

    for i in enemy:
        if i[0] < 230:
            i[0] += i[3].speed
            i[2] = 0
        if check1.collidepoint(i[0], i[1]):
            i[1] += i[3].speed
            i[2] = 1
        if check2.collidepoint(i[0], i[1]):
            i[0] += i[3].speed
            i[2] = 0
        if check3.collidepoint(i[0], i[1]):
            i[1] -= i[3].speed
            i[2] = 2
        if check4.collidepoint(i[0], i[1]):
            i[0] += i[3].speed
            i[2] = 0

        count += 1
        screen.blit(pics[count][i[2]], i[:2])


def moveEnemy5(screen, enemy):
    count = -1
    check1 = Rect(100, 260, 327, 50)
    check2 = Rect(427, 260, 50, 235)
    check3 = Rect(427, 495, 900, 50)

    for i in enemy:
        if i[1] < 260:
            i[1] += i[3].speed
            i[2] = 1
        if check1.collidepoint(i[0], i[1]):
            i[0] += i[3].speed
            i[2] = 0
        if check2.collidepoint(i[0], i[1]):
            i[1] += i[3].speed
            i[2] = 1
        if check3.collidepoint(i[0], i[1]):
            i[0] += i[3].speed
            i[2] = 0

        count += 1
        screen.blit(pics[count][i[2]], i[:2])


def drawScene1(screen):
    screen.blit(map1, (0, 0))


def drawScene2(screen):
    screen.blit(map2, (0, 0))


def drawScene3(screen):
    screen.blit(map3, (0, 0))


def drawScene4(screen):
    screen.blit(map4, (0, 0))


def drawScene5(screen):
    screen.blit(map5, (0, 0))


def hudElements(screen):
    screen.blit(hud, (550, 20))
    screen.blit(hudRects, (20, 20))
    screen.blit(dialoguePic, (600, 600))


defC = None
ready = False
gameOver = False
activeDefenses = []


def prep(screen, towerPos):
    global defC
    global money
    global ready
    global click
    readyRect = Rect(830, 120, 179, 69)
    upgradeRect = Rect(750, 662, 70, 30)
    buyRects = [Rect(607, 28, 59, 63), Rect(682, 28, 61, 63), Rect(758, 28, 61, 63), Rect(834, 28, 61, 63),
                Rect(908, 28, 61, 63), Rect(982, 28, 61, 63)]
    cancelRect = Rect(20, 125, 125, 30)

    txtD1 = txtFont2.render("Basic Soldier - Cost: $250, Damage: 25", True, BLACK)
    txtD2 = txtFont2.render("Machine Gun - Cost: $500, Damage: 35", True, BLACK)
    txtD3 = txtFont2.render("Anti-Tank Gun - Cost: $800, Damage: 80", True, BLACK)
    txtD4 = txtFont2.render("Bunker - Cost: $1000, Damage: 100", True, BLACK)
    txtD5 = txtFont2.render("Fortress - Cost: $1250, Damage: 150", True, BLACK)
    txtD6 = txtFont2.render("Heavy AT Gun - Cost: $1500, Damage: 200", True, BLACK)

    txtS1 = txtFont2.render("Basic Soldier - Damage:", True, BLACK)
    txtS2 = txtFont2.render("Machine Gun - Damage:", True, BLACK)
    txtS3 = txtFont2.render("Anti-Tank Gun - Damage:", True, BLACK)
    txtS4 = txtFont2.render("Bunker - Damage:", True, BLACK)
    txtS5 = txtFont2.render("Fortress - Damage:", True, BLACK)
    txtS6 = txtFont2.render("Heavy AT Gun - Damage:", True, BLACK)
    towerDescription = [txtD1, txtD2, txtD3, txtD4, txtD5, txtD6]
    towerStats = [txtS1, txtS2, txtS3, txtS4, txtS5, txtS6]

    ##generating defense images/sounds
    defenses = [soldier, heavyMG, antiTank, bunker, fortress, heavyGun]
    defensePics = []
    for i in defenses:
        defensePics.append(image.load(i.filename))
    sounds = [gun_sound, gun_sound, cannon_sound, gun_sound, gun_sound, cannon_sound]

    draw.rect(screen, RED, readyRect, 2)
    screen.blit(readyPic, (830, 120))
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if readyRect.collidepoint(mx, my):
        draw.rect(screen, (255, 255, 0), readyRect, 2)
        if click:
            ready = True

    for i in range(len(buyRects)):
        if buyRects[i].collidepoint(mx, my):
            draw.rect(screen, YELLOW, buyRects[i], 2)
            if click:
                defC = int(i)

    if defC != None:
        draw.rect(screen, GREEN, buyRects[defC], 2)
        screen.blit(towerDescription[defC], (620, 630))
        cancelRect = Rect(20, 125, 125, 30)
        screen.blit(cancelPic, (20, 125))

        # money and stuff
        for i in range(len(towerPos)):
            if towerPos[i][1] == False:
                draw.rect(screen, RED, towerPos[i][0], 3)
                if towerPos[i][0].collidepoint(mx, my):
                    draw.rect(screen, YELLOW, towerPos[i][0], 3)
                    if click and money - defenses[defC].price >= 0:
                        mixer.Sound.play(place_sound)
                        # tower picture, blit position,  tower class variable, tower position index, damage, upgrade cost, delay counter, delay, sound type
                        activeDefenses.append([defensePics[defC], towerPos[i][2], defenses[defC], towerPos[i][4],
                                               int(defenses[defC].damage), defenses[defC].uCost, 0,
                                               defenses[defC].delay, sounds[defC]])
                        money -= defenses[defC].price
                        towerPos[i][1] = True
                        towerPos[i][5] = defC
                    if money - defenses[defC].price < 0:
                        noMoney = txtFont2.render("Not enough money for this tower.", True, RED)
                        screen.blit(noMoney, (620, 660))

        if cancelRect.collidepoint(mx, my):
            draw.rect(screen, RED, cancelRect, 2)
            if click:
                defC = None

    if defC == None:
        select = True
        for i in towerPos:
            if i[0].collidepoint(mx, my) and i[1] == True and select == True:
                draw.rect(screen, YELLOW, i[0], 3)
                if click:
                    i[3] = True
            if i[3] == True:
                select = False
                draw.rect(screen, GREEN, buyRects[i[5]], 2)
                screen.blit(towerStats[i[5]], (620, 630))
                txtUpgrade = txtFont2.render("UPGRADE?", True, BLACK)
                draw.rect(screen, BLACK, upgradeRect, 2)
                for a in activeDefenses:
                    if a[1] == i[2]:
                        damageDes = txtFont2.render("%i" % (a[4]), True, BLACK)
                        screen.blit(damageDes, (850, 630))
                        if type(a[5]) == int:
                            txtuCost = txtFont2.render("$%i" % (a[5]), True, BLACK)
                        else:
                            txtuCost = txtFont2.render(a[5], True, BLACK)

                        if upgradeRect.collidepoint(mx, my):
                            if type(a[5]) == int:
                                draw.rect(screen, GREEN, upgradeRect, 2)
                                if click:
                                    a[4] += 10 * (i[5] + 1)
                                    a[5] = None
                                    if money - defenses[i[5]].uCost >= 0:
                                        money -= defenses[i[5]].uCost

                cancelRect = Rect(20, 125, 125, 30)

                screen.blit(txtUpgrade, (650, 670))
                screen.blit(txtuCost, (763, 670))
                screen.blit(cancelPic, (20, 125))

                cancelRect = Rect(20, 125, 125, 30)
                deleteRect = Rect(20, 160, 125, 30)
                draw.rect(screen, GREEN, i[0], 3)
                screen.blit(cancelPic, (20, 125))
                screen.blit(deletePic, (20, 160))

                if deleteRect.collidepoint(mx, my):
                    draw.rect(screen, RED, deleteRect, 2)
                    if click:
                        i[3] = False
                        i[1] = False
                        for a in activeDefenses:
                            if a[3] == i[4]:
                                activeDefenses.remove(a)
                                money += a[2].refund
                        select = True
                if cancelRect.collidepoint(mx, my):
                    draw.rect(screen, RED, cancelRect, 2)
                    if click:
                        i[3] = False
                        select = True


def damageEnemies(enemy, activeDefenses, towerPos):
    global money, score
    for a in activeDefenses:
        for e in enemy:
            if towerPos[a[3]][6].collidepoint(e[0], e[1]) and e[5] == False:
                if a[6] == 0:
                    mixer.Sound.play(a[8])
                    screen.blit(muzzleFlash, (towerPos[a[3]][2]))
                    e[4] -= a[4]
                    a[6] = a[7]
                if a[6] > 0:
                    a[6] -= 1
            if e[4] <= 0:
                e[5] = True


def prev1():
    running = True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect = Rect(380, 320, 300, 100)
    while running:
        screen.blit(pr1, (0, 0))
        screen.blit(pressToStart, (380, 320))
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if pressRect.collidepoint(mx, my):
            draw.rect(screen, RED, pressRect, 3)
            if mb[0] == 1:
                return "lev1"

        display.flip()


def prev2():
    running = True
    mixer.music.load("FSE-Assets/sound/startMusic1.mp3")
    mixer.music.play(-1)
    pressRect = Rect(380, 320, 300, 100)
    while running:
        screen.blit(pr2, (0, 0))
        screen.blit(pressToStart, (380, 320))
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if pressRect.collidepoint(mx, my):
            draw.rect(screen, RED, pressRect, 3)
            if mb[0] == 1:
                return "lev2"

        display.flip()


def prev3():
    running = True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect = Rect(380, 320, 300, 100)
    while running:
        screen.blit(pr3, (0, 0))
        screen.blit(pressToStart, (380, 320))
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if pressRect.collidepoint(mx, my):
            draw.rect(screen, RED, pressRect, 3)
            if mb[0] == 1:
                return "lev3"

        display.flip()


def prev4():
    running = True
    mixer.music.load("FSE-Assets/sound/startMusic1.mp3")
    mixer.music.play(-1)
    pressRect = Rect(380, 320, 300, 100)
    while running:
        screen.blit(pr4, (0, 0))
        screen.blit(pressToStart, (380, 320))
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if pressRect.collidepoint(mx, my):
            draw.rect(screen, RED, pressRect, 3)
            if mb[0] == 1:
                return "lev4"

        display.flip()


def prev5():
    running = True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect = Rect(380, 320, 300, 100)
    while running:
        screen.blit(pr5, (0, 0))
        screen.blit(pressToStart, (380, 320))
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if pressRect.collidepoint(mx, my):
            draw.rect(screen, RED, pressRect, 3)
            if mb[0] == 1:
                return "lev5"

        display.flip()


def lev1():
    global defC, ready, activeDefenses, money, score, click, gameOver

    money = 4500
    pause = False
    running = True
    myclock = time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)

    quitRect = Rect(260, 25, 150, 40)

    # rect, status, blit position, edit status, rect, active tower #
    # subtract 91 from x,y, make 212 the length and width
    towerPos1 = [[Rect(115, 273, 50, 50), False, (115, 273), False, 0, None, Rect(21, 162, 212, 212)],
                 [Rect(264, 114, 50, 50), False, (264, 114), False, 1, None, Rect(173, 23, 212, 212)],
                 [Rect(319, 242, 50, 50), False, (319, 242), False, 2, None, Rect(190, 131, 212, 212)],
                 [Rect(217, 529, 50, 50), False, (217, 529), False, 3, None, Rect(126, 400, 212, 212)],
                 [Rect(388, 342, 50, 50), False, (388, 342), False, 4, None, Rect(297, 251, 212, 212)],
                 [Rect(570, 342, 50, 50), False, (570, 342), False, 5, None, Rect(479, 251, 212, 212)],
                 [Rect(750, 342, 50, 50), False, (750, 342), False, 6, None, Rect(659, 251, 212, 212)],
                 [Rect(418, 503, 50, 50), False, (418, 503), False, 7, None, Rect(327, 412, 212, 212)],
                 [Rect(598, 503, 50, 50), False, (598, 503), False, 8, None, Rect(507, 412, 212, 212)],
                 [Rect(778, 503, 50, 50), False, (778, 503), False, 9, None, Rect(688, 412, 212, 212)]]
    # x,y,frame,enemy type,health,death status
    enemy = [[0, 190, 0, transport, transport.health, False], [100, 190, 0, transport, transport.health, False],
             [-100, 190, 0, heavyTank, heavyTank.health, False], [-250, 190, 0, heavyTank, heavyTank.health, False],
             [-400, 190, 0, heavyTank, heavyTank.health, False], [-650, 190, 0, heavyTank, heavyTank.health, False],
             [-800, 190, 0, heavyTank, heavyTank.health, False]]

    click = False
    while running:

        myclock.tick(60)
        drawScene1(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic, (260, 25))
        draw.rect(screen, BLACK, quitRect, 2)
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evt.type == MOUSEBUTTONUP:
                click = False
        music(None)
        for a in activeDefenses:
            screen.blit(a[0], a[1])

        if quitRect.collidepoint(mx, my):
            draw.rect(screen, RED, quitRect, 3)
            if mb[0] == 1:
                pause = True

        if pause == True:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(sureRect, (335, 235))
            returnRect = Rect(465, 375, 140, 35)
            leaveRect = Rect(435, 425, 205, 35)
            if returnRect.collidepoint(mx, my):
                draw.rect(screen, RED, returnRect, 3)
                if mb[0] == 1:
                    pause = False
            if leaveRect.collidepoint(mx, my):
                draw.rect(screen, RED, leaveRect, 3)
                if mb[0] == 1:
                    pause = False
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "levelSelect"

        if ready == False and pause == False:
            prep(screen, towerPos1)

        if ready == True and gameOver == False and pause == False:
            genEnemies(enemy)
            moveEnemy(screen, enemy)
            baseHealth(enemy)
            healthBars(enemy)
            damageEnemies(enemy, activeDefenses, towerPos1)

        if gameOver:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(loseRect, (335, 235))
            retryRect = Rect(350, 405, 128, 50)
            mainRect = Rect(510, 405, 187, 50)
            draw.rect(screen, RED, (945, 375, 100, 10), 0)

            if retryRect.collidepoint(mx, my):
                draw.rect(screen, RED, retryRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "prev1"
            if mainRect.collidepoint(mx, my):
                draw.rect(screen, RED, mainRect, 3)
                if mb[0] == 1 and click == False:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
        count = 0
        for i in enemy:
            if i[5] == True:
                count += 1
            if count == len(enemy):
                endScreen = Surface((width, height), SRCALPHA)
                endScreen.fill((220, 220, 220, 127))
                screen.blit(endScreen, (0, 0))
                screen.blit(victoryRect, (320, 225))
                retryRect = Rect(350, 405, 128, 50)
                mainRect = Rect(510, 405, 187, 50)

        display.flip()

    return "levelSelect"


def lev2():
    global defC, ready, activeDefenses, money, score, click, gameOver
    money = 6000

    running = True
    pause = False
    myclock = time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect = Rect(260, 25, 150, 40)
    # subtract 91 from x,y, make 212 the length and width
    towerPos2 = [[Rect(75, 430, 50, 50), False, (75, 430), False, 1, None, Rect(-26, 339, 212, 212)],
                 [Rect(210, 430, 50, 50), False, (210, 430), False, 2, None, Rect(119, 339, 212, 212)],
                 [Rect(210, 300, 50, 50), False, (210, 300), False, 3, None, Rect(119, 209, 212, 212)],
                 [Rect(225, 125, 50, 50), False, (225, 125), False, 4, None, Rect(134, 34, 212, 212)],
                 [Rect(425, 125, 50, 50), False, (425, 125), False, 5, None, Rect(334, 34, 212, 212)],
                 [Rect(600, 125, 50, 50), False, (600, 125), False, 6, None, Rect(509, 34, 212, 212)],
                 [Rect(425, 300, 50, 50), False, (425, 300), False, 7, None, Rect(334, 209, 212, 212)],
                 [Rect(560, 300, 50, 50), False, (560, 300), False, 8, None, Rect(469, 209, 212, 212)],
                 [Rect(750, 275, 50, 50), False, (750, 275), False, 9, None, Rect(659, 184, 212, 212)],
                 [Rect(825, 375, 50, 50), False, (825, 375), False, 10, None, Rect(734, 284, 212, 212)]]

    enemy = [[-100, 510, 0, heavyTank, heavyTank.health, True], [-250, 510, 0, heavyTank, heavyTank.health, True],
             [-400, 510, 0, heavyTank, heavyTank.health, True], [-550, 510, 0, heavyTank, heavyTank.health, True],
             [-700, 510, 0, heavyTank, heavyTank.health, True]]
    while running:
        myclock.tick(60)
        drawScene2(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic, (260, 25))
        draw.rect(screen, BLACK, quitRect, 2)
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evt.type == MOUSEBUTTONUP:
                click = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        music(None)

        for a in activeDefenses:
            screen.blit(a[0], a[1])

        if quitRect.collidepoint(mx, my):
            draw.rect(screen, RED, quitRect, 3)
            if mb[0] == 1:
                pause = True

        if pause == True:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(sureRect, (335, 235))
            returnRect = Rect(465, 375, 140, 35)
            leaveRect = Rect(435, 425, 205, 35)
            if returnRect.collidepoint(mx, my):
                draw.rect(screen, RED, returnRect, 3)
                if mb[0] == 1:
                    pause = False
            if leaveRect.collidepoint(mx, my):
                draw.rect(screen, RED, leaveRect, 3)
                if mb[0] == 1:
                    pause = False
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 6000
                    score = 0
                    return "levelSelect"

        if ready == False and pause == False:
            prep(screen, towerPos2)

        if ready == True and gameOver == False and pause == False:
            genEnemies(enemy)
            moveEnemy2(screen, enemy)
            baseHealth(enemy)
            healthBars(enemy)
            damageEnemies(enemy, activeDefenses, towerPos2)

        if gameOver:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(loseRect, (320, 225))
            retryRect = Rect(350, 405, 128, 50)
            mainRect = Rect(510, 405, 187, 50)
            draw.rect(screen, RED, (945, 375, 100, 10), 0)
            if retryRect.collidepoint(mx, my):
                draw.rect(screen, RED, retryRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "lev2"
            if mainRect.collidepoint(mx, my):
                draw.rect(screen, RED, mainRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
        display.flip()
    return "levelSelect"


def lev3():
    global defC, ready, activeDefenses, money, score, click, gameOver

    money = 7000
    pause = False
    running = True
    myclock = time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect = Rect(260, 25, 150, 40)
    # subtract 91 from x,y, make 212 the length and width
    towerPos3 = [[Rect(52, 391, 50, 50), False, (52, 391), False, 1, None],
                 [Rect(200, 391, 50, 50), False, (200, 391), False, 2, None],
                 [Rect(190, 563, 50, 50), False, (190, 563), False, 3, None],
                 [Rect(274, 294, 50, 50), False, (274, 294), False, 4, None],
                 [Rect(274, 136, 50, 50), False, (274, 136), False, 5, None],
                 [Rect(450, 136, 50, 50), False, (450, 136), False, 6, None],
                 [Rect(474, 325, 50, 50), False, (474, 325), False, 7, None],
                 [Rect(630, 305, 50, 50), False, (630, 305), False, 8, None],
                 [Rect(700, 136, 50, 50), False, (700, 136), False, 11, None]]

    enemy = [[-100, 480, 0, heavyTank], [-250, 480, 0, heavyTank], [-400, 480, 0, heavyTank], [-650, 480, 0, heavyTank],
             [-800, 480, 0, heavyTank]]
    while running:
        myclock.tick(60)
        drawScene3(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic, (260, 25))
        draw.rect(screen, BLACK, quitRect, 2)
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evt.type == MOUSEBUTTONUP:
                click = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        music(None)

        for a in activeDefenses:
            screen.blit(a[0], a[1])

        if quitRect.collidepoint(mx, my):
            draw.rect(screen, RED, quitRect, 3)
            if mb[0] == 1:
                pause = True

        if pause == True:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(sureRect, (335, 235))
            returnRect = Rect(465, 375, 140, 35)
            leaveRect = Rect(435, 425, 205, 35)
            if returnRect.collidepoint(mx, my):
                draw.rect(screen, RED, returnRect, 3)
                if mb[0] == 1:
                    pause = False
            if leaveRect.collidepoint(mx, my):
                draw.rect(screen, RED, leaveRect, 3)
                if mb[0] == 1:
                    pause = False
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "levelSelect"

        if ready == False and pause == False:
            prep(screen, towerPos3)

        if ready == True and gameOver == False and pause == False:
            genEnemies(enemy)
            moveEnemy3(screen, enemy)
            baseHealth(enemy)

        if gameOver:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(loseRect, (320, 225))
            retryRect = Rect(350, 405, 128, 50)
            mainRect = Rect(510, 405, 187, 50)
            draw.rect(screen, RED, (945, 375, 100, 10), 0)
            if retryRect.collidepoint(mx, my):
                draw.rect(screen, RED, retryRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 7000
                    score = 0
                    return "lev3"
            if mainRect.collidepoint(mx, my):
                draw.rect(screen, RED, mainRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 7000
                    score = 0

        display.flip()
    return "levelSelect"


def lev4():
    global defC, ready, activeDefenses, money, score, click, gameOver

    money = 8500
    pause = False
    running = True
    myclock = time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect = Rect(260, 25, 150, 40)
    # subtract 91 from x,y, make 212 the length and width
    towerPos4 = [[Rect(107, 355, 50, 50), False, (107, 355), False, 1, None],
                 [Rect(193, 190, 50, 50), False, (193, 190), False, 2, None],
                 [Rect(331, 298, 50, 50), False, (331, 298), False, 3, None],
                 [Rect(331, 423, 50, 50), False, (331, 423), False, 4, None],
                 [Rect(457, 472, 50, 50), False, (457, 472), False, 5, None],
                 [Rect(241, 647, 50, 50), False, (241, 647), False, 6, None],
                 [Rect(689, 429, 50, 50), False, (689, 429), False, 7, None],
                 [Rect(495, 260, 50, 50), False, (495, 260), False, 8, None],
                 [Rect(686, 240, 50, 50), False, (686, 240), False, 9, None],
                 [Rect(820, 409, 50, 50), False, (820, 409), False, 10, None]]
    enemy = [[-100, 280, 0, heavyTank], [-250, 280, 0, heavyTank], [-400, 280, 0, heavyTank], [-650, 280, 0, heavyTank],
             [-800, 280, 0, heavyTank]]
    while running:
        myclock.tick(60)
        drawScene4(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic, (260, 25))
        draw.rect(screen, BLACK, quitRect, 2)
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evt.type == MOUSEBUTTONUP:
                click = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        music(None)
        for a in activeDefenses:
            screen.blit(a[0], a[1])

        if quitRect.collidepoint(mx, my):
            draw.rect(screen, RED, quitRect, 3)
            if mb[0] == 1:
                pause = True

        if pause == True:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(sureRect, (335, 235))
            returnRect = Rect(465, 375, 140, 35)
            leaveRect = Rect(435, 425, 205, 35)
            if returnRect.collidepoint(mx, my):
                draw.rect(screen, RED, returnRect, 3)
                if mb[0] == 1:
                    pause = False
            if leaveRect.collidepoint(mx, my):
                draw.rect(screen, RED, leaveRect, 3)
                if mb[0] == 1:
                    pause = False
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 8500
                    score = 0
                    return "levelSelect"

        if ready == False and pause == False:
            prep(screen, towerPos4)

        if ready == True and gameOver == False and pause == False:
            genEnemies(enemy)
            moveEnemy4(screen, enemy)
            baseHealth(enemy)

        if gameOver:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(loseRect, (320, 225))
            retryRect = Rect(350, 405, 128, 50)
            mainRect = Rect(510, 405, 187, 50)
            draw.rect(screen, RED, (945, 375, 100, 10), 0)
            if retryRect.collidepoint(mx, my):
                draw.rect(screen, RED, retryRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "lev4"
            if mainRect.collidepoint(mx, my):
                draw.rect(screen, RED, mainRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 8500
                    score = 0
        display.flip()
    return "levelSelect"


def lev5():
    global defC, ready, activeDefenses, money, score, click, gameOver

    money = 10000
    running = True
    pause = False
    myclock = time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect = Rect(260, 25, 150, 40)
    # subtract 91 from x,y, make 212 the length and width
    towerPos5 = [[Rect(30, 197, 50, 50), False, (30, 197), False, 1, None],
                 [Rect(232, 173, 50, 50), False, (232, 173), False, 2, None],
                 [Rect(382, 173, 50, 50), False, (382, 173), False, 3, None],
                 [Rect(228, 337, 50, 50), False, (228, 337), False, 4, None],
                 [Rect(332, 379, 50, 50), False, (332, 379), False, 5, None],
                 [Rect(332, 520, 50, 50), False, (332, 520), False, 6, None],
                 [Rect(525, 262, 50, 50), False, (525, 262), False, 7, None],
                 [Rect(525, 409, 50, 50), False, (525, 409), False, 8, None],
                 [Rect(645, 409, 50, 50), False, (645, 409), False, 9, None],
                 [Rect(459, 589, 50, 50), False, (459, 589), False, 10, None],
                 [Rect(815, 409, 50, 50), False, (815, 409), False, 11, None]]
    enemy = [[130, -100, 0, heavyTank], [130, -250, 0, heavyTank], [130, -400, 0, heavyTank], [130, -650, 0, heavyTank],
             [130, -800, 0, heavyTank]]
    while running:
        myclock.tick(60)
        drawScene5(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic, (260, 25))
        draw.rect(screen, BLACK, quitRect, 2)
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evt.type == MOUSEBUTTONUP:
                click = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        music(None)
        for a in activeDefenses:
            screen.blit(a[0], a[1])

        if quitRect.collidepoint(mx, my):
            draw.rect(screen, RED, quitRect, 3)
            if mb[0] == 1:
                pause = True

        if pause == True:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(sureRect, (335, 235))
            returnRect = Rect(465, 375, 140, 35)
            leaveRect = Rect(435, 425, 205, 35)
            if returnRect.collidepoint(mx, my):
                draw.rect(screen, RED, returnRect, 3)
                if mb[0] == 1:
                    pause = False
            if leaveRect.collidepoint(mx, my):
                draw.rect(screen, RED, leaveRect, 3)
                if mb[0] == 1:
                    pause = False
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 10000
                    score = 0
                    return "levelSelect"

        if ready == False and pause == False:
            prep(screen, towerPos5)

        if ready == True and gameOver == False and pause == False:
            genEnemies(enemy)
            moveEnemy5(screen, enemy)
            hudElements(screen)
            moneyScore(screen)
            baseHealth(enemy)

        if gameOver:
            endScreen = Surface((width, height), SRCALPHA)
            endScreen.fill((220, 220, 220, 127))
            screen.blit(endScreen, (0, 0))
            screen.blit(loseRect, (320, 225))
            retryRect = Rect(350, 405, 128, 50)
            mainRect = Rect(510, 405, 187, 50)
            draw.rect(screen, RED, (945, 375, 100, 10), 0)
            if retryRect.collidepoint(mx, my):
                draw.rect(screen, RED, retryRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 2000
                    score = 0
                    return "lev5"
            if mainRect.collidepoint(mx, my):
                draw.rect(screen, RED, mainRect, 3)
                if mb[0] == 1:
                    defC = None
                    editCond = False
                    activeDefenses = []
                    running = False
                    ready = False
                    gameOver = False
                    money = 10000
                    score = 0
        display.flip()
    return "levelSelect"


def creds():
    global mx, my
    mixer.music.load("FSE-Assets/sound/sovietTheme.mp3")
    mixer.music.play()
    running = True
    while running:
        screen.blit(credMenu, (0, 0))
        screen.blit(crossPic, (960, 50))
        backButton = Rect(950, 40, 50, 50)
        draw.rect(screen, BLACK, backButton, 3)
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                return "exit"
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if backButton.collidepoint(mx, my):
            draw.rect(screen, YELLOW, backButton, 3)
            if mb[0] == 1:
                running = False
        display.flip()
    return "main"


def instructions():
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    running = True
    while running:
        screen.blit(instructMenu, (0, 0))
        screen.blit(crossPic, (960, 50))
        backButton = Rect(950, 40, 50, 50)
        draw.rect(screen, BLACK, backButton, 3)
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                return "exit"
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        if backButton.collidepoint(mx, my):
            draw.rect(screen, YELLOW, backButton, 3)
            if mb[0] == 1:
                running = False
        display.flip()
    return "main"


def levelSelect():
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    levelRects = [Rect(122, 260, 240, 160), Rect(407, 262, 250, 160), Rect(696, 262, 250, 160),
                  Rect(257, 493, 240, 160), Rect(564, 492, 240, 160)]
    levels = ["prev1", "prev2", "prev3", "prev4", "prev5"]
    running = True
    click = False
    while running:
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                return "exit"
            if evnt.type == MOUSEBUTTONDOWN:
                click = True
            if evnt.type == MOUSEBUTTONUP:
                click = False
        screen.blit(levelSelectMenu, (0, 0))
        screen.blit(crossPic, (960, 50))
        backButton = Rect(950, 40, 50, 50)
        draw.rect(screen, BLACK, backButton, 3)

        if backButton.collidepoint(mx, my):
            draw.rect(screen, YELLOW, backButton, 3)
            if mb[0] == 1:
                running = False
        for i in range(len(levelRects)):
            if levelRects[i].collidepoint(mx, my):
                draw.rect(screen, RED, levelRects[i], 3)
                if mb[0] == 1 and click == False:
                    return levels[i]
        display.flip()
    return "main"


def main():
    mixer.music.load("FSE-Assets/sound/menuMusic.mp3")
    mixer.music.play(-1)
    buttons = [Rect(57, 294, 210, 47), Rect(57, 370, 270, 49), Rect(57, 448, 170, 49)]
    vals = ["levelSelect", "instructions", "credits"]
    running = True
    click = False
    while running:
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"
            if evnt.type == MOUSEBUTTONDOWN:
                click = True
                music(True)
            if evnt.type == MOUSEBUTTONUP:
                click = False

        screen.blit(mainMenu, (0, 0))
        backButton = Rect(950, 650, 50, 50)
        draw.rect(screen, RED, backButton, 3)
        screen.blit(crossPic, (960, 660))
        music(None)

        for i in range(len(buttons)):
            if buttons[i].collidepoint(mx, my):
                draw.rect(screen, RED, buttons[i], 3)
                if mb[0] == 1 and click == False:
                    return vals[i]
        if backButton.collidepoint(mx, my):
            draw.rect(screen, YELLOW, backButton, 3)
            if mb[0] == 1:
                return "exit"
        display.flip()


size = width, height = 1050, 750
screen = display.set_mode(size)
display.set_caption("The Great Patriotic War")
iconPic = image.load("FSE-Assets/icon.png")
display.set_icon(iconPic)
running = True
current = "main"

while current != "exit":
    # menu
    if current == "main":
        current = main()
    if current == "levelSelect":
        current = levelSelect()
    if current == "instructions":
        current = instructions()
    if current == "credits":
        current = creds()
    # previews
    if current == "prev1":
        current = prev1()
    if current == "prev2":
        current = prev2()
    if current == "prev3":
        current = prev3()
    if current == "prev4":
        current = prev4()
    if current == "prev5":
        current = prev5()
    # levels
    if current == "lev1":
        current = lev1()
    if current == "lev2":
        current = lev2()
    if current == "lev3":
        current = lev3()
    if current == "lev4":
        current = lev4()
    if current == "lev5":
        current = lev5()

    #final victory
    if current=="victory":
        current=victory()

quit()
