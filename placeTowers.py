#placeTower.py
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
tower="no tower"
mx,my=mouse.get_pos()

heavyGunRect=Rect(100,100,50,50)
draw.rect(screen,GREEN,heavyGunRect,1)
heavyGun=image.load("FSE-Assets/Defenses/heavyGun.png")
heavyGun=transform.scale(heavyGun,(50,50))
screen.blit(heavyGun,(100,100))

def placeTower(t):
    
    if t!="no tower":
        screenShot=screen.copy()
        defenseImage=image.load("FSE-Assets/Defenses/"+t+".png")
        defenseImage=transform.scale(defenseImage,(100,100))
        screen.blit(defenseImage,(mx,my))
        
        if mb[0]==1:
            
            
            screen.blit(defenseImage,(mx,my))
        if mb[0]==0:
            screen.blit(screenShot,(0,0))
        
        
    
cond=False    
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
    if mb[0]==1:
        if heavyGunRect.collidepoint(mx,my) and tower=="no tower":
            imag=screen.subsurface(heavyGunRect).copy()
            tower="heavyGun"
    
            
            placeTower(tower)
            cond=True
        elif heavyGunRect.collidepoint(mx,my) and tower=="heavy gun":
            tower="no tower"
    if cond:
        screen.fill(BLACK)
        draw.rect(screen,GREEN,heavyGunRect,1)
        screen.blit(heavyGun,(100,100))
        placeTower(tower)
        
        
        
    
    
    
    
    display.flip() 

quit()
