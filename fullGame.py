#mainGame
from pygame import *
from math import *
from random import *
from datetime import datetime

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)

init()
#load pictures
mainMenu=image.load("FSE-Assets/mainscreen.jpg")
credMenu=image.load("FSE-Assets/credits.jpg")
instructMenu=image.load("FSE-Assets/instructions.jpg")
levelSelectMenu=image.load("FSE-Assets/levelSelect.jpg")
cross=image.load("FSE-Assets/cross.png")
hudimg=image.load("FSE-Assets/hud.jpg")
hudRect=image.load("FSE-Assets/hudRect.png")
readyPic=image.load("FSE-Assets/readyRect.jpg")
quitP=image.load("FSE-Assets/quitRect.png")
dialogueP=image.load("FSE-Assets/dialogueRect.png")
cancelPic=image.load("FSE-Assets/cancelRect.png")
deletePic=image.load("FSE-Assets/deleteRect.png")
mutePic=image.load("FSE-Assets/musicPicMUTE.png")
eigthNote=image.load("FSE-Assets/musicPic.png")

txtFont=font.SysFont("Stencil",25)
txtFont2=font.SysFont("Stencil",17)

#loading maps
map1=image.load("FSE-Assets/Maps/map1.jpg")
map2=image.load("FSE-Assets/Maps/map2.jpg")
map3=image.load("FSE-Assets/Maps/map3.jpg")
map4=image.load("FSE-Assets/Maps/map4.jpg")
map5=image.load("FSE-Assets/Maps/map5.jpg")

#transform pictures
hud=transform.scale(hudimg,(500,75))
hudRects=transform.scale(hudRect,(200,95))
quitPic=transform.scale(quitP,(150,40))
crossPic=transform.scale(cross,(30,30))
dialoguePic=transform.scale(dialogueP,(400,110))




mx,my=mouse.get_pos()
mb=mouse.get_pressed()


class AirPods:
    value = float('-Inf')
    sound_isolation = None
    sound_profile = "tinny"
    def __init__(self):
        print("Airpods evalution: \nValue: %s\nSound Isolation: %s\nSound Profile: %s"%(self.value, self.sound_isolation, self.sound_profile))




class enemyType:

    def __init__(self,name,speed,health):
        self.name=name
        self.speed=speed
        self.health=health
        self.filename="FSE-Assets/Enemies/"+name+".png"

infantry=enemyType('infantry',1.5,100)
transport=enemyType('transport',1.7,400)
motorcycle=enemyType('motorcycle',2,250)
lightTank=enemyType('lightTank',1,700)
heavyTank=enemyType('heavyTank',0.7,1000)
tankDestroyer=enemyType('tankDestroyer',0.8,900)

class towerType:

    def __init__(self,name,damage,price,uCost):
        self.name=name
        self.damage=damage
        self.price=price
        self.uCost=uCost
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',80,800,350)
bunker=towerType('bunker',100,1000,450)
fortress=towerType('fortress',150,1250,600)
heavyGun=towerType('heavyGun',200,1500,700)
heavyMG=towerType('heavyMG',35,500,200)
soldier=towerType('soldier',25,250,100)

def genEnemies(enemy):
    global pics
    pics=[]
    for i in enemy:
        img=[]
        img.append(image.load(i[2].filename))
        img.append(transform.rotate(image.load(i[2].filename),-90))
        img.append(transform.rotate(image.load(i[2].filename),-270))
        img.append(transform.rotate(image.load(i[2].filename),-180))
        pics.append(img)
    return pics

def moneyScore(screen):
    money=2000
    score=0
    txtMoney=txtFont.render("$"+str(money),True,RED)
    txtScore=txtFont.render(str(score),True,RED)
    screen.blit(txtMoney,(100,30))
    screen.blit(txtScore,(110,84))

def moveEnemy(screen,enemyList,enemy):
    frame=0
    count=0
    for i in enemy:
        if i[0]<315:
            i[0]+=i[2].speed
            frame=0
        if i[0]>=315 and i[1]>210:
            i[1]-=i[2].speed
            frame=2
        if i[1]<=210 and i[0]<720:
            i[0]+=i[2].speed
            frame=0
        if i[0]>=690 and i[1]<670:
            i[1]+=i[2].speed*2
            frame=1
        if i[1]>=670 and i[0]==690:
            i[0]+=i[2].speed*2
            frame=0

        screen.blit(enemyList[count][int(frame)],(i[0],i[1]))
        count+=1

def drawScene1(screen):
    screen.blit(map1,(0,0))
def drawScene2(screen):
    screen.blit(map2,(0,0))
def drawScene3(screen):
    screen.blit(map3,(0,0))
def drawScene4(screen):
    screen.blit(map4,(0,0))
def drawScene5(screen):
    screen.blit(map5,(0,0))

def hudElements(screen):
    screen.blit(hud,(550,20))
    screen.blit(hudRects,(20,20))
    screen.blit(dialoguePic,(600,600))


