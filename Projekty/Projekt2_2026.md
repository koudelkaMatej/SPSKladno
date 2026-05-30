# Projekt 2 – Grafická Python aplikace: Hra nebo Systém (2. ročník / 2026)

## Cíl projektu

Navázat na konzolovou aplikaci z 1. ročníku a přidat **grafickou vrstvu** – buď jako **hru v Pygame**, nebo jako **desktopový systém v PyQt**. Zároveň přejít na **objektově orientované programování (OOP)** – kód bude postavený na třídách a metodách. Skupiny jsou stejné jako v 1. ročníku a pracují ve stejném repozitáři, který rozšíří.

---

## Volba technologie – na začátku roku

Každá skupina si na začátku školního roku vybere **jednu ze dvou cest**:

| Cesta | Technologie | Vhodné pro skupiny, jejichž P1 bylo... |
|-------|-------------|----------------------------------------|
| **Hra v Pygame** | Python + Pygame | Kvíz, textová adventura, hra nebo evidence s herními prvky |
| **Desktopový systém v PyQt** | Python + PyQt6 | Evidence, pokladna, objednávkový systém, správce dat |

> Volbu skupiny schvaluje učitel **do konce září**. Volbu lze zdůvodnit – pokud má skupina silný argument pro jinou cestu, učitel zvýší.

---

## Nové v 2. ročníku – OOP

V 1. ročníku jste psali funkcionálně. Nyní přechází kód na **objekty a třídy**.

### Co se od vás očekává:
- Alespoň **2 vlastní třídy** s atributy a metodami
- Třídy zastupují objekty z problémové domény (např. `Hrac`, `Polozka`, `Hra`, `Databaze`, `Okno`)
- Data přestávají být v globálních proměnných – jsou uložena v atributech objektů
- Kód z 1. ročníku **refaktorujte do tříd** – nepište znovu od nuly, stavte na předchozí práci
- Každá třída a metoda musí mít **docstring**

### Příklad pro skupinu „Pokladna":

```python
class Polozka:
    """Reprezentuje jednu položku v košíku pokladny."""

    def __init__(self, nazev: str, cena: float, mnozstvi: int = 1):
        self.nazev = nazev
        self.cena = cena
        self.mnozstvi = mnozstvi

    def celkova_cena(self) -> float:
        """Vrátí celkovou cenu položky (cena × množství)."""
        return self.cena * self.mnozstvi


class Kosik:
    """Spravuje seznam položek v košíku."""

    def __init__(self):
        self.polozky: list[Polozka] = []

    def pridej(self, polozka: Polozka) -> None:
        """Přidá položku do košíku."""
        self.polozky.append(polozka)

    def celkem(self) -> float:
        """Vrátí součet cen všech položek v košíku."""
        return sum(p.celkova_cena() for p in self.polozky)
```

---

## Organizace práce

### Skupiny
- **Stejné skupiny jako v 1. ročníku** (3–4 členové)
- Práce pokračuje ve **stejném gitovém úložišti**
- Repozitář dostane novou větev `develop-r2` pro práce 2. ročníku

### Workflow – stejný jako v 1. ročníku

```
main (vždy funkční – merge pouze přes PR)
 │
 ├── develop-r2 (integrační větev 2. ročníku)
 │     │
 │     ├── feature/oop-refaktoring
 │     ├── feature/herni-smycka
 │     ├── feature/gui-menu
 │     └── feature/ukládání-dat
```

### Pravidla pro commity

Stejná jako v 1. ročníku:

```
✅  feat: přidána třída Hrac s metodou pohyb()
✅  refactor: menu přepsáno do třídy HlavniMenu
✅  fix: opravena chyba v metodě uloz_data()
✅  docs: doplněny docstringy ke třídě Kosik

❌  update
❌  hotovo
❌  oprava2_finalni_OPRAVDU
```

---

## Role ve skupině

Každý člen **v každém sprintu zastává jinou roli** – všichni tak do konce roku vyzkouší každou roli přesně jednou.

Za každý sprint dostane žák **1 známku** hodnocenou individuálně podle toho, jak plnil svoji aktuální roli.

---

### 🟦 Role 1: Vedoucí projektu *(Project Lead)*

**Zodpovídá za:**
- Na začátku sprintu vytvoří **GitHub Issues** pro každý požadavek, přiřadí je členům
- Vytvoří větev `develop-r2` (pokud neexistuje), hlídá workflow
- **Merguje schválené Pull Requesty** do `develop-r2`
- Na konci sprintu otevře **Release PR** (`develop-r2` → `main`) a prezentuje výsledky
- Pomáhá ostatním při blockerech, řeší konflikty při mergi
- **Prezentuje práci týmu** při kontrolním termínu

