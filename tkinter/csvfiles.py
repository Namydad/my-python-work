from tkinter import *
import csv
import matplotlib.pyplot as plt

with open('/home/namydad/Schreibtisch/Prog Python/my-python-work/tkinter/csv files/Temperatur-2021-Mannheim.csv', newline='') as csvfile:
    temperatur = list(csv.reader(csvfile))

monat=[1,2,3,4,5,6,7,8,9,10,11,12]
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(monat,temperatur,c='red')

plt.title("Temperatur")
plt.xlabel("Monat")
plt.ylabel("Temperatur")

plt.show()
