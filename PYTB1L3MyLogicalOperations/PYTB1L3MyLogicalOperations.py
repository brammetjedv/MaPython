name = "erwin henraat"
job = "teacher"
moneyInAccount = 1300

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.

def buyABrandNewMotorcycle():
    for index in range(100):
        print(":)")

if name == "erwin henraat" and job != None or moneyInAccount > 10000:
    buyABrandNewMotorcycle()

naam2 = "Bram"
job2 = "bezorger"
moneyInAccount2 = 200
watIkGraagWil = "Valve Index"
prijs = 1079


if naam2 == "Bram" and moneyInAccount2 >= prijs or prijs < moneyInAccount2:
    print("je hebt genoeg geld voor " + watIkGraagWil)
elif naam2 == "Bram" and moneyInAccount2 < prijs:
    if job2 == "bezorger":
        print("Ga sparen!")
    elif job2 == None:
        print("zoek een baan!")
