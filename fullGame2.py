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
blackHeart=image.load("FSE-Assets/blackHeart.png")
loseRect=image.load("FSE-Assets/loseRect.png")
pressToStart=image.load("FSE-Assets/previews/pushtostart.png")

txtFont=font.SysFont("FSE-Assets/fonts/kremlin.ttf",25)
txtFont2=font.SysFont("Stencil",17)
txtFont3=font.SysFont("Stencil",20)

#loading map previews
pr1=image.load("FSE-Assets/previews/lvl1prev.jpg")
pr2=image.load("FSE-Assets/previews/lvl2prev.jpg")
pr3=image.load("FSE-Assets/previews/lvl3prev.jpg")
pr4=image.load("FSE-Assets/previews/lvl4prev.jpg")
pr5=image.load("FSE-Assets/previews/lvl5prev.jpg")

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
blackHeart=transform.scale(blackHeart,(25,25))

money=6000
score=0
'''
class AirPods:
    value = float("-Inf")
    price = "Too high"
    sound_signature = "Tinny"
    sound_isolation = None
    name = "AirPods"

class Asian:
    name = "Asian"
    def __init__(self, name):
        self.name = name
    def checkItemValue(self, item):
        print("%s's item assesement of %s:"%(self.name, item.name))
        print("Value: %s\nPrice: %s\nSound Signature: %s\nSound Isolation: %s"%(item.value, item.price, item.sound_signature, item.sound_isolation))

ryanAirPod = AirPods()
chris = Asian("Chris")

chris.checkItemValue(ryanAirPod)
'''
class enemyType:

    def __init__(self,name,speed,health,damage):
        self.name=name
        self.speed=speed
        self.health=health
        self.damage=damage
        self.filename="FSE-Assets/Enemies/"+name+".png"

infantry=enemyType('infantry',1.5,100,5)
transport=enemyType('transport',1.7,400,10)
motorcycle=enemyType('motorcycle',2,250,5)
lightTank=enemyType('lightTank',1,700,15)
heavyTank=enemyType('heavyTank',0.7,1000,20)
tankDestroyer=enemyType('tankDestroyer',0.8,1100,25)

class towerType:

    def __init__(self,name,damage,price,uCost,refund):
        self.name=name
        self.damage=damage
        self.price=price
        self.uCost=uCost
        self.refund=refund
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',80,800,350,400)
bunker=towerType('bunker',100,1000,450,500)
fortress=towerType('fortress',150,1250,600,625)
heavyGun=towerType('heavyGun',200,1500,700,750)
heavyMG=towerType('heavyMG',35,500,200,250)
soldier=towerType('soldier',25,250,100,125)

def genEnemies(enemy):
    global pics
    pics=[]
    for i in enemy:
        img=[]
        img.append(image.load(i[3].filename))
        img.append(transform.rotate(image.load(i[3].filename),-90))
        img.append(transform.rotate(image.load(i[3].filename),-270))
        img.append(transform.rotate(image.load(i[3].filename),-180))
        pics.append(img)
    return pics

def moneyScore(screen):
    global money
    global activeDefenses
    global score
    txtMoney=txtFont.render("$"+str(money),True,RED)
    txtScore=txtFont.render(str(score),True,RED)
    screen.blit(txtMoney,(100,30))
    screen.blit(txtScore,(110,84))

def baseHealth(enemy):
    global gameOver
    screen.blit(blackHeart,(940,350))
    bars=100
    count=0
    draw.rect(screen,BLACK,(944,374,102,12),0)
    for i in enemy:
        if i[0]>=900:
            bars-=i[3].damage
            if bars<=0:
                bars=0
    
    baseHealth=txtFont3.render(str(bars),True,BLACK)
    screen.blit(baseHealth,(965,353))
    draw.rect(screen,RED,(1044,375,bars-100,10),0)
    draw.rect(screen,GREEN,(945,375,bars,10),0)

    if bars==0:
        gameOver=True

def moveEnemy(screen,enemy):
    count=-1
    for i in enemy:
        if i[0]<220:
            i[0]+=i[3].speed
            i[2]=0
        if i[0]>=220 and i[1]<420:
            i[1]+=i[3].speed
            i[2]=1
        if i[1]>=410:
            i[0]+=i[3].speed
            i[2]=0
        count+=1
        screen.blit(pics[count][i[2]],i[:2])

def moveEnemy2(screen,enemy):
    count=-1
    for i in enemy:
        if i[0]<315:
            i[0]+=i[3].speed
            i[2]=0
        if i[0]>=315 and i[1]>210:
            i[1]-=i[3].speed
            i[2]=2
        if i[1]<=210 and i[0]<720:
            i[0]+=i[3].speed
            i[2]=0
        if i[0]>=690 and i[1]<670:
            i[1]+=i[3].speed*2
            i[2]=1
        if i[1]>=670 and i[0]==690:
            i[0]+=i[3].speed*2
            i[2]=0
            
        count+=1
        screen.blit(pics[count][i[2]],i[:2])

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

