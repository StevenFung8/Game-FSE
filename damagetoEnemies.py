from time import *
from pygame import *
from math import *
from random import *
from tkinter import *
width=1050
height=750
screen=display.set_mode((width,height))

RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
pathCol=(128,128,128,255)
pathCol2=(129,128,124,255)
init()
map1=image.load("FSE-Assets/Maps/map1.jpg")
deadSoldier=image.load("FSE-Assets/enemies/dead.png")

boomPics=[]
for i in range(28):
    boomPics+=[image.load("FSE-Assets/bomb wait/images\\Explode-05_frame_"+str(i)+".gif")]

class towerType:

    def __init__(self,name,damage,price,upgrade,uCost):
        self.name=name
        self.damage=damage
        self.price=price
        self.upgrade=upgrade
        self.uCost=uCost
        self.filename="FSE-Assets/Defenses/"+name+".png"

antiTank=towerType('antiTank',80,800,False,300)
bunker=towerType('bunker',100,1000,False,350)
fortress=towerType('fortress',150,1250,False,450)
heavyGun=towerType('heavyGun',200,1500,False,500)
heavyMG=towerType('heavyMG',35,500,False,200)
soldier=towerType('soldier',25,250,False,150)

class enemyType:

    def __init__(self,name,speed,health,damage):
        self.name=name
        self.speed=speed
        self.health=health
        self.damage=damage
        self.filename="FSE-Assets/Enemies/"+name+".png"

infantry=enemyType('infantry',1.5,200,5)
transport=enemyType('transport',1.7,400,5)
motorcycle=enemyType('motorcycle',2,250,10)
lightTank=enemyType('lightTank',1,700,15)
heavyTank=enemyType('heavyTank',0.7,1000,20)

#fonts

comicSans40=font.SysFont("Comic Sans MS",40)
stencil20=font.SysFont("Stencil",20)
stencil40=font.SysFont("Stencil",40)

def genEnemies(enemy):
    global pics
    DELAY=2
    pics=[]
    '''
    for i in range(len(enemyList)):
        enemyList[i][DELAY]=30
        print(enemyList[i][DELAY])
        if enemyList[i][DELAY]>0:
            enemyList[i][DELAY]-=1
        if enemyList[i][DELAY]==0:
            enemy.append(enemyList[i])
            enemyList.remove(enemyList[i])
    '''
    for i in enemy:
        img=[]
        img.append(image.load(i[4].filename))
        img.append(transform.rotate(image.load(i[4].filename),-90))
        img.append(transform.rotate(image.load(i[4].filename),-270))
        img.append(transform.rotate(image.load(i[4].filename),-180))
        pics.append(img)
    
def moveEnemy(screen,enemy):
    count=-1
    for i in enemy:
        if i[0]<220:
            i[0]+=i[4].speed
            i[3]=0
        if i[0]>=220 and i[1]<420:
            i[1]+=i[4].speed
            i[3]=1
        if i[1]>=410:
            i[0]+=i[4].speed
            i[3]=0
        count+=1
        screen.blit(pics[count][i[3]],i[:2])

    display.flip()

def bombAnimation(screen,bombs):
    for bomb in bombs:
        screen.blit(boomPics[bomb[3]],bomb[:2])

def advanceBombs(bombs):
    for bomb in bombs[:]:
        bomb[2]+=1
        if bomb[2]>90 and bomb[2]%5==0:
            bomb[3]+=1
            if bomb[3]==28:
                bombs.remove(bomb)

def damageCollide(screen,defenses,enemy):
    screen.blit(image.load(defenses[0].filename),(600,500))
    rangeRect=(525,425,200,200)
    draw.rect(screen,RED,rangeRect,3)
    enemyRect=[Rect(int(enemy[i][0]-100),int(enemy[i][1]-100),125,125) for i in range(len(enemy))]
    for i in enemy:
        if enemyRect[i].colliderect(rangeRect):
            enemy[i][5]-=defenses[4].damage
        if enemy[i][5]<=0:
            enemy.remove(enemy[i])
    
def baseHealth(enemy):
    blackHeart=image.load("FSE-Assets/blackHeart.png")
    blackHeart=transform.scale(blackHeart,(25,25))
    screen.blit(blackHeart,(940,350))
    bars=100
    count=0
    draw.rect(screen,BLACK,(944,374,102,12),0)
    for i in enemy:
        if i[0]>=900:
            bars-=i[4].damage
            if bars<=0:
                bars=0
    
    baseHealth=stencil20.render(str(bars),True,BLACK)
    screen.blit(baseHealth,(965,353))
    draw.rect(screen,RED,(1044,375,bars-100,10),0)
    draw.rect(screen,GREEN,(945,375,bars,10),0)

    if bars==0:
        draw.rect(screen,RED,(945,375,100,10),0)
        endScreen=Surface((width,height),SRCALPHA)
        endScreen.fill((220,220,220,127))
        screen.blit(endScreen,(0,0))
        youLost=stencil40.render("GAME OVER",True,BLACK)
        screen.blit(youLost,(400,350))
           
def healthBars(enemy):
    for i in enemy:
        draw.rect(screen,BLACK,(i[0]+14,i[1]-11,52,9),0)
        draw.rect(screen,GREEN,(i[0]+15,i[1]-10,50,7),0)
        
def drawScene(screen):
    screen.blit(map1,(0,0))
    
        #[x,y,DELAY,FRAME,className]
#enemy=[]
enemy=[[-100,190,0,0,infantry,infantry.health],[-160,190,0,0,infantry,infantry.health]]
defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    genEnemies(enemy)
            
    moveEnemy(screen,enemy)
    drawScene(screen)
    baseHealth(enemy)
    healthBars(enemy)
    damageCollide(screen,defenses,enemy)
    
    myclock.tick(60)

quit()

