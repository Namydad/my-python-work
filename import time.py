import time
print("Countdown Start")
for i in range(10, 0, -1):
  print("Liftoff in:", i)
  time.sleep(1)
  if i==3:
      print("Ignition Sequence starting.") 
print("Take off!!!")