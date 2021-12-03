#Zahlenraten
import random
import math
attempt = 1
active = True
number = 5
while active:
    print(attempt)
    guess = int(input("Guess the Number"))
    if number > guess:
        print("Die Zahl ist größer als was sie geratet haben")
    if number < guess:
        print("Die Zahl ist kleiner als was sie geratet haben")
    if guess == number:
        active = False
    if (attempt == 7):
        if guess == number:
            attempt =-1
            active = False
        else:
            active = False
    attempt = attempt + 1

if attempt == 8:
    print("Leider nicht Richtig! Starte eine neue Runde.")

if guess == number:
    print("Richtig")