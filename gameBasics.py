#gametemplate.py

'''
THIS WILL BE YOUR MAIN LOOP FOR ALL GAMES

while running:
    get input from user
    move good guy (Only MOVING!! not drawing)
    move bad guy  (Only MOVING!! not drawing)
    move other stuff  (only MOVING!! not drawing)
    check instruction
    draw scene (background, player, enemies, bullets...)
    delay (myglock.tick(60))
    

'''

from pygame import *
from math import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
YELLOW=(255,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
ex=20
ey=20
myglock=time.Clock()

enemies=[[0,20],[100,20],[200,20],[300,20],[400,20],[500,20]]

def drawScene(screen,badGuys,goodX,goodY):
    screen.fill(BLACK)
    for guys in badGuys:
        draw.circle(screen,RED,(guys[0],guys[1]),20)
    draw.circle(screen,GREEN,(mx,my),20)
    display.flip()9

def moveEnemies(badGuys,goodX,goodY):
    for guy in badGuys:
        if goodX>guy[0]:
            guy[0]+=2
        if goodX<guy[0]:
            guy[0]-=2
        if goodY>guy[1]:
            guy[1]+=2
        if goodY<guy[1]:
            guy[1]-=2
def checkHits(badGuys,goodX,goodY):
    for i in range(len(badGuys)): #badGuys is a 2D list
        d=sqrt((goodX-badGuys[i][0])**2+(goodY-badGuys[i][1])**2)
        if d<40:
            badGuys[i][0]=i*100
            badGuys[i][1]=20
             
        

        
    
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    moveEnemies(enemies,mx,my)
    checkHits(enemies,mx,my)
    drawScene(screen,enemies,mx,my)
    

    

    myglock.tick(10)
    display.flip() 

quit()

