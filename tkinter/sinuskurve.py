import tkinter
from tkinter import *
import math

window = Tk()
window.geometry("600x800")
window.title("Parabel")

canvasGrafik = tkinter.Canvas(window, width=500, height=400, bg='white')
canvasGrafik.grid()
canvasGrafik.place(x=50,y=250)
canvasGrafik.create_line(10,0,10,400)
canvasGrafik.create_line(10,200,500,200)

a=0.01
b=20

def draw_sinuskurve():
    a = float(EntryA.get())
    b = float(EntryB.get())
    canvasGrafik.create_line(10,0,10,400)
    canvasGrafik.create_line(10,200,500,200)
    mx=10
    my=200
    for x in range(0,361,1):
        bogenmass = x*2*math.pi/360.0
        y=a*math.sin(bogenmass*b)
        canvasGrafik.create_line(mx,my,x+10,200-y)
        mx=x+10
        my=200-y
def reset():
    canvasGrafik.delete('all')
    canvasGrafik.create_line(10,0,10,400)
    canvasGrafik.create_line(10,200,500,200)
    
    
labelA = Label(window, bg='red', text='Amplitude')
labelA.place(y=50,x=20,height=50, width=100)
EntryA = Entry(window, bg='grey', text=float)
EntryA.place(y=50,x=120,height=50,)

labelA = Label(window, bg='red', text='Frequenz')
labelA.place(y=100,x=20,height=50,width=100)
EntryB = Entry(window, bg='grey', text=float)
EntryB.place(y=100,x=120,height=50,)

parabel= Button(window, bg='grey', text='Sinuskurve zeichen', command=draw_sinuskurve)
parabel.place(y=200,x=20,height=50,)

parabeldelete= Button(window, bg='grey', text='Koordinatensystem leeren', command=reset)
parabeldelete.place(y=200,x=170,height=50,)


window.mainloop()