<<<<<<< HEAD
green = "\33[1;32m"
reset = "\33[0m"
print(f"{green}Hello world{reset} už normal 💖")
=======
# ZeroDivisionError ValueError
try:
    a = 5
    b = int(input("Zadej číslo: "))
    c = a / b
    print("Výsledek:", c)
except ZeroDivisionError:
    print("Chyba: Nelze dělit nulou!")
except ValueError:
    print("Chyba: Neplatný vstup, zadejte číslo!")
>>>>>>> a721b05 (main)