def music():
    pause=False
    muteRect=Rect(400,400,80,80)
    draw.rect(screen,RED,muteRect,1)
    screen.blit(mutePic,(400,400))

    if mb[0] == 1 and muteRect.collidepoint(mx, my) and pause == False:
        pause=True
    print(pause)




    
defC=None

def prep(screen,towerPos):
    global defC
    ready=False
    placeCond = True

defC=None
ready=False
activeDefenses=[]

def prep(screen,towerPos):
    global defC
    global ready
    global activeDefenses
    readyRect=Rect(830,120,179,69)
    upgradeRect=Rect(750,662,70,30)
    buyRects=[Rect(607,28,59,63),Rect(682,28,61,63),Rect(758,28,61,63),Rect(834,28,61,63),Rect(908,28,61,63),Rect(982,28,61,63)]
    cancelRect=Rect(20,125,125,30)

    txtD1=txtFont2.render("Basic Soldier - Cost: $250, Damage: 25",True,BLACK)
    txtD2=txtFont2.render("Machine Gun - Cost: $500, Damage: 35",True,BLACK)
    txtD3=txtFont2.render("Anti-Tank Gun - Cost: $800, Damage: 80",True,BLACK)
    txtD4=txtFont2.render("Bunker - Cost: $1000, Damage: 100",True,BLACK)
    txtD5=txtFont2.render("Fortress - Cost: $1250, Damage: 150",True,BLACK)
    txtD6=txtFont2.render("Heavy AT Gun - Cost: $1500, Damage: 200",True,BLACK)
    towerDescription=[txtD1,txtD2,txtD3,txtD4,txtD5,txtD6]

    ##generating defense images
    defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]
    defensePics=[]
    for i in defenses:
        defensePics.append(image.load(i.filename))

    draw.rect(screen,RED,readyRect,2)
    screen.blit(readyPic,(830,120))
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if readyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,0),readyRect,2)
        if mb[0]==1:
            ready=True

    for i in range(len(buyRects)):
        if buyRects[i].collidepoint(mx,my):
            draw.rect(screen,YELLOW,buyRects[i],2)
            if mb[0]==1:
                defC=int(i)
    


    if defC!=None:
        draw.rect(screen,GREEN,buyRects[defC],2)
        #screen.blit(defensePics[i],(630,630))
        screen.blit(towerDescription[defC],(620,630))
        txtUpgrade=txtFont2.render("UPGRADE?",True,BLACK)
        txtuCost=txtFont2.render("$%2i"%(defenses[defC].uCost),True,BLACK)
        cancelRect=Rect(20,125,125,30)

        screen.blit(txtUpgrade,(650,670))
        screen.blit(txtuCost,(763,670))
        screen.blit(cancelPic,(20,125))
        draw.rect(screen,BLACK,upgradeRect,2)

        for i in range(len(towerPos)):
            if towerPos[i][1]==False:
                draw.rect(screen,RED,towerPos[i][0],3)
                if towerPos[i][0].collidepoint(mx,my):
                    draw.rect(screen,YELLOW,towerPos[i][0],3)
                    if mb[0]==1:
                        activeDefenses.append([defensePics[defC],towerPos[i][2]])
                        towerPos[i][1]=True
                    
        if cancelRect.collidepoint(mx,my):
            draw.rect(screen,RED,cancelRect,2)
            if mb[0]==1:
                defC=None

def upgrade():
    global money
    for i in range(len(buyRects)):
        if upgradeRect.collidepoint(mx,my):
            draw.rect(screen,GREEN,upgradeRect,2)
            if click:
                money-=defenses[i].uCost
                defenses[i].uCost = None
                defenses[i].damage+=10*(i+1)

                
airpods = AirPods()
            


airpods = AirPods()


