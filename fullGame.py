#mainGame
from pygame import *
from math import *
from random import *

#basic colours
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)

init()
#load pictures
mainMenu=image.load("FSE-Assets/mainscreen.jpg")
credMenu=image.load("FSE-Assets/credits.jpg")
instructMenu=image.load("FSE-Assets/instructions.jpg")
levelSelectMenu=image.load("FSE-Assets/levelSelect.jpg")
cross=image.load("FSE-Assets/cross.png")
hudimg=image.load("FSE-Assets/hud.jpg")
hudRect=image.load("FSE-Assets/hudRect.png")
readyPic=image.load("FSE-Assets/readyRect.jpg")
quitP=image.load("FSE-Assets/quitRect.png")
dialogueP=image.load("FSE-Assets/dialogueRect.png")
cancelPic=image.load("FSE-Assets/cancelRect.png")
deletePic=image.load("FSE-Assets/deleteRect.png")
mutePic=image.load("FSE-Assets/musicPicMUTE.png")
eigthNote=image.load("FSE-Assets/musicPic.png")
blackHeart=image.load("FSE-Assets/blackHeart.png")
loseRect=image.load("FSE-Assets/loseRect.png")
pressToStart=image.load("FSE-Assets/previews/pushtostart.png")
muzzleFlash=image.load("FSE-Assets/muzzleFlash.png")
wreck=image.load("FSE-Assets/wreckage.png")
dead=image.load("FSE-Assets/enemies/dead.png")
victoryRect=image.load("FSE-Assets/victoryRect.png")
sureRect=image.load("FSE-Assets/sureRect.png")
finalLevel=image.load("FSE-Assets/finalLevel.png")

txtFont=font.SysFont("FSE-Assets/fonts/kremlin.ttf",25)
txtFont2=font.SysFont("Stencil",17)
txtFont3=font.SysFont("Stencil",20)
txtFont4=font.SysFont("Stencil",35)

#loading map previews
pr1=image.load("FSE-Assets/previews/lvl1prev.jpg")
pr2=image.load("FSE-Assets/previews/lvl2prev.jpg")
pr3=image.load("FSE-Assets/previews/lvl3prev.jpg")
pr4=image.load("FSE-Assets/previews/lvl4prev.jpg")
pr5=image.load("FSE-Assets/previews/lvl5prev.jpg")

#loading maps
map1=image.load("FSE-Assets/Maps/map1.jpg")
map2=image.load("FSE-Assets/Maps/map2.jpg")
map3=image.load("FSE-Assets/Maps/map3.jpg")
map4=image.load("FSE-Assets/Maps/map4.jpg")
map5=image.load("FSE-Assets/Maps/map5.jpg")

#transform pictures
hud=transform.scale(hudimg,(500,75))
hudRects=transform.scale(hudRect,(200,95))
quitPic=transform.scale(quitP,(150,40))
crossPic=transform.scale(cross,(30,30))
dialoguePic=transform.scale(dialogueP,(400,110))
blackHeart=transform.scale(blackHeart,(25,25))
mutePic=transform.scale(mutePic,(37,35))
eigthNote=transform.scale(eigthNote,(37,35))

#sounds
mixer.init()
place_sound = mixer.Sound("FSE-Assets/sound/placeSound.wav")
gun_sound = mixer.Sound("FSE-Assets/sound/gunShot.wav")
cannon_sound = mixer.Sound("FSE-Assets/sound/gunShotCannon.wav")
remove_sound = mixer.Sound(("FSE-Assets/sound/removeSound.wav"))
explosion_sound = mixer.Sound(("FSE-Assets/sound/explosion.wav"))

money=0 #the starting amount of money you have 
score=0 #your starting score 
pause=False #if the music is paused or not, starts off paused.

#this is the first class which defines all the characteristics of each enemy troop
class enemyType:

    def __init__(self,name,speed,health,damage,prize):
        self.name=name #name of the enemy troop 
        self.speed=speed #the speed at which the enemy troop travel downs the path 
        self.health=health #the health of the enemy 
        self.damage=damage #the amount of damage the troop does to the base when it reaches the end of the path  
        self.prize=prize #the amount of money you get when you kill a enemy troop 
        self.filename="FSE-Assets/Enemies/"+name+".png" #the name to load the picture into the game 

infantry=enemyType('infantry',2,200,5,40) #so these are all the properties of the troops 
transport=enemyType('transport',2.5,400,10,50) #for example, 'transport' has a speed of 1.7, 400 health, does 10 damage to the base, and you get 175 dollars if you kill it 
motorcycle=enemyType('motorcycle',3,250,10,75)
lightTank=enemyType('lightTank',1.7,700,15,100)
heavyTank=enemyType('heavyTank',1.5,1000,20,200)
tankDestroyer=enemyType('tankDestroyer',1.3,1100,25,300)

class towerType: #this is the class that defines all the properties for the towers 

    def __init__(self,name,damage,price,uCost,refund,delay):
        self.name=name #this is the name of the tower 
        self.damage=damage #this is the amount of damage the tower would do to the enemy troop 
        self.price=price #how much it costs to get this tower
        self.uCost=uCost #how much money it takes to upgrade the towers 
        self.refund=refund #how much money you get if you refund the tower 
        self.delay=delay #the rate of fire of the tower (ie. the heaveMG would attack faster than the antitank)
        self.filename="FSE-Assets/Defenses/"+name+".png" #the file path to load the picture into the game 
 
antiTank=towerType('antiTank',80,800,350,400,40) #so these are all the properties for the towers 
bunker=towerType('bunker',25,1000,450,500,10) #for example the 'bunker' would deal 30 damage to troops, cost 1000 dollars, cost 450 to upgrade, you get 500 if you refund it, and it fires every 10 ticks 
fortress=towerType('fortress',100,1250,600,625,50)
heavyGun=towerType('heavyGun',150,1500,700,750,50)
heavyMG=towerType('heavyMG',6.3,500,200,250,5)
soldier=towerType('soldier',25,250,100,125,20)

def genEnemies(enemy): #this function loads all the images for the enemy troops for each level 
    global pics #list that contains the pictures of the troops for each level
    global deadPics #list that contains the pictures of the troops when they die for each level 
    pics=[]
    deadPics=[]
    for i in enemy: #for every enemy in each level 
        img=[]
        img.append(image.load(i[3].filename)) #the original picture (i[3] is the name of the troop )
        img.append(transform.rotate(image.load(i[3].filename),-90)) #the picture but rotated 90 degress for when its going down the path
        img.append(transform.rotate(image.load(i[3].filename),-270)) #the picture but rotated 270 for when its going up the path 
        img.append(transform.rotate(image.load(i[3].filename),-180))#the picture but rotated 180 for when its going left of the path
        pics.append(img) #append the list into the pics list to make a 2D list
        #this makes it so that the first index of img is the image facing the right, second is down, third is up, and fourth is left
    for i in enemy:
        img=[]
        if i[3]==infantry:
            img.append(dead)
            img.append(transform.rotate(dead,-90))
            img.append(transform.rotate(dead,-270))
            img.append(transform.rotate(dead,-180))
            deadPics.append(img)
        else:
            img.append(wreck)
            img.append(transform.rotate(wreck,-90))
            img.append(transform.rotate(wreck,-270))
            img.append(transform.rotate(wreck,-180))
            deadPics.append(img)
    return pics #outputs the pics list 

