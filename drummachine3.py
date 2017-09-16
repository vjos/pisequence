from gpiozero import Button,LED
from signal import pause
from time import sleep
import pygame
import tkinter

stepList = "0110010011010111000111000111001010101010101000011111110000000001"


button1 = Button(2)
button2 = Button(3)
button3 = Button(4)
button4 = Button(14)
button5 = Button(25)
button6 = Button(8)
button7 = Button(7)
button8 = Button(1)

ledBlue = LED(6)
ledRed = LED(13)
ledGreen = LED(19)
ledYellow = LED(26)
ledWhite = LED(5)

squareSize = 25

pygame.mixer.pre_init(22050, -16, 1, 256)
pygame.mixer.init()
pygame.init()

snd1 = pygame.mixer.Sound('sounds/kick3.wav')
snd2 = pygame.mixer.Sound('sounds/hats2.wav')
snd3 = pygame.mixer.Sound('sounds/snare2.wav')

def playKick():
    snd1.play()
    ledBlue.toggle()
    sleep(0.1)
    ledBlue.toggle()

def playHats():
    snd2.play()
    ledRed.toggle()
    sleep(0.1)
    ledRed.toggle()

def playSnare():
    snd3.play()
    ledGreen.toggle()
    sleep(0.1)
    ledGreen.toggle()

def newSequence():
    pass

def liveMachine():
    #assign hardware buttons to drum functions
    button8.when_pressed = playKick
    button7.when_pressed = playHats
    button6.when_pressed = playSnare

    #GUI
    top = tkinter.Tk()
    menubar = tkinter.Menu(top)

    #menu bars
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=newSequence)
    filemenu.add_command(label="Save", command=newSequence)
    filemenu.add_command(label="Open", command=newSequence)
    filemenu.add_separator()
    filemenu.add_command(label="Switch Mode", command=sequencer)
    menubar.add_cascade(label="File", menu=filemenu)

    rnnmenu = tkinter.Menu(menubar, tearoff=0)
    rnnmenu.add_command(label="Learn", command=newSequence)
    rnnmenu.add_command(label="Generate", command=newSequence)
    menubar.add_cascade(label="RNN", menu=rnnmenu)
    
    #assigning drum functions to software buttons
    kickButton = tkinter.Button(top, text ="Kick", command = playKick, width=6, fg='white', bg='blue')
    kickButton.pack(side=tkinter.LEFT)
    hatsButton = tkinter.Button(top, text ="Hats", command = playHats, width=6, fg='white', bg='red')
    hatsButton.pack(side=tkinter.LEFT)
    snareButton = tkinter.Button(top, text ="Snare", command = playSnare, width=6, fg='white', bg='green')
    snareButton.pack(side=tkinter.LEFT)

    #more tkinter stuff
    top.config(menu=menubar)
    top.mainloop()

    #idk if this is needed
    #pause

def sequencer():
    #GUI
    top = tkinter.Tk()
    menubar = tkinter.Menu(top)

    #menu bars
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=newSequence)
    filemenu.add_command(label="Save", command=newSequence)
    filemenu.add_command(label="Open", command=newSequence)
    filemenu.add_separator()
    filemenu.add_command(label="Switch Mode", command=liveMachine)
    menubar.add_cascade(label="File", menu=filemenu)

    rnnmenu = tkinter.Menu(menubar, tearoff=0)
    rnnmenu.add_command(label="Learn", command=newSequence)
    rnnmenu.add_command(label="Generate", command=newSequence)
    menubar.add_cascade(label="RNN", menu=rnnmenu)

    #draws the canvas 
    
    canvas1 = tkinter.Canvas(top, width=squareSize*8, height=squareSize*8)
    canvas1.pack()

    counter = 0
    for j in range(4):
        for i in range(4):
            if(int(stepList[counter]) == 1):
                canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2,              squareSize*2*i + squareSize,   squareSize*j*2 + squareSize, fill="blue")
                counter += 1
            else:
                canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2,              squareSize*2*i + squareSize,   squareSize*j*2 + squareSize, fill="light cyan")
                counter += 1
            if(int(stepList[counter]) == 1):
                canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2,              squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize, fill="red")
                counter += 1
            else:
                canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2,              squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize, fill="light cyan")
                counter += 1
            if(int(stepList[counter]) == 1):
                canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2 + squareSize, squareSize*2*i + squareSize,   squareSize*j*2 + squareSize*2, fill="green")
                counter += 1
            else:
                canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2 + squareSize, squareSize*2*i + squareSize,   squareSize*j*2 + squareSize*2, fill="light cyan")
                counter += 1
            if(int(stepList[counter]) == 1):
                canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2 + squareSize, squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize*2, fill="yellow")
                counter += 1
            else:
                canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2 + squareSize, squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize*2, fill="light cyan")
                counter += 1
            
    #more tkinter stuff
    top.config(menu=menubar)
    top.mainloop()

    pause()

sequencer()
