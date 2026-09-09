# Projekt 4 – Maturitní projekt (4. ročník)

## Cíl projektu

Samostatně vytvořit **kompletní softwarový projekt**, který integruje vše, co jste se naučili během tříletého studia: datovou logiku, grafickou aplikaci a webovou vrstvu s databází. Projekt obsahuje **všechny části** zpracovávané ve skupinách během předchozích 3 let: **webovou prezentaci, hru/aplikaci a databázi** – vše vzájemně propojené. Tento projekt je **podmínkou pro přistoupení k praktické maturitní zkoušce**.

---

## Organizace práce

### Práce je **individuální**
- Každý žák pracuje **sám**
- Učitel založí repozitář pro žáka **učitelské gitové úložiště** (GitHub) a přidá žáky jako **collaborators** 
- Žák použije znalosti získané během výuky a **všechny části projektu vytvoří sám** (web, hra, databáze)
- Žák **nevyužil AI** pro **generování celých bloků kódu**, ale **pouze pro inspiraci, komentování, generování textu hry a pomoc s konkrétními problémy**
- **Doporučení:** Veřejný repozitář ušetří starosti s přístupy

---

## Volba technologie

> **Žák smí používat POUZE technologie, se kterými jsme pracovali v průběhu studia – nebo Godot s GDScriptem v Pythonu**

### Povolené herní/aplikační technologie (vyber jednu):

| Možnost | Technologie | Vhodné pro |
|---------|-------------|------------|
| **A** | Python + Pygame | Klasické 2D hry (platformer, shooter, puzzle, RPG...) |
| **B** | Python + PyQt6 | Desktopová aplikace / systém s GUI |
| **C** | Godot (GDScript) | Pokročilejší 2D/3D hry, animace, fyzika |

> **Volbu technologie nahlaste učiteli nejpozději do konce září.** Pokud zvolíte Godot, musí projekt jít spustit na školních počítačích – ověřte to na začátku října.


---

## Kontrolní termíny

| # | Období | Co by mělo být hotové |
|---|--------|-----------------------|
| 1 | **Začátek listopadu** | Výběr tématu, funkční menu, návrh rozložení projektu (datové toky – co-kde-kam-odkud), návrh databáze, ER diagram |
| 2 | **Začátek ledna** | Základní pohyb a logika hry, práce s databází, komunikace DB s webovou stránkou a hrou |
| 3 | **Konec února** | Dodělávání detailů a oprava chyb, vylepšení na základě zpětné vazby vyučujících |
| 4 | **14 dní před praktickou maturitní zkouškou** | **Finální odevzdání** – kompletní, funkční projekt | Prezentace projektu ve třídě, vzájemné hodnocení (peer review) |

> **Pozn.:** Termíny 3 a 4 se mohou krýt nebo jít těsně po sobě – v takovém případě žák může dostat **3 známky místo 4**.

---

## Doporučený postup práce

Jedná se o individuální projekt – všechno děláte sami. Níže je doporučený harmonogram, **na co se soustředit v každé fázi**.

### 1. fáze (září – začátek listopadu)

| Oblast | Co dělat |
|--------|-----------|
| **Plánování** | Vybrat téma hry, navrhnout rozložení projektu (datové toky: co-kde-kam-odkud) |
| **Databáze** | Navrhnout a zakreslit **ER diagram**, vytvořit CREATE TABLE skripty (`schema.sql`) |
| **Hra** | Funkční **hlavní menu** (start, ukončení), základní okno |
| **Web** | Základ Flask projektu, stránka index, základní navigace |
| **Git** | Založit repozitář, nastavit strukturu složek, pravidelně commitovat |

### 2. fáze (listopad – začátek ledna)

| Oblast | Co dělat |
|--------|-----------|
| **Hra** | **Základní pohyb a logika** – postava se pohybuje, reaguje na vstupy, herní smyčka funguje |
| **Databáze** | Vložit vzorová data (INSERT), napsat SELECT dotazy (JOIN, WHERE, ORDER BY) |
| **Propojení** | Hra ukládá skóre do DB, web čte data z DB |
| **Web** | Implementovat **login + registraci** s hashováním hesla, zobrazit herní výsledky z databáze |
| **Dokumentace** | Komentovat kód průběžně, začít uživatelský manuál |

### 3. fáze (začátek ledna – konec února)

