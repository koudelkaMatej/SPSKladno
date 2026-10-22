try:
    with open("neexistuje.txt", "r") as soubor:
        obsah = soubor.read()
except FileNotFoundError as chyba:
    print(f"❌ Soubor nenalezen!")
    print(f"   Detail: {chyba}")
    print(f"   Typ chyby: {type(chyba).__name__}")