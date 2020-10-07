
import random

isRunning = True

while ( isRunning == True ) :

    print("herhaal dit")

    num = random.randrange(5)
    if ( num == 3 ) :
        isRunning = False
else:

    print("nee")

print("----------------------------------------------------------")

lijstA = ["yogurt", 19, False, 'f', 7.3]
lijstB = ["kaas", "blokkies"]

for waarde in lijstA:
    print(waarde)
print("----------------------------------------------------------")

print(lijstB)

for waarde in lijstB:
    waarde = "leuk"
    print(waarde)

print(lijstB)

print("----------------------------------------------------------")

for index in range( len( lijstB ) ):
    print( lijstB[index] )

print("----------------------------------------------------------")
    
