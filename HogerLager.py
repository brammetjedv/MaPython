# doel:
# een spelletje maken waar de speler moet raden of het volgende getal
# hoger of lager word.

# Stappenplan:
# - Een random nummer van 1 t/m 10 maken.
# - Toon speler het getal en vrag of het volgende getal hoger of lager wordt
# - Er moet een volgend getal gegenreerd worden.
# - Er moet gekeken worden of de speler gelijk heeft
# - De speler moet weten of hij of zij gewonnen of verloren heeft

import random

randomGetal = random.randrange(1, 11)

print("Het getal van 1 t/m 10 is: ", randomGetal)
print("Wordt het volgende getal hoger [H] of lager [L]?")

antwoord = input()

randomGetal2 = random.randrange(1, 11)

if ( (randomGetal2 > randomGetal) and antwoord == "H"):
    print("Het nieuwe getal is", randomGetal2)
    print("Het was inderdaad hoger!")
elif ( (randomGetal2 < randomGetal) and antwoord == "L"):
    print("Het nieuwe getal is", randomGetal2)
    print("Het was inderdaad lager!")     
elif ( (randomGetal2 > randomGetal) and antwoord == "L"):
    print("Het nieuwe getal is", randomGetal2)
    print("Nee helaas het was Hoger!")
elif ( (randomGetal2 < randomGetal) and antwoord == "H"):
    print("Het nieuwe getal is", randomGetal2)
    print("Nee helaas het was Lager!")
else:
    print("Het nieuwe getal is", randomGetal2)
    print("Wat een geluk! Het was exact hetzelfde!")


