from tkinter import *
import tkinter.messagebox

#login

'''
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0,column=0, sticky=E)
label_2.grid(row=1,column=0, sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)
'''

#binding
'''
def printName(event):
    print("hey im josh")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-3>", printName)
button_1.pack()
'''

#using classes
class MyButtons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print message",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("OK LuL")


root = Tk()

b = MyButtons(root)

#status bar
status = Label(root, text="Doing Nothing", bd=1, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

#alert
tkinter.messagebox.showinfo('Window Title', "Monkeys LUL")
answer = tkinter.messagebox.askquestion('Question 1', "Are you here?")
if(answer == 'yes'):
    print("OK")
else:
    print(":(")

canvas = Canvas(root,width=200,height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,200,100)
answer2 = tkinter.messagebox.askquestion('Question 2', "Delete Line?")
if(answer2 == "yes"):
    canvas.delete(blackLine)


root.mainloop()                             
