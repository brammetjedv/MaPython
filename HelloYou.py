print("Hello you! ik ben Bram de Vries")

print("Wat is jou naam?")


naam = input()

print("Hello" + " " + naam + "!")

print("Wil je de tijd en datum zien" + " " + naam + "?")


import datetime

tijd = datetime.datetime.now()

antwoord = input("schrijf yes of no: ") 
if antwoord == "yes" or antwoord == "Yes":
    print(tijd.strftime("%A") + " " + tijd.strftime("%d") + " " + tijd.strftime("%B") + " " + tijd.strftime("%X"))
elif antwoord != "yes" or antwoord != "Yes": 
    print("Ok... Dan niet")

print("Bedankt voor het doen van mijn script")

exit