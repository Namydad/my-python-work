from textwrap import fill
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile

color='black'

window = Tk()
window.geometry("1900x1080")
window.title("Drawing Board")

def clear():
    DrawingBoard.delete('all')
    DrawingBoard.create_rectangle(0,0,1900,1080)

def setze(colorinfo):
    global color
    color = colorinfo

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
    DrawingBoard.create_oval(x1, y1, x2, y2,fill=color)
    


menubar = Menu(window, background='white', foreground='black', activebackground='white', activeforeground='black')

filemenu = Menu(menubar, background='white', foreground='black', activebackground='white', activeforeground='black')
colormenu = Menu(menubar, background='white', foreground='black', activebackground='white', activeforeground='black')
colormenu.add_command(label="Red", command=lambda:setze("red"))
colormenu.add_command(label="Green", command=lambda:setze("green"))
colormenu.add_command(label="Blue", command=lambda:setze("blue"))
filemenu.add_command(label="Clear", command=clear )
"""filemenu.add_command(label="Save", command=save_file)"""
filemenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="File", menu=filemenu,)
menubar.add_cascade(label="Colors", menu=colormenu,)
window.config(menu=menubar)

DrawingBoard = Canvas(window, width=1000, height=800,bg='white')
DrawingBoard.pack(expand = YES, fill = BOTH)
DrawingBoard.bind("<B1-Motion>", painting)
message = Label(window, text="Press and Drag to draw on your drawing board!")
message.pack(side=BOTTOM)

window.mainloop()