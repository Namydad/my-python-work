import tkinter
from tkinter import *
import math
from unittest import TestProgram

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

"""
max < temperatur[i]
max <- temperatur

min > temperatur[i]
min <- temperatur

summe=summe+temperatur[i]

mittelwert=summe/len(temperatur)

"""

print(arrayAusgabe())

print("The Minimum is ",end="")
print(min(temperatur))

print("The Maximum is ",end="")
print(max(temperatur))

avg=sum(temperatur)/len(temperatur)
print("The Average is ",end="")
print(avg)

"""window.mainloop()"""