n = int(input("Bitte geben sie eine Zahl an von der Sie die Fakultät haben wollen: "))
factorial = 1
  
for i in range(1,n+1):
    factorial = factorial * i
      
print ("The factorial of n is : ",end="")
print (factorial)