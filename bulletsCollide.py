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
     #  x   y  atk m  hp
enemy=[[100,200,10, 5,600]]
    #     x   y  Atk  range
soldier=[400,350, 5, 150]
enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]

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
    
    display.flip()

def checkRange(enemy,defense):
    enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]
    for i in range(len(enemy)):
        dist=sqrt((int(soldier[X])-(enemyRect[i][0]+enemyRect[i][2]//2))**2+(int(soldier[Y])-(enemyRect[i][1]+enemyRect[i][3]//2))**2)
        print(enemyRect[i][0]+enemyRect[i][3]/2)
        print(dist)
        print(enemy[i][HP])
        if dist<=180:
            enemy[i][HP]-=10
            if enemy[i][HP]<=0:
                del enemy[i]
            
    
myglock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    #checkRange(enemy,soldier)
    drawScene(enemy,soldier)
    checkRange(enemy,soldier)
    myglock.tick(10)
print("Chris is gay")
quit()

        
