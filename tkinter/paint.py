import tkinter
from tkinter import *

window = Tk()
window.geometry("600x800")
window.title("Parabel")

def painting(event):
    x=event.x()
    y=event.y()

fenster.bind("<Button-1>", painting)
fenster.bind("<ButtonRelease-1>", painting)
fenster.bind("<B1-Motion>", painting)


window.mainloop()