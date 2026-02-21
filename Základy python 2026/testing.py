# === Zpracování strukturovaných dat ===
# Nejprve vytvoříme ukázkový soubor:
with open("znamky.txt", "w") as f:
    f.write("Adam 1 2 1 3\n")
    f.write("Bára 2 1 1 2\n")
    f.write("Cyril 3 2 4 2\n")
    f.write("Dana 1 1 1 1\n")

# Nyní ho přečteme a zpracujeme:
print(f"{'Jméno':<10} {'Známky':<15} {'Průměr':>6}")
print("-" * 35)

with open("znamky.txt", "r") as f:
    for radek in f:
        casti = radek.strip().split()     # ["Adam", "1", "2", "1", "3"]
        jmeno = casti[0]                   # "Adam"
        znamky = [int(z) for z in casti[1:]]  # [1, 2, 1, 3]
        prumer = sum(znamky) / len(znamky)
        print(f"{jmeno:<10} {str(znamky):<15} {prumer:>6.2f}")