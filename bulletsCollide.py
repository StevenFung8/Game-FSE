
#graphicsTemplate.py   (sideShooter.py)
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
ER=5
     #  x   y  atk m  hp
enemy=[100,200,10, 5,100,False]

    #     x   y  Atk  range
soldier=[400,350, 5, 300]

bullets=[]


def drawScene(enemy,defense):
    enemy[X]+=enemy[M]
    if enemy[X]<30 or enemy[X]>770:
         enemy[M]*=-1
    
    screen.fill(WHITE)
    draw.circle(screen,(45,123,189),(int(soldier[X]),int(soldier[Y])),40)
    draw.rect(screen,BLACK,(int(soldier[X])-150,int(soldier[Y])-150,int(soldier[R]),int(soldier[R])),2)
    draw.rect(screen,(255,140,209),(int(enemy[X]),int(enemy[Y]),30,30))
    for b in bull:
        draw.circle(screen,GREEN,(b[0],b[1]),4)
    display.flip()

def checkRange(enemy,defense):
    enemy=Rect(int(enemy[X]),int(enemy[Y]),30,30)
    Range=Rect(int(soldier[X])-150,int(soldier[Y])-150,int(soldier[R]),int(soldier[R]))
    if enemy.colliderect(Range):
        enemy[ER]=True
    else:
        enemy[ER]=False
        #global dist
        #dist=sqrt((int(soldier[X])-int(enemy[X]))**2+(int(soldier[Y])-int(enemy[Y]))**2)

def moveBullets(bull):
    for b in bull:
        b[0]+=b[2]#horiz movement
        b[1]+=b[3]#vert movement
    

        
def collideBullets(enemy,defense):
    enemy=Rect(int(enemy[X]),int(enemy[Y]),30,30)
    Range=Rect(int(soldier[X])-150,int(soldier[Y])-150,int(soldier[R]),int(soldier[R]))
    if enemy.colliderect(Range):
        dist=sqrt((int(soldier[X])-int(enemy[X]))**2-(int(soldier[Y])-int(enemy[Y])))
myglock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
    def drawScene(enemy,defense):
        enemy[X]+=enemy[M]
        if enemy[X]<30 or enemy[X]>770:
            enemy[M]*=-1
    
        screen.fill(WHITE)
        draw.circle(screen,(45,123,189),(int(soldier[X]),int(soldier[Y])),40)
        draw.rect(screen,BLACK,(int(soldier[X])-150,int(soldier[Y])-150,int(soldier[R]),int(soldier[R])),2)
        draw.rect(screen,(255,140,209),(int(enemy[X]),int(enemy[Y]),30,30))
        display.flip()

    def collideBullets(enemy,defense):
        enemy=Rect(int(enemy[X]),int(enemy[Y]),30,30)
        Range=Rect(int(soldier[X])-150,int(soldier[Y])-150,int(soldier[R]),int(soldier[R]))
        if enemy.colliderect(Range):
            dist=sqrt((int(soldier[X])-int(enemy[X]))**2-(int(soldier[Y])-int(enemy[Y])))
            
    checkRange(enemy,soldier)
    moveBullets(bullets)
    drawScene(enemy,soldier)
    myglock.tick(40)
print("Chris is fuckign gay")
quit()

        
