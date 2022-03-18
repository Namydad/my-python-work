from tkinter import *
from flask import template_rendered
import numpy as np
import os
import matplotlib.pyplot as plt


pfad=os.path.dirname(os.path.abspath(__file__))
filename=pfad+"/csv files/Temperatur-2021-Mannheim.csv"
with open(filename) as datei:
    temperatur = np.loadtxt(datei,delimiter=';',)

monat=[1,2,3,4,5,6,7,8,9,10,11,12]
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(monat,temperatur,c='red')
plt.scatter(monat,temperatur,marker="o")
for i in range(1,13):
    plt.annotate(str(temperatur[i-1]),(i,temperatur[i-1]))
    print(str(temperatur[i-1]))

plt.title("Temperatur")
plt.xlabel("Monat")
plt.ylabel("Temperatur")

plt.show()
