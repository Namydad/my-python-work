import random
nr = int(input("Welche Zahl soll von 0 bis 99 soll erraten werden? "))
guess = 0
y = 0 
x = 99
for guess in range(0,10,1):
    algorithmguess = random.randint(y,x)
    if algorithmguess == nr:
        print("Ihre Zahl " + str(nr) + " wurde erraten")
        guess = 11
    else:
        whatisit = int(input("Ist die Zahl größer(1) oder kleiner(2) als " + str(algorithmguess) + "?"))
        if whatisit==1:
            y=algorithmguess+1
        elif whatisit==2:
            x=algorithmguess-1
        else:
            print("Wrong Input new Guess made!")
            guess = -1
"""
    if guess == 11:
        again = int(input("Wollen Sie nochmal spielen? (0/1)"))
        if again == 0:
            print("Thanks for Playing!")
        if again == 1:
            print("Time for another round!")
            guess = 0
            y = 0 
            x = 99
            algorithmguess = 0
            nr = int(input("Welche Zahl soll von 0 bis 99 soll erraten werden? "))
"""

    
