from tkinter import *
from tkinter import messagebox
import random
from random import randint
from tkinter.ttk import LabeledScale

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

number = 0
guessnumber=1

def generate():
    number = random.randrange(0,100)
    LabelC['text'] = number

def guess():
    LabelL.config(text = 'You pressed the button!')
    guessnr= int(NumberInput.get())
    number=int(LabelC['text'])
    guessnumber=int(LabelD['text'])
    guessnumber=guessnumber+1
    if number==guessnr:
        LabelL.config(text = 'Guessed Correctly in ' + str(guessnumber) + ' Attempts.')
        guessnumber=1
    else:
        LabelL.config(text = 'Wrong Guess')
    if number>guessnr:
        LabelBS.config(text = 'The Number is bigger')
    elif number<guessnr:
        LabelBS.config(text = 'The Number is smaller')  
def reset():
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelC['text'] = number

LabelT = Label(window,text='Zufallszahl:',)
LabelT.place(x=200,y=160)

LabelC = Label(window,text=number,)
LabelC.place(x=200,y=180,)

LabelD = Label(window,text=guessnumber)
LabelD.place(x=200,y=120)

LabelL = Label(window,text='Guess')
LabelL.place(x=250,y=180)

LabelBS = Label(window,text='')
LabelBS.place(x=350,y=180)

LabelN = Label(window,text='Zufallszahl-Nr:',)
LabelN.place(x=200,y=200)

NumberInput = Entry(window,bg='white',fg='black',text=int,)
NumberInput.place(x=200,y=220)
NumberInput.insert(0,0)

BCalc = Button(window,text='Zufallszahlen generieren', command=generate)
BCalc.place(x=200,y=260)

CCalc = Button(window,text='Guess',command=guess)
CCalc.place(x=200,y=300)

DCalc = Button(window,text='Reset', command=reset)
DCalc.place(x=200,y=340)

window.mainloop()