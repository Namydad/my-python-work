import time

reihe=int(input("Welche Zahlenreihe wollen Sie? "))

for y in range(1,11,1):
    if y==10:
        print(y*reihe, "  ",end="")
    else:
        print(y*reihe, " | ",end="")

print("Fertig")