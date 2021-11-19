#Chess/Rice Problem

import math

chessboardspaces = 64
y = 1
for chessboardspaces in range(1,65,1):
    x=y+(y-1)
    print("Anzahl auf Feld Nummer " + str(chessboardspaces)+" ist gleich = "+str(y)+" Gesamt: "+str(x))
    y=y*2