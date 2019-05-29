
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
UCOST=4
PRIZE=5
     #  x   y  atk m  hp
enemy=[[100,200,10, 5,600, 100]]
    #     x   y  Atk  range  upgrade cost
soldier=[400,350, 10, 150,   100 ]

enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]
hubRect=Rect(3,400,252,195)
upgradeRect=Rect(124,550,90,30)
money=400
font.init()
stencilFont1=font.SysFont("stencil",47)
stencilFont2=font.SysFont("stencil",20)
stencilFont3=font.SysFont("stencil",14)

soldierDisplay=False

upgradeCheck=False

def drawScene(enemy,defense):
    global soldierDisplay
    global upgradeCheck
    screen.fill(WHITE)
    for  i in range(len(enemy)):
        enemy[i][X]+=enemy[i][M]
        if enemy[i][X]<30 or enemy[i][X]>770:
            enemy[i][M]*=-1
    enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))] 
    for i in range(len(enemyRect)):
        draw.rect(screen,(255,140,209),enemyRect[i])
    draw.rect(screen,(45,123,189),(360,310,80,80)) #soldier x is starting pos of x+1/2 width, y is starting pos of y+1/2 length
    draw.rect(screen,BLACK,hubRect,2)
    draw.rect(screen,BLACK,upgradeRect,2)
    if upgradeRect.collidepoint(mx,my):
        if upgradeCheck:
            draw.rect(screen,GREEN,upgradeRect,2)
    screen.blit(stencilFont1.render("BARRACKS",True,(255,140,209)),(5,402))
    screen.blit(stencilFont2.render("ATTACK:",True,(255,140,209)),(8,462))
    screen.blit(stencilFont2.render("RANGE:",True,(255,140,209)),(8,502))
    screen.blit(stencilFont2.render("Upgrade?",True,(255,140,209)),(8,558))

    
    dist=sqrt((int(soldier[X])-mx)**2+(int(soldier[Y])-my)**2)
    if dist<=45:
        draw.circle(screen,BLACK,(int(soldier[X]),int(soldier[Y])),int(soldier[R]),2)
        if click:
            soldierDisplay=True
            upgradeCheck=True
            
    if soldierDisplay:
        screen.blit(stencilFont2.render("%2i"%(int(soldier[ATK])),True,(255,140,209)),(100,463))
        if upgradeCheck:
            screen.blit(stencilFont2.render(" -----> %2i"%(int(soldier[ATK])+5),True,(255,140,209)),(125,463))
        screen.blit(stencilFont2.render("%2i"%(soldier[R]),True,(255,140,209)),(100,503))
        try:
            screen.blit(stencilFont2.render("$%2i"%(soldier[UCOST]),True,(255,140,209)),(145,557))
        except:
            screen.blit(stencilFont2.render("NONE",True,(255,140,209)),(145,557))
        
    display.flip()
    
def upgrade(soldier):
    global money
    global upgradeCheck
    if upgradeRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,upgradeRect,2)
        if click:
            try:
                money-=int(soldier[UCOST])
                soldier[ATK]+=5
                del soldier[UCOST]
                upgradeCheck=False
                print("p e b n i s")
            except:
                pass

def checkRange(enemy,defense):
    global money
    enemyRect=[Rect(int(enemy[i][X]),int(enemy[i][Y]),30,30) for i in range(len(enemy))]
    for i in range(len(enemy)):
        dist=sqrt((int(soldier[X])-(enemyRect[i][0]+enemyRect[i][2]//2))**2+(int(soldier[Y])-(enemyRect[i][1]+enemyRect[i][3]//2))**2)
        #print(dist)
        #print(enemy[i][HP])
        if dist<=180:
            enemy[i][HP]-=soldier[2]
            if enemy[i][HP]<=0:
                money+=enemy[i][PRIZE]
                print(money)
                del enemy[i]


myglock=time.Clock()
running=True
while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click=True

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    drawScene(enemy,soldier)
    upgrade(soldier)
    checkRange(enemy,soldier)
    myglock.tick(10)
print("Chris is gay")
quit()




