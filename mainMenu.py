#mainGame
from pygame import *
from math import *
from random import *
from datetime import datetime
init()
mainMenu=image.load("FSE-Assets/mainscreen.jpg")

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)

def main():
    global mx,my
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic.mp3")
    mixer.music.play()
    running=True
    buttons=[Rect(57,294,210,47),Rect(57,370,270,49),Rect(57,448,170,49)]
    vals=["game","instructions","credits"]
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(mainMenu,(0,0))
        for i in range(len(buttons)):
            draw.rect(screen,RED,buttons[i],3)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(255,255,0),buttons[i],3)
                if mb[0]==1:
                    return vals[i]
        display.flip()

def creds():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play()
    running=True
    reButton=Rect(100,100,50,50)
    mb=mouse.get_pressed()
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
        if reButton.collidepoint(mx,my) and mb[0]==1:
            running=False
        display.flip()
    return "menu"

def instructions():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play()
    running=True
    reButton=Rect(100,100,50,50)
    mb=mouse.get_pressed()
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
        if reButton.collidepoint(mx,my) and mb[0]==1:
            running=False
        display.flip()
    return "menu"

size=width,height=1050,750
screen=display.set_mode(size)
display.set_caption("The Great Patriotic War")
iconPic=image.load("FSE-Assets/icon.png")
display.set_icon(iconPic)
running=True
current="main"

while current!="exit":
    if current=="main":
        current=main()
    if current=="game":
        current=game()
    if current=="instructions":
        current=instructions()
    if current=="credits":
        current=creds()
    
quit()
