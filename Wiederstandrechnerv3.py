# Wiederstandsrechner.py

"""
erstellt von Tobias
Updated am 15.10.21
Version 3.0
"""

#Wiederstandsrechner v3

import math

y = int(input("Wie viele Wiederstände? [1/2/0]"))
if y==1:
    r1 = float(input ("Bitte Widerstand eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand neu eingeben"))
elif y==2:
    r1 = float(input ("Bitte Widerstand 1 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    r2 = float(input ("Bitte Widerstand 2 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 and r2 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand 1 neu eingeben"))
        r2 = float(input("Bitte Wiederstand 2 neu eingeben"))
else:
    r1 = float(input ("Bitte Widerstand 1 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    r2 = float(input ("Bitte Widerstand 2 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    r3 = float(input ("Bitte Widerstand 2 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 and r2 and r3 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand 1 neu eingeben"))
        r2 = float(input("Bitte Wiederstand 2 neu eingeben"))
        r3 = float(input("Bitte Wiederstand 2 neu eingeben"))

        
if y == 1:
    x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    if x==1:
        print("Der Wiederstand Gesamt aus " + str(r1) + " bleibt: " + str(r1)) #Hier wird Wiederstand addiert da diese in einer Gerade so gerechnet werden
    else:
        print("Der Ersatzwiederstand aus " + str(r1) + " bleibt: " + str(r1)) # Bleibt gleich
elif y == 2:
    x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    if x==1:
        print("Der Wiederstand Gesamt aus " + str(r1) + " und " + str(r2) + " ist: " + str(r1 + r2)) #Hier wird Wiederstand addiert da diese in einer Gerade so gerechnet werden
    else:
        print("Der Ersatzwiederstand aus " + str(r1) + " und " + str(r2) + " ist: " + str(1/1/r1 + 1/1/r2)) # Hier wird Wiederstand x hoch -1 gerechnet
else:
    x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    if x==1:
        print("Der Wiederstand Gesamt aus " + str(r1) + " und " + str(r2) + " ist: " + str(r1 + r2 + r3)) #Hier wird Wiederstand addiert da diese in einer Gerade so gerechnet werden
    else:
        print("Der Ersatzwiederstand aus " + str(r1) + " und " + str(r2) + " und " + str(r3) + " ist: " + str(1/1/r1 + 1/1/r2 + 1/1/r3)) # Hier wird Wiederstand x hoch -1 gerechnet


"""
elif y>1:
    print("Wrong Input")
    y = int(input("Nur ein Wiederstand? [1/0]"))
elif y<0:
    print("Wrong Input")
    y = int(input("Nur ein Wiederstand? [1/0]"))
    r1 = float(input ("Bitte Widerstand 1 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    r2 = float(input ("Bitte Widerstand 2 eingeben: ")) # r ist der Radius der vom User eingegeben wird
    if r1 and r2 == 0: # r = 0 ist eine falsche Eingabe
        print ("Falsche Eingabe")
        r1 = float(input("Bitte Wiederstand 1 neu eingeben"))
        r2 = float(input("Bitte Wiederstand 2 neu eingeben"))

    elif x>1:
        print("Wrong Input")
        x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
    elif x<0:
        print("Wrong Input")
        x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
"""