def healthBars(enemy):
    for i in enemy: #for all enemy troops in the level
        if i[5]==False: #if the troop is not dead 
            draw.rect(screen,BLACK,(i[0]+14,i[1]-11,i[3].health/10+2,9),0) #the outline of the healthbar, the length of the black bar is determined by starting health of the troop
            draw.rect(screen,GREEN,(i[0]+15,i[1]-10,i[4]/10,7),0) #the actual health of the troop, starts full, and the length decreases as the health goes down by taking the current
            #health of the troop and dividing it by 10 

def moneyScore(screen): #function to blit the amoount of money you have and the score you currently have 
    global money #global variable of money
    global activeDefenses 
    global score
    txtMoney=txtFont.render("$"+str(money),True,RED) #renders the amount of money you have 
    txtScore=txtFont.render(str(score),True,RED) #renders the score 
    screen.blit(txtMoney,(100,30))
    screen.blit(txtScore,(110,84))

def baseHealth(enemy,enemy2):
    global gameOver #if health goes to zero
    global ready,ready2
    screen.blit(blackHeart,(940,350))
    bars=100 #starting health of the base 
    count=0
    draw.rect(screen,BLACK,(944,374,102,12),0) #draws the outline of the health bar 
    for i in enemy: #for every enemy in the level
        if i[0]>=900: #if the enemy reaches the base
            if i[5]==False: #If they are not dead
                bars-=i[3].damage #subtract the health of the base by the damage that they deal (defined in the enemyType class)
            if i[5]==True and i[0]>=1100: #makes sure if the enemy is off the screen and becomes "dead" in-game, the damage done to the base is still applied
                bars-=i[3].damage
            if bars<=0: #if it goes negative, set it back to zero
                mixer.Sound.play(explosion_sound)
                bars=0
        if i[0]>=1100: #if the enemy passes through the base, its job is done, so it becomes "dead", though it was never killed by a tower
            i[5]=True

    for i in enemy2:  #same thing but with the second wave of enemies
        if i[0]>=900: 
            if i[5]==False: 
                bars-=i[3].damage 
            if i[5]==True and i[0]>=1100: 
                bars-=i[3].damage
            if bars<=0: 
                mixer.Sound.play(explosion_sound)
                bars=0
        if i[0]>=1100: 
            i[5]=True
            
    baseHealth=txtFont3.render(str(bars),True,BLACK) #renders the health beside the black heart
    screen.blit(baseHealth,(965,353))
    draw.rect(screen,RED,(1044,375,bars-100,10),0) #blits a red rectangle, and the length will be start at 0, because bars starts a 100, and as bars goes up, negative number is the length
    draw.rect(screen,GREEN,(945,375,bars,10),0) #the green rect, starts with a length of 100 and decreases as the health goes down (length is dependant to health)
    if bars==0: #when bars is zero (no health), starts the gameOver function 
        gameOver=True

def music(state): #this function is used to toggle the music (mute and unmute)

    global pause #the variable to control the toggle
    global current #to determine what screen is on right now 
    if current=="main": #if its the main menu, the position of the mute rect is different
        muteRect=Rect(870,650,50,50)
        screen.blit(eigthNote, (875,655))
    else: #if its not the main menu, its at another spot
        muteRect = Rect(420, 25, 40, 40)
        screen.blit(eigthNote, (420, 27))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if state is not None: #this only starts if mouse is being pressed down

        if state: #if state is true
            if muteRect.collidepoint(mx, my) and pause == False: #if i press it and music is playing, it would pause it
                pause = True
                mixer.music.pause()
            elif muteRect.collidepoint(mx, my) and pause == True: #if i press it and the music is paused, it woudl play it again
                pause = False
                mixer.music.unpause()


    if pause: #if the music is paused, it needs to blit the paused music image
        if current=="main": #main menu location is different from the position in the levels 
            screen.blit(mutePic,(875,655))
        else:
            screen.blit(mutePic, (421, 27))

    if muteRect.collidepoint(mx,my): #if the mouse is over the rect, highlight it yellow
        draw.rect(screen, YELLOW, muteRect, 3)
    else:
        draw.rect(screen, RED, muteRect, 3)

def moveEnemy(screen,enemy): #for each level, when a enemy troop reaches the end of a path, it needs to know to turn, and this is what the function is used for 
    count=-1 #counter for number of enemies in the list
    for i in enemy:
        i[7]-=1
        if i[5]==False and i[7]<=0:
            if i[0]<220: #for the first section of the path, if it doesn't hit the end of the path, the enemy troop will move at a constant speed defined in the enemyType class
                i[0]+=i[3].speed
                i[2]=0 # i[2] is the 'frame' part of the 2D list, and it defines the frame that is needed for this section of the path. I this case, the frame needed is the troop facing right
            if i[0]>=220 and i[1]<420: #this is the second section of the path, the path that goes down, and it will move at a constant speed 
                i[1]+=i[3].speed
                i[2]=1 #the frame needed here is the one that faces down, so i[2] changes to 1 
            if i[1]>=410: #third section of the path, and it will travel at a constant speed
                i[0]+=i[3].speed
                i[2]=0 #the frame changes back to the troop facing to the right 
        count+=1 #counter for each enemy in the enemy list, and adds one for each enemy
        if i[5]==False and i[7]<=0: #if troops are not dead and their delay is less than zero
            screen.blit(pics[count][i[2]],i[:2]) #blits all the pictures needed, pics[count][i[2]] is the image and what rotation is needed, and i[:2] is the point at where you shoudl blit it
        if i[5]==True and i[0]<=1100:
            screen.blit(deadPics[count][i[2]],(i[0],i[1]+15))


def moveEnemy2(screen,enemy): #this is for the second level, because the path is different for each level, enemies must move different 
    count=-1 #counter for number of eneimes in the list 

    check1=Rect(300,220,65,350) #each section of the path has a rect, so when the enemy troop collides with the rect, it will turn the enemy troop 
    check2=Rect(300,155,365,65)
    check3=Rect(665,210,65,230)
    check4=Rect(665,440,900,65)

    for i in enemy:
        i[7]-=1
        if i[5]==False and i[7]<=0:
            if i[0]<300:
                i[0]+=i[3].speed
                i[2]=0
            if check1.collidepoint(i[0],i[1]):
                i[1]-=i[3].speed
                i[2]=2
            if check2.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0
            if check3.collidepoint(i[0],i[1]):
                i[1]+=i[3].speed
                i[2]=1
            if check4.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0

        count+=1
        if i[5]==False and i[7]<=0:
            screen.blit(pics[count][i[2]],i[:2])
        if i[5]==True and i[0]<=1100:
            screen.blit(deadPics[count][i[2]],(i[0],i[1]+15))

