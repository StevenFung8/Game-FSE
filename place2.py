from pygame import * 
from math import *
from random import *
screen=display.set_mode((1050,750))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)

map1=image.load("FSE-Assets/Maps/map2.jpg")
hudimg=image.load("FSE-Assets/hud.jpg")
hud=transform.scale(hudimg,(500,75))

mapRect=Rect(0,0,1050,750)

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
tankDestroyer=enemyType('tankDestroyer',0.8,1200)

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

def drawScene(screen):
    screen.blit(map1,(0,0))
    screen.blit(hud,(550,20))
    
defC="none"
def placeTowers(buyRects,towerPosition,defensePics):
    global defC
    cond=False
    activeDefenses=[]
    for i in buyRects:
        if i.collidepoint(mx,my):
            draw.rect(screen,RED,i,2)
    if click:
        if buyRects[0].collidepoint(mx,my):
            print("Click")
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
        
    if True:
        if defC==0:
            if mapRect.collidepoint(mx,my):
                for p in towerPosition:
                    draw.rect(screen,GREEN,p,3)
                screen.blit(defensePics[0],(mx-20,my-20))
                ax,ay=mx-20,my-20
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
                    screen.blit(defensePics[defC],(t[0],t[1]))
                    print(t[0],t[1])
                    towerPosition.remove(t)
            cond=False
            defC="none"

    for a in activeDefenses:
        screen.blit(defensePics[a[0]],(a[1],a[2]))
    

buyRects=[Rect(607,28,59,63),Rect(682,28,61,63),Rect(758,28,61,63),Rect(834,28,61,63),Rect(908,28,61,63),Rect(982,28,61,63)]

defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]
defensePics=[]
for i in defenses:
    defensePics.append(image.load(i.filename))

mapRect=Rect(0,0,1050,750)

mixer.init()
mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
mixer.music.play(-1)
########### I SET THE VOLUME OFF TO NOT KILL THE EARS ########
#mixer.music.set_volume(0)
##############################

towerPosition=[Rect(75,450,50,50),Rect(225,450,50,50),Rect(225,300,50,50),Rect(225,125,50,50),Rect(425,125,50,50),
               Rect(600,125,50,50),Rect(425,300,50,50),Rect(600,300,50,50),Rect(750,275,50,50),Rect(825,375,50,50)]

myclock=time.Clock()
running=True
while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click=True
            capture=screen.copy()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #print(click)
    drawScene(screen)
    placeTowers(buyRects,towerPosition,defensePics)
    
    myclock.tick(60)
        
    display.flip()
quit()
