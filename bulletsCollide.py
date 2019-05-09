#graphicsTemplate.py   (sideShooter.py)
from pygame import *
from math import *
from random import *
screen=display.set_mode((800,600))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)

MAXRAPID=10

rapid=MAXRAPID
guy=[100,300]
#targets=[]
#for i in range(5):
#    targets.append(Rect(randint(500,750),randint(100,500),40,40))
v=[5,0]#horiz and vertical speed
          #x   y vx vy
#bullets=[[170,45,2,1],[250,200,2,-1]] #this will be a 2D list

x=20
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    keys=key.get_pressed()
    guy=mouse.get_pos()
    draw.circle(screen,RED,(x,500),20)
    if x>0 and x<580:
        x+=1
    if x>=580:
        x-=1
display.flip()
print("Chris is fuckign gay")
quit()

        
