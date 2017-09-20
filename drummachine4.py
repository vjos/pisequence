'''from gpiozero import Button,LED'''
from time import sleep
import tkinter
import os

directory = os.getcwd()

step = 0
stepList = "1111111100100100000111000111001010101010101000011111110000000001"

squareSize = 25

sequencePlaying = False

'''
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

pygame.mixer.pre_init(22050, -16, 1, 256)
pygame.mixer.init()
pygame.init()

snd1 = pygame.mixer.Sound('kick3.wav')
snd2 = pygame.mixer.Sound('hats2.wav')
snd3 = pygame.mixer.Sound('snare2.wav')
snd4 = pygame.mixer.Sound('hats2.wav')
'''

def save(string):
    directory_list = os.listdir(directory)
    next_free = 0
    number = ''
    
    for i in range(len(directory_list)):
        test_string = directory_list[i]
        for j in range(len(test_string)):
            if(test_string[j].isdigit()):
                number += test_string[j]

        if(number.isdigit()):        
            if(int(number) > next_free):
                next_free = int(number)

        number = ''

    next_free += 1
        
    file_name = ("sequence" + str(next_free) + ".txt")
    F = open(file_name, "w")
    F.write(string)
    F.close() 

def read(number):
    file_name = ("sequence" + str(number) + ".txt")
    F = open(file_name, "r")
    string = F.read()
    F.close()
    return string

'''
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

def playCowbell():
    snd4.play()
    ledYellow.toggle()
    sleep(0.1)
    ledYellow.toggle()
'''

def newSequence():
    pass

def playSequence():
    global sequencePlaying
    sequencePlaying = True
    print("PLAY")

def pauseSequence():
    global sequencePlaying
    sequencePlaying = False
    print("PAUSE")

def playpause():
    global step 
    
    if(sequencePlaying):
        pauseSequence()
    else:
        playSequence()

    if(sequencePlaying):
        drum = 0
        
        kick = False
        hats = False
        snare = False
        cowbell = False
        
        for i in range(len(stepList)):
            '''
            if(int(stepList[i]) == 1 and i%4 == 0):
                #trigger bass drum
                playKick()
            elif(int(stepList[i]) and (i+3)%4 == 0):
                #trigger hats
                playHats()
            elif(int(stepList[i]) and (i+2)%4 == 0):
                #trigger snare
                playSnare()
            elif(int(stepList[i]) and (i+1)%4 == 0):
                #trigger cowbell
                playCowbell()
            '''
            drum += 1
            
            highlightNext(i)
            
            if(drum == 4):        
                step += 1
                drum = 0
                sleep(0.3)

def new():
    global stepList

    stepList = "0000000000000000000000000000000000000000000000000000000000000000"
        
    for i in range(64):
        canvas1.itemconfig(canvasList[i],fill='light cyan')
    canvas1.after(1,new)

def highlightNext(square):
    if(square==0):
        if(int(stepList[square]) == 1):
            canvas1.itemconfig(canvasList[square],fill='cornflower blue')
        else:
            canvas1.itemconfig(canvasList[square],fill='white')
        if(int(stepList[square+60]) == 1):
            canvas1.itemconfig(canvasList[square+60],fill='blue')
        else:
            canvas1.itemconfig(canvasList[square+60],fill='light cyan')
    elif(square==1):
        if(int(stepList[square]) == 1):
            canvas1.itemconfig(canvasList[square],fill='salmon3')
        else:
            canvas1.itemconfig(canvasList[square],fill='white')
        if(int(stepList[square+60]) == 1):
            canvas1.itemconfig(canvasList[square+60],fill='red')
        else:
            canvas1.itemconfig(canvasList[square+60],fill='light cyan')
    elif(square==2):
        if(int(stepList[square]) == 1):
            canvas1.itemconfig(canvasList[square],fill='medium spring green')
        else:
            canvas1.itemconfig(canvasList[square],fill='white')
        if(int(stepList[square+60]) == 1):
            canvas1.itemconfig(canvasList[square+60],fill='green')
        else:
            canvas1.itemconfig(canvasList[square+60],fill='light cyan')
    elif(square==3):
        if(int(stepList[square]) == 1):
            canvas1.itemconfig(canvasList[square],fill='goldenrod1')
        else:
            canvas1.itemconfig(canvasList[square],fill='white')
        if(int(stepList[square+60]) == 1):
            canvas1.itemconfig(canvasList[square+60],fill='yellow')
        else:
            canvas1.itemconfig(canvasList[square+60],fill='light cyan')
    else:
        if(square%4 == 0):
            if(int(stepList[square]) == 1):
                canvas1.itemconfig(canvasList[square],fill='cornflower blue')
            else:
                canvas1.itemconfig(canvasList[square],fill='white')
            if(int(stepList[square-4]) == 1):
                canvas1.itemconfig(canvasList[square-4],fill='blue')
            else:
                canvas1.itemconfig(canvasList[square-4],fill='light cyan')
        elif((square+3)%4 == 0):
            if(int(stepList[square]) == 1):
                canvas1.itemconfig(canvasList[square],fill='salmon3')
            else:
                canvas1.itemconfig(canvasList[square],fill='white')
            if(int(stepList[square-4]) == 1):
                canvas1.itemconfig(canvasList[square-4],fill='red')
            else:
                canvas1.itemconfig(canvasList[square-4],fill='light cyan')
        elif((square+2)%4 == 0):
            if(int(stepList[square]) == 1):
                canvas1.itemconfig(canvasList[square],fill='medium spring green')
            else:
                canvas1.itemconfig(canvasList[square],fill='white')
            if(int(stepList[square-4]) == 1):
                canvas1.itemconfig(canvasList[square-4],fill='green')
            else:
                canvas1.itemconfig(canvasList[square-4],fill='light cyan')
        elif((square+1)%4 == 0):
            if(int(stepList[square]) == 1):
                canvas1.itemconfig(canvasList[square],fill='goldenrod1')
            else:
                canvas1.itemconfig(canvasList[square],fill='white')
            if(int(stepList[square-4]) == 1):
                canvas1.itemconfig(canvasList[square-4],fill='yellow')
            else:
                canvas1.itemconfig(canvasList[square-4],fill='light cyan')
    canvas1.after(1, newSequence)


