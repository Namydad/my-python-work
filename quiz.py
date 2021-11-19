pz=0
print ("- QUIZ -")
f1ra="a" #frag 1 richtige antwort
print("- FRAGE 1 -")
print("Wie viele Buchstaben hat das hawaiianische Alphabet?")
print("a. 12")
print("b. 6")
print("c. 28")
print("d. 34")
v=0
a= input("Antwort:")
if a == "a":
    print("Korrekt!")
    pz=pz+10
else:
    print("Versuchen Sie es nocheinmal")
    v=1
    while a != f1ra or v<=3:
        v=v+1
        print("- FRAGE 1 -")
        print("Wie viele Buchstaben hat das hawaiianische Alphabet?")
        print("a. 12")
        print("b. 6")
        print("c. 28")
        print("d. 34")
        a = input("Antwort:")
        pz=pz-2.5
print("- FRAGE 2 -")
v=0
f2ra="b"
print("Ein Bauer hat 16 Schafe. Fast alle sterben, außer 9. Wie viele Schafe bleiben übrig?	")
print("a. 7")
print("b. 9")
print("c. 6")
print("d. 16")
a= input("Antwort:")
if a == f2ra:
    print("Korrekt!")
    pz=pz+10
else:
    v=1
    print("Versuchen Sie es nocheinmal")
    while a != f2ra or v!=3:
        print("- FRAGE 2 -")
        print("Ein Bauer hat 16 Schafe. Fast alle sterben, außer 9. Wie viele Schafe bleiben übrig?	")
        print("a. 7")
        print("b. 9")
        print("c. 6")
        print("d. 16")
        v=v+1
        a= input("Antwort:")
        pz=pz-2.5

print(pz)