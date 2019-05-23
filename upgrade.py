#Range.py
from pygame import *
from math import *
from random import *
screen=display.set_mode((800,600))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)

X=0
Y=1
ATK=2
M=3
R=3
HP=4
PRIZE=5
     #  x   y  atk m  hp
enemy=[[100,200,10, 5,600, 100]]
    #     x   y  Atk  range
soldier=[400,350, 10, 150]

enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]
hubRect=Rect(3,400,252,195)
money=400
font.init()
stencilFont=font.SysFont("stencil",55)
def drawScene(enemy,defense):
    screen.fill(WHITE)
    for  i in range(len(enemy)):
        enemy[i][X]+=enemy[i][M]
        if enemy[i][X]<30 or enemy[i][X]>770:
            enemy[i][M]*=-1
    enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))] 
    for i in range(len(enemyRect)):
        draw.rect(screen,(255,140,209),enemyRect[i])
    draw.circle(screen,(45,123,189),(int(soldier[X]),int(soldier[Y])),40)
    draw.circle(screen,BLACK,(int(soldier[X]),int(soldier[Y])),int(soldier[R]),2)  #range circle
    draw.rect(screen,BLACK,hubRect,2)
    screen.blit(stencilFont.render("UPGRADE",True,(255,140,209)),(5,402))
    display.flip()

def upgrade(soldier):
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if mb[0]==1:
        
        dist=sqrt((int(soldier[X])-mx)**2+(int(soldier[Y])-my))
        if dist<=180:
            soldier[ATK]+=10
    

def checkRange(enemy,defense):
    global money
    enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]
    for i in range(len(enemy)):
        dist=sqrt((int(soldier[X])-(enemyRect[i][0]+enemyRect[i][2]//2))**2+(int(soldier[Y])-(enemyRect[i][1]+enemyRect[i][3]//2))**2)
        print(enemyRect[i][0]+enemyRect[i][3]/2)
        print(dist)
        print(enemy[i][HP])
        if dist<=180:
            enemy[i][HP]-=soldier[2]
            if enemy[i][HP]<=0:
                money+=enemy[i][PRIZE]
                print(money)
                del enemy[i]


myglock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    #checkRange(enemy,soldier)
    drawScene(enemy,soldier)
    upgrade(soldier)
    checkRange(enemy,soldier)
    myglock.tick(10)
print("Chris is gay")
quit()
