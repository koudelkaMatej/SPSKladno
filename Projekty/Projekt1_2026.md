# Projekt 1 – Konzolová Python aplikace (1. ročník / 2026)

## Cíl projektu

Vytvořit **funkční konzolovou Python aplikaci** s menu, ukládáním dat do souboru a logikou postavenou výhradně na **sekvenčním programování** – tedy bez tříd a OOP. Cílem je nejen naprogramovat aplikaci, ale také si vyzkoušet, jak funguje **skutečný softwarový vývoj ve firmě** – práce v týmu, plánování, větvení v Gitu, code review a testování.

---

## Téma aplikace

Každá skupina si vybere **vlastní téma** z níže uvedených oblastí (nebo navrhne vlastní – schválí učitel):

| Typ aplikace | Příklady |
|---|---|
| **Evidence / Správce dat** | Knihovna (půjčování knih), katalog filmů, žákovská knížka |
| **Obchodní systém** | Jednoduchá pokladna, objednávkový systém, sklad |
| **Hra / Kvíz** | Textová adventura, kvíz s ukládáním výsledků, hádání čísel se statistikami |
| **Utilita** | Správce úkolů (TODO list), převodník jednotek s historií, generátor hesel |

Aplikace musí splňovat **funkční požadavky** (viz níže) – téma je jen obal.

---

## Organizace práce

### Skupiny
- **3–4 členové** (dle počtu žáků ve třídě)
- Skupiny jsou **neměnné po celé 3 roky** (1.–3. ročník)

### Zahájení práce

1. **Učitel** na GitHubu zakládá organizaci třídy (např. `SPS-Kladno-2026`) a každé skupině vytvoří **repozitář** s názvem skupiny (např. `skupina-snake`, `skupina-pokladna`)
2. Přidá **všechny členy skupiny** jako collaborators s právy `Write`
3. Nastaví **branch protection** na větvi `main`:
   - Změny do `main` jsou možné **pouze přes Pull Request**
   - PR musí mít **alespoň 1 schválení** (review)
4. Součástí repozitáře je od začátku soubor `ISSUES.md` pro zápis nalezených chyb při peer review

> **Proč GitHub?** Ve skutečných firmách kód nikdo nepíše sám a neodesílá rovnou do produkce. Používají se větve, pull requesty a code review – přesně to budete dělat i vy.

---

## Workflow – jak se pracuje (simulace firemního vývoje)

```
main (produkční větev – vždy funkční, merge pouze přes PR)
 │
 ├── develop (integrační větev – sem se slévají hotové featury)
 │     │
 │     ├── feature/menu             ← vývojář pracuje tady
 │     ├── feature/ukladani-dat
 │     └── feature/vyhledavani
 │
 └── (nikdy přímo – vždy přes PR z develop do main)
```

### Postup pro každou featuru:

```
1. Vedoucí vytvoří GitHub Issue s popisem požadavku
2. Vývojář vytvoří větev:  git checkout -b feature/nazev-featury
3. Vývojář implementuje + commituje průběžně
4. Analytik zkontroluje, zda kód odpovídá specifikaci a flowchartům
5. Vývojář otevře Pull Request do větve develop
6. Tester provede code review v PR (schválí nebo napíše připomínky)
7. Vedoucí schválený PR merguje
8. Na konci sprintu: Vedoucí merguje develop → main (Release PR)
```

### Pravidla pro commity

Zprávy commitů píšte **v češtině nebo angličtině**, vždy smysluplně:

```
✅  feat: přidáno menu s volbami 1-4
✅  fix: opravena chyba při prázdném vstupu
✅  docs: přidány flowcharty pro modul vyhledávání
✅  test: otestovány hraničních stavy vstupu

❌  update
❌  aaa
❌  finalni verze2_v3_FINAL
```

---

## Role ve skupině

Každý člen **v každém sprintu zastává jinou roli** – všichni tak do konce roku vyzkouší každou roli přesně jednou.

Za každý sprint dostane žák **1 známku** hodnocenou individuálně podle toho, jak plnil svoji aktuální roli.

---

### 🟦 Role 1: Vedoucí projektu *(Project Lead / Scrum Master)*

Vedoucí je zodpovědný za **organizaci sprintu** a **kvalitu výstupu celého týmu**.

