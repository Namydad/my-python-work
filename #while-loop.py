#while-loop
"""
i = 1
while i < 100:
    print(str(i)+(". ")+("Ich soll im Unterricht nicht Schlafen"))
    i += 1
print("Ende der Schleife")
"""
#Countdown auf 0
"""
i = 10
while i > 0:
    print(str(i)+(". ")+("Ich soll im Unterricht nicht Schlafen"))
    i -= 1
print("Ende der Schleife")
"""
"""
import time
i = 10
print("Countdown Start")
while i >= 0:
    print(("Lift off in ")+ str(i) +("."))
    if i==3:
        print("ignition sequence started")
    i -= 1
    time.sleep(1)
print("Lift off!")
"""

#for loop
"""
for i in range(0, 100, 1):
  print(i,"Durchlauf: Ich soll im Unterricht nicht Schlafen")
"""
#for loop
import time
print("Countdown Start")
for i in range(10, 0, -1):
  print("Liftoff in:", i)
  time.sleep(1)
  if i==3:
      print("Ignition Sequence starting.") 
print("Take off!!!")