---

### 🟩 Role 2: Analytik / Dokumentátor *(Tech Writer + Analyst)*

**Zodpovídá za:**
- Napíše nebo aktualizuje **specifikaci featury** (vstup, výstup, okrajové případy)
- Ke každé featurě vytvoří nebo aktualizuje **vývojový diagram**
- Aktualizuje `README.md` – jak projekt spustit, co přibylo
- Píše nebo kontroluje **docstringy** ke třídám a metodám
- Udržuje dokumentaci aktuální (co projekt umí, jak se ovládá)

---

### 🟨 Role 3: Vývojář *(Developer)*

**Zodpovídá za:**
- Pracuje vždy ve **feature větvi**
- Implementuje zadanou featuru dle specifikace analytika
- **Refaktoruje kód** z 1. ročníku do tříd (OOP)
- Kód je čitelný – smysluplné názvy, bez globálních proměnných tam, kde to dává smysl
- Po dokončení otevře **Pull Request** a požádá testera o review
- Opraví připomínky z code review

---

### 🟥 Role 4: Tester / Grafik *(QA + UI Designer)*

Tato role má **dvě části** – obě jsou povinné:

**Jako tester:**
- Testuje implementovanou featuru (normální vstupy, hraniční stavy, špatné vstupy)
- Nalezené chyby zapíše jako **komentář do Pull Requestu**
- Provede **code review** (čitelnost, OOP správnost, docstringy, shoda se specifikací)
- Schválí nebo zamítne PR s komentáři

**Jako grafik / UI designer:**
- **Pro Pygame:** Připravuje grafické assety (sprity, pozadí, tlačítka) v externím editoru (GIMP, Piskel, Malování) a od 3. sprintu je integruje do kódu
- **Pro PyQt:** Navrhuje rozložení oken, volí widgety, ladí vizuál formulářů a tabulek

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **Tester a Analytik se sloučí** do jedné.

---

## Sprinty a kontrolní termíny

| Sprint | Období | Co se buduje | GitHub aktivita |
|--------|--------|-------------|-----------------|
| **1** | Začátek února | OOP refaktoring P1, základní třídní struktura projektu, první GUI okno | Nové Issues, feature větve, PR do develop-r2 |
| **2** | Polovina března | Funkční jádro – herní smyčka (Pygame) nebo hlavní okno s daty (PyQt) | PRy s review, mergování, rotace rolí |
| **3** | Konec dubna | Grafika propojená s kódem, interakce, ukládání dat přes třídy | PRy, oprava chyb, code review |
| **4** | Začátek června | Finální funkční aplikace, dokumentace kompletní, Release PR do main | Release PR, peer review, prezentace |

