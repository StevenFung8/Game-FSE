#enemyDamage.py
from pygame import *
from math import *
init()

size=width,height=600,500
screen=display.set_mode(size)

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

tower=Rect(250,200,50,50)
rangeRect=Rect(170,130,200,200)

myClock=time.Clock()
running=True
while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    draw.rect(screen,RED,rangeRect)
    draw.rect(screen,GREEN,tower)
    mx,my=mouse.get_pos()
    display.flip()

quit()