**Zodpovídá za:**
- Na začátku sprintu vytvoří **GitHub Issues** pro každý požadavek daného sprintu, přiřadí je členům
- Vytvoří větev `develop` (pokud neexistuje) a hlídá, aby vývojář pracoval ve feature větvích
- **Merguje schválené Pull Requesty** do `develop`
- Na konci sprintu otevře **Release PR** (`develop` → `main`) a prezentuje, co bylo hotovo
- **Prezentuje práci týmu** při kontrolním termínu
- Pomáhá ostatním, pokud se zaseknou – řeší konflikty při mergi

> *Ve firmě je to mix role Scrum Mastera a Tech Leada – plánuje, koordinuje, dbá na kvalitu a je zodpovědný za to, co jde do produkce.*

---

### 🟩 Role 2: Analytik *(Business Analyst / Tech Writer)*

Analytik zajišťuje, že **všichni vědí, co se má udělat a jak** – píše specifikace a dokumentaci.

**Zodpovídá za:**
- Napíše nebo aktualizuje **specifikaci featury** (co má dělat, jaký je vstup/výstup, okrajové případy)
- Ke každé featurě vytvoří **vývojový diagram** – dříve než vývojář začne kódovat
- Udržuje `README.md` – popis aplikace, jak ji spustit, jaké má funkce
- Píše **docstringy** k hotovým funkcím (popis parametrů a návratové hodnoty)

> *Ve firmě je to Business Analyst nebo Technical Writer – bez něj by vývojář nevěděl, co přesně implementovat, a zákazník by nevěděl, jak produkt používat.*

---

### 🟨 Role 3: Vývojář *(Developer / Programmer)*

Vývojář **píše kód** – implementuje featury podle specifikace a flowchartů analytika.

**Zodpovídá za:**
- Pracuje vždy ve **feature větvi** (nikdy přímo v `main` ani `develop`)
- Implementuje zadanou featuru dle specifikace analytika
- Kód je **čitelný**: smysluplné názvy proměnných a funkcí, logická struktura
- Každá funkce má stručný **docstring** (popis, co dělá)
- Po dokončení otevře **Pull Request** a požádá testera o review
- Opraví připomínky z code review

> *Toto je nejčastější role ve firmě. Dobrý vývojář nepíše jen funkční kód – píše kód, který ostatní přečtou a pochopí.*

---

### 🟥 Role 4: Tester / Code Reviewer *(QA Engineer / Reviewer)*

Tester zajišťuje **kvalitu kódu a správnost funkce** – je to poslední brána před mergem.

**Zodpovídá za:**
- **Testuje** implementovanou featuru: zkouší normální vstupy, prázdný vstup, špatný typ, mezní hodnoty
- Nalezené chyby zapíše jako **komentář do Pull Requestu** (ne přímo do kódu)
- Provede **code review** v PR:
  - Je kód čitelný?
  - Odpovídá specifikaci?
  - Jsou ošetřeny chybné vstupy?
  - Má funkce docstring?
- Pokud je vše OK → **schválí PR** (Approve)
- Pokud jsou chyby → **zamítne PR** (Request changes) s komentáři

> *Ve firmě je QA Engineer a code reviewer klíčová role – bez ní by chyby šly rovnou k zákazníkovi. Code review navíc pomáhá šířit znalosti v týmu.*

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **Tester a Analytik se sloučí** do jedné (Analytik-Tester).

---

## Sprinty a kontrolní termíny

| Sprint | Období | Co se buduje | GitHub aktivita |
|--------|--------|-------------|-----------------|
| **1** | Začátek února | Základní struktura, menu, první I/O | Repo setup, první Issues, feature větve, 1. Release PR |
| **2** | Polovina března | Hlavní logika aplikace, práce s daty | Nové Issues, PRy s review, mergování |
| **3** | Konec dubna | Ukládání/načítání dat ze souboru, ošetření chyb | PRy se zamítnutím a opravou |
| **4** | Začátek června | Dokončení, refaktoring, finální testování | Release PR do main, závěrečná prezentace |

