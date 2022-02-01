from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1900x1080")
window.title("Buttons-Test")

def helloCallBack(B):
    msg = messagebox.showinfo( "Hello Python", B)

A=Button(window, text = "Please press me", bg="red", activebackground="black",fg="black", activeforeground="white")
A.place(x= 50, y = 200)

B = Button(window, text = "Hello world", bg="yellow") #"""command = helloCallBack"""
B.place(x = 100,y = 150)
window.mainloop()

