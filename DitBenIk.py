print("Hello you! ik ben Bram de Vries")

print("Wat is jou naam?")


naam = input()

print("Hello" + " " + naam + "!")

print("Wil je de tijd en datum zien" + " " + naam + "?")


import datetime

tijd = datetime.datetime.now()

antwoord1 = input("schrijf yes of no: ") 
if antwoord1 == "yes" or antwoord1 == "Yes":
    print(tijd.strftime("%A") + " " + tijd.strftime("%d") + " " + tijd.strftime("%B") + " " + tijd.strftime("%X"))
elif antwoord1 != "yes" or antwoord1 != "Yes": 
    print("Ok... Dan niet")

print("Oke nu wat vragen over mij")

print("waar woon ik?")
print("A. Amsterdam")
print("B. Haarlem")
print("C. Abcoude")

antGoed = 0

antwoord2 = input("A   B  of  C?")
if antwoord2 == "A" or antwoord2 == "a":
    print("Ja goed!")
    antGoed += 1
elif antwoord2 == "B" or antwoord2 == "b":
    print("Nee helaas het was: A. Amsterdam")
elif antwoord2 == "C" or antwoord2 == "c":
    print("Nee helaas het was: A. Amsterdam")    
    
    
print("Hoeveel huisdieren heb ik?")
print("A. 1")
print("B. 4")
print("C. 3")


antwoord3 = input("A   B  of  C?")
if antwoord3== "C" or antwoord2 == "c":
    print("Ja goed!")
    antGoed += 1
elif antwoord3 == "B" or antwoord2 == "b":
    print("Nee helaas het was: C. 3")
elif antwoord3 == "A" or antwoord2 == "a":
    print("Nee helaas het was: C. 3")
    
    
    
print("hoe oud ben ik?")
print("A. 17")
print("B. 16")
print("C. 18")


antwoord4 = input("A   B  of  C?")
if antwoord4 == "A" or antwoord2 == "a":
    print("Ja goed!")
    antGoed += 1
elif antwoord4 == "B" or antwoord2 == "b":
    print("Nee helaas het was: A. 17")
elif antwoord4 == "C" or antwoord2 == "c":
    print("Nee helaas het was: A. 17")
    
    
    
    
    
print("Je had " + str(antGoed) + " antwoorden goed!")
    
    