| Oblast | Co dělat |
|--------|-----------|
| **Hra** | Doladit mechaniky, opravit bugy, hra se zeptá na jméno hráče |
| **Databáze** | Doplnit UPDATE, DELETE, ověřit **normalizaci (BCNF)** |
| **Web** | Aktualizovat obsah, přidat screenshoty ze hry, vývojové diagramy |
| **Testy** | Napsat minimálně **3 automatizované testy** na důležité funkce |
| **Dokumentace** | Dokončit docstringy u všech tříd/funkcí, finalizovat manuál |

### 4. fáze (březen – 14 dní před maturitou)

| Oblast | Co dělat |
|--------|-----------|
| **Vše** | Finální testování – hra nepadá, web funguje, DB odpovídá, vše je propojené |
| **Dokumentace** | SQL skripty přiloženy, ER diagram aktuální, manuál hotový |
| **Git** | Vyčistit repozitář, zkontrolovat historii commitů, označit finální verzi tagem `v1.0` |
| **Kvalita** | Zpětná vazba učitele zapracována, kód čitelný a komentovaný |

> **Tip:** Pracujte průběžně a pravidelně commitujte. Nenechávejte vše na poslední chvíli – projekt je rozsáhlý a musí obsahovat všechny části.

---

## Funkční požadavky

### Projekt musí obsahovat VŠECHNY následující části:

### 1. Herní / grafická část

**Pygame nebo PyQt6:**

| Požadavek | Detail |
|-----------|--------|
| **OOP** | Kód postaven na třídách; min. 3 vlastní třídy s docstringy |
| **Grafické rozhraní** | Aplikace má okno – ne konzoli |
| **Hlavní menu** | Menu s tlačítky (start, nastavení, exit) ovládatelné myší/klávesnicí |
| **Herní smyčka** | Funkční event loop / update + render smyčka |
| **Herní logika** | Funkční a smysluplná – hra/systém dělá to, co má dělat |
| **Ukládání výsledků** | Výsledky (jméno, skóre nebo výstup) se ukládají do databáze |
| **Stabilita** | Aplikace nesmí padat při normálním použití |

**Godot (GDScript):**

| Požadavek | Detail |
|-----------|--------|
| **Scény a skripty** | Projekt má strukturu scén; skripty jsou v GDScriptu |
| **Hlavní menu** | Funkční menu scéna (start, exit, případně nastavení) |
| **Herní logika** | Funkční pohyb, kolize nebo jiné mechaniky odpovídající hernímu žánru |
| **Ukládání výsledků** | Výsledky se ukládají do databáze (přes HTTP API nebo přímo přes SQLite) |
| **Stabilita** | Hra nesmí padat při normálním hraní |

> 💡 **Příklad alternativního projektu – Skladovací systém (PyQt6):**
> Místo hry může být desktopová aplikace se smysluplnou funkcionalitou. Požadavky se přeloží takto:
>
> | Herní požadavek | Ekvivalent v aplikaci |
> |---|---|
> | Herní smyčka | Qt event loop, okno běží a reaguje na vstupy |
> | Menu + start/ukončení | Hlavní okno s navigací, tlačítka Zavřít / Nová položka |
> | Interakce (klávesnice/myš) | Formuláře, tabulky, filtry, tlačítka |
> | Ukládání skóre do DB | CRUD – přidání, úprava, mazání záznamů v DB |
> | Zjistit kdo hrál | Přihlášení nebo výběr uživatele při spuštění |


### 2. Webová stránka (Flask, JS, PHP)

| Požadavek | Detail |
|-----------|--------|
| **Min. 4 stránky** | Index, login, registrace, žebříček výsledků |
| **Navigační lišta** | Konzistentní navigace na všech stránkách |
| **Login a registrace** | Heslo **hashované** (`werkzeug.security, bcrypt`), session management |
| **Zobrazení dat z DB** | Stránka se žebříčkem zobrazuje data načtená z databáze |
| **Jinja2 šablony** | Dědičnost šablon (`{% extends %}`), základní layout v `base.html` |
| **Vlastní CSS** | Maximálně 1 CSS soubor, konzistentní vizuál |
| **Bezpečnost** | Parametrizované SQL dotazy (žádné f-stringy s uživatelskými daty v SQL) |
| **Obsah** | Informace o hře, vývojové diagramy, pravidla, informace o autorovi |

---

### 3. Databáze

