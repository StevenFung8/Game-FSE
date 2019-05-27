from pygame import * 
from math import *
from random import *
screen=display.set_mode((1050,750))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
marker=Surface((200,200),SRCALPHA)
defC="none"
cond=False
ready=False

font.init()

txtFont=font.SysFont("Bradley Hand ITC",35)

map2=image.load("FSE-Assets/Maps/map2.jpg")
hudimg=image.load("FSE-Assets/hud.jpg")
hudRect=image.load("FSE-Assets/hudRect.png")
readyPic=image.load("FSE-Assets/readyRect.jpg")

hud=transform.scale(hudimg,(500,75))
hudRects=transform.scale(hudRect,(200,95))

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
    screen.blit(txtScore,(110,80))

def prep(screen):
    ready=False
    draw.rect(screen,RED,readyRect,2)
    screen.blit(readyPic,(830,120))
    if readyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,0),readyRect,2)
        if mb[0]==1:
            ready=True
    return ready


buyRects=[Rect(610,31,57,57),Rect(685,31,57,57),Rect(760,31,57,57),Rect(834,31,57,57),Rect(908,31,57,57),Rect(982,31,57,57)]
readyRect=Rect(830,120,179,69)

defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]
defensePics=[]
for i in defenses:
    defensePics.append(image.load(i.filename))

enemy=[[-100,500,transport],[-100,500,tankDestroyer],[-100,500,motorcycle],[-100,500,lightTank],[-100,500,infantry],[-100,500,heavyTank]]
pics=[]

for i in enemy:
    img=[]
    img.append(image.load(i[2].filename))
    img.append(transform.rotate(image.load(i[2].filename),-90))
    img.append(transform.rotate(image.load(i[2].filename),-270))
    img.append(transform.rotate(image.load(i[2].filename),-180))
    pics.append(img)

mapRect=Rect(0,0,1050,750)

activeDefenses=[]

mixer.init()
mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
mixer.music.play(-1)

towerPosition=[Rect(75,450,50,50),Rect(225,450,50,50),Rect(225,300,50,50),Rect(225,125,50,50),Rect(425,125,50,50),
               Rect(600,125,50,50),Rect(425,300,50,50),Rect(600,300,50,50),Rect(750,275,50,50),Rect(825,375,50,50)]

myclock=time.Clock()
running=True
while running:
    myclock.tick(60)
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            capture=screen.copy()

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
            
    drawScene(screen)
    moveEnemy(screen,pics,enemy)

    if ready==False:
        prep(screen)
    if ready:
        moveEnemy(screen,pics,enemy)
    '''
)    for i in buyRects:
        if i.collidepoint(mx,my):
            draw.rect(screen,RED,i,2)
    if mb[0]==1:
        if buyRects[0].collidepoint(mx,my):
            defC=0
        elif buyRects[1].collidepoint(mx,my):
            defC=1
        elif buyRects[2].collidepoint(mx,my):
            defC=2
        elif buyRects[3].collidepoint(mx,my):
            defC=3
        elif buyRects[4].collidepoint(mx,my):
            defC=4
        elif buyRects[5].collidepoint(mx,my):
            defC=5
        
    if mb[0]==1:
        if defC==0:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[0],(mx-15,my-15))
                ax,ay=mx-15,my-15
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True      
        elif defC==1:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[1],(mx-30,my-30))
                ax,ay=mx-30,my-30
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True      
        elif defC==2:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[2],(mx-40,my-35))
                ax,ay=mx-40,my-35
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True      
        elif defC==3:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[3],(mx-25,my-25))
                ax,ay=mx-25,my-25
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True      
        elif defC==4:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[4],(mx-55,my-40))
                ax,ay=mx-55,my-40
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True      
        elif defC==5:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[5],(mx-40,my-50))
                ax,ay=mx-40,my-50 ##### fix this line, IT IS RELATIVE TO THE SAME THINGS
                for t in towerPosition:
                    if t.collidepoint(mx,my):
                        cond=True             
    if mb[0]==0:
        if cond==True:
            activeDefenses.append([defC,ax,ay])
            for t in towerPosition:
                if t.collidepoint(mx,my):
                    towerPosition.remove(t)
            cond=False
            defC="none"

    for a in activeDefenses:
        screen.blit(defensePics[a[0]],(a[1],a[2]))
        print(a)
    '''
    display.flip()
quit()
