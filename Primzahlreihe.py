# rechner gibt alle primzahlen aus in range von nutzer

ug=int(input("Geben Sie die Untergrenze ein\n->"))
og=int(input("Geben Sie die Obergrenze ein\n->"))

for i in range (ug,og+1,1):
    z=0
# z = zahl = primzahl?
    for z in range(2,i-1,1):  
        if i%z == 0:
            break
    else:
        print(i)