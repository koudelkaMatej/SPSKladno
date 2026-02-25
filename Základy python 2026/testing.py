#TODO
vstup = int(input("Zadej číslo: "))
print("Zadal jsi číslo: ",vstup)
suma = 0
for radek in range(1,vstup+2):
    for sloupec in range(1,radek):
        print(sloupec,end="")
        suma += sloupec
    print()
print(suma)