Při každém kontrolním termínu může učitel (jako „zákazník") **přidat nebo změnit požadavky** – přesně jako v reálném vývoji.

---

## Doporučený postup práce – příklad pro 4 členy (A, B, C, D)

### Sprint 1 – Základní struktura (začátek února)

| Člen | Role | Co dělá |
|------|------|---------|
| **A** | Vedoucí | Nastaví repozitář (větve `main`, `develop`), vytvoří GitHub Issues pro sprint 1, přiřadí úkoly, připraví prezentaci |
| **B** | Analytik | Napíše specifikaci aplikace (co bude umět) + flowchart pro **hlavní menu** a základní navigaci, vytvoří `README.md` |
| **C** | Vývojář | Vytvoří větev `feature/menu`, implementuje **hlavní menu** dle specifikace, otevře PR do `develop` |
| **D** | Tester | Otestuje menu (všechny volby, neplatný vstup), provede code review v PR, schválí nebo vrátí s komentáři |

### Sprint 2 – Hlavní logika (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **B** | Vedoucí | Merguje PR ze sprintu 1, vytvoří Issues pro sprint 2, prezentuje postup |
| **C** | Analytik | Napíše specifikaci pro **jádro aplikace** (přidávání/zobrazování dat) + flowcharty, doplní README |
| **D** | Vývojář | Implementuje hlavní datové operace (`feature/operace-data`), otevře PR |
| **A** | Tester | Testuje datové operace, provede code review, schválí nebo vrátí s připomínkami |

### Sprint 3 – Soubory a ošetření chyb (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **C** | Vedoucí | Řídí sprint, merguje PRy, hlídá konzistenci aplikace, prezentuje |
| **D** | Analytik | Specifikuje **ukládání a načítání dat** (formát souboru, co se ukládá) + flowcharty, doplní docstringy |
| **A** | Vývojář | Implementuje čtení/zápis do souboru (`feature/soubory`), ošetří výjimky, otevře PR |
| **B** | Tester | Testuje soubory (neexistující soubor, poškozený soubor, prázdný soubor), code review |

### Sprint 4 – Finalizace (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **D** | Vedoucí | Otevře finální Release PR (`develop` → `main`), koordinuje opravy, prezentuje výsledek celého projektu |
| **A** | Analytik | Finalizuje `README.md`, doplní všechny chybějící docstringy, zkontroluje konzistenci dokumentace |
| **B** | Vývojář | Refaktoring – vylepší čitelnost kódu, odstraní duplicity, opraví zbývající chyby z Issues |
| **C** | Tester | Celkové závěrečné testování aplikace, zkontroluje všechna Issues, zajistí že jsou uzavřená |

> **Každý člen tak do konce roku vyzkouší všechny 4 role a každý přispěje 1 vývojovým diagramem (sprint, ve kterém je Analytik).**

---

## Funkční požadavky na aplikaci

### Povinné prvky

| Požadavek | Popis |
|-----------|-------|
| **Hlavní menu** | Textové menu s číslovanými volbami, smyčka dokud uživatel nezvolí ukončení |
| **Minimálně 4 funkce** | Aplikace má alespoň 4 oddělené funkce (ne vše v `main`) |
| **Práce se seznamem nebo slovníkem** | Data jsou uložena v paměti v kolekci |
| **Ukládání do souboru** | Data se při ukončení uloží, při spuštění se načtou (formát: TXT, CSV nebo JSON) |
| **Ošetření vstupů** | Špatný vstup (písmeno místo čísla, prázdný vstup) neukončí program pádem |
| **Vyhledávání nebo filtrování** | Uživatel může vyhledat nebo filtrovat data |

### Dokumentace (povinná součást)

- Každá **funkce** má docstring (co dělá, parametry, co vrací)
- `README.md` popisuje, co aplikace dělá, jak ji spustit a jaké má funkce
- Z **historie commitů** musí být patrné, kdo co vytvořil
- V repozitáři jsou **flowcharty** (obrázky nebo odkaz na draw.io) pro klíčové části logiky

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **Python 3** – základní datové typy, funkce, cykly, podmínky, práce se soubory
- **Standardní knihovny** – `os`, `json`, `csv`, `random`, `math`, `datetime`
- **Git** + **GitHub** pro správu verzí (větve, Pull Requesty, Issues, code review)
- Nástroje pro vývojové diagramy (draw.io, ruční nákres, Lucidchart)

### ❌ Zakázáno
- Třídy a OOP (`class`) – to přijde v 2. ročníku
- Externí knihovny (pip install ...) – pokud nebyly probírány ve výuce
- AI generátory celých bloků kódu
- Kopírování cizího kódu bez pochopení

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní porozumění základům Pythonu.**

---

## Hodnocení

### Známky za sprinty – individuální

Každý žák získá **4 známky** (1 za každý sprint). Hodnotí se **výhradně aktuální role**:

| Kritérium | Vedoucí | Analytik | Vývojář | Tester |
|-----------|---------|----------|---------|--------|
| Splnění role | ✅ | ✅ | ✅ | ✅ |
| Kvalita výstupu | Issues + merge | Specifikace + flowcharty | Čitelnost + funkčnost kódu | Hloubka testování + review |
| Práce s Gitem | Mergování, Release PR | Commity dokumentace | Feature větve, smysluplné commity | Komentáře v PR |
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
> [Peer review] Program spadne při zadání písmene místo čísla v menu
> [Peer review] Po ukončení se data neuloží do souboru
> [Peer review] Funkce hledej_polozku() nemá žádný docstring
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti** (větev `main`)
- Aplikace musí jít **spustit na školních počítačích** bez dodatečné instalace
- Z **historie commitů a Pull Requestů** musí být patrné, kdo co dělal a v jaké roli
- Repozitář obsahuje: zdrojový kód, `README.md`, flowcharty, uzavřená Issues z peer review

---

## Tipy pro realistické napodobení firemního vývoje

| Praxe ve firmě | Co budete dělat |
|---|---|
| Zadání od zákazníka | Učitel = zákazník, může měnit požadavky mezi sprinty |
| Planning meeting | Začátek každého sprintu – vedoucí vytvoří Issues, tým si rozdělí úkoly |
| Feature branches | Každá funkce = vlastní větev (`feature/...`) |
| Code review | Tester schvaluje nebo vrací PR s komentáři před mergem |
| Daily standup | Krátká zpráva v Issue nebo komentář: „Dnes jsem udělal X, zítra plánuji Y" |
| Sprint review | Kontrolní termín = prezentace zákazníkovi (učiteli) |
| Bug tracking | Chyby = GitHub Issues s labelem `bug` |
| Release | Merge `develop` → `main` před každým kontrolním termínem |

---

---

# 🗺️ Roadmapa Sprintu 1 – krok za krokem

> Tato sekce ukazuje **přesně co, kdy a jak** by měl každý člen týmu udělat během prvního sprintu.  
> Příklad je pro skupinu s tématem **„Pokladna"** (A = Vedoucí, B = Analytik, C = Vývojář, D = Tester).  
> Časový rámec: **2–3 týdny** (od zahájení do kontrolního termínu).

---

## 📅 Den 1 – Kick-off (první hodina spolu)

### Celý tým společně:
- [ ] Dohodnout se na **tématu aplikace** a základní myšlence
- [ ] Každý si **naklonuje repozitář**:
  ```bash
  git clone https://github.com/SPS-Kladno-2026/skupina-pokladna.git
  cd skupina-pokladna
  ```
- [ ] Ověřit, že každý vidí repozitář a má přístup

### 🟦 Vedoucí (A) – den 1:
- [ ] Vytvořit větev `develop` a odeslat ji na GitHub:
  ```bash
  git checkout -b develop
  git push -u origin develop
  ```
- [ ] Na GitHubu v záložce **Issues** vytvořit Issues pro sprint 1:

  | # | Název Issue | Přiřazeno |
  |---|-------------|-----------|
  | 1 | `Specifikace aplikace a flowchart menu` | B (Analytik) |
  | 2 | `README.md – popis projektu` | B (Analytik) |
  | 3 | `Implementace hlavního menu` | C (Vývojář) |
  | 4 | `Testování a code review menu` | D (Tester) |

- [ ] Každé Issue přiřadit správnému členovi (pole *Assignees*)
- [ ] Přidat label: `sprint-1`

---

## 📅 Dny 2–4 – Analytik připravuje specifikaci

### 🟩 Analytik (B):

**Krok 1 – Vytvořit větev pro dokumentaci:**
```bash
git checkout develop
git checkout -b docs/specifikace-sprint1
```

**Krok 2 – Napsat specifikaci** (soubor `docs/specifikace_menu.md`):

```markdown
## Specifikace: Hlavní menu pokladny

### Co má dělat:
Po spuštění programu se zobrazí textové menu s volbami:
  1. Přidat položku
  2. Zobrazit košík
  3. Zaplatit a ukončit
  0. Konec bez placení

### Vstup:
- Uživatel zadá číslo volby (celé číslo)
- Neplatný vstup (písmeno, číslo mimo rozsah) → vypsat chybovou zprávu a znovu se zeptat

### Výstup:
- Zobrazí příslušnou zprávu nebo zavolá příslušnou funkci
- Smyčka běží, dokud uživatel nezvolí 0 nebo 3

### Okrajové případy:
- Vstup "" (Enter bez textu) → chybová zpráva
- Vstup "abc" → chybová zpráva
- Vstup "99" → chybová zpráva
```

**Krok 3 – Nakreslit flowchart** (draw.io nebo na papír, vyfotit/exportovat jako PNG):
- Uložit jako `docs/flowchart_menu.png`

**Krok 4 – Napsat `README.md`**:
```markdown
# Pokladna – skupinový projekt 2026

## Popis
Konzolová pokladna pro malý obchod. Umožňuje přidávat zboží, zobrazit košík a zaplatit.

## Spuštění
python main.py

## Funkce (sprint 1)
- Hlavní menu s volbami
```

**Krok 5 – Commit a push:**
```bash
git add docs/specifikace_menu.md docs/flowchart_menu.png README.md
git commit -m "docs: specifikace menu, flowchart a README pro sprint 1"
git push -u origin docs/specifikace-sprint1
```

**Krok 6 – Otevřít Pull Request** na GitHubu:
- Base: `develop` ← Compare: `docs/specifikace-sprint1`
- Název: `docs: specifikace a README pro sprint 1`
- Popis: odkaz na Issue #1 a #2 (`Closes #1, Closes #2`)
- Assignee: B, Reviewer: A (Vedoucí)

**Krok 7 – Vedoucí (A) PR zkontroluje a merguje** do `develop`

---

## 📅 Dny 3–7 – Vývojář implementuje menu

> Vývojář může začít pracovat **paralelně** s analytikem – nejdřív jen prázdná kostra, pak implementace dle specifikace.

### 🟨 Vývojář (C):

**Krok 1 – Stáhnout aktuální `develop` a vytvořit feature větev:**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/menu
```

**Krok 2 – Napsat kód** (soubor `main.py`):

```python
def zobraz_menu():
    """Vypíše hlavní menu pokladny na obrazovku."""
    print("\n=== POKLADNA ===")
    print("1. Přidat položku")
    print("2. Zobrazit košík")
    print("3. Zaplatit a ukončit")
    print("0. Konec bez placení")
    print("================")


def nacti_volbu():
    """
    Načte a vrátí platnou volbu z hlavního menu (0–3).
    Opakuje dotaz, dokud uživatel nezadá platné číslo.
    """
    while True:
        vstup = input("Vaše volba: ").strip()
        if vstup in ("0", "1", "2", "3"):
            return int(vstup)
        print("Neplatná volba. Zadejte číslo 0–3.")


def main():
    """Hlavní smyčka programu."""
    print("Vítejte v pokladně!")
    while True:
        zobraz_menu()
        volba = nacti_volbu()

        if volba == 1:
            print("→ Přidání položky (zatím není implementováno)")
        elif volba == 2:
            print("→ Zobrazení košíku (zatím není implementováno)")
        elif volba == 3:
            print("Děkujeme za nákup. Na shledanou!")
            break
        elif volba == 0:
            print("Program ukončen.")
            break


if __name__ == "__main__":
    main()
```

**Krok 3 – Průběžné commity** (ne vše najednou na konci!):
```bash
# Po napsání funkce zobraz_menu():
git add main.py
git commit -m "feat: přidána funkce zobraz_menu()"

# Po napsání funkce nacti_volbu():
git add main.py
git commit -m "feat: přidána funkce nacti_volbu() s ošetřením vstupu"

# Po napsání main():
git add main.py
git commit -m "feat: hlavní smyčka programu v main()"

git push -u origin feature/menu
```

**Krok 4 – Otevřít Pull Request** na GitHubu:
- Base: `develop` ← Compare: `feature/menu`
- Název: `feat: implementace hlavního menu`
- Popis:
  ```
  Implementuje hlavní textové menu dle specifikace v docs/specifikace_menu.md.

  Co bylo přidáno:
  - funkce zobraz_menu()
  - funkce nacti_volbu() s ošetřením neplatného vstupu
  - hlavní smyčka v main()

  Closes #3
  ```
- Reviewer: D (Tester)

---

## 📅 Dny 6–8 – Tester provádí code review

### 🟥 Tester (D):

**Krok 1 – Stáhnout feature větev a otestovat lokálně:**
```bash
git fetch origin
git checkout feature/menu
python main.py
```

**Krok 2 – Testovací scénáře** (zkouší ručně):

| Scénář | Vstup | Očekávaný výsledek | Výsledek |
|--------|-------|-------------------|----------|
| Platná volba | `1` | Zobrazí zprávu o přidání | ✅ |
| Platná volba | `0` | Ukončí program | ✅ |
| Písmeno místo čísla | `abc` | Chybová zpráva, opakuje dotaz | ✅ |
| Prázdný Enter | `` | Chybová zpráva, opakuje dotaz | ✅ |
| Číslo mimo rozsah | `5` | Chybová zpráva, opakuje dotaz | ✅ |
| Záporné číslo | `-1` | Chybová zpráva, opakuje dotaz | ✅ |

**Krok 3 – Code review v PR na GitHubu:**

Tester zkontroluje:
- [ ] Mají všechny funkce docstring?
- [ ] Jsou názvy funkcí smysluplné?
- [ ] Je kód čitelný a logicky uspořádaný?
- [ ] Odpovídá implementace specifikaci analytika?
- [ ] Jsou ošetřeny všechny okrajové případy ze specifikace?

**Příklad komentáře v PR (pokud tester najde problém):**
> 🔴 `nacti_volbu()`: Zkus zadat `"  1  "` (s mezerami) – program to nepřijme, ale měl by (uživatel omylem stiskne mezeru). Doporučuji přidat `.strip()` před porovnáváním.

**Pokud vše sedí → Tester klikne "Approve" a napíše:**
> ✅ Otestovány všechny scénáře ze specifikace, vše funguje správně. Kód je čitelný, funkce mají docstringy. Schvaluji merge.

**Pokud jsou připomínky → "Request changes":**
- Vývojář (C) opraví kód, commituje: `fix: ošetřen vstup s mezerami v nacti_volbu()`
- Pushuje do stejné větve – PR se automaticky aktualizuje
- Tester znovu zkontroluje a schválí

---

## 📅 Den 8–9 – Vedoucí merguje a připravuje Release

### 🟦 Vedoucí (A):

**Krok 1 – Zkontrolovat, že PR je schválený** (zelená fajfka od Testera)

**Krok 2 – Mergovat `feature/menu` → `develop`** (na GitHubu tlačítko *Merge pull request*)
- Zvolte **"Squash and merge"** nebo **"Create a merge commit"** dle dohody týmu
- Po mergi větev smažte (tlačítko *Delete branch*)

**Krok 3 – Lokálně aktualizovat develop:**
```bash
git checkout develop
git pull origin develop
```

**Krok 4 – Otevřít Release PR** (`develop` → `main`):
- Název: `Release: Sprint 1 – základní menu`
- Popis: Co bylo hotovo v tomto sprintu, co zbývá
- Reviewer: libovolný člen (nebo všichni)

**Krok 5 – Po schválení mergovat do `main`** → aplikace je v "produkci"

**Krok 6 – Připravit prezentaci** (2–3 minuty):
- Co jsme budovali a proč?
- Ukázka funkčního menu
- Co jsme se naučili / s čím byl problém
- Co plánujeme v dalším sprintu

---

## 📅 Den 10 – Kontrolní termín (Sprint Review)

### Celý tým:
- [ ] **Vedoucí prezentuje** – ukáže fungující aplikaci, projde GitHub repozitář (Issues, PR, větve)
- [ ] Učitel (zákazník) dá zpětnou vazbu a **případně změní/přidá požadavky** pro sprint 2
- [ ] Ostatní skupiny dostanou čas na **peer review** – testují vaši aplikaci a píší Issues

### Po kontrolním termínu:
- [ ] Projít Issues od peer review – zapsat do svých GitHub Issues s labelem `peer-review`
- [ ] Vedoucí naplánuje sprint 2 – nové Issues, rotace rolí

---

## ✅ Checklist – co musí být hotovo před kontrolním termínem Sprint 1

### Repozitář:
- [ ] Větve `main` a `develop` existují, `main` je chráněna
- [ ] Feature větev `feature/menu` byla mergována do `develop` přes PR
- [ ] Release PR (`develop` → `main`) byl vytvořen a mergován
- [ ] Všechna Sprint 1 Issues jsou uzavřena

### Kód:
- [ ] `main.py` existuje a jde spustit (`python main.py`)
- [ ] Hlavní menu zobrazuje volby a reaguje na vstup
- [ ] Neplatný vstup program neshodí
- [ ] Každá funkce má docstring

### Dokumentace:
- [ ] `README.md` popisuje projekt a jak ho spustit
- [ ] `docs/specifikace_menu.md` popisuje chování menu
- [ ] `docs/flowchart_menu.png` (nebo `.jpg`) obsahuje vývojový diagram

### GitHub aktivita:
- [ ] Každý člen má alespoň **3 commity** (v rámci své role)
- [ ] PR byl vytvořen, obsahuje popis a odkaz na Issue
- [ ] Code review obsahuje alespoň 1 komentář testera
- [ ] Commit zprávy jsou smysluplné (ne `update`, `aaa` apod.)

---

---

# 🖱️ Totéž v VS Code – bez příkazové řádky

> Všechny Git operace z roadmapy výše lze udělat **klikáním v VS Code** přes panel **Source Control** (ikona větviček vlevo, nebo `Ctrl+Shift+G`).  
> Níže je přehled ekvivalentů ke každému bash příkazu.

---

## Klonování repozitáře

**Bash:**
```bash
git clone https://github.com/SPS-Kladno-2026/skupina-pokladna.git
```

**VS Code:**
1. Otevřete VS Code (bez otevřené složky)
2. Klikněte `Ctrl+Shift+P` → napište **Git: Clone**
3. Vložte URL repozitáře z GitHubu → Enter
4. Vyberte složku, kam se má projekt uložit
5. Klikněte **Open** v notifikaci, která se objeví

---

## Vytvoření nové větve

**Bash:**
```bash
git checkout -b feature/menu
```

**VS Code:**
1. Vlevo dole klikněte na název aktuální větve (např. `main`)
2. Zvolte **Create new branch...**
3. Napište název větve (např. `feature/menu`) → Enter
4. VS Code automaticky přepne na novou větev

> 💡 Název aktuální větve je vždy vidět v levém dolním rohu stavového řádku.

---

## Přepnutí na existující větev

**Bash:**
```bash
git checkout develop
```

**VS Code:**
1. Klikněte na název větve vlevo dole
2. Ze seznamu vyberte větev, na kterou chcete přepnout
3. Pokud ji nevidíte, zvolte nejdřív **Fetch** (viz níže) – stáhne přehled větví ze serveru

---

## Stažení změn ze serveru (fetch / pull)

**Bash:**
```bash
git pull origin develop
```

**VS Code:**
1. Otevřete **Source Control** panel (`Ctrl+Shift+G`)
2. Klikněte na **⋯** (tři tečky) vpravo nahoře v panelu
3. Zvolte **Pull** (stáhne a sloučí změny z aktuální větve)  
   – nebo **Fetch** (jen zkontroluje, co je nového, ale neslouží)

> 💡 Alternativně: klikněte na ikonu 🔄 v levém dolním rohu stavového řádku (synchronizační šipky).

---

## Commitování změn

**Bash:**
```bash
git add main.py
git commit -m "feat: přidána funkce zobraz_menu()"
```

**VS Code:**
1. Otevřete **Source Control** panel (`Ctrl+Shift+G`)
2. Ve skupině **Changes** uvidíte všechny změněné soubory
3. Najeďte na soubor, který chcete přidat do commitu, a klikněte na **+** (Stage Changes)
   - Soubor se přesune do skupiny **Staged Changes**
   - Chcete přidat vše: klikněte **+** vedle nadpisu *Changes*
4. Do pole **Message** nahoře napište zprávu commitu (např. `feat: přidána funkce zobraz_menu()`)
5. Klikněte na **✓ Commit** (nebo `Ctrl+Enter`)

> ⚠️ Dokud soubor není v **Staged Changes**, commit ho neobsahuje – stejné jako `git add`.

---

## Odeslání větve na GitHub (push)

**Bash:**
```bash
git push -u origin feature/menu
```

**VS Code:**
1. Po commitu se v panelu Source Control zobrazí tlačítko **Publish Branch** (při prvním push nové větve)  
   – klikněte na něj → větev se odešle na GitHub
2. Při dalších pushech stejné větve: klikněte na **⋯ → Push**  
   – nebo na ikonu 🔄 v levém dolním rohu

---

## Otevření Pull Requestu

Pull Request se **vždy vytváří na webu GitHub** (nebo přes rozšíření GitHub Pull Requests). VS Code samotné PR nevytváří.

**Postup na GitHubu:**
1. Přejděte na stránku repozitáře na `github.com`
2. GitHub obvykle automaticky nabídne banner: **„Compare & pull request"** – klikněte na něj
3. Pokud ne: záložka **Pull requests** → zelené tlačítko **New pull request**
4. Nastavte:
   - **base:** `develop` (kam chcete mergovat)
   - **compare:** `feature/menu` (vaše větev)
5. Vyplňte název a popis, přidejte Reviewera (Testera), odkažte na Issue (`Closes #3`)
6. Klikněte **Create pull request**

> 💡 Doporučené rozšíření: **GitHub Pull Requests** (od GitHub) – umožňuje vytvářet a recenzovat PR přímo ve VS Code bez přepínání do prohlížeče.

---

## Code review v Pull Requestu

Code review probíhá **na webu GitHub** – VS Code ho přímo nepodporuje bez rozšíření.

**Postup na GitHubu (Tester):**
1. Přejděte na PR v záložce **Pull requests**
2. Klikněte na záložku **Files changed** – uvidíte všechny změny (zelené = přidané, červené = odebrané)
3. Pro přidání komentáře k řádku: klikněte na **+** vlevo od čísla řádku → napište komentář → **Add single comment**
4. Po prohlédnutí všeho klikněte vpravo nahoře na **Review changes**:
   - ✅ **Approve** – vše je OK, PR lze mergovat
   - 🔴 **Request changes** – jsou problémy, vývojář musí opravit
5. Napište souhrnný komentář a potvrďte

---

## Mergování PR (Vedoucí)

Merge PR se provádí **na webu GitHub**:
1. Přejděte na PR
2. Zkontrolujte, že má zelený štítek ✅ **Approved**
3. Klikněte na zelené tlačítko **Merge pull request** → **Confirm merge**
4. Klikněte **Delete branch** (odstraní feature větev po mergi – udržuje repozitář čistý)

---

## Přehled: bash ↔ VS Code

| Co chcete udělat | Git bash | VS Code |
|---|---|---|
| Klonovat repo | `git clone <url>` | `Ctrl+Shift+P` → *Git: Clone* |
| Vytvořit větev | `git checkout -b nazev` | Klik na větev vlevo dole → *Create new branch* |
| Přepnout větev | `git checkout nazev` | Klik na větev vlevo dole → vybrat ze seznamu |
| Stáhnout změny | `git pull` | Source Control → ⋯ → *Pull* |
| Přidat soubory | `git add soubor.py` | Source Control → klik na **+** u souboru |
| Commitovat | `git commit -m "zprava"` | Source Control → napsat zprávu → **✓ Commit** |
| Odeslat na GitHub | `git push` | Source Control → ⋯ → *Push* / tlačítko *Publish Branch* |
| Vytvořit PR | – | Na webu github.com nebo rozšíření *GitHub Pull Requests* |
| Provést review | – | Na webu github.com → záložka *Files changed* |
| Mergovat PR | – | Na webu github.com → tlačítko *Merge pull request* |