Při každém kontrolním termínu může učitel (jako „zákazník") **přidat nebo změnit požadavky**.

---

## Doporučený postup práce – příklad pro 4 členy (A, B, C, D)

### Sprint 1 – OOP refaktoring a základ (začátek února)

| Člen | Role | Co dělá |
|------|------|---------|
| **A** | Vedoucí | Vytvoří `develop-r2`, nastaví Issues pro sprint 1, rozdělí úkoly, nastaví strukturu složek projektu, prezentuje |
| **B** | Analytik | Navrhne **třídní diagram** (jaké třídy, jaké metody), napíše specifikaci refaktoringu, aktualizuje README |
| **C** | Vývojář | Vytvoří větev `feature/oop-refaktoring`, přepíše kód z P1 do tříd dle specifikace, otevře PR |
| **D** | Tester/Grafik | Otestuje refaktorovaný kód (chová se stejně jako P1?), provede code review, zároveň zahájí tvorbu grafiky / wireframu GUI |

### Sprint 2 – Jádro aplikace (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **B** | Vedoucí | Merguje PRy z S1, vytvoří Issues pro S2, hlídá funkčnost, prezentuje |
| **C** | Analytik | Specifikuje **hlavní obrazovku / herní smyčku**, flowcharty interakcí, doplní docstringy |
| **D** | Vývojář | Implementuje herní smyčku (Pygame) nebo hlavní okno s daty (PyQt), otevře PR |
| **A** | Tester/Grafik | Testuje jádro, code review, pokračuje v přípravě grafiky / UI návrhu |

### Sprint 3 – Propojení grafiky a dat (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **C** | Vedoucí | Kontroluje propojení grafiky s kódem, řeší bugy, prezentuje |
| **D** | Analytik | Specifikuje ukládání dat přes třídy, aktualizuje dokumentaci, doplní schémata |
| **A** | Vývojář | Implementuje ukládání/načítání dat přes metody tříd (`feature/ukladani`), otevře PR |
| **B** | Tester/Grafik | Testuje ukládání dat (chybné soubory, prázdné vstupy), finalizuje grafiku / UI widgety |

### Sprint 4 – Finalizace (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **D** | Vedoucí | Otevře Release PR (`develop-r2` → `main`), koordinuje finální opravy, prezentuje výsledek |
| **A** | Analytik | Finalizuje `README.md`, doplní chybějící docstringy, zkontroluje třídní diagramy |
| **B** | Vývojář | Refaktoring – vylepší čitelnost, odstraní duplicity, opraví zbývající chyby z Issues |
| **C** | Tester/Grafik | Finální testování, zkontroluje Issues, zajistí, že vše funguje – hra/app jde spustit |

---

## Funkční požadavky

### Společné pro obě cesty (Pygame i PyQt)

| Požadavek | Popis |
|-----------|-------|
| **OOP – min. 2 třídy** | Alespoň dvě vlastní třídy s atributy a metodami; každá má docstring |
| **Navázání na P1** | Kód z 1. ročníku je refaktorován do tříd, logika aplikace zachována |
| **Grafické rozhraní** | Aplikace má okno – ne konzoli |
| **Ukládání dat** | Data se ukládají do souboru (JSON, CSV nebo TXT) a při spuštění se načtou |
| **Ošetření chyb** | Špatný vstup neukončí aplikaci pádem |

### Pygame – specifické požadavky

| Požadavek | Popis |
|-----------|-------|
| **Herní smyčka** | `while running:` smyčka s `event handling`, `update()` a `render()` |
| **Hlavní menu** | Grafické menu s tlačítky ovladatelnými myší nebo klávesnicí |
| **Pohyb / interakce** | Hráč nebo objekt se pohybuje a reaguje na vstupy |
| **Grafika** | Vlastní sprity (ne pouze barevné obdélníky), načítané ze souborů |
| **Skóre nebo stav hry** | Aplikace sleduje a zobrazuje stav (skóre, životy, postup) |

### PyQt – specifické požadavky

| Požadavek | Popis |
|-----------|-------|
| **Hlavní okno** | `QMainWindow` nebo `QWidget` s navigací (menu lišta nebo záložky) |
| **Zobrazení dat** | Data z P1 zobrazena v tabulce (`QTableWidget`) nebo listu (`QListWidget`) |
| **Formulář** | Přidávání/editace záznamu přes formuláře (`QLineEdit`, `QComboBox`, ...) |
| **Signály a sloty** | Alespoň 3 tlačítka propojená se signály/sloty (přidat, smazat, uložit...) |
| **Validace vstupu** | Prázdný nebo neplatný vstup je zachycen a zobrazí chybovou hlášku |

### Dokumentace (povinná součást)
- Z **Git historie** musí být patrné, kdo co napsal
- Každá **třída a metoda** má docstring
- `README.md` obsahuje: co aplikace dělá, jak ji spustit, seznam hlavních tříd
- Přiloženy **třídní diagramy** nebo alespoň seznam tříd s metodami (jako tabulka nebo obrázek)
- Přiloženy **flowcharty** klíčových procesů (aktualizace nebo nové pro P2)

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **Python 3** – OOP, třídy, metody, dědičnost
- **Pygame** (pro herní cestu) nebo **PyQt6** (pro systémovou cestu)
- **Standardní knihovny Pythonu** (`os`, `json`, `csv`, `random`, `math`, `datetime`)
- **Git** + **GitHub** pro správu verzí
- Grafické editory pro tvorbu spritů nebo UI wireframů (GIMP, Piskel, Figma – jen návrh)

### ❌ Zakázáno
- Jiné herní enginy nebo GUI frameworky (Tkinter je výjimka – jen po dohodě s učitelem)
- Jiné programovací jazyky
- AI generátory celých bloků kódu
- Kopírování cizího kódu bez pochopení

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí OOP v Pythonu.**

---

## Hodnocení

### Známky za sprinty – individuální

Každý žák získá **4 známky** (1 za každý sprint). Hodnotí se výhradně aktuální role:

| Kritérium | Vedoucí | Analytik | Vývojář | Tester/Grafik |
|-----------|---------|----------|---------|---------------|
| Splnění role | ✅ | ✅ | ✅ | ✅ |
| Kvalita výstupu | Issues + merge | Spec. + diagramy | OOP správnost + funkčnost | Testování + grafika |
| Práce s Gitem | Merge, Release PR | Commity dokumentace | Feature větve, commity | Komentáře v PR |
| Týmová spolupráce | Koordinace | Komunikace spec. | Reakce na review | Zpětná vazba |
| Prezentace | ✅ | – | – | – |

### Vzájemné hodnocení skupin (peer review)

Při každém kontrolním termínu skupiny navzájem **testují aplikace ostatních skupin** a hledají chyby.

#### Nalezené chyby ve VAŠEM projektu *(motivace dělat kvalitně)*
- Za každých **5 nalezených chyb** ve vaší aplikaci dostane **celý tým známku 5** (váha 1)

#### Nalezení chyb v CIZÍM projektu *(motivace pečlivě testovat)*
- Za každé **2 nalezené chyby** v projektu jiné skupiny dostane **jednotlivec, který chybu našel, známku 1** (váha 1)

> **Pravidla peer review:**
> - Chyba musí být **reálná a ověřitelná** – učitel rozhoduje sporné případy
> - Duplicitní hlášení stejné chyby se nepočítá
> - Chyby se zapisují **jako GitHub Issue** v repozitáři kontrolované skupiny (label: `peer-review`)
> - Issue musí být vytvořeno **do konce hodiny** po odprezentování
> - Kdo vytvoří Issue jako **první**, má přednost při duplicitách
>
> **Formát GitHub Issue:**
> - **Název:** `[Peer review] Stručný popis chyby`
> - **Popis:** Co se stane, jak to reprodukovat, co se očekávalo
> - **Label:** `peer-review`
>
> Příklady:
> ```
> [Peer review] Aplikace padá při kliknutí na tlačítko „Přidat" s prázdným polem
> [Peer review] Třída Hrac nemá žádný docstring
> [Peer review] Hra se při skóre 0 zasekne v nekonečné smyčce
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti** (větev `main`)
- Aplikace musí jít **spustit na školních počítačích** bez dodatečné instalace
- Z **Git historie a Pull Requestů** musí být patrné, kdo co dělal a v jaké roli
- Repozitář obsahuje: zdrojový kód, `README.md`, třídní diagramy, flowcharty, uzavřená Issues z peer review

---

---

# 🗺️ Roadmapa Sprintu 1 – krok za krokem

> Tato sekce ukazuje **přesně co, kdy a jak** by měl každý člen týmu udělat během prvního sprintu.  
> Příklad je pro skupinu s tématem **„Pokladna"** (PyQt cesta) – pro Pygame je postup analogický.  
> A = Vedoucí, B = Analytik, C = Vývojář, D = Tester/Grafik.  
> Časový rámec: **2–3 týdny**.

---

## 📅 Den 1 – Kick-off

### Celý tým společně:
- [ ] Rozhodnout: **Pygame nebo PyQt?**
- [ ] Projít kód z P1 a domluvit se, **co se přepíše do tříd**
- [ ] Každý si stáhne aktuální repozitář:
  ```bash
  git clone https://github.com/SPS-Kladno-2026/skupina-pokladna.git
  cd skupina-pokladna
  git checkout main
  git pull
  ```

### 🟦 Vedoucí (A) – den 1:
- [ ] Vytvořit větev `develop-r2`:
  ```bash
  git checkout -b develop-r2
  git push -u origin develop-r2
  ```
- [ ] Nastavit na GitHubu **branch protection** pro `main` (PR + 1 review)
- [ ] Vytvořit **GitHub Issues** pro sprint 1:

  | # | Název Issue | Přiřazeno |
  |---|-------------|-----------|
  | 5 | `Třídní diagram – návrh tříd pro P2` | B (Analytik) |
  | 6 | `OOP refaktoring konzolové logiky z P1` | C (Vývojář) |
  | 7 | `Testování refaktorovaného kódu + wireframe GUI` | D (Tester/Grafik) |

---

## 📅 Dny 2–4 – Analytik navrhuje třídy

### 🟩 Analytik (B):

**Krok 1 – Vytvořit větev:**
```bash
git checkout develop-r2
git checkout -b docs/tridni-diagram-sprint1
```

**Krok 2 – Napsat třídní diagram** (soubor `docs/tridni_diagram.md`):

```markdown
## Třídní diagram – Pokladna P2

### Třída: Polozka
- Atributy: nazev (str), cena (float), mnozstvi (int)
- Metody: celkova_cena() → float

### Třída: Kosik
- Atributy: polozky (list[Polozka])
- Metody: pridej(polozka), odeber(index), celkem() → float, uloz(soubor), nacti(soubor)

### Třída: HlavniOkno (QMainWindow)
- Atributy: kosik (Kosik), tabulka (QTableWidget)
- Metody: obnov_tabulku(), pridej_polozku(), odeber_polozku(), zaplatit()
```

**Krok 3 – Commit a push:**
```bash
git add docs/tridni_diagram.md
git commit -m "docs: třídní diagram pro OOP refaktoring pokladny"
git push -u origin docs/tridni-diagram-sprint1
```

**Krok 4 – Otevřít Pull Request** do `develop-r2`, Reviewer: A (Vedoucí), closes #5

---

## 📅 Dny 3–8 – Vývojář přepisuje logiku do tříd

### 🟨 Vývojář (C):

**Krok 1 – Větev:**
```bash
git checkout develop-r2
git pull origin develop-r2
git checkout -b feature/oop-refaktoring
```

**Krok 2 – Přepsat logiku z P1 do tříd** (soubor `src/modely.py`):

```python
import json


class Polozka:
    """Reprezentuje jednu položku v košíku."""

    def __init__(self, nazev: str, cena: float, mnozstvi: int = 1):
        self.nazev = nazev
        self.cena = cena
        self.mnozstvi = mnozstvi

    def celkova_cena(self) -> float:
        """Vrátí cenu × množství."""
        return self.cena * self.mnozstvi

    def to_dict(self) -> dict:
        """Převede položku na slovník pro uložení do JSON."""
        return {"nazev": self.nazev, "cena": self.cena, "mnozstvi": self.mnozstvi}


class Kosik:
    """Spravuje seznam položek v košíku pokladny."""

    def __init__(self):
        self.polozky: list[Polozka] = []

    def pridej(self, polozka: Polozka) -> None:
        """Přidá položku do košíku."""
        self.polozky.append(polozka)

    def odeber(self, index: int) -> None:
        """Odebere položku na daném indexu."""
        if 0 <= index < len(self.polozky):
            self.polozky.pop(index)

    def celkem(self) -> float:
        """Vrátí celkovou cenu všech položek v košíku."""
        return sum(p.celkova_cena() for p in self.polozky)

    def uloz(self, soubor: str) -> None:
        """Uloží košík do JSON souboru."""
        with open(soubor, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.polozky], f, ensure_ascii=False, indent=2)

    def nacti(self, soubor: str) -> None:
        """Načte košík z JSON souboru. Pokud soubor neexistuje, košík zůstane prázdný."""
        try:
            with open(soubor, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.polozky = [Polozka(**d) for d in data]
        except FileNotFoundError:
            pass
```

**Krok 3 – Průběžné commity:**
```bash
git add src/modely.py
git commit -m "feat: třída Polozka s metodami celkova_cena a to_dict"

git add src/modely.py
git commit -m "feat: třída Kosik – pridej, odeber, celkem, uloz, nacti"
```

**Krok 4 – Pull Request** do `develop-r2`, closes #6

---

## 📅 Dny 6–10 – Tester testuje, Grafik navrhuje UI

### 🟥 Tester/Grafik (D):

**Jako tester:**
- Otestuje třídy: přidání, odebrání, uložení, načtení, prázdný košík, neexistující soubor
- Zapiš komentáře do PR #6: co funguje, co ne
- Schval nebo zamítni PR

**Jako grafik (PyQt cesta):**
- Nakresli **wireframe hlavního okna** (na papír, Figma nebo draw.io):
  - Tabulka s položkami
  - Formulář: Název, Cena, Množství
  - Tlačítka: Přidat, Odebrat, Zaplatit, Uložit
- Ulož wireframe jako `docs/wireframe_hlavni_okno.png` a commitni:
```bash
git checkout -b docs/wireframe-gui
git add docs/wireframe_hlavni_okno.png
git commit -m "docs: wireframe hlavního okna PyQt aplikace"
git push -u origin docs/wireframe-gui
```
- Otevři PR do `develop-r2`, closes #7

---

## 📅 Den 10–12 – Vedoucí merguje a uzavírá sprint

### 🟦 Vedoucí (A):

- [ ] Zkontrolovat a mergovat PR z `docs/tridni-diagram` → `develop-r2`
- [ ] Zkontrolovat a mergovat PR z `feature/oop-refaktoring` → `develop-r2`
- [ ] Zkontrolovat a mergovat PR z `docs/wireframe-gui` → `develop-r2`
- [ ] Otevřít **Release PR**: `develop-r2` → `main`
  - Název: `Release Sprint 1 – OOP refaktoring a třídní návrh`
  - Popis: co bylo hotovo, odkaz na Issues
- [ ] Prezentovat výsledky sprint 1

> **Sprint 1 je hotov, když:** třídy jsou v kódu, kód z P1 je refaktorovaný do tříd, wireframe GUI je v docs a Release PR je mergnut do main.