def moveEnemy3(screen,enemy):
    count=-1
    for i in enemy:
        i[7]-=1
        if i[5]==False and i[7]<=0:
            if i[0]<370:
                i[0]+=i[3].speed
                i[2]=0
            if i[0]>=370 and i[1]>=220:
                i[1]-=i[3].speed
                i[2]=2
            if i[1]<=220:
                i[0]+=i[3].speed
                i[2]=0

        count+=1
        if i[5]==False and i[7]<=0:
            screen.blit(pics[count][i[2]],i[:2])
        if i[5]==True and i[0]<=1100:
            screen.blit(deadPics[count][i[2]],(i[0],i[1]+15))

def moveEnemy4(screen,enemy):
    count=-1

    check1=Rect(230,280,60,280)
    check2=Rect(230,560,360,60)
    check3=Rect(590,330,60,300)
    check4=Rect(590,270,900,60)

    for i in enemy:
        i[7]-=1
        if i[5]==False and i[7]<=0:
            if i[0]<230:
                i[0]+=i[3].speed
                i[2]=0
            if check1.collidepoint(i[0],i[1]):
                i[1]+=i[3].speed
                i[2]=1
            if check2.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0
            if check3.collidepoint(i[0],i[1]):
                i[1]-=i[3].speed
                i[2]=2
            if check4.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0

        count+=1
        if i[5]==False and i[7]<=0:
            screen.blit(pics[count][i[2]],i[:2])
        if i[5]==True and i[0]<=1100:
            screen.blit(deadPics[count][i[2]],(i[0],i[1]+15))
            
def moveEnemy5(screen,enemy):
    count=-1
    check1=Rect(100,260,327,50)
    check2=Rect(427,260,50,235)
    check3=Rect(427,495,900,50)

    for i in enemy:
        i[7]-=1
        if i[5]==False and i[7]<=0:
            if i[1]<260:
                i[1]+=i[3].speed
                i[2]=1
            if check1.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0
            if check2.collidepoint(i[0],i[1]):
                i[1]+=i[3].speed
                i[2]=1
            if check3.collidepoint(i[0],i[1]):
                i[0]+=i[3].speed
                i[2]=0

        count+=1
        if i[5]==False and i[7]<=0:
            screen.blit(pics[count][i[2]],i[:2])
        if i[5]==True and i[0]<=1100:
            screen.blit(deadPics[count][i[2]],(i[0],i[1]+15))

def drawScene1(screen):
    screen.blit(map1,(0,0))
def drawScene2(screen):
    screen.blit(map2,(0,0))
def drawScene3(screen):
    screen.blit(map3,(0,0))
def drawScene4(screen):
    screen.blit(map4,(0,0))
def drawScene5(screen):
    screen.blit(map5,(0,0))

def hudElements(screen):
    screen.blit(hud,(550,20))
    screen.blit(hudRects,(20,20))
    screen.blit(dialoguePic,(600,600))

defC=None
ready=False
ready2=False
gameOver=False
activeDefenses=[]

