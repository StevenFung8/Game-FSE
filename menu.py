#mainGame
from pygame import *
from math import *
from random import *
from datetime import datetime
init()
mainMenu=image.load("FSE-Assets/mainscreen.jpg")
credMenu=image.load("FSE-Assets/credits.jpg")
instructMenu=image.load("FSE-Assets/instructions.jpg")

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)

def creds():
    global mx,my
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play()
    running=True
    while running:
        screen.blit(credMenu,(0,0))
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
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic2.mp3")
    mixer.music.play(-1)
    mixer.music.play()
    running=True
    while running:
        screen.blit(instructMenu,(0,0))
        backButton=Rect(950,40,50,50)
        draw.rect(screen,BLACK,backButton,3)
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        if backButton.collidepoint(mx,my):
            draw.rect(screen,YELLOW,backButton,3)
            if mb[0]==1:
                running=False
        display.flip()
    return "main"

def main():
    mixer.init()
    mixer.music.load("FSE-Assets/sound/menuMusic.mp3")
    mixer.music.play(-1)
    buttons=[Rect(57,294,210,47),Rect(57,370,270,49),Rect(57,448,170,49)]
    vals=["game","instructions","credits"]
    running=True
    while running:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
        screen.blit(mainMenu,(0,0))
        for i in range(len(buttons)):
            draw.rect(screen,RED,buttons[i],3)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(255,255,0),buttons[i],3)
                if mb[0]==1:
                    return vals[i]
        display.flip()

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
