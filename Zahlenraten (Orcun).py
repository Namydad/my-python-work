import random
x = 0
y = 99
while True:
    r=random.randint(x,y)
    print(r)
    frage=int(input("[9] für größer als meine Zahl [1] für kleiner als meine Zahl [5] für Identisch"))

    if frage==9:
        y=r-1
    elif frage==1:
        x=r+1
    elif frage==5:
        print("Das Programm hat gewonnen")
        again=str(input("Wollen sie nochmal spielen [J/N]"))
        if again == 'J':
            x = 0
            y = 99
        else:
            print("Danke fürs spielen")
            break