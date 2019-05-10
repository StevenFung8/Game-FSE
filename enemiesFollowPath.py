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

def moveEnemy(enemy):
    global frame
    xSpeed=0
    ySpeed=0
    if enemy[0]<220:
        xSpeed=2
        enemy[0]+=xSpeed
    if enemy[0]>=220 and enemy[1]<420:
        ySpeed=2
        enemy[1]+=ySpeed
        frame=1
    if enemy[1]>=420:
        xSpeed=1
        enemy[0]+=2
        frame=0

def drawScene(screen,enemyList,enemy):
    screen.blit(map1,(0,0))
    screen.blit(enemyList[int(frame)],(enemy[0],enemy[1]))
    display.flip()

tank1=image.load("FSE-Assets/Enemies/heavyTank.png")
pics=[]
tank2=transform.rotate(tank1,-90)
tank3=transform.rotate(tank1,90)
tank4=transform.rotate(tank1,180)

pics.append(tank1)
pics.append(tank2)
pics.append(tank3)
pics.append(tank4)

enemy=[40,190]
frame=0

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    moveEnemy(enemy)
    drawScene(screen,pics,enemy)
    mx,my=mouse.get_pos()
    print(mx,my)

    myclock.tick(60)

    display.flip()
quit()