def lev1():
    global defC
    global ready
    global activeDefenses
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                #rect,status,blit position
    towerPos1=[[Rect(115,273,50,50),False,(115,273)],[Rect(264,114,50,50),False,(264,114)],[Rect(319,242,50,50),False,(319,242)],[Rect(217,529,50,50),False,(217,529)],[Rect(388,342,50,50),False,(388,342)],[Rect(570,342,50,50),False,(570,342)],
               [Rect(750,342,50,50),False,(750,342)],[Rect(418,503,50,50),False,(418,503)],[Rect(598,503,50,50),False,(598,503)],[Rect(778,503,50,50),False,(778,503)]]
    while running:
        myclock.tick(60)
        drawScene1(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                defC=None
                activeDefenses=[]
                running=False
                return "levelSelect"
        #genPics(enemy)
        prep(screen,towerPos1)
        music()
        #moveEnemy(screen,pics,enemy)

        display.flip()

    return "main"

def lev2():
    global defC
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos2=[[Rect(75,430,50,50),False],[Rect(225,430,50,50),False],[Rect(225,300,50,50),False],[Rect(225,125,50,50),False],[Rect(425,125,50,50),False],
            [Rect(600,125,50,50),False],[Rect(425,300,50,50),False],[Rect(600,300,50,50),False],[Rect(750,275,50,50),False],[Rect(825,375,50,50),False]]
    while running:
        myclock.tick(60)
        drawScene2(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                running=False
                defC=None
                return "levelSelect"
        #genPics(enemy)
        prep(screen,towerPos2)
        #moveEnemy(screen,pics,enemy)
        display.flip()
    return "main"

def lev3():
    global defC
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos3=[[Rect(52,391,50,50),False],[Rect(200,391,50,50),False],[Rect(190,563,50,50),False],[Rect(274,294,50,50),False],[Rect(274,136,50,50),False],[Rect(450,136,50,50),False],
            [Rect(474,325,50,50),False],[Rect(630,305,50,50),False],[Rect(800,305,50,50),False],[Rect(580,136,50,50),False],[Rect(700,136,50,50),False]]
    while running:
        myclock.tick(60)
        drawScene3(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                running=False
                defC=None
                return "levelSelect"
        #genPics(enemy)
        prep(screen,towerPos3)
        #moveEnemy(screen,pics,enemy)
        display.flip()
    return "main"

def lev4():
    global defC
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos4=[[Rect(107,355,50,50),False],[Rect(193,190,50,50),False],[Rect(331,298,50,50),False],[Rect(331,423,50,50),False],[Rect(457,472,50,50),False],
            [Rect(241,647,50,50),False],[Rect(689,429,50,50),False],[Rect(495,260,50,50),False],[Rect(686,240,50,50),False],[Rect(820,409,50,50),False]]
    while running:
        myclock.tick(60)
        drawScene4(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                running=False
                defC=None
                return "levelSelect"
        #genPics(enemy)
        prep(screen,towerPos4)
        #moveEnemy(screen,pics,enemy)
        display.flip()
    return "main"

def lev5():
    global defC
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    draw.rect(screen,BLACK,quitRect,2)
    towerPos5=[[Rect(30,197,50,50),False],[Rect(232,173,50,50),False],[Rect(382,173,50,50),False],[Rect(228,337,50,50),False],[Rect(332,379,50,50),False],[Rect(332,520,50,50),False],
            [Rect(525,262,50,50),False],[Rect(525,409,50,50),False],[Rect(645,409,50,50),False],[Rect(459,589,50,50),False],[Rect(815,409,50,50),False]]
    while running:
        myclock.tick(60)
        drawScene5(screen)
        hudElements(screen)
        moneyScore(screen)
        screen.blit(quitPic,(260,25))
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        print(mx,my)

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                running=False
                defC=None
                return "levelSelect"
        #genPics(enemy)
        prep(screen,towerPos5)
        #moveEnemy(screen,pics,enemy)
        display.flip()
    return "main"

def creds():
    global mx,my
    mixer.init()
    mixer.music.load("FSE-Assets/sound/sovietTheme.mp3")
    mixer.music.play()
    running=True
    while running:
        screen.blit(credMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        display.flip()
    return "main"

def instructions():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    running=True
    while running:
        screen.blit(instructMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        display.flip()
    return "main"

def levelSelect():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    levelRects=[Rect(122,260,240,160),Rect(407,262,250,160),Rect(696,262,250,160),Rect(257,493,240,160),Rect(564,492,240,160)]
    levels=["lev1","lev2","lev3","lev4","lev5"]
    running=True
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
        screen.blit(levelSelectMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)

        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        for i in range(len(levelRects)):
            if levelRects[i].collidepoint(mx,my):
                draw.rect(screen,RED,levelRects[i],3)
                if mb[0]==1:
                    return levels[i]
        display.flip()
    return "main"

def main():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic.mp3")
    mixer.music.play(-1)
    buttons=[Rect(57,294,210,47),Rect(57,370,270,49),Rect(57,448,170,49)]
    vals=["levelSelect","instructions","credits"]
    running=True
    click=False
    while running:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
            if evnt.type==MOUSEBUTTONDOWN:
                click=True
            if evnt.type==MOUSEBUTTONUP:
                click=False
        screen.blit(mainMenu,(0,0))
        backButton=Rect(950,650,50,50)
        musicButton=Rect(870,650,50,50)
        draw.rect(screen,RED,backButton,3)
        draw.rect(screen,RED,musicButton,3)
        screen.blit(crossPic,(960,660))

        for i in range(len(buttons)):
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,RED,buttons[i],3)
                if mb[0]==1 and click==False:
                    return vals[i]
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                return "exit"
        display.flip()

size=width,height=1050,750
screen=display.set_mode(size)
display.set_caption("The Great Patriotic War")
iconPic=image.load("FSE-Assets/icon.png")
display.set_icon(iconPic)
running=True
current="main"

while current!="exit":
    if current=="main":
        current=main()
    if current=="levelSelect":
        current=levelSelect()
    if current=="instructions":
        current=instructions()
    if current=="credits":
        current=creds()
    if current=="lev1":
        current=lev1()
    if current=="lev2":
        current=lev2()
    if current=="lev3":
        current=lev3()
    if current=="lev4":
        current=lev4()
    if current=="lev5":
        current=lev5()

quit()
