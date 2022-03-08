import tkinter
from tkinter import *
import math

"""window = Tk()
window.geometry("600x800")
window.title("Temperatur Mannheim")"""

temperatur=[0,2,3,5,6,1,2,3,4]

def arrayAusgabe():
    print(temperatur)
    print("Länge " + str(len(temperatur)))
    
    for i in range(0,len(temperatur)):
        print(temperatur[i])

"""    for element in temperatur:
        print(element)      """
print(arrayAusgabe())
print("The Minimum is ",end="")
print(min(temperatur))
print("The Maximum is ",end="")
print(max(temperatur))


"""window.mainloop()"""