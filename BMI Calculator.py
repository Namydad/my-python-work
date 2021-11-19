# BMI Calculator.py

"""
erstellt von Tobias
Updated am 15.10.21
Version 3.0
"""

#BMI Calculator

import math
y = float(input("Bitte geben Sie ihr Gewicht an: "))
x = float(input("Bitte geben Sie ihre Größe an: "))
bmi = float(y/x**2*10000)
print(("Ihr Body Mass Index beträgt: ") + str(bmi))

if bmi > float(18.4) or bmi < float(25.1):
    print("Sie haben einen Idealen BMI betrag")
elif bmi < float (18.5):
    print("Sie haben leider einen unterdurschnittlichen Body Mass Index schauen sie mehr auf Ihre geringe kcal Zufuhr und sprechen sie mit einem Ernährungsberater oder Arzt")
elif bmi > float (25):
    print("Sie haben leider einen überdurschnittlichen Body Mass Index achten sie auf Ihre hohe kcal Zufuhr und sprechen sie mit einem Ernährungsberater oder Arzt")

print(("Warnung!: ") + ("Bedenken Sie bitte das der Body Mass Index eine Gewichtsrechnung ist die keine Pflicht sondern ein auf die Situationbezogenen vorschlag für ein Ideal geben soll."))