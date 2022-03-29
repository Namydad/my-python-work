from textwrap import fill
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile

color='black'

object="freestyle"

window = Tk()
window.geometry("1900x1080")
window.title("Drawing Board")

def clear():
    DrawingBoard.delete('all')

def setcolor(colorinfo):
    global color
    color = colorinfo

def setobject(objectinfo):
    global object
    object = objectinfo

"""def save_file():
	Files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = Files, defaultextension = Files)"""

def painting(event,):
    x1=event.x-2.5
    y1=event.y-2.5
    x2=event.x+2.5
    y2=event.y+2.5
    if object=="freestyle":
        DrawingBoard.create_oval(x1, y1, x2, y2,fill=color)

def click(event): 
    global merkex,merkey
    merkex=event.x
    merkey=event.y

def geometry(event):
    x2=event.x
    y2=event.y
    if object=="rectangle":
        DrawingBoard.create_rectangle(merkex,merkey,x2,y2, outline=color, fill=color)

menubar = Menu(window, background='white', foreground='black', activebackground='white', activeforeground='black')

filemenu = Menu(menubar, background='white', foreground='black', activebackground='white', activeforeground='black')
colormenu = Menu(menubar, background='white', foreground='black', activebackground='white', activeforeground='black')
objectmenu = Menu(menubar, background='white', foreground='black', activebackground='white', activeforeground='black')
objectmenu.add_command(label="Freestyle", command=lambda:setobject("freestyle"))
objectmenu.add_command(label="Rectangle", command=lambda:setobject("rectangle"))
objectmenu.add_command(label="Test", command=lambda:setcolor("Test"))
colormenu.add_command(label="Red", command=lambda:setcolor("red"))
colormenu.add_command(label="Green", command=lambda:setcolor("green"))
colormenu.add_command(label="Blue", command=lambda:setcolor("blue"))
colormenu.add_command(label="Black", command=lambda:setcolor("black"))
colormenu.add_command(label="Pink", command=lambda:setcolor("pink"))
filemenu.add_command(label="Clear", command=clear )
"""filemenu.add_command(label="Save", command=save_file)"""
filemenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="File", menu=filemenu,)
menubar.add_cascade(label="Colors", menu=colormenu,)
menubar.add_cascade(label="Object", menu=objectmenu,)
window.config(menu=menubar)

DrawingBoard = Canvas(window, width=1000, height=800,bg='white')
DrawingBoard.pack(expand = YES, fill = BOTH)
DrawingBoard.bind("<B1-Motion>", painting)
DrawingBoard.bind("<Button-1>", click)
DrawingBoard.bind("<ButtonRelease-1>", geometry)
message = Label(window, text="Press and Drag to draw on your drawing board!")
message.pack(side=BOTTOM)

window.mainloop()

"""


░█░█░█░█░█▀▀░█▀█
░█▄█░█▀█░█▀▀░█░█
░▀░▀░▀░▀░▀▀▀░▀░▀
░▀█▀░█░█░█▀▀
░░█░░█▀█░█▀▀
░░▀░░▀░▀░▀▀▀
░▀█▀░█▄█░█▀█░█▀█░█▀▀░▀█▀░█▀█░█▀▄
░░█░░█░█░█▀▀░█░█░▀▀█░░█░░█░█░█▀▄
░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀
░▀█▀░█▀▀
░░█░░▀▀█
░▀▀▀░▀▀▀
░█▀▀░█░█░█▀▀
░▀▀█░█░█░▀▀█
░▀▀▀░▀▀▀░▀▀▀     

"""
