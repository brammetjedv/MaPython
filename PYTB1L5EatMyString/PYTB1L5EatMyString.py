def eatMe(text):
    text = text[0:len(text)-1]
    print(text)
    while len(text) > 0:
        eatMe(text)
        break
        
        
        
        

eatMe("Eet me op")
eatMe("Hey het werkt!")