| Požadavek | Detail |
|-----------|--------|
| **ER diagram** | Zakreslen a přiložen k projektu (`docs/er_diagram.png` nebo PDF) |
| **Vztahy** | Min. 3 tabulky, využívá 1:N i M:N (tedy i JOIN při čtení dat) |
| **DDL skripty** | `CREATE TABLE` s: datový typ, `UNIQUE`, `NOT NULL`, `AUTO_INCREMENT`/`AUTOINCREMENT`, `PRIMARY KEY`, `FOREIGN KEY`, `DEFAULT` |
| **DML – INSERT** | Min. 3 vzorové záznamy do každé tabulky (`db/seed.sql lze zapsat i do dokumentace` ) |
| **SELECT dotazy** | `JOIN`, `WHERE`, `ORDER BY`, `GROUP BY`, `LIKE`, agregační funkce (`db/queries.sql`) |
| **DML – úpravy** | `UPDATE` a `DELETE` příkazy přiloženy |
| **Normalizace** | Minimálně po **Boyceho-Coddovu normální formu (BCNF)** |
| **Komunikace** | S databází komunikuje web (přes Flask) i hra (přes Python) |

### 4. Propojení

| Požadavek | Detail |
|-----------|--------|
| **Hra → DB** | Hra/app ukládá výsledky do databáze po skončení |
| **Web → DB** | Web čte data z databáze a zobrazuje je |
| **Sdílená databáze** | Všechny části pracují se stejnou databází |

Všechny tři části (web + hra + DB) musí **spolu komunikovat** – min. vždy 2 mezi sebou (DB a hra, DB a web).

### 5. Automatizované testy

| Požadavek | Detail |
|-----------|--------|
| **Min. 3 testy** | Testy pokrývají důležité funkce projektu |
| **Framework** | `pytest` nebo `unittest` |
| **Spustitelnost** | Testy musí jít spustit a musí procházet (`pytest` bez chyb) |
| **Smysluplnost** | Každý test má jasný název a testuje konkrétní chování – ne jen `assert True` |

Příklady dobrých testů:
```python
def test_kosik_celkem_prazdny():
    """Prázdný košík má celkovou cenu 0."""
    k = Kosik()
    assert k.celkem() == 0.0

def test_kosik_pridej_polozku():
    """Po přidání položky je počet položek v košíku 1."""
    k = Kosik()
    k.pridej(Polozka("Rohlík", 2.5))
    assert len(k.polozky) == 1

def test_uloz_a_nacti_kosik(tmp_path):
    """Uložený a znovu načtený košík má stejné položky."""
    k = Kosik()
    k.pridej(Polozka("Máslo", 45.0, 2))
    soubor = tmp_path / "kosik.json"
    k.uloz(str(soubor))
    k2 = Kosik()
    k2.nacti(str(soubor))
    assert len(k2.polozky) == 1
    assert k2.polozky[0].nazev == "Máslo"
```

### 6. Dokumentace

| Požadavek | Detail |
|-----------|--------|
| **Git historie** | Každá fáze obsahuje minimálně **5 commitů** s popisnými zprávami |
| **Docstringy** | Každá třída, metoda a Flask route má docstring/komentář |
| **README.md** | Jak spustit hru, web a databázi; seznam závislostí (`requirements.txt`) |
| **ER diagram** | Aktuální, přiložen v repozitáři |
| **SQL skripty** | Všechny skripty přiloženy (`schema.sql`, `seed.sql`, `queries.sql`) |
| **Vývojové diagramy** | Flowcharty klíčových mechanik (min. 3) |

#### Povinné dokumenty (každý jako samostatný soubor v repozitáři)

Každý dokument může být odevzdán jako html stránka či jako samostatný soubor (např. `.md`, `.pdf`, `.docx`, `.txt`, `.pptx`).

**1. Dokumentace projektu** (`dokumentace.*`)
- Název, účel projektu, použité technologie
- Popis funkce aplikace a hlavní vlastnosti
- Struktura projektu – přehled složek a klíčových souborů
- Postup spuštění a základní ovládání
- Použité knihovny a požadavky na prostředí
- Známá omezení a návrh dalšího rozšíření

**2. Uživatelský manuál** (`manual.*`)
- Název aplikace, účel, cílový uživatel
- Postup spuštění (OS, verze Pythonu, potřebné knihovny)
- Popis uživatelského rozhraní a ovládání
- Příklady běžného použití
- Popis možných chyb a doporučený postup při jejich výskytu
- Shrnutí a návrh dalšího zlepšení

