from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1900x1080")
window.title("Ja Nein Box")

def buttonclickY():
    lOutput['text'] = 'Nice!'
    buttonY['state'] = DISABLED
    buttonN['state'] = DISABLED
    buttonR['state'] = NORMAL
    buttonY['bg'] = 'grey'
    buttonN['bg'] = 'grey'
    
def buttonclickN():
    lOutput['text'] = 'Goodluck!'
    buttonY['state'] = DISABLED
    buttonN['state'] = DISABLED
    buttonR['state'] = NORMAL
    buttonY['bg'] = 'grey'
    buttonN['bg'] = 'grey'
def buttonclickR():
    buttonY['state'] = NORMAL
    buttonN['state'] = NORMAL
    buttonR['state'] = DISABLED
    buttonY['bg'] = 'green'
    buttonN['bg'] = 'red'
    lOutput['text'] = ''


labelQ = Label(window,text="Do you have Experience with Python and Tkinter?")
labelQ.place(x=100,y=100,)

buttonY= Button(window,bg="green",fg="black",text='Yes',command=buttonclickY)
buttonY.place(x=100,y=120,)

buttonN= Button(window,bg="red",fg="black",text='No',command=buttonclickN)
buttonN.place(x=150,y=120,)

buttonR= Button(window,bg="black",fg="white",text='Reset',command=buttonclickR,state='disabled',)
buttonR.place(x=100,y=150,)

lOutput= Label(window,bg=None,text='',fg='black',)
lOutput.place(x=100,y=200)

window.mainloop()