def prep(screen,towerPos):
    global defC,money,ready,ready2,click,wave
    
    readyRect=Rect(830,120,179,69)
    upgradeRect=Rect(750,662,70,30)
    buyRects=[Rect(607,28,59,63),Rect(682,28,61,63),Rect(758,28,61,63),Rect(834,28,61,63),Rect(908,28,61,63),Rect(982,28,61,63)]
    cancelRect=Rect(20,125,125,30)

    txtD1=txtFont2.render("Basic Soldier - Cost: $250, Damage: 25",True,BLACK)
    txtD2=txtFont2.render("Machine Gun - Cost: $500, Damage: 35",True,BLACK)
    txtD3=txtFont2.render("Anti-Tank Gun - Cost: $800, Damage: 80",True,BLACK)
    txtD4=txtFont2.render("Bunker - Cost: $1000, Damage: 100",True,BLACK)
    txtD5=txtFont2.render("Fortress - Cost: $1250, Damage: 150",True,BLACK)
    txtD6=txtFont2.render("Heavy AT Gun - Cost: $1500, Damage: 200",True,BLACK)

    txtS1=txtFont2.render("Basic Soldier - Damage:",True,BLACK)
    txtS2=txtFont2.render("Machine Gun - Damage:",True,BLACK)
    txtS3=txtFont2.render("Anti-Tank Gun - Damage:",True,BLACK)
    txtS4=txtFont2.render("Bunker - Damage:",True,BLACK)
    txtS5=txtFont2.render("Fortress - Damage:",True,BLACK)
    txtS6=txtFont2.render("Heavy AT Gun - Damage:",True,BLACK)
    towerDescription=[txtD1,txtD2,txtD3,txtD4,txtD5,txtD6]
    towerStats=[txtS1,txtS2,txtS3,txtS4,txtS5,txtS6]

    ##generating defense images/sounds
    defenses=[soldier,heavyMG,antiTank,bunker,fortress,heavyGun]
    defensePics=[]
    for i in defenses:
        defensePics.append(image.load(i.filename))
    sounds=[gun_sound,gun_sound,cannon_sound,gun_sound,gun_sound,cannon_sound]

    draw.rect(screen,RED,readyRect,2)
    screen.blit(readyPic,(830,120))
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if readyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,0),readyRect,2)
        if click and wave=="first": #checks what wave is coming up next
            ready=True #changes the first wave's "ready" variable

    if readyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,0),readyRect,2)
        if click and wave=="second": #checks if the second wave is coming
            ready2=True #changes the 2nd wave's "ready" variable

    for i in range(len(buyRects)):
        if buyRects[i].collidepoint(mx,my):
            draw.rect(screen,YELLOW,buyRects[i],2)
            if click:
                defC=int(i)

    if defC!=None:
        draw.rect(screen,GREEN,buyRects[defC],2)
        screen.blit(towerDescription[defC],(620,630))
        cancelRect=Rect(20,125,125,30)
        screen.blit(cancelPic,(20,125))

        #money and stuff
        for i in range(len(towerPos)):
            if towerPos[i][1]==False:
                draw.rect(screen,RED,towerPos[i][0],3)
                if towerPos[i][0].collidepoint(mx,my):
                    draw.rect(screen,YELLOW,towerPos[i][0],3)
                    if click and money-defenses[defC].price>=0:
                        mixer.Sound.play(place_sound)
                                                #tower picture, blit position,  tower class variable, tower position index, damage, upgrade cost, delay counter, delay, sound type
                        activeDefenses.append([defensePics[defC],towerPos[i][2],defenses[defC],towerPos[i][4],int(defenses[defC].damage),defenses[defC].uCost,0,defenses[defC].delay,sounds[defC]])
                        money-=defenses[defC].price
                        towerPos[i][1]=True
                        towerPos[i][5]=defC
                    if money-defenses[defC].price<0:
                        noMoney = txtFont2.render("Not enough money for this tower.", True, RED)
                        screen.blit(noMoney,(620,660))

        if cancelRect.collidepoint(mx,my):
            draw.rect(screen,RED,cancelRect,2)
            if click:
                defC=None

    #This is the tower edit program - selecting, upgrade, delete

    select=False #select checks if a tower is already selected. If a tower is selected already, select prohibits the player from choosing another tower
    if defC==None: #no tower is selected
        select=True #the played can select a tower while true
        for i in towerPos:
            if i[0].collidepoint(mx,my) and i[1]==True and select==True: #if the player hovers over a tower space,there is a tower, and the player has not
                print(i[1],select)
                draw.rect(screen,YELLOW,i[0],3)                          #selected a tower yet, the space will be highlighted
                if click:   
                    i[3]=True   #the tower can be edited if the player clicks on it.
                    
            if i[3]:
                select=False  #while a tower is selected, the player cannot select another until they choose cancel
                draw.rect(screen,GREEN,buyRects[i[5]],2) #highlights the tower
                screen.blit(towerStats[i[5]],(620,630)) #this will blit the individual tower's damage
                
                txtUpgrade=txtFont2.render("UPGRADE?",True,BLACK)
                draw.rect(screen,BLACK,upgradeRect,2)
                for a in activeDefenses: #checks all active towers
                    if a[1]==i[2]: #checks which active tower is on the selected tower space
                        damageDes=txtFont2.render("%i"%(a[4]),True,BLACK) #the individual tower's attack is a[4]
                        screen.blit(damageDes,(850,630))
                        if type(a[5])==int: #if upgraded, a[5] will be None - not an int value
                            txtuCost=txtFont2.render("$%i"%(a[5]),True,BLACK) #price of upgrade
                        else:
                            txtuCost=txtFont2.render(a[5],True,BLACK) #will blit nothing

                        if upgradeRect.collidepoint(mx,my): 
                            if type(a[5])==int:
                                draw.rect(screen,GREEN,upgradeRect,2) #will highlight upgradeRect when hovered over and if the tower has not been upgraded
                                if click:
                                    mixer.Sound.play(place_sound)
                                    a[4]+=10*(i[5]+1) #increasing the attack
                                    a[5]=None  #once upgraded, the upgrade cost will be nothing
                                    if money-defenses[i[5]].uCost>=0: #will only upgrade if the player has enough money
                                        money-=defenses[i[5]].uCost

                cancelRect=Rect(20,125,125,30)
                
                screen.blit(txtUpgrade,(650,670))
                screen.blit(txtuCost,(763,670))
                screen.blit(cancelPic,(20,125))

                cancelRect=Rect(20,125,125,30) #rect for cancelling a tower selection
                deleteRect=Rect(20,160,125,30) #rect for deleting an active tower
                draw.rect(screen,GREEN,i[0],3)
                screen.blit(cancelPic,(20,125))
                screen.blit(deletePic,(20,160))

                if deleteRect.collidepoint(mx,my):
                    draw.rect(screen,RED,deleteRect,2)
                    if click:
                        mixer.Sound.play(remove_sound)
                        i[3]=False #when deleted, tower edit status reverts
                        i[1]=False #when deleted, the tower space goes empty
                        for a in activeDefenses:
                            if a[3]==i[4]: #checks which active tower was on the selected tower space
                                activeDefenses.remove(a) #deletes the tower from the active list
                                money+=a[2].refund #give back money 
                        #select=True #player can select a tower again
                        
                if cancelRect.collidepoint(mx,my):
                    draw.rect(screen,RED,cancelRect,2)
                    if click:
                        i[3]=False #tower edit status reverts
                        #select=True #player can select a tower again

def damageEnemies(enemy,activeDefenses,towerPos):
    global money,score
    for a in activeDefenses:
        flashList=list(towerPos[a[3]][2])
        for e in enemy:
            if towerPos[a[3]][6].collidepoint(e[0],e[1]) and e[5]==False:
                if a[6]==0:
                    mixer.Sound.play(a[8])
                    screen.blit(muzzleFlash,(flashList[0]-25,flashList[1]+13))
                    e[4]-=a[4]
                    a[6]=a[7]
                if a[6]>0:
                    a[6]-=1
            if e[4]<=0:
                e[5]=True
            if e[5]==True:
                money+=e[6]
                score+=e[6]
                e[6]=0


def victory(score):
    running=True
    mixer.music.load("FSE-Assets/sound/sovietTheme.mp3")
    mixer.music.play(-1)
    mainMenuRect=Rect(573,620,400,50)
    click=False
    finalScore = txtFont4.render(str(score), True, BLACK)
    while running:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(finalLevel,(13,17))
        screen.blit(finalScore,(830,302))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
            if evt.type==MOUSEBUTTONUP:
                click=False

        if mainMenuRect.collidepoint(mx,my):
            draw.rect(screen,BLACK,mainMenuRect,3)
            if mb[0]==1 and click==False:
                running=False

        display.flip()
    return "levelSelect"


def prev1():
    running=True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr1,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev1"

        display.flip()