defC=None
ready=False
gameOver=False
activeDefenses=[]

def prep(screen,towerPos):
    global defC
    global ready
    global activeDefenses
    global money
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

    noMoney=txtFont2.render("Not enough money for this tower.",True,BLACK)
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
        screen.blit(towerDescription[defC],(620,630))
        txtUpgrade=txtFont2.render("UPGRADE?",True,BLACK)
        txtuCost=txtFont2.render("$%2i"%(defenses[defC].uCost),True,BLACK)
        cancelRect=Rect(20,125,125,30)

        screen.blit(txtUpgrade,(650,670))
        screen.blit(txtuCost,(763,670))
        screen.blit(cancelPic,(20,125))
        
        if upgradeRect.collidepoint(mx,my):
            draw.rect(screen,GREEN,upgradeRect,2)
        else:
            draw.rect(screen,BLACK,upgradeRect,2)

        for i in range(len(towerPos)):
            if towerPos[i][1]==False:
                draw.rect(screen,RED,towerPos[i][0],3)
                if towerPos[i][0].collidepoint(mx,my):
                    draw.rect(screen,YELLOW,towerPos[i][0],3)
                    if mb[0]==1 and money-defenses[defC].price>=0:
                        activeDefenses.append([defensePics[defC],towerPos[i][2],defenses[defC],towerPos[i][4],defenses[defC].damage])
                        money-=defenses[defC].price
                        towerPos[i][1]=True
                    
        if cancelRect.collidepoint(mx,my):
            draw.rect(screen,RED,cancelRect,2)
            if mb[0]==1:
                defC=None

    if defC==None:
        for i in towerPos:
            if i[0].collidepoint(mx,my) and i[1]==True:
                draw.rect(screen,YELLOW,i[0],3)
                if mb[0]==1:
                    i[3]=True
            if i[3]==True:
                deleteRect=Rect(20,125,125,30)
                draw.rect(screen,GREEN,i[0],3)
                screen.blit(deletePic,(20,125))
                if deleteRect.collidepoint(mx,my):
                    draw.rect(screen,RED,deleteRect,2)
                    if mb[0]==1:
                        i[3]=False
                        i[1]=False
                        for a in activeDefenses:
                            if a[3]==i[4]:
                                activeDefenses.remove(a)
                                money+=a[2].refund
'''                        
def upgrade():
    global money
    for i in range(len(buyRects)):
        if upgradeRect.collidepoint(mx,my):
            if click:
                money-=defenses[i].uCost
                defenses[i].uCost = None
                defenses[i].damage+=10*(i+1)
'''

def prev1():
    running=True
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr1,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev1"
            
        display.flip()

def prev2():
    running=True
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr2,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev2"
            
        display.flip()

def prev3():
    running=True
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr3,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev3"
            
        display.flip()

def prev4():
    running=True
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr4,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev4"
            
        display.flip()

def prev5():
    running=True
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr5,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev5"
            
        display.flip()

def lev1():
    global defC
    global ready
    global activeDefenses
    global money
    global score
    global gameOver
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                #rect, status, blit position, edit status, rect #
    towerPos1=[[Rect(115,273,50,50),False,(115,273),False,1],[Rect(264,114,50,50),False,(264,114),False,2],
               [Rect(319,242,50,50),False,(319,242),False,3],[Rect(217,529,50,50),False,(217,529),False,4],
               [Rect(388,342,50,50),False,(388,342),False,5],[Rect(570,342,50,50),False,(570,342),False,6],
               [Rect(750,342,50,50),False,(750,342),False,7],[Rect(418,503,50,50),False,(418,503),False,8],
               [Rect(598,503,50,50),False,(598,503),False,9],[Rect(778,503,50,50),False,(778,503),False,10]]
    enemy=[[-100,190,0,heavyTank],[-200,190,0,heavyTank],[-300,190,0,heavyTank],[-400,190,0,heavyTank],[-500,190,0,heavyTank]]

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
                editCond=False
                activeDefenses=[]
                running=False
                ready=False
                gameOver=False
                money=2000
                score=0
                return "levelSelect"
        if ready==False:
            prep(screen,towerPos1)
            
        if ready==True and gameOver==False:
            genEnemies(enemy)
            moveEnemy(screen,enemy)
            baseHealth(enemy)

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(300,200))
            retryRect=Rect(330,380,128,50)
            mainRect=Rect(490,380,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)
            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    gameOver=False
                    money=2000
                    score=0
                    return "lev1"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    gameOver=False
                    money=2000
                    score=0
        display.flip()

    return "levelSelect"

