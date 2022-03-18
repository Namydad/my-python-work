from tkinter import *
from tkinter import messagebox
import random
from random import randint
from tkinter.ttk import LabeledScale

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

number = 0
guessnumber=0
guessed=[]
def generate():
    number = random.randrange(1,100)
    LabelC['text'] = number

def guess():
    LabelL.config(text = 'You pressed the button!')
    guessnr= int(NumberInput.get())
    number=int(LabelC['text'])
    guessnumber=int(LabelD['text'])
    guessnumber=guessnumber+1
    LabelD['text']=guessnumber
    if number==guessnr:
        LabelL.config(text = 'Guessed Correctly in ' + str(guessnumber) + ' Attempts.')
        guessnumber=1
        LabelD['text']= 1
        LabelBS.config(text = '')
    else:
        LabelL.config(text = 'Wrong Guess')
    if number>guessnr:
        LabelBS.config(text = 'The Number is bigger')
        guessed.append(str(guessnr)+" ist kleiner als")
        LabelGuessed.config(text = guessed)
    elif number<guessnr:
        LabelBS.config(text = 'The Number is smaller')
        guessed.append(str(guessnr)+" ist größer als")
        LabelGuessed.config(text = guessed)
def reset():
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    guessed=[]        
    LabelGuessed.config(text = guessed)
    LabelC['text'] = number
    LabelD['text']= 0

LabelT = Label(window,text='Zufallszahl:',)
LabelT.place(x=200,y=160)

LabelC = Label(window,text=number,)
LabelC.place(x=200,y=180,)

LabelD = Label(window,text="Guess: ")
LabelD.place(x=200,y=120)

LabelD = Label(window,text=guessnumber)
LabelD.place(x=260,y=120)

LabelL = Label(window,text='Guess')
LabelL.place(x=200,y=140)

LabelBS = Label(window,text='')
LabelBS.place(x=200,y=160)

LabelGuessedTEXT = Label(window,text="Alle geratene Zahlen:")
LabelGuessedTEXT.place(x=200,y=100)

LabelGuessed = Label(window,text=guessed,)
LabelGuessed.place(x=340,y=100)

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