**3. Prezentace pro investora** (`prezentace.*`)
- Název projektu, autor, stručné představení problému
- K čemu projekt slouží, hlavní přínosy
- Cílová skupina a konkurenční výhoda
- Použité technologie a princip fungování (bez detailů kódu)
- Ukázka funkčnosti – příklad využití v praxi
- Možnosti dalšího rozvoje a potenciál komercializace
- Závěr – proč by projekt mohl být zajímavý pro investora

**4. Přehled pro nového spolupracovníka** (`prehled.*`)
- Název, účel a stručný popis projektu
- Struktura složek a souborů, role hlavních částí
- Základní logika aplikace a popis hlavních datových toků
- Použité technologie, knihovny a nástroje
- Postup spuštění a informace potřebné pro další vývoj
- Upozornění na důležité části kódu, možná rizika a omezení

---

## Bezpečnostní požadavky

> Nedodržení těchto pravidel je automaticky **chyba hodnocená jako 5** v hodnocení za příslušnou část.

| Riziko | Povinné opatření |
|--------|------------------|
| **SQL injection** | Vždy parametrizované dotazy: `cursor.execute("... WHERE id = ?", (id,))` |
| **Hesla v plaintextu** | Nikdy – používejte `werkzeug.security.generate_password_hash()` a `check_password_hash()` |
| **Secret key** | `app.secret_key` nikdy necommitovat jako pevný řetězec do Git – použijte proměnnou prostředí nebo `.env` soubor (přidejte `.env` do `.gitignore`) |
| **Přístup bez přihlášení** | Chráněné stránky ověřují session: `if 'user_id' not in session` |

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce, případně Godot s GDScriptem.**

### ✅ Povoleno

| Oblast | Technologie |
|--------|-------------|
| **Hra / GUI** | Python 3 + Pygame, Python 3 + PyQt6, nebo Godot 4 (GDScript) |0
| **Web** | Python 3 + Flask + Jinja2 nebo JS/PHP|
| **Databáze** | SQLite nebo MySQL / MariaDB |
| **Frontend** | HTML 5 + CSS 3 (vlastní – bez frameworků) + JS|
| **Testování** | `pytest`, `unittest` |
| **Verzování** | Git + GitHub |
| **Standardní knihovny** | `os`, `json`, `csv`, `random`, `math`, `datetime`, `werkzeug`, ... |
| **Grafika** | GIMP, Piskel, Malování – pro tvorbu spritů |

### ❌ Zakázáno
- Herní enginy (Unity, Unreal, apod.)
- Jiné webové frameworky (Django, FastAPI, Node.js, Express, ...)
- CSS frameworky (Bootstrap, Tailwind, Bulma, ...)
- ORM knihovny (SQLAlchemy, Peewee, ...) – SQL dotazy pište ručně
- NoSQL databáze (MongoDB, Firebase, ...)
- Frontend frameworky (React, Vue, Angular, ...)
- AI generátory kódu pro celé bloky nebo funkce
- Kopírování cizího kódu bez pochopení a úpravy

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí všech technologií.**

---

## Struktura doporučeného repozitáře

```
maturitni-projekt-jmeno/
├── game/                   ← Pygame / PyQt / Godot projekt
│   ├── main.py             (nebo project.godot pro Godot)
│   ├── src/
│   │   ├── modely.py
│   │   └── ...
│   └── assets/
├── web/                    ← Flask aplikace
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── leaderboard.html
│   └── static/
│       └── css/
├── db/                     ← SQL skripty
│   ├── schema.sql
│   ├── seed.sql
│   └── queries.sql
├── tests/                  ← automatizované testy
│   └── test_modely.py
├── docs/                   ← dokumentace
│   ├── er_diagram.png
│   ├── flowchart_1.png
│   ├── flowchart_2.png
│   ├── manual.md
│   ├── dokumentace.md
│   ├── prezentace.md
│   └── prehled.md
├── .gitignore
├── requirements.txt
└── README.md
```

### Obsah `.gitignore`
```
__pycache__/
*.pyc
.env
*.db
venv/
.godot/
```
pripojeni.py
---

## Hodnocení

### Známky
- Žák získá **až 4 známky** (1 za každý kontrolní termín)

