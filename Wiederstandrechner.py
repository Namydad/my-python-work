# Wiederstandsrechner.py

"""
erstellt von Tobias
am 8.10.21
Version 1.0
"""

#Wiederstandsrechner

import math

y = int(input("Nur ein Wiederstand? [1/0]"))
if y==1:
    r1 = float(input ("Bitte Widerstand 1 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand neu eingeben"))
else:
    r1 = float(input ("Bitte Widerstand 1 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    r2 = float(input ("Bitte Widerstand 2 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand neu eingeben"))
    if r2 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r2 = float(input("Bitte Wiederstand größe neu Eingeben: "))
        
if y == 1:
    x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    if x==1:
        print("Der Wiederstand Gesamt aus " + str(r1) + " ist: " + str(r1)) #Hier wird Wiederstand addiert da diese in einer Gerade so gerechnet werden
    elif x>1:
        print("Wrong Input")
    elif x<0:
        print("Wrong Input")
    else:
        print("Der Ersatzwiederstand aus " + str(r1) + " ist: " + str(r1)) # Bleibt gleich
else:
    x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    if x==1:
        print("Der Wiederstand Gesamt aus " + str(r1) + " und " + str(r2) + " ist: " + str(r1 + r2)) #Hier wird Wiederstand addiert da diese in einer Gerade so gerechnet werden
    elif x>1:
        print("Wrong Input")
    elif x<0:
        print("Wrong Input")
    else:
        print("Der Ersatzwiederstand aus " + str(r1) + " und " + str(r2) + " ist: " + str(1/1/r1 + 1/1/r2)) # Hier wird Wiederstand x hoch -1 gerechnet
