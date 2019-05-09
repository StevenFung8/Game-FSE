from pygame import *
from math import *
from random import *
screen=display.set_mode((1050,750))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
pathCol=(128,128,128,255)
pathCol2=(129,128,124,255)

map1=image.load("FSE-Assets/Maps/map1.jpg")

class enemyType:

    def __init__(self,name,speed,health):
        self.name=name
        self.speed=speed
        self.health=health
        self.filename="FSE-Assets/Enemies/"+name+".png"

infantry=enemyType('infantry',1.5,200)
transport=enemyType('transport',1.7,400)
motorcycle=enemyType('motorcycle',2,250)
lightTank=enemyType('lightTank',1,700)
heavyTank=enemyType('heavyTank',0.7,1000)

def moveEnemy(enemy):
    global frame
    for i in enemy:
        if i[0]<220:
            i[0]+=i[2].speed
        if i[0]>=220 and i[1]<420:
            i[1]+=i[2].speed
            frame=1
        if i[1]>=420:
            i[0]+=i[2].speed
            frame=0

def drawScene(screen,enemyList,enemy):
    screen.blit(map1,(0,0))
    for i in enemy:
        screen.blit(enemyList[int(frame)],(i[0],i[1]))
    display.flip()

tank1=image.load(heavyTank.filename)
pics=[]
tank2=transform.rotate(tank1,-90)
tank3=transform.rotate(tank1,90)
tank4=transform.rotate(tank1,180)

pics.append(tank1)
pics.append(tank2)
pics.append(tank3)
pics.append(tank4)

enemy=[[40,190,heavyTank]]
frame=0

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    moveEnemy(enemy)
    drawScene(screen,pics,enemy)

    myclock.tick(60)

    display.flip()
quit()
