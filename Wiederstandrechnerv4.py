# Wiederstandsrechner.py

"""
erstellt von Tobias
Updated am 15.10.21
Version 3.0
"""

#Wiederstandsrechner v3

import math

input_string = input('Bitte die Wiederstände mir Leertaste getrennt eingeben: ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

if user_list == 0: 
    print("Wrong input")
    
x = int(input("Ist die Schaltung in Reihe? [1/0]: "))
if x == 1:
    print("Der Wiederstand Gesamt= ", sum(user_list))

