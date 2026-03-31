# Desetiminutovka: Váš kód sem 👇
pocet = 0
def pocet_cislic(n):
    global pocet
    pocet += 1
    if n < 10:
        return pocet
    else:
        return pocet_cislic(n//10) 
    
print(pocet_cislic(12453))