def lev2():
    global defC
    global ready
    global activeDefenses
    global money
    global score
    global gameOver
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos2=[[Rect(75,430,50,50),False,(75,430),False,1],[Rect(225,430,50,50),False,(225,430),False,2],[Rect(225,300,50,50),False,(225,300),False,3],
               [Rect(225,125,50,50),False,(225,125),False,4],[Rect(425,125,50,50),False,(425,125),False,5],
                [Rect(600,125,50,50),False,(600,125),False,6],[Rect(425,300,50,50),False,(425,300),False,7],[Rect(600,300,50,50),False,(600,300),False,8],
               [Rect(750,275,50,50),False,(750,275),False,9],[Rect(825,375,50,50),False,(825,375),False,10]]
    enemy=[[-100,500,0,heavyTank],[-200,500,0,heavyTank],[-300,500,0,heavyTank],[-400,500,0,heavyTank],[-500,500,0,heavyTank]]
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

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                defC=None
                editCond=False
                activeDefenses=[]
                running=False
                ready=False
                money=2000
                score=0
                return "levelSelect"
        
        if ready==False:
            prep(screen,towerPos2)

        if ready==True and gameOver==False:
            genEnemies(enemy)
            moveEnemy2(screen,enemy)
            baseHealth(enemy)

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(300,200))
            retryRect=Rect(330,380,128,50)
            mainRect=Rect(490,380,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)
            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    gameOver=False
                    money=2000
                    score=0
                    return "lev2"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    gameOver=False
                    money=2000
                    score=0
        display.flip()
    return "levelSelect"

def lev3():
    global defC
    global ready
    global activeDefenses
    global money
    global score
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos3=[[Rect(52,391,50,50),False,(52,391),False,1],[Rect(200,391,50,50),False,(200,391),False,2],[Rect(190,563,50,50),False,(190,563),False,3],
               [Rect(274,294,50,50),False,(274,294),False,4],[Rect(274,136,50,50),False,(274,136),False,5],[Rect(450,136,50,50),False,(450,136),False,6],
            [Rect(474,325,50,50),False,(474,325),False,7],[Rect(630,305,50,50),False,(630,305),False,8],[Rect(800,305,50,50),False,(800,305),False,9],
               [Rect(580,136,50,50),False,(580,136),False,10],[Rect(700,136,50,50),False,(700,136),False,11]]
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
        
        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                defC=None
                editCond=False
                activeDefenses=[]
                running=False
                ready=False
                money=2000
                score=0
                return "levelSelect"
        if ready==False:
            prep(screen,towerPos3)
        display.flip()
    return "levelSelect"

def lev4():
    global defC
    global ready
    global activeDefenses
    global money
    global score
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    towerPos4=[[Rect(107,355,50,50),False,(107,355),False,1],[Rect(193,190,50,50),False,(193,190),False,2],[Rect(331,298,50,50),False,(331,298),False,3],
               [Rect(331,423,50,50),False,(331,423),False,4],[Rect(457,472,50,50),False,(457,472),False,5],
            [Rect(241,647,50,50),False,(241,647),False,6],[Rect(689,429,50,50),False,(689,429),False,7],[Rect(495,260,50,50),False,(495,260),False,8],
               [Rect(686,240,50,50),False,(686,240),False,9],[Rect(820,409,50,50),False,(820,409),False,10]]
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

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                defC=None
                editCond=False
                activeDefenses=[]
                running=False
                ready=False
                money=2000
                score=0
                return "levelSelect"
        if ready==False:
            prep(screen,towerPos4)
        display.flip()
    return "levelSelect"

def lev5():
    global defC
    global ready
    global activeDefenses
    global money
    global score
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    draw.rect(screen,BLACK,quitRect,2)
    towerPos5=[[Rect(30,197,50,50),False,(30,197),False,1],[Rect(232,173,50,50),False,(232,173),False,2],[Rect(382,173,50,50),False,(382,173),False,3],
               [Rect(228,337,50,50),False,(228,337),False,4],[Rect(332,379,50,50),False,(332,379),False,5],[Rect(332,520,50,50),False,(332,520),False,6],
            [Rect(525,262,50,50),False,(525,262),False,7],[Rect(525,409,50,50),False,(525,409),False,8],[Rect(645,409,50,50),False,(645,409),False,9],
               [Rect(459,589,50,50),False,(459,589),False,10],[Rect(815,409,50,50),False,(815,409),False,11]]
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

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                defC=None
                editCond=False
                activeDefenses=[]
                running=False
                ready=False
                money=2000
                score=0
                return "levelSelect"
        if ready==False:
            prep(screen,towerPos5)
        display.flip()
    return "levelSelect"

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
    levels=["prev1","prev2","prev3","prev4","prev5"]
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
    #menu
    if current=="main":
        current=main()
    if current=="levelSelect":
        current=levelSelect()
    if current=="instructions":
        current=instructions()
    if current=="credits":
        current=creds()
    #previews
    if current=="prev1":
        current=prev1()
    if current=="prev2":
        current=prev2()
    if current=="prev3":
        current=prev3()
    if current=="prev4":
        current=prev4()
    if current=="prev5":
        current=prev5()
    #levels
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
