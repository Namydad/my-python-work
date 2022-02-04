from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - 10
    y0 = y - 10
    x1 = x + 10
    y1 = y + 10
    return canvasName.create_oval(x0, y0, x1, y1)

create_circle(100, 100, 20, myCanvas)
create_circle(50, 25, 10, myCanvas)
root.mainloop()