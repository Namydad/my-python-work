from tkinter import *
from tkinter import messagebox
from turtle import color
from math import pi

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

def squares():
    for i in range(5,50,5):
        canvasGraphic.create_line((5*2)*5,(i+5)*5,(25*2)*5,(i+5)*5, fill='white')
        canvasGraphic.create_line((i+5)*5,(5*2)*5,(i+5)*5,(25*2)*5, fill='white')
        
    

LabelT = Label(window,text='Gitternetz', fg="blue",)
LabelT.place(x=200,y=205)


BCalc = Button(window,text='Zeichnen', command=squares)
BCalc.place(x=280,y=200)

canvasGraphic = Canvas(window, width=600, height=600, bg='black',)
canvasGraphic.place(x=200,y=260)

window.mainloop()