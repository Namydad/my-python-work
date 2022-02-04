from tkinter import *
from tkinter import messagebox
from turtle import color
from math import pi

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

number = 0
u=0
f=0

def calculation():
    number= int(NumberInput.get())
    u=number*pi*2
    f=pi*number*number
    u_float = "{:.2f}".format(u)
    f_float = "{:.2f}".format(f)
    LabelU['text'] = u_float
    LabelF['text'] = f_float
    for i in range(number,1,-2):
        canvasGraphic.create_oval(1,1,i,i, fill="white")
    
   
def reset():
    NumberInput.delete(0,'end')
    NumberInput.insert(0,str(number))
    LabelU['text'] = number
    LabelF['text'] = number

LabelT = Label(window,text='Kreisberechnung', fg="blue",)
LabelT.place(x=200,y=160)

LabelN = Label(window,text='Radius',)
LabelN.place(x=200,y=200)

NumberInput = Entry(window,bg='white',text=int,)
NumberInput.place(x=200,y=220)
NumberInput.insert(0,0)

LabelU = Label(window,text='Umfang: '+ str(u)+'cm',)
LabelU.place(x=200,y=250)

LabelF = Label(window,text='Fläche:'+ str(f)+'cm²',)
LabelF.place(x=200,y=280)

BCalc = Button(window,text='Calculate', command=calculation)
BCalc.place(x=200,y=320)

BCalc = Button(window,text='Reset', command=reset)
BCalc.place(x=200,y=350)

canvasGraphic = Canvas(window, width=400, height=400, bg='black',)
canvasGraphic.place(x=200,y=400)

window.mainloop()