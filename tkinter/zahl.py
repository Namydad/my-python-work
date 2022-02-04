from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

number = 0

def calculation():
    number= int(NumberInput.get())
    number= number+1
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelC['text'] = number
    
def reset():
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelC['text'] = number

LabelT = Label(window,text='Current Number:',)
LabelT.place(x=200,y=160)

LabelC = Label(window,text=number,)
LabelC.place(x=200,y=180,)

LabelN = Label(window,text='Enter the Amount to add:',)
LabelN.place(x=200,y=200)

NumberInput = Entry(window,bg='white',text=int,)
NumberInput.place(x=200,y=220)
NumberInput.insert(0,0)

BCalc = Button(window,text='Calculate', command=calculation)
BCalc.place(x=200,y=240)

BCalc = Button(window,text='Reset', command=reset)
BCalc.place(x=200,y=270)

window.mainloop()