### Co se hodnotí

| Kritérium | Váha | Popis |
|-----------|:----:|---------|
| **Kompletnost** | 3 | Projekt obsahuje VŠECHNY části (web, aplikaci/hru, databázi a jejich propojení) |
| **Funkčnost** | 3 | Vše běží, nic nepadá, projekt lze spustit na školních PC |
| **Kvalita kódu** | 2 | Čitelnost, struktura, docstringy u všech tříd a funkcí |
| **Kvalita SQL** | 2 | Normalizace (BCNF), správné použití dotazů, DDL/DML |
| **Dokumentace** | 2 | Komentáře v kódu, všechny 4 povinné dokumenty, vývojové diagramy |
| **Celkový dojem** | 2 | Smysluplnost tématu, přehlednost, úroveň zpracování |
| **Testy** | 1 | Automatizované testy existují, jdou spustit a procházejí |
| **Práce s Gitem** | 1 | Pravidelné commity v každé fázi, smysluplné zprávy |
| **Komunikace s učitelem** | 1 | Reakce na zpětnou vazbu, aktivní přístup při kontrolních termínech |

### Vzájemné hodnocení (peer review)

Při kontrolních termínech si žáci navzájem **kontrolují projekty spolužáků** a hledají chyby (nefunkční části, chyby v kódu, SQL problémy, rozbitý web, chybějící dokumentace apod.).

#### Nalezené chyby ve VAŠEM projektu (trest za špatnou kvalitu)
- Za každých **5 nalezených chyb** ve vašem projektu dostanete **známku 5** (váha 1)
- Motivace: testujte svůj projekt důkladně před odevzdáním

#### Nalezení chyb v CIZÍM projektu (odměna za pečlivost)
- Za každé **2 nalezené chyby** v projektu spolužáka dostanete **známku 1** (váha 1)
- Motivace: pečlivě kontrolujte práci ostatních – pomáháte jim i sobě

> **Pravidla peer review:**
> - Chyba musí být **reálná a ověřitelná** (učitel rozhoduje sporné případy)
> - Duplicitní hlášení stejné chyby se nepočítá
> - Chyby se zapisují do souboru **Issues.txt** v gitovém úložišti kontrolovaného projektu
> - **Commit** s nalezenou chybou musí být odeslán **do konce hodiny** po odprezentování ve třídě
> - Kdo pošle commit jako **první**, má přednost v případě nalezení stejné chyby
>
> **Formát zápisu do Issues.txt:**
> ```
> 1. Hra padá po 30 sekundách – nekontrolovaná vyjímka v herní smyčce (Koudelka)
> 2. Registrace na webu neumožňuje zadat heslo delší než 8 znaků (Novák)
> 3. SELECT dotaz na výsledky nezobrazuje jméno hráče (Dvořáková)
> ```
>
> **Formát commit zprávy:**
> ```
> git commit -m "Issue: hra padá po 30 sekundách – nekontrolovaná vyjímka"
> ```

### Podmínka pro maturitu
> Žák **musí tento projekt odevzdat**, aby byl z předmětu programování hodnocen a mohl přistoupit k **praktické maturitní zkoušce v řádném termínu**.

Hodnocení kompletního projektu v posledním termínu **začíná na stupni 4 (dostatečný)** – tím, že projekt obsahuje všechny části. Dále se hodnocení zlepšuje dle kvality zpracování na základě uvážení vyučujícího. Tzn. pokud žák splní všechny požadavky v tomto dokumentu, tak se dostal na známku 4 a dále se může zlepšit až na 1 (výborný) v závislosti na kvalitě zpracování, komunikaci a zpětné vazbě od učitele a spolužáků (peer review).

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti** (větev `main`)
- Projekt musí jít **spustit na školních PC v učebně VT6** bez speciálních kroků krom `pip install -r requirements.txt`
- SQL skripty přiloženy v repozitáři (`db/` složka)
- ER diagram přiložen v repozitáři (`docs/` složka)
- Testy musí jít spustit
- Finální verze je označena tagem: `v1.x` případně se za finální verzi bere verze odevzdaná v den kontrolního termínu či 14 dní před maturitou
- **Deadline: 14 dní před praktickou maturitní zkouškou či v kontrolním termínu**

> **Projekt nahraný jako jeden velký commit v den odevzdání = nesplnění podmínek pro přistoupení k maturitě.**
