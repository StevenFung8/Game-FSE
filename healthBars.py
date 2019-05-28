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
heavyTank=enemyType('heavyTank',0.7,1000,20)

def moveEnemy(screen,enemyList,enemy):
    frame=0
    for i in range(len(enemy)):
        if enemy[i][0]<220:
            enemy[i][0]+=enemy[i][2].speed
            frame=0
        if enemy[i][0]>=220 and enemy[i][1]<420:
            enemy[i][1]+=enemy[i][2].speed
            frame=1
        if enemy[i][1]>=410:
            enemy[i][0]+=enemy[i][2].speed
            frame=0
        screen.blit(enemyList[i][int(frame)],(enemy[i][0],enemy[i][1]))
        #if enemy[i][0]>=900:
            #enemy.remove(enemy[i])
    display.flip()



def base(enemy):
    bars=100
    count=0
    draw.rect(screen,BLACK,(944,374,102,12),0)
    for i in range(len(enemy)):
        if enemy[i][0]>=900:
            count+=1
    
    bars=bars-count*10
    draw.rect(screen,GREEN,(945,375,bars,10),0)
    
    
            
           
def healthBars(enemy):
    for e in enemy:
        draw.rect(screen,BLACK,(e[0]+14,e[1]-11,52,12),0)
        draw.rect(screen,GREEN,(e[0]+15,e[1]-10,50,10),0)
def drawScene(screen):
    screen.blit(map1,(0,0))

enemy=[[-100,190,transport],[-100,190,heavyTank],[-100,190,motorcycle],[-100,190,lightTank],[-100,190,infantry]]
pics=[]

for i in enemy:
    img=[]
    img.append(image.load(i[2].filename))
    img.append(transform.rotate(image.load(i[2].filename),-90))
    pics.append(img)

'''
def drawEnemies(screen,enemyList,enemy):
    for i in range(len(enemy)):
        screen.blit(enemyList[i][int(frame)],(enemy[i][0],enemy[i][1]))
        if enemy[i][0]>=900:
            enemy.remove(enemy[i])
    display.flip()
'''
myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    moveEnemy(screen,pics,enemy)
    drawScene(screen)
    #drawEnemies(screen,pics,enemy)
    base(enemy)
    healthBars(enemy)
    myclock.tick(60)

quit()

