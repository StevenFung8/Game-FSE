
#placeTowers.py
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)


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

myclock=time.Clock()

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    display.flip() 


    drawScene(screen)
    myclock.tick(60)
    mx,my=mouse.get_pos()

    for i in buyRects:
        if i.collidepoint(mx,my):
            draw.rect(screen,RED,i,2)

    display.flip()

quit()
