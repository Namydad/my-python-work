import tkinter
from tkinter import *

window = Tk()
window.geometry("600x800")
window.title("Parabel")

canvasGrafik = tkinter.Canvas(window, width=500, height=400)
canvasGrafik.grid()

a=0.01

def draw_parabel():
    canvasGrafik.create_line(250,0,250,400)
    canvasGrafik.create_line(0,200,500,200)
    for x in range(0,201):
        y=a*x**2
        canvasGrafik.create_oval(250+x,200-y,251+x,201-y)
        canvasGrafik.create_oval(250-x,200-y,251-x,201-y)

draw_parabel()


window.mainloop()