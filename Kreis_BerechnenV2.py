#Kreis_BerechnenV2.py

"""
erstellt von Tobias
am 5.10.21
Version 2.0
"""

#Kreis Berechnen 

from math import pi # Importiert die Zahl für PI von Pythons Mathe Script
r = float(input ("Bitte Radius größe Eingeben: ")) # r ist der Radius der vom User eingegeben wird

if r == 0: # r = 0 ist eine falsche Eingabe
    print ("Falsche Eingabe")
    r = float(input("Bitte Radius größe neu Eingeben: "))

x = int(input("Wollen sie die Fläche des Kreises [1/0]: "))
if x == 1:
    print ("Die Fläche des Kreises mit Radius " + str(r) + " is: " + str(pi * r**2)) # Hier wird die normale Matheformel für die Fläche benutzt 2xPIxr hoch 2
    y = int(input("Wollen sie den Umfang des Kreises [1/0]: "))
    if y == 1: 
        print ("Der Umfang des Kreises mit Radius " + str(r) + " is: " + str(pi * r * 2)) # Hier wird der Umfang berechnet mit der formel PI x R x 2
        z = int(input("Wollen sie den Radius des Kreises [1/0]: "))
        if z == 1:
            print ("Der Durchmesser des Kreises mit Radius " + str(r) + " is: " + str(r * 2)) # Durchmesser = R x 2 ## + str(r) + gibt nochmal die angegebene Zahl im Satz wieder daher wird der Satz in 2 Teile getrennt "Anfangssatz" "="
    elif y == 0:
        z = int(input("Wollen sie den Radius des Kreises [1/0]: "))
        if z == 1:
            print ("Der Durchmesser des Kreises mit Radius " + str(r) + " is: " + str(r * 2)) # Durchmesser = R x 2 ## + str(r) + gibt nochmal die angegebene Zahl im Satz wieder daher wird der Satz in 2 Teile getrennt "Anfangssatz" "="
elif x == 0:
    y = int(input("Wollen sie den Umfang des Kreises [1/0]: "))
    if y == 1: 
        print ("Der Umfang des Kreises mit Radius " + str(r) + " is: " + str(pi * r * 2)) # Hier wird der Umfang berechnet mit der formel PI x R x 2
        z = int(input("Wollen sie den Radius des Kreises [1/0]: "))
        if z == 1:
            print ("Der Durchmesser des Kreises mit Radius " + str(r) + " is: " + str(r * 2)) # Durchmesser = R x 2 ## + str(r) + gibt nochmal die angegebene Zahl im Satz wieder daher wird der Satz in 2 Teile getrennt "Anfangssatz" "="
    elif y == 0:
        z = int(input("Wollen sie den Radius des Kreises [1/0]: "))
        if z == 1:
            print ("Der Durchmesser des Kreises mit Radius " + str(r) + " is: " + str(r * 2)) # Durchmesser = R x 2 ## + str(r) + gibt nochmal die angegebene Zahl im Satz wieder daher wird der Satz in 2 Teile getrennt "Anfangssatz" "="
else:
    print("Keine Output ausgewählt")
