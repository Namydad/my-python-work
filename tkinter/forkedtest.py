from tkinter import *   

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')
  
button = Button(tkWindow, text = 'Submit', bg='#ffffff', activebackground='#00ff00')  
button.pack()  
  
tkWindow.mainloop()