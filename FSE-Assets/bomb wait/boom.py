"""
boom.py
-  The whole point of this example is the way I set a timer on the animation. 
   I see each bomb as a list of 4 things [X, Y, counter, animationFrame]. I set
   the X,Y when the bomb is dropped, and set counter and animationFrame to 0.
   Each time around the loop I advance the timer, after 90 frames have passed
   I start advancing the animationFrame. When the animation Frame goes out of
   range I remove it from the list.
"""

from pygame import *
from random import randint

X=0
Y=1
DELAY=2
FRAME=3

init()
size = width, height = 500, 500
screen = display.set_mode(size)
boomPics = []
for i in range(28):
    boomPics += [image.load("images\\Explode-05_frame_"+str(i)+".gif")]

""" draws the current state of the game """
def drawScene(screen,guy, bombs):    
    screen.fill((0,0,0))   
    draw.rect(screen, (255,0,0), guy+[10,10])
    for bomb in bombs:
        if bomb[3]==0:
            draw.circle(screen,(255,255,0), (bomb[0]+120,bomb[1]+90),5)
        screen.blit(boomPics[bomb[FRAME]], bomb[:2])        
    display.flip()

''' For each of the bombs advance it's delay. If it's been 90 loop iterations
    then for every 5 loops advance the animation frame by one. If the animation
    is done remove it from the list of bombs. '''
        
def advanceBombs(bombs):
    for bomb in bombs[:]:       
        bomb[DELAY]+=1
        if bomb[DELAY] > 90 and bomb[DELAY]%5==0: # the DELAY acts as a wait to start the
            bomb[FRAME]+=1                          
            if bomb[FRAME]==28:
                bombs.remove(bomb)
    print(bombs)
          


def moveGuy(guy,dropCount):
    keys = key.get_pressed()
    
    if keys[K_LEFT] and guy[X] > 0:
        guy[X] -= 10
    if keys[K_RIGHT] and guy[X] < 790:
        guy[X] += 10
    if keys[K_DOWN] and guy[Y] < 590:
        guy[Y] += 10
    if keys[K_UP] and guy[Y] > 0:
        guy[Y] -= 10
    if keys[K_SPACE] and dropCount == 0:
        bombs.append([guy[X]-120,guy[Y]-90,0,0])
        dropCount = 0
    if dropCount > 0:
        dropCount-=1
    return dropCount

running = True          
myClock = time.Clock()  
guy = [250,0]
bombs = []              # list of [x,y,timeCounter, frame]
dropCount = 0
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False

    dropCount = moveGuy(guy, dropCount)
    advanceBombs(bombs)
    drawScene(screen, guy, bombs)
    myClock.tick(60)

quit()
