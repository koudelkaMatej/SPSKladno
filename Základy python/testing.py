class Utulek:
    def __init__(self, nazev, kapacita, zvirata=None):
        self.nazev = nazev
        self.kapacita = kapacita
        self.zvirata = [] if zvirata is None else zvirata
    def pridej_zvire(self, zvire):
        if len(self.zvirata) < self.kapacita:
            if zvire in self.zvirata:
                print(f"{zvire} už je v útulku.")
            else:
                self.zvirata.append(zvire)
                print(f"{zvire} byl přidán do útulku.")
        else:
            print("Útulek je plný!")

    def odeber_zvire(self, zvire):
        if zvire in self.zvirata:
            self.zvirata.remove(zvire)
            print("Zviře bylo odebráno")
        else:
            print("Zvíře v utulku není")

    def __str__(self):
        return f"Utulek '{self.nazev}' s kapacitou {self.kapacita} a zviraty: {', '.join(self.zvirata) if self.zvirata else 'žádná zvířata'}"       
zv1 = "Jezevec"
Utulek_bez_zvirat = Utulek("Happy Paws", 5)
Utulek_s_zviraty = Utulek("Animal Haven", 3, [zv1,"Kočka"])
Utulek_s_zviraty.pridej_zvire("Rybička")
Utulek_s_zviraty.pridej_zvire("Kytka")
Utulek_s_zviraty.odeber_zvire("Kytka")
Utulek_s_zviraty.odeber_zvire("Kočka")
print(Utulek_s_zviraty)