def prev2():
    running=True
    mixer.music.load("FSE-Assets/sound/startMusic1.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr2,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev2"

        display.flip()

def prev3():
    running=True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr3,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev3"

        display.flip()

def prev4():
    running=True
    mixer.music.load("FSE-Assets/sound/startMusic1.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr4,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev4"

        display.flip()

def prev5():
    running=True
    mixer.music.load("FSE-Assets/sound/startMusic2.mp3")
    mixer.music.play(-1)
    pressRect=Rect(380,320,300,100)
    while running:
        screen.blit(pr5,(0,0))
        screen.blit(pressToStart,(380,320))
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if pressRect.collidepoint(mx,my):
            draw.rect(screen,RED,pressRect,3)
            if mb[0]==1:
                return "lev5"

        display.flip()

def lev1():
    global defC,ready,ready2,activeDefenses,money,score,click,gameOver,wave
    
    money=4500
    pause=False
    running=True
    myclock=time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)

    quitRect=Rect(260,25,150,40)

                #rect, status, blit position, edit status, rect, active tower #
                # subtract 91 from x,y, make 212 the length and width
    towerPos1=[[Rect(115,273,50,50),False,(115,273),False,0,None,Rect(5,162,160,100)],[Rect(264,114,50,50),False,(264,114),False,1,None,Rect(60,162,212,130)],
               [Rect(319,242,50,50),False,(319,242),False,2,None,Rect(190,131,212,230)],[Rect(217,529,50,50),False,(217,529),False,3,None,Rect(126,400,212,212)],
               [Rect(388,342,50,50),False,(388,342),False,4,None,Rect(297,251,212,212)],[Rect(570,342,50,50),False,(570,342),False,5,None,Rect(479,251,212,212)],
               [Rect(750,342,50,50),False,(750,342),False,6,None,Rect(659,251,212,212)],[Rect(418,503,50,50),False,(418,503),False,7,None,Rect(327,412,212,212)],
               [Rect(598,503,50,50),False,(598,503),False,8,None,Rect(507,412,212,212)],[Rect(778,503,50,50),False,(778,503),False,9,None,Rect(688,412,212,212)]]
    
            #x,y,frame,enemy type,health,death status, prize, delay
    enemy=[[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,30],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,90],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,150],
           [-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,210],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,270],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,330],
           [-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,390],[-100,190,0,transport,transport.health,False,transport.prize,450],[-100,190,0,transport,transport.health,False,transport.prize,530],
           [-100,190,0,transport,transport.health,False,transport.prize,610],[-100,190,0,transport,transport.health,False,transport.prize,700],[-100,190,0,transport,transport.health,False,transport.prize,780],
           [-100,190,0,infantry,infantry.health,False,infantry.prize,820],[-100,190,0,infantry,infantry.health,False,infantry.prize,880],[-100,190,0,infantry,infantry.health,False,infantry.prize,940],[-100,190,0,infantry,infantry.health,False,infantry.prize,1000],
           [-100,190,0,infantry,infantry.health,False,infantry.prize,1060],[-100,190,0,infantry,infantry.health,False,infantry.prize,1120],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1200],
           [-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1320],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1440],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1560],
           [-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1680]] #1st wave
    
    enemy2=[[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,30],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,90],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,150],
           [-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,210],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,270],[-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,330],
           [-100,190,0,motorcycle,motorcycle.health,False,motorcycle.prize,390],[-100,190,0,transport,transport.health,False,transport.prize,450],[-100,190,0,transport,transport.health,False,transport.prize,530],
           [-100,190,0,transport,transport.health,False,transport.prize,610],[-100,190,0,transport,transport.health,False,transport.prize,700],[-100,190,0,transport,transport.health,False,transport.prize,780],
           [-100,190,0,infantry,infantry.health,False,infantry.prize,820],[-100,190,0,infantry,infantry.health,False,infantry.prize,880],[-100,190,0,infantry,infantry.health,False,infantry.prize,940],[-100,190,0,infantry,infantry.health,False,infantry.prize,1000],
           [-100,190,0,infantry,infantry.health,False,infantry.prize,1060],[-100,190,0,infantry,infantry.health,False,infantry.prize,1120],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1200],
           [-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1320],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1440],[-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1560],
           [-100,190,0,lightTank,lightTank.health,False,lightTank.prize,1680]] #2nd wave
    
    click=False
    wave="first"
    while running:
        myclock.tick(60)
        drawScene1(screen)
        hudElements(screen)
        moneyScore(screen)
        baseHealth(enemy,enemy2)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evt.type==MOUSEBUTTONUP:
                click=False
        music(None)
        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                pause=True

        if pause==True:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(sureRect,(335,235))
            returnRect=Rect(465,375,140,35)
            leaveRect=Rect(435,425,205,35)
            if returnRect.collidepoint(mx,my):
                draw.rect(screen,RED,returnRect,3)
                if mb[0]==1:
                    pause=False
            if leaveRect.collidepoint(mx,my):
                draw.rect(screen,RED,leaveRect,3)
                if mb[0]==1:
                    pause=False
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    score=0
                    return "levelSelect"

        if ready==False and pause==False and wave=="first": #checks if either ready variable is false, so it calls the prep functions
            prep(screen,towerPos1)
        if ready2==False and pause==False and wave=="second":
            prep(screen,towerPos1)
            

        if ready==True and gameOver==False and pause==False: #if the first ready variable is true, it will call the functions for the first enemy list
            genEnemies(enemy) #generating enemies
            moveEnemy(screen,enemy) #move
            healthBars(enemy)  #health bars
            damageEnemies(enemy,activeDefenses,towerPos1) #damage

        if ready2==True and gameOver==False and pause==False: #if the 2nd ready variable becomes true, it will call the game functions for the second enemy list
            genEnemies(enemy2)
            moveEnemy(screen,enemy2)
            healthBars(enemy2)
            damageEnemies(enemy2,activeDefenses,towerPos1)    

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(335,235))
            retryRect=Rect(365,415,128,50)
            mainRect=Rect(525,415,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)

            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
                    return "prev1"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1 and click==False:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
        
        count=0 #counter for the first enemy list
        for i in enemy: 
            if i[5]==True: #for each "dead" or enemy that passed through the base, the count will go up
                count+=1
            if count==len(enemy): #if the counter is the same as the length of the enemy list, it means all the enemies have either died
            #or passed over the base, signalling the end of the wave
                wave="second"  #changes the wave variable to the second wave
                ready=False #makes the first ready variable false

        #there are only 2 waves per level, so this is the final wave
        count2=0
        for i in enemy2:
            if i[5]==True:
                count2+=1
            if count2==len(enemy2): #signals the end of the game (all 2 waves cleared)
                endScreen=Surface((width,height),SRCALPHA)
                endScreen.fill((220,220,220,127))
                screen.blit(endScreen,(0,0))
                screen.blit(victoryRect,(320,225))
                redoRect=Rect(445,353,150,40)
                nextRect=Rect(410,404,217,40)
                if redoRect.collidepoint(mx,my):
                    draw.rect(screen,RED,redoRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev1"
                if nextRect.collidepoint(mx,my):
                    draw.rect(screen,RED,nextRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev2"

        display.flip()
    return "levelSelect"

def lev2():
    global defC,ready,ready2,activeDefenses,money,score,click,gameOver,wave
    money=6000

    running=True
    pause=False
    myclock=time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                # subtract 91 from x,y, make 212 the length and width
    towerPos2=[[Rect(75,430,50,50),False,(75,430),False,0,None,Rect(-26,339,212,212)],[Rect(210,430,50,50),False,(210,430),False,1,None,Rect(119,339,212,212)],
               [Rect(210,300,50,50),False,(210,300),False,2,None,Rect(119,209,212,212)],[Rect(225,125,50,50),False,(225,125),False,3,None,Rect(134,34,212,212)],
               [Rect(425,125,50,50),False,(425,125),False,4,None,Rect(334,34,212,212)],[Rect(600,125,50,50),False,(600,125),False,5,None,Rect(509,34,212,212)],
               [Rect(425,300,50,50),False,(425,300),False,6,None,Rect(334,209,212,212)],[Rect(560,300,50,50),False,(560,300),False,7,None,Rect(469,209,212,212)],
               [Rect(750,275,50,50),False,(750,275),False,8,None,Rect(659,184,212,212)],[Rect(825,375,50,50),False,(825,375),False,9,None,Rect(734,284,212,212)]]

    enemy=[[-100,510,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]] #1st wave
    enemy2=[[-100,510,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]]#2nd wave
    
    wave="first"
    click=False
    while running:
        myclock.tick(60)
        drawScene2(screen)
        hudElements(screen)
        moneyScore(screen)
        baseHealth(enemy,enemy2)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        music(None)

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                pause=True

        if pause==True:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(sureRect,(335,235))
            returnRect=Rect(465,375,140,35)
            leaveRect=Rect(435,425,205,35)
            if returnRect.collidepoint(mx,my):
                draw.rect(screen,RED,returnRect,3)
                if mb[0]==1:
                    pause=False
            if leaveRect.collidepoint(mx,my):
                draw.rect(screen,RED,leaveRect,3)
                if mb[0]==1:
                    pause=False
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    score=0
                    return "levelSelect"

        if ready==False and pause==False and wave=="first": #checks if either ready variable is false, so it calls the prep functions
            prep(screen,towerPos2)
        if ready2==False and pause==False and wave=="second":
            prep(screen,towerPos2)
            

        if ready==True and gameOver==False and pause==False: #if the first ready variable is true, it will call the functions for the first enemy list
            genEnemies(enemy) #generating enemies
            moveEnemy2(screen,enemy) #move
            healthBars(enemy)  #health bars
            damageEnemies(enemy,activeDefenses,towerPos2) #damage

        if ready2==True and gameOver==False and pause==False: #if the 2nd ready variable becomes true, it will call the game functions for the second enemy list
            genEnemies(enemy2)
            moveEnemy2(screen,enemy2)
            healthBars(enemy2)
            damageEnemies(enemy2,activeDefenses,towerPos2)    

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(335,235))
            retryRect=Rect(365,415,128,50)
            mainRect=Rect(525,415,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)

            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
                    return "prev2"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1 and click==False:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
        
        count=0 #counter for the first enemy list
        for i in enemy: 
            if i[5]==True: #for each "dead" or enemy that passed through the base, the count will go up
                count+=1
            if count==len(enemy): #if the counter is the same as the length of the enemy list, it means all the enemies have either died
            #or passed over the base, signalling the end of the wave
                wave="second"  #changes the wave variable to the second wave
                ready=False #makes the first ready variable false

        #there are only 2 waves per level, so this is the final wave
        count2=0
        for i in enemy2:
            if i[5]==True:
                count2+=1
            if count2==len(enemy2): #signals the end of the game (all 2 waves cleared)
                endScreen=Surface((width,height),SRCALPHA)
                endScreen.fill((220,220,220,127))
                screen.blit(endScreen,(0,0))
                screen.blit(victoryRect,(320,225))
                redoRect=Rect(445,353,150,40)
                nextRect=Rect(410,404,217,40)
                if redoRect.collidepoint(mx,my):
                    draw.rect(screen,RED,redoRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev2"
                if nextRect.collidepoint(mx,my):
                    draw.rect(screen,RED,nextRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev3"

        display.flip()
    return "levelSelect"

def lev3():
    global defC,ready,ready2,activeDefenses,money,score,click,gameOver,wave

    money=7000
    pause=False
    running=True
    myclock=time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                # subtract 91 from x,y, make 212 the length and width
    towerPos3=[[Rect(52,391,50,50),False,(52,391),False,0,None,Rect(-41,300,212,212)],[Rect(200,391,50,50),False,(200,391),False,1,None,Rect(109,300,212,212)],
               [Rect(190,563,50,50),False,(190,563),False,2,None,Rect(99,472,212,212)],[Rect(274,294,50,50),False,(274,294),False,3,None,Rect(183,203,212,212)],
               [Rect(274,136,50,50),False,(274,136),False,4,None,Rect(183,45,212,212)],[Rect(450,136,50,50),False,(450,136),False,5,None,Rect(359,45,212,212)],
               [Rect(575,136,50,50),False,(575,136),False,6,None,Rect(484,45,212,212)],[Rect(474,325,50,50),False,(474,325),False,7,None,Rect(383,134,212,212)],
               [Rect(630,305,50,50),False,(630,305),False,8,None,Rect(539,214,212,212)],[Rect(700,136,50,50),False,(700,136),False,9,None,Rect(609,45,212,212)],
               [Rect(755,305,50,50),False,(630,305),False,8,None,Rect(664,214,212,212)]]

    enemy=[[-100,480,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]]
    enemy2=[[-100,480,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]] #2nd wave
    
    wave="first"
    click=False
    while running:
        myclock.tick(60)
        drawScene3(screen)
        hudElements(screen)
        moneyScore(screen)
        baseHealth(enemy,enemy2)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        music(None)

        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                pause=True

        if pause==True:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(sureRect,(335,235))
            returnRect=Rect(465,375,140,35)
            leaveRect=Rect(435,425,205,35)
            if returnRect.collidepoint(mx,my):
                draw.rect(screen,RED,returnRect,3)
                if mb[0]==1:
                    pause=False
            if leaveRect.collidepoint(mx,my):
                draw.rect(screen,RED,leaveRect,3)
                if mb[0]==1:
                    pause=False
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    score=0
                    return "levelSelect"

        if ready==False and pause==False and wave=="first": #checks if either ready variable is false, so it calls the prep functions
            prep(screen,towerPos3)
        if ready2==False and pause==False and wave=="second":
            prep(screen,towerPos3)
            

        if ready==True and gameOver==False and pause==False: #if the first ready variable is true, it will call the functions for the first enemy list
            genEnemies(enemy) #generating enemies
            moveEnemy3(screen,enemy) #move
            healthBars(enemy)  #health bars
            damageEnemies(enemy,activeDefenses,towerPos3) #damage

        if ready2==True and gameOver==False and pause==False: #if the 2nd ready variable becomes true, it will call the game functions for the second enemy list
            genEnemies(enemy2)
            moveEnemy3(screen,enemy2)
            healthBars(enemy2)
            damageEnemies(enemy2,activeDefenses,towerPos3)    

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(335,235))
            retryRect=Rect(365,415,128,50)
            mainRect=Rect(525,415,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)

            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
                    return "prev3"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1 and click==False:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
        
        count=0 #counter for the first enemy list
        for i in enemy: 
            if i[5]==True: #for each "dead" or enemy that passed through the base, the count will go up
                count+=1
            if count==len(enemy): #if the counter is the same as the length of the enemy list, it means all the enemies have either died
            #or passed over the base, signalling the end of the wave
                wave="second"  #changes the wave variable to the second wave
                ready=False #makes the first ready variable false

        #there are only 2 waves per level, so this is the final wave
        count2=0
        for i in enemy2:
            if i[5]==True:
                count2+=1
            if count2==len(enemy2): #signals the end of the game (all 2 waves cleared)
                endScreen=Surface((width,height),SRCALPHA)
                endScreen.fill((220,220,220,127))
                screen.blit(endScreen,(0,0))
                screen.blit(victoryRect,(320,225))
                redoRect=Rect(445,353,150,40)
                nextRect=Rect(410,404,217,40)
                if redoRect.collidepoint(mx,my):
                    draw.rect(screen,RED,redoRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev3"
                if nextRect.collidepoint(mx,my):
                    draw.rect(screen,RED,nextRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev4"

        display.flip()
    return "levelSelect"

def lev4():
    global defC,ready,ready2,activeDefenses,money,score,click,gameOver,wave

    money=8500
    pause=False
    running=True
    myclock=time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                # subtract 91 from x,y, make 212 the length and width

    towerPos4=[[Rect(107,355,50,50),False,(107,355),False,0,None,Rect(16,264,212,212)],[Rect(193,190,50,50),False,(193,190),False,1,None,Rect(102,99,212,212)],
               [Rect(331,298,50,50),False,(331,298),False,2,None,Rect(240,207,212,212)],[Rect(331,423,50,50),False,(331,423),False,3,None,Rect(240,332,212,212)],
               [Rect(457,472,50,50),False,(457,472),False,4,None,Rect(366,381,212,212)],[Rect(241,647,50,50),False,(241,647),False,5,None,Rect(150,556,212,212)],
               [Rect(689,429,50,50),False,(689,429),False,6,None,Rect(598,338,212,212)],[Rect(495,260,50,50),False,(495,260),False,7,None,Rect(404,169,212,212)],
               [Rect(686,240,50,50),False,(686,240),False,8,None,Rect(595,149,212,212)],[Rect(820,409,50,50),False,(820,409),False,9,None,Rect(781,318,212,212)]]

    enemy=[[-100,280,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]]#1st wave
    enemy2=[[-100,280,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]] #2nd wave
    
    wave="first"
    while running:
        myclock.tick(60)
        drawScene4(screen)
        hudElements(screen)
        moneyScore(screen)
        baseHealth(enemy,enemy2)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        music(None)
        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                pause=True

        if pause==True:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(sureRect,(335,235))
            returnRect=Rect(465,375,140,35)
            leaveRect=Rect(435,425,205,35)
            if returnRect.collidepoint(mx,my):
                draw.rect(screen,RED,returnRect,3)
                if mb[0]==1:
                    pause=False
            if leaveRect.collidepoint(mx,my):
                draw.rect(screen,RED,leaveRect,3)
                if mb[0]==1:
                    pause=False
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    score=0
                    return "levelSelect"

        if ready==False and pause==False and wave=="first": #checks if either ready variable is false, so it calls the prep functions
            prep(screen,towerPos4)
        if ready2==False and pause==False and wave=="second":
            prep(screen,towerPos4)
            

        if ready==True and gameOver==False and pause==False: #if the first ready variable is true, it will call the functions for the first enemy list
            genEnemies(enemy) #generating enemies
            moveEnemy4(screen,enemy) #move
            healthBars(enemy)  #health bars
            damageEnemies(enemy,activeDefenses,towerPos4) #damage

        if ready2==True and gameOver==False and pause==False: #if the 2nd ready variable becomes true, it will call the game functions for the second enemy list
            genEnemies(enemy2)
            moveEnemy4(screen,enemy2)
            healthBars(enemy2)
            damageEnemies(enemy2,activeDefenses,towerPos4)    

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(335,235))
            retryRect=Rect(365,415,128,50)
            mainRect=Rect(525,415,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)

            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
                    return "prev4"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1 and click==False:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
        
        count=0 #counter for the first enemy list
        for i in enemy: 
            if i[5]==True: #for each "dead" or enemy that passed through the base, the count will go up
                count+=1
            if count==len(enemy): #if the counter is the same as the length of the enemy list, it means all the enemies have either died
            #or passed over the base, signalling the end of the wave
                wave="second"  #changes the wave variable to the second wave
                ready=False #makes the first ready variable false

        #there are only 2 waves per level, so this is the final wave
        count2=0
        for i in enemy2:
            if i[5]==True:
                count2+=1
            if count2==len(enemy2): #signals the end of the game (all 2 waves cleared)
                endScreen=Surface((width,height),SRCALPHA)
                endScreen.fill((220,220,220,127))
                screen.blit(endScreen,(0,0))
                screen.blit(victoryRect,(320,225))
                redoRect=Rect(445,353,150,40)
                nextRect=Rect(410,404,217,40)
                if redoRect.collidepoint(mx,my):
                    draw.rect(screen,RED,redoRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev4"
                if nextRect.collidepoint(mx,my):
                    draw.rect(screen,RED,nextRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev5"

        display.flip()
    return "levelSelect"

def lev5():
    global defC,ready,ready2,activeDefenses,money,score,click,gameOver,wave

    money=10000
    running=True
    pause=False
    myclock=time.Clock()
    mixer.music.load("FSE-Assets/sound/bgMusic.mp3")
    mixer.music.play(-1)
    quitRect=Rect(260,25,150,40)
                # subtract 91 from x,y, make 212 the length and width
    towerPos5=[[Rect(30,197,50,50),False,(30,197),False,0,None,Rect(-59,106,212,212)],[Rect(232,173,50,50),False,(232,173),False,1,None,Rect(141,84,212,212)],
               [Rect(382,173,50,50),False,(382,173),False,2,None,Rect(291,82,212,212)],[Rect(228,337,50,50),False,(228,337),False,3,None,Rect(137,246,212,212)],
               [Rect(332,379,50,50),False,(332,379),False,4,None,Rect(241,288,212,212)],[Rect(332,520,50,50),False,(332,520),False,5,None,Rect(241,429,212,212)],
               [Rect(525,262,50,50),False,(525,262),False,6,None,Rect(434,171,212,212)],[Rect(525,409,50,50),False,(525,409),False,7,None,Rect(434,418,212,212)],
               [Rect(645,409,50,50),False,(645,409),False,8,None,Rect(554,418,212,212)],[Rect(459,589,50,50),False,(459,589),False,9,None,Rect(368,498,212,212)],
               [Rect(815,409,50,50),False,(815,409),False,10,None,Rect(724,418,212,212)]]
    enemy=[[130,-100,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]]
    enemy2=[[130,-100,0,motorcycle,motorcycle.health,False,motorcycle.prize,30]]

    wave="first"
    
    while running:
        myclock.tick(60)
        drawScene5(screen)
        hudElements(screen)
        moneyScore(screen)
        baseHealth(enemy,enemy2)
        screen.blit(quitPic,(260,25))
        draw.rect(screen,BLACK,quitRect,2)
        click=False
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                return "exit"
            if evt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evt.type==MOUSEBUTTONUP:
                click=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        music(None)
        for a in activeDefenses:
            screen.blit(a[0],a[1])

        if quitRect.collidepoint(mx,my):
            draw.rect(screen,RED,quitRect,3)
            if mb[0]==1:
                pause=True

        if pause==True:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(sureRect,(335,235))
            returnRect=Rect(465,375,140,35)
            leaveRect=Rect(435,425,205,35)
            if returnRect.collidepoint(mx,my):
                draw.rect(screen,RED,returnRect,3)
                if mb[0]==1:
                    pause=False
            if leaveRect.collidepoint(mx,my):
                draw.rect(screen,RED,leaveRect,3)
                if mb[0]==1:
                    pause=False
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    score=0
                    return "levelSelect"

        if ready==False and pause==False and wave=="first": #checks if either ready variable is false, so it calls the prep functions
            prep(screen,towerPos5)
        if ready2==False and pause==False and wave=="second":
            prep(screen,towerPos5)
            

        if ready==True and gameOver==False and pause==False: #if the first ready variable is true, it will call the functions for the first enemy list
            genEnemies(enemy) #generating enemies
            moveEnemy5(screen,enemy) #move
            healthBars(enemy)  #health bars
            damageEnemies(enemy,activeDefenses,towerPos5) #damage
            hudElements(screen)
            moneyScore(screen)

        if ready2==True and gameOver==False and pause==False: #if the 2nd ready variable becomes true, it will call the game functions for the second enemy list
            genEnemies(enemy2)
            moveEnemy5(screen,enemy2)
            healthBars(enemy2)
            damageEnemies(enemy2,activeDefenses,towerPos5)
            hudElements(screen)
            moneyScore(screen)

        if gameOver:
            endScreen=Surface((width,height),SRCALPHA)
            endScreen.fill((220,220,220,127))
            screen.blit(endScreen,(0,0))
            screen.blit(loseRect,(335,235))
            retryRect=Rect(365,415,128,50)
            mainRect=Rect(525,415,187,50)
            draw.rect(screen,RED,(945,375,100,10),0)

            if retryRect.collidepoint(mx,my):
                draw.rect(screen,RED,retryRect,3)
                if mb[0]==1:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
                    return "prev5"
            if mainRect.collidepoint(mx,my):
                draw.rect(screen,RED,mainRect,3)
                if mb[0]==1 and click==False:
                    defC=None
                    editCond=False
                    activeDefenses=[]
                    running=False
                    ready=False
                    ready2=False
                    gameOver=False
                    money=2000
                    score=0
        
        count=0 #counter for the first enemy list
        for i in enemy: 
            if i[5]==True: #for each "dead" or enemy that passed through the base, the count will go up
                count+=1
            if count==len(enemy): #if the counter is the same as the length of the enemy list, it means all the enemies have either died
            #or passed over the base, signalling the end of the wave
                wave="second"  #changes the wave variable to the second wave
                ready=False #makes the first ready variable false

        #there are only 2 waves per level, so this is the final wave
        count2=0
        for i in enemy2:
            if i[5]==True:
                count2+=1
            if count2==len(enemy2): #signals the end of the game (all 2 waves cleared)
                endScreen=Surface((width,height),SRCALPHA)
                endScreen.fill((220,220,220,127))
                screen.blit(endScreen,(0,0))
                screen.blit(victoryRect,(320,225))
                redoRect=Rect(445,353,150,40)
                nextRect=Rect(410,404,217,40)
                if redoRect.collidepoint(mx,my):
                    draw.rect(screen,RED,redoRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "prev5"
                if nextRect.collidepoint(mx,my):
                    draw.rect(screen,RED,nextRect,3)
                    if mb[0]==1 and click==False:
                        defC=None
                        editCond=False
                        activeDefenses=[]
                        ready=False
                        ready2=False
                        running=False
                        return "victory"

        display.flip()
    return "levelSelect"

def creds():
    global mx,my
    mixer.music.load("FSE-Assets/sound/sovietTheme.mp3")
    mixer.music.play()
    running=True
    while running:
        screen.blit(credMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        display.flip()
    return "main"

def instructions():
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    running=True
    while running:
        screen.blit(instructMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        display.flip()
    return "main"

def levelSelect():
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    levelRects=[Rect(122,260,240,160),Rect(407,262,250,160),Rect(696,262,250,160),Rect(257,493,240,160),Rect(564,492,240,160)]
    levels=["prev1","prev2","prev3","prev4","prev5"]
    running=True
    click=False
    while running:
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
                return "exit"
            if evnt.type==MOUSEBUTTONDOWN:
                click=True
            if evnt.type==MOUSEBUTTONUP:
                click=False
        screen.blit(levelSelectMenu,(0,0))
        screen.blit(crossPic,(960,50))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)

        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        for i in range(len(levelRects)):
            if levelRects[i].collidepoint(mx,my):
                draw.rect(screen,RED,levelRects[i],3)
                if mb[0]==1 and click==False:
                    return levels[i]
        display.flip()
    return "main"

def main():
    mixer.music.load("FSE-Assets/sound/menuMusic.mp3")
    mixer.music.play(-1)
    buttons=[Rect(57,294,210,47),Rect(57,370,270,49),Rect(57,448,170,49)]
    vals=["levelSelect","instructions","credits"]
    running=True
    click=False
    while running:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
            if evnt.type==MOUSEBUTTONDOWN:
                click=True
                music(True)
            if evnt.type==MOUSEBUTTONUP:
                click=False

        screen.blit(mainMenu,(0,0))
        backButton=Rect(950,650,50,50)
        draw.rect(screen,RED,backButton,3)
        screen.blit(crossPic,(960,660))
        music(None)

        for i in range(len(buttons)):
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,RED,buttons[i],3)
                if mb[0]==1 and click==False:
                    return vals[i]
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                return "exit"
        display.flip()

size=width,height=1050,750
screen=display.set_mode(size)
display.set_caption("The Great Patriotic War")
iconPic=image.load("FSE-Assets/icon.png")
display.set_icon(iconPic)
running=True
current="main"

while current!="exit":
    #menu
    if current=="main":
        current=main()
    if current=="levelSelect":
        current=levelSelect()
    if current=="instructions":
        current=instructions()
    if current=="credits":
        current=creds()
    #previews
    if current=="prev1":
        current=prev1()
    if current=="prev2":
        current=prev2()
    if current=="prev3":
        current=prev3()
    if current=="prev4":
        current=prev4()
    if current=="prev5":
        current=prev5()
    #levels
    if current=="lev1":
        current=lev1()
    if current=="lev2":
        current=lev2()
    if current=="lev3":
        current=lev3()
    if current=="lev4":
        current=lev4()
    if current=="lev5":
        current=lev5()

    #final victory
    if current=="victory":
        current=victory(score)

quit()
