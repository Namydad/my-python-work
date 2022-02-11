from tkinter import *
from tkinter import messagebox
from turtle import color
from math import pi

window = Tk()
window.geometry("1900x1080")
window.title("Calculator")

def squares():
    for i in range(5,50,5):
        canvasGraphic.create_line((5*2)*5,(i+5)*5,(25*2)*5,(i+5)*5, fill='white') #vertical
        canvasGraphic.create_line((i+5)*5,(5*2)*5,(i+5)*5,(25*2)*5, fill='white') #horizontal
        for z in range(0,35,5):
            for i in range(5,50,10):
                canvasGraphic.create_rectangle((5.1+i+z)*5,(10.1+z)*5,(9.8+i+z)*5,(14.8+z)*5, fill='red') #v
                canvasGraphic.create_rectangle((10.1+i+z)*5,(15.1+z)*5,(14.8+i+z)*5,(19.8+z)*5, fill='red')#v
                canvasGraphic.create_rectangle((10.1+z)*5,(5.1+i+z)*5,(14.8+z)*5,(9.8+i+z)*5, fill='red') #h
                canvasGraphic.create_rectangle((15.1+z)*5,(10.1+i+z)*5,(19.8+z)*5,(14.8+i+z)*5, fill='red') #h

        if i == 45:
            canvasGraphic.create_rectangle((5.1+i)*5,(10.1)*5,(300+i)*5,(300)*5, fill='black')
            canvasGraphic.create_rectangle((10.1)*5,(5.1+i)*5,(300)*5,(300+i)*5, fill='black')
            canvasGraphic.create_rectangle((10.1+i)*5,(15.1)*5,(300+i)*5,(300)*5, fill='black')
            canvasGraphic.create_rectangle((15.1)*5,(10.1+i)*5,(300)*5,(300+i)*5, fill='black')

        
    

LabelT = Label(window,text='Gitternetz', fg="blue",)
LabelT.place(x=200,y=205)


BCalc = Button(window,text='Zeichnen', command=squares)
BCalc.place(x=280,y=200)

canvasGraphic = Canvas(window, width=600, height=600, bg='black',)
canvasGraphic.place(x=200,y=260)

window.mainloop()