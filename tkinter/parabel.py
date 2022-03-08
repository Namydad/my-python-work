import tkinter
from tkinter import *

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
    c = float(EntryC.get())
    canvasGrafik.create_line(0,0,0,400)
    canvasGrafik.create_line(0,200,500,200)
    for x in range(0,360):
        y=0.01*a*x**2+b*x+c
        canvasGrafik.create_oval(10+x,200-y,10+x,201-y)
def reset():
    canvasGrafik.delete('all')
    canvasGrafik.create_line(0,0,0,400)
    canvasGrafik.create_line(0,200,500,200)
    
labelA = Label(window, bg='red', text='x²')
labelA.place(y=50,x=20,height=50, width=50)
EntryA = Entry(window, bg='grey', text=float)
EntryA.place(y=50,x=70,height=50,)

labelA = Label(window, bg='red', text='x')
labelA.place(y=100,x=20,height=50,width=50)
EntryB = Entry(window, bg='grey', text=float)
EntryB.place(y=100,x=70,height=50,)

labelA = Label(window, bg='red', text='y')
labelA.place(y=150,x=20,height=50,width=50)
EntryC = Entry(window, bg='grey', text=float)
EntryC.place(y=150,x=70,height=50,)

parabel= Button(window, bg='grey', text='Parabel zeichen', command=draw_sinuskurve)
parabel.place(y=200,x=20,height=50,)

parabeldelete= Button(window, bg='grey', text='Koordinatensystem leeren', command=reset)
parabeldelete.place(y=200,x=150,height=50,)


window.mainloop()