from random import randint
from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

number = 0

def generate():
    number = random.randrange(0,100)
    LabelC['text'] = number

def calculation():
    number= int(NumberInput.get())
    if number==0:
        
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelC['text'] = number
    
def reset():
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelC['text'] = number

LabelT = Label(window,text='Zufallszahl:',)
LabelT.place(x=200,y=160)

LabelC = Label(window,text=number,)
LabelC.place(x=200,y=180,)

LabelN = Label(window,text='Zufallszahl-Nr:',)
LabelN.place(x=200,y=200)

NumberInput = Entry(window,bg='white',fg='black',text=int,)
NumberInput.place(x=200,y=220)
NumberInput.insert(0,0)

BCalc = Button(window,text='Zufallszahlen generieren', command=generate)
BCalc.place(x=200,y=260)

BCalc = Button(window,text='Reset', command=reset)
BCalc.place(x=200,y=300)

window.mainloop()