'''               
def liveMachine():
    #assign hardware buttons to drum functions
    button8.when_pressed = playKick
    button7.when_pressed = playHats
    button6.when_pressed = playSnare
    button5.when_pressed = playCowbell

    #GUI
    top = tkinter.Tk()
    menubar = tkinter.Menu(top)

    #menu bars
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Save", command=newSequence)
    filemenu.add_command(label="Open", command=newSequence)
    menubar.add_cascade(label="File", menu=filemenu)

    rnnmenu = tkinter.Menu(menubar, tearoff=0)
    rnnmenu.add_command(label="Learn", command=newSequence)
    rnnmenu.add_command(label="Generate", command=newSequence)
    menubar.add_cascade(label="RNN", menu=rnnmenu)
    
    #assigning drum functions to software buttons
    kickButton = tkinter.Button(top, text ="Kick", command = playKick, width=7, fg='white', bg='blue')
    kickButton.pack(side=tkinter.LEFT)
    hatsButton = tkinter.Button(top, text ="Hats", command = playHats, width=7, fg='white', bg='red')
    hatsButton.pack(side=tkinter.LEFT)
    snareButton = tkinter.Button(top, text ="Snare", command = playSnare, width=7, fg='white', bg='green')
    snareButton.pack(side=tkinter.LEFT)
    cowbellButton = tkinter.Button(top, text ="Cowbell", command = playCowbell, width=7, fg='black', bg='yellow')
    cowbellButton.pack(side=tkinter.LEFT)

    #more tkinter stuff
    top.config(menu=menubar)
    top.mainloop()
'''

if(True):
    #GUI
    top = tkinter.Tk()
    menubar = tkinter.Menu(top)
 
    #draws the canvas 
    
    canvas1 = tkinter.Canvas(top, width=squareSize*8, height=squareSize*8)
    canvas1.pack()

    #menu bars
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Save", command=newSequence)
    filemenu.add_command(label="Open", command=newSequence)
    '''filemenu.add_separator()
    filemenu.add_command(label="Switch Mode", command=liveMachine)'''
    menubar.add_cascade(label="File", menu=filemenu)

    rnnmenu = tkinter.Menu(menubar, tearoff=0)
    rnnmenu.add_command(label="Learn", command=newSequence)
    rnnmenu.add_command(label="Generate", command=newSequence)
    menubar.add_cascade(label="RNN", menu=rnnmenu)

    counter = 0

    canvasList = []
    
    for j in range(4):
        for i in range(4):
            if(int(stepList[counter]) == 1):
                canvasList.append(canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2,              squareSize*2*i + squareSize,   squareSize*j*2 + squareSize, fill="blue"))
                counter += 1
            else:
                canvasList.append(canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2,              squareSize*2*i + squareSize,   squareSize*j*2 + squareSize, fill="light cyan"))
                counter += 1
            if(int(stepList[counter]) == 1):
                canvasList.append(canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2,              squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize, fill="red"))
                counter += 1
            else:
                canvasList.append(canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2,              squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize, fill="light cyan"))
                counter += 1
            if(int(stepList[counter]) == 1):
                canvasList.append(canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2 + squareSize, squareSize*2*i + squareSize,   squareSize*j*2 + squareSize*2, fill="green"))
                counter += 1
            else:
                canvasList.append(canvas1.create_rectangle(squareSize*2*i,              squareSize*j*2 + squareSize, squareSize*2*i + squareSize,   squareSize*j*2 + squareSize*2, fill="light cyan"))
                counter += 1
            if(int(stepList[counter]) == 1):
                canvasList.append(canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2 + squareSize, squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize*2, fill="yellow"))
                counter += 1
            else:
                canvasList.append(canvas1.create_rectangle(squareSize*2*i + squareSize, squareSize*j*2 + squareSize, squareSize*i*2 + squareSize*2, squareSize*j*2 + squareSize*2, fill="light cyan"))
                counter += 1

    #play function

    '''button1.when_pressed = playpause'''

    #more tkinter stuff
    top.config(menu=menubar)
    top.mainloop()
