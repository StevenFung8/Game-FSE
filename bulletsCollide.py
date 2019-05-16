#Range.py
from pygame import *
from math import *
from random import *
screen=display.set_mode((800,600))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)

MAXRAPID=10

rapid=MAXRAPID
guy=[100,300]
#targets=[]
#for i in range(5):
#    targets.append(Rect(randint(500,750),randint(100,500),40,40))
v=[5,0]#horiz and vertical speed
          #x   y vx vy
#bullets=[[170,45,2,1],[250,200,2,-1]] #this will be a 2D list
X=0
Y=1
ATK=2
M=3# movement of enemy
R=3
HP=4

     #  x   y  atk m  hp
enemy=[[100,200,10, 5,100]]

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
        if dist<=180:
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

        
