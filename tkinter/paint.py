import tkinter
from tkinter import *


window = Tk()
window.geometry("600x800")
window.title("Parabel")

def painting(event):
    x=event.x
    y=event.y

window.bind("<Button-1>", painting)
window.bind("<ButtonRelease-1>", painting)
window.bind("<B1-Motion>", painting)

canvasGrafik = tkinter.Canvas(window, width=500, height=400, bg='white')
canvasGrafik.grid()
canvasGrafik.place(x=50,y=250)
canvasGrafik.create_line(10,0,10,400)
canvasGrafik.create_line(10,200,500,200)

window.mainloop()