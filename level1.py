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

infantry=enemyType('infantry',1.5,100)
transport=enemyType('transport',1.7,400)
motorcycle=enemyType('motorcycle',2,250)
lightTank=enemyType('lightTank',1,700)
heavyTank=enemyType('heavyTank',0.7,1000)

class towerType:

    def __init__(self,name,damage,control):
        self.name=name
        self.damage=damage
        self.control=control
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',150,False)
bunker=towerType('bunker',50,False)
fortress=towerType('fortress',250,False)
heavyGun=towerType('heavyGun',350,False)
heavyMG=towerType('heavyMG',20,False)
soldier=towerType('soldier',25,False)

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

enemy=[[40,190,infantry]]
frame=0

for i in enemy:
    pics=[]
    img=image.load(i[2].filename)
    img2=transform.rotate(img,-90)
    pics.append(img)
    pics.append(img2)

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    moveEnemy(enemy)
    drawScene(screen,pics,enemy)
print("Chris ur fuckign gay")

    myclock.tick(60)

    display.flip()
quit()
