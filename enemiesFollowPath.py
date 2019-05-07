from pygame import *
from math import *
from random import *
from datetime import datetime
init()

map1=image.load("Maps/map1.jpg")
enemy1=image.load("Enemies/soldier2.png")
enemy2=image.load("Enemies/motorcycle.png")
enemy3=image.load("Enemies/transport.png")
deadEnemy=image.load("Enemies/deadGerman.png")
wreck=image.load("Enemies/wreckage.png")

RED=(255,0,0)

def enemies():
    enemyList=[]
    for i in range(8):
        enemyList.append(enemy2)
    for i in range(20):
        enemyList.append(enemy1)
    for i in range(5):
        enemyList.append(enemy3)
    for i in enemyList:
        screen.blit(i,(40,245))

def drawScene():
    running=True
    quitButton=Rect(950,25,50,50)
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(map1,(0,0))
        draw.rect(screen,RED,quitButton,3)
        
        display.flip()
    
size=width,height=1050,750
screen=display.set_mode(size)

running=True

drawScene()
enemies()

quit()
