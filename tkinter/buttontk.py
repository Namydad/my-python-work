from enum import auto
from tkinter import *

from tkinter import messagebox

window = Tk()
window.geometry("1900x1080")
window.title("Buttons-Test")

A=Button(window, text = "Please press me", bg="red")
A.place(x=100,y=100)


B = Button(window, text = "Hello world", bg="yellow") #"""command = helloCallBack"""
B.place(x = 100,y = 150)
window.mainloop()