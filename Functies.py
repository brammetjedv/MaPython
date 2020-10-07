def startLopen():
    print("waar ga ik heen?")

startLopen()

print("----------------------------------------")

def lopen(aantal):
        print("ik loop ", aantal, " stappen naar voren" )



lopen(3)

print("----------------------------------------")

def beweeg(x = 0):
    if (x > 0):
        print("ik loop ", x, " stap(pen) naar voren")
    elif (x < 0):
        print("ik loop ", (x - (2 * x)), " stap(pen) naar achteren" )        
    else:
        print("ik sta stil")

beweeg(7)
beweeg(-7)
