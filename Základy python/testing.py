try:
  cislo1 = int(input("Zapiš dělenec: "))
  cislo2 = int(input("Zapiš dělitel: "))
  vysledek = cislo1 / cislo2
  print("Podíl:", vysledek)
except ZeroDivisionError:
  print("Chyba: Nelze dělit nulou!")
except ValueError:
  print("Chyba: Zadej platné celé číslo né písmeno!")