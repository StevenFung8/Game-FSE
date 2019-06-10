from time import *
from pygame import *
from math import *
from random import *
from tkinter import *
width=1050
height=750
screen=display.set_mode((width,height))

RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
pathCol=(128,128,128,255)
pathCol2=(129,128,124,255)
init()
map1=image.load("FSE-Assets/Maps/map1.jpg")

boomPics=[]
for i in range(28):
    boomPics+=[image.load("FSE-Assets/bomb wait/images/Explode-05_frame_"+str(i)+".gif")]

class towerType:

    def __init__(self,name,damage,price,upgrade,uCost):
        self.name=name
        self.damage=damage
        self.price=price
        self.upgrade=upgrade
        self.uCost=uCost
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',80,800,False,300)
bunker=towerType('bunker',100,1000,False,350)
fortress=towerType('fortress',150,1250,False,450)
heavyGun=towerType('heavyGun',200,1500,False,500)
heavyMG=towerType('heavyMG',35,500,False,200)
soldier=towerType('soldier',25,250,False,150)

class enemyType:

    def __init__(self,name,speed,health,damage):
        self.name=name
        self.speed=speed
        self.health=health
        self.damage=damage
        self.filename="FSE-Assets/Enemies/"+name+".png"

infantry=enemyType('infantry',1.5,200,5)
transport=enemyType('transport',1.7,400,5)
motorcycle=enemyType('motorcycle',2,250,10)
lightTank=enemyType('lightTank',1,700,15)
heavyTank=enemyType('heavyTank',0.7,900,20)

#fonts

comicSans40=font.SysFont("Comic Sans MS",40)
stencil20=font.SysFont("Stencil",20)
stencil40=font.SysFont("Stencil",40)

def genEnemies(enemy,enemyList):
    global pics
    delay=0
    pics=[]
    if delay==0 and len(enemyList)>0:
        enemy.append(enemyList[0])
        enemyList.remove(enemyList[0])
        delay=30
    if delay>0:
        delay-=1

    for i in enemy:
        img=[]
        img.append(image.load(i[3].filename))
        img.append(transform.rotate(image.load(i[3].filename),-90))
        pics.append(img)
    
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

    display.flip()

def bombAnimation(screen,bombList):
    FRAME=0
    for bomb in bombList:
        screen.blit(boomPics[bomb[FRAME]],(900,600))
        FRAME+=1

def baseHealth(enemy):
    blackHeart=image.load("FSE-Assets/blackHeart.png")
    blackHeart=transform.scale(blackHeart,(25,25))
    screen.blit(blackHeart,(940,350))
    bars=100
    count=0
    draw.rect(screen,BLACK,(944,374,102,12),0)
    for i in enemy:
        if i[0]>=900:
            bars-=i[3].damage
            if bars<=0:
                bars=0
    
    baseHealth=stencil20.render(str(bars),True,BLACK)
    screen.blit(baseHealth,(965,353))
    draw.rect(screen,RED,(1044,375,bars-100,10),0)
    draw.rect(screen,GREEN,(945,375,bars,10),0)

    if bars==0:
        draw.rect(screen,RED,(945,375,100,10),0)
        endScreen=Surface((width,height),SRCALPHA)
        endScreen.fill((220,220,220,127))
        screen.blit(endScreen,(0,0))
        youLost=stencil40.render("GAME OVER",True,BLACK)
        screen.blit(youLost,(400,350))
           
def healthBars(enemy):
    for i in enemy:
        draw.rect(screen,BLACK,(i[0]+14,i[1]-11,i[3].health/10+2,9),0)
        draw.rect(screen,GREEN,(i[0]+15,i[1]-10,i[3].health/10,7),0)
        
def drawScene(screen):
    screen.blit(map1,(0,0))
    
        #[x,y,FRAME,className]
enemy=[]
enemyList=[[-100,190,0,infantry],[-200,190,0,infantry],[-300,190,0,infantry],[-450,190,0,heavyTank]]

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    genEnemies(enemy,enemyList)
            
    moveEnemy(screen,enemy)
    drawScene(screen)
    baseHealth(enemy)
    healthBars(enemy)
    
    myclock.tick(60)

quit()

