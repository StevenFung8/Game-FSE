from pygame import * 
from math import *
from random import *
screen=display.set_mode((1050,750))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)

map1=image.load("FSE-Assets/Maps/map1.jpg")
hudimg=image.load("FSE-Assets/hud.jpg")
hud=transform.scale(hudimg,(500,75))

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

buyRects=[Rect(610,31,57,57),Rect(685,31,57,57),Rect(760,31,57,57),Rect(834,31,57,57),Rect(908,31,57,57),Rect(982,31,57,57)]
for i in buyRects:
    draw.rect(screen,RED,i,3)

defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]
defensePics=[]
for i in defenses:
    defensePics.append(image.load(i.filename))

mapRect=Rect(0,0,1050,750)

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            capture=screen.copy()
            
    drawScene(screen)
    myclock.tick(60)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    holding='none'
    for i in buyRects:
        if i.collidepoint(mx,my):
            draw.rect(screen,RED,i,2)

    if mb[0]==1:
        if buyRects[0].collidepoint(mx,my):
            screen.set_clip(mapRect)
            defC="soldier"
        elif buyRects[1].collidepoint(mx,my):
            screen.set_clip(mapRect)
            defC="heavyMG"

    if mb[0]==1:
        if defC=="soldier":
            if mapRect.collidepoint(mx,my):
                holding="monkey"
                screen.blit(defensePics[0],(mx-75,my-75))
                towerScreen=screen.copy()
                
                
                
                
        elif defC=="heavyMG":
            if mapRect.collidepoint(mx,my):
                screen.blit(defensePics[1],(mx-75,my-75))
    if mb[0]==0 and holding=="monkey":
        screen.blit(towerScreen)
        screen.blit(defensePics[0],(mx-75,my-75))
    display.flip()
quit()
