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
mainMenu=image.load("FSE-Assets/mainscreen.jpg")
credMenu=image.load("FSE-Assets/credits.jpg")
instructMenu=image.load("FSE-Assets/instructions.jpg")
levelSelectMenu=image.load("FSE-Assets/levelSelect.jpg")
cross=image.load("FSE-Assets/cross.png")

txtFont=font.SysFont("Stencil",27)

map2=image.load("FSE-Assets/Maps/map2.jpg")
hudimg=image.load("FSE-Assets/hud.jpg")
hudRect=image.load("FSE-Assets/hudRect.png")
readyPic=image.load("FSE-Assets/readyRect.jpg")
quitP=image.load("FSE-Assets/quitRect.png")

hud=transform.scale(hudimg,(500,75))
hudRects=transform.scale(hudRect,(200,95))
quitPic=transform.scale(quitP,(150,40))
crossPic=transform.scale(cross,(30,30))

money=2000
score=0
txtMoney=txtFont.render("$"+str(money),True,RED)
txtScore=txtFont.render(str(score),True,RED)

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

    def __init__(self,name,damage,price):
        self.name=name
        self.damage=damage
        self.price=price
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',150,800)
bunker=towerType('bunker',50,1000)
fortress=towerType('fortress',250,1250)
heavyGun=towerType('heavyGun',350,1500)
heavyMG=towerType('heavyMG',20,500)
soldier=towerType('soldier',25,250)

def genPics(enemy):
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

def drawScene(screen):
    screen.blit(map2,(0,0))
    screen.blit(hud,(550,20))
    screen.blit(hudRects,(20,20))
    screen.blit(txtMoney,(100,30))
    screen.blit(txtScore,(110,84))

def prep(screen):
    ready=False
    readyRect=Rect(830,120,179,69)
    draw.rect(screen,RED,readyRect,2)
    screen.blit(readyPic,(830,120))
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if readyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,0),readyRect,2)
        if mb[0]==1:
            ready=True

def lev2():
    ready=False
    running=True
    myclock=time.Clock()
    mixer.init()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
    enemy=[[-100,500,transport],[-100,500,tankDestroyer],[-100,500,motorcycle],[-100,500,lightTank],[-100,500,infantry],[-100,500,heavyTank]]
    while running:
        myclock.tick(60)
        drawScene(screen)
        screen.blit(quitPic,(260,25))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                running=False
                return "levelSelect"
        genPics(enemy)
        prep(screen)
        moveEnemy(screen,pics,enemy)
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
        for i in range(len(buttons)):
            draw.rect(screen,RED,buttons[i],3)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(255,255,0),buttons[i],3)
                if mb[0]==1 and click==False:
                    return vals[i]
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
