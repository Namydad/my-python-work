#ausdruecke_und_operatoren.py

"""
erstellt von Tobias
am 24.09.21
Version 1.0
"""

#Ausdrücke und Operatoren

x = 5+2 # Addieren
print("x =",x)
print(type(x))

y = 5-2 # Subtrahieren
print("y =",y)
print(type(y))

d = 5*2 # Multiplizieren
print("d =",d)
print(type(d))

g = 5/2 # Dividieren #g ist float
print("g =",g)
print(type(g))

"""
Rechnen mit Floats in Python 2.7
g = float(5)/float(2) # Dividieren #g ist float
print("g =",g)
print(type(g))
"""

g = 5/5 # G ist trotzdem Float (1.0) #neues g überschreibt altes g
print("g =",g)
print(type(g))

u = 5 // 2 #ganzzahldivision
print("u =",u)
print(type(u))

z = 5 % 2 #zahl-ganzzahldivision=rest
print("z =",z)
print(type(z))

r = 5**5 #potenzieren 5 hoch 5
print("5 hoch 5 =",r)
print(type(r))
