# Projekt 4 – Maturitní projekt (4. ročník / 2026)

## Cíl projektu

Samostatně vytvořit **kompletní softwarový projekt**, který integruje vše, co jste se naučili během tříletého studia: datovou logiku z P1, grafickou aplikaci z P2 a webovou vrstvu s databází z P3. Projekt je **podmínkou pro přistoupení k praktické maturitní zkoušce**.

---

## Organizace práce

### Práce je individuální
- Každý žák pracuje **sám**
- Žák si zakládá **vlastní gitové úložiště** (GitHub) a přidá učitele jako collaboratora s právy `Read`
- **Doporučení:** Veřejný repozitář ušetří starosti s přístupy

---

## Volba technologie – NOVÉ PRAVIDLO 2026

> **Žák smí používat POUZE technologie, se kterými jsme pracovali v průběhu studia – nebo Godot s GDScriptem (případně Python bindingem).**

**Není povoleno volit libovolný jiný jazyk nebo framework** po dohodě s učitelem (jako tomu bylo v předchozích letech). Cílem je prokázat zvládnutí technologií, které jste studovali, nikoliv naučit se na poslední chvíli nový jazyk.

### Povolené herní technologie (vyber jednu):

| Možnost | Technologie | Vhodné pro |
|---------|-------------|------------|
| **A** | Python + Pygame | Klasické 2D hry (platformer, shooter, puzzle, RPG...) |
| **B** | Python + PyQt6 | Desktopová aplikace / systém s GUI |
| **C** | Godot (GDScript nebo gdscript Python-like syntaxe) | Pokročilejší 2D/3D hry, animace, fyzika |

> **Volbu technologie nahlaste učiteli nejpozději do konce září.** Pokud zvolíte Godot, musí projekt jít spustit na školních počítačích – ověřte to na začátku října.

---

## Kontrolní termíny

| # | Období | Co musí být hotové |
|---|--------|--------------------|
| **1** | Začátek listopadu | Výběr tématu, funkční menu (hra i web), ER diagram, návrh datových toků, první commity |
| **2** | Konec ledna | Základní herní logika, databáze s daty, napojení hry na DB, login na webu |
| **3** | Konec března | Vše funguje dohromady, automatizované testy, zapracovaná zpětná vazba z termínu 2 |
| **4** | 14 dní před praktickou maturitou | **Finální odevzdání** – kompletní, funkční, zdokumentovaný projekt |

> **Pozn.:** Termíny 3 a 4 se mohou časově přiblížit. V takovém případě může žák obdržet **3 hodnocení místo 4** – toto závisí na ročním plánu.

---

## Doporučený postup práce

### 1. fáze (září – začátek listopadu)

| Oblast | Co dělat |
|--------|----------|
| **Plánování** | Vybrat téma, navrhnout datové toky (co-kde-kam-odkud) |
| **Databáze** | Navrhnout a nakreslit ER diagram, napsat `schema.sql` |
| **Hra/app** | Funkční menu (start, ukončení), základní okno |
| **Web** | Základ Flask projektu, stránka index, navigace |
| **Git** | Založit repozitář, nastavit strukturu složek, první commity |

> **Tip:** Nepoužívejte větve `feature/...` povinně (pracujete sami), ale pravidelné commity se smysluplnými zprávami jsou **povinné** – slouží jako důkaz průběžné práce.

### 2. fáze (listopad – konec ledna)

| Oblast | Co dělat |
|--------|----------|
| **Hra/app** | Základní herní logika – pohyb, interakce, herní stavy |
| **Databáze** | Vzorová data (`INSERT`), SELECT dotazy (JOIN, WHERE, ORDER BY) |
| **Propojení** | Hra ukládá výsledky do DB, web čte data z DB |
| **Web** | Login a registrace s hashováním, zobrazení herních výsledků |
| **Dokumentace** | Komentáře průběžně, začít uživatelský manuál |

### 3. fáze (leden – konec března)

| Oblast | Co dělat |
|--------|----------|
| **Hra/app** | Doladit mechaniky, opravit bugy, zeptat se na jméno hráče |
| **Databáze** | UPDATE, DELETE skripty, ověření normalizace (BCNF) |
| **Web** | Aktualizovaný obsah, screenshoty, vývojové diagramy |
| **Testy** | Napsat minimálně **3 automatizované testy** (`pytest` nebo `unittest`) |
| **Dokumentace** | Dokončit docstringy, finalizovat manuál, aktualizovat ER diagram |

### 4. fáze (březen – 14 dní před maturitou)

| Oblast | Co dělat |
|--------|----------|
| **Vše** | Finální testování – hra nepadá, web funguje, DB odpovídá, vše je propojené |
| **Dokumentace** | SQL skripty přiloženy, ER diagram aktuální, manuál hotový |
| **Git** | Vyčistit repozitář, zkontrolovat historii commitů, tag `v1.0` |
| **Kvalita** | Zapracovaná zpětná vazba z termínů 1–3, kód čitelný a komentovaný |

---

## Funkční požadavky

Projekt musí obsahovat **VŠECHNY** následující části:

---

### 1. Herní / grafická část

**Pygame nebo PyQt:**

| Požadavek | Detail |
|-----------|--------|
| **OOP** | Kód postaven na třídách; min. 3 vlastní třídy s docstringy |
| **Grafické rozhraní** | Aplikace má okno – ne konzoli |
| **Hlavní menu** | Menu s tlačítky (start, nastavení, exit) ovládatelné myší/klávesnicí |
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

> **Poznámka k Godotu:** Napojení na databázi lze realizovat buď přes SQLite plugin pro Godot, nebo přes Flask API (`HTTPRequest` node → Flask endpoint → DB). Obě varianty jsou akceptovatelné – konzultujte s učitelem.

---

### 2. Webová stránka (Flask)

| Požadavek | Detail |
|-----------|--------|
| **Min. 4 stránky** | Index, login, registrace, žebříček výsledků |
| **Login a registrace** | Heslo **hashované** (`werkzeug.security`), session management |
| **Zobrazení dat z DB** | Stránka se žebříčkem zobrazuje data načtená z databáze |
| **Jinja2 šablony** | Dědičnost šablon (`{% extends %}`), základní layout v `base.html` |
| **Vlastní CSS** | Minimálně 1 CSS soubor, konzistentní vizuál |
| **Bezpečnost** | Parametrizované SQL dotazy (žádné f-stringy s uživatelskými daty v SQL) |

---

### 3. Databáze (SQL)

| Požadavek | Detail |
|-----------|--------|
| **ER diagram** | Nakreslen a přiložen (`docs/er_diagram.png` nebo PDF) |
| **Vztahy** | Min. 3 tabulky, využity vztahy 1:N i M:N |
| **DDL skripty** | `CREATE TABLE` s: datový typ, `UNIQUE`, `NOT NULL`, `AUTO_INCREMENT`/`AUTOINCREMENT`, `PRIMARY KEY`, `FOREIGN KEY`, `DEFAULT` |
| **DML – INSERT** | Min. 3 vzorové záznamy do každé tabulky (`db/seed.sql`) |
| **SELECT dotazy** | `JOIN`, `WHERE`, `ORDER BY`, `GROUP BY`, `LIKE`, agregační funkce (`db/queries.sql`) |
| **DML – úpravy** | `UPDATE` a `DELETE` příkazy přiloženy |
| **Normalizace** | Minimálně po **Boyceho-Coddovu normální formu (BCNF)** |

---

### 4. Propojení

| Požadavek | Detail |
|-----------|--------|
| **Hra → DB** | Hra/app ukládá výsledky do databáze po skončení |
| **Web → DB** | Web čte data z databáze a zobrazuje je |
| **Sdílená databáze** | Všechny části pracují se stejnou databází |

---

### 5. Automatizované testy *(navíc oproti skupinovým projektům)*

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

---

### 6. Dokumentace

| Požadavek | Detail |
|-----------|--------|
| **Git historie** | Pravidelné commity s popisnými zprávami – viditelná průběžná práce |
| **Docstringy** | Každá třída, metoda a Flask route má docstring/komentář |
| **README.md** | Jak spustit hru, web a databázi; seznam závislostí (`requirements.txt`) |
| **ER diagram** | Aktuální, přiložen v repozitáři |
| **SQL skripty** | Všechny skripty přiloženy (`schema.sql`, `seed.sql`, `queries.sql`) |
| **Uživatelský manuál** | Jak hru/systém ovládat (jako hráč/uživatel) |
| **Vývojové diagramy** | Flowcharty klíčových mechanik (min. 2) |

---

## Bezpečnostní požadavky

> Nedodržení těchto pravidel je automaticky **chyba hodnocená jako 5** v hodnocení za příslušnou část.

| Riziko | Povinné opatření |
|--------|-----------------|
| **SQL injection** | Vždy parametrizované dotazy: `cursor.execute("... WHERE id = ?", (id,))` |
| **Hesla v plaintextu** | Nikdy: `werkzeug.security.generate_password_hash()` a `check_password_hash()` |
| **Secret key** | `app.secret_key` nikdy necommitovat jako pevný řetězec do Git – použijte proměnnou prostředí nebo `.env` soubor (přidejte `.env` do `.gitignore`) |
| **Přístup bez přihlášení** | Chráněné stránky ověřují session: `if 'user_id' not in session` |

---

## Povolené technologie

> **POUZE technologie ze školy nebo Godot s GDScriptem.**

### ✅ Povoleno

| Oblast | Technologie |
|--------|-------------|
| **Hra / GUI** | Python 3 + Pygame, Python 3 + PyQt6, nebo Godot 4 (GDScript) |
| **Web** | Python 3 + Flask + Jinja2 |
| **Databáze** | SQLite nebo MySQL / MariaDB |
| **Frontend** | HTML 5 + CSS 3 (vlastní – bez frameworků) |
| **Testování** | `pytest`, `unittest` |
| **Verzování** | Git + GitHub |
| **Standardní knihovny** | `os`, `json`, `csv`, `random`, `math`, `datetime`, `werkzeug`, ... |
| **Grafika** | GIMP, Piskel, Malování – pro tvorbu spritů |

### ❌ Zakázáno

- Jiné programovací jazyky (JavaScript, C#, Java, C++, Rust, ...)
- Jiné herní enginy (Unity, Unreal, GameMaker, ...)
- Jiné webové frameworky (Django, FastAPI, Node.js, Express, ...)
- CSS frameworky (Bootstrap, Tailwind, Bulma, ...)
- ORM knihovny (SQLAlchemy, Peewee, ...) – SQL dotazy pište ručně
- NoSQL databáze (MongoDB, Firebase, ...)
- Frontend frameworky (React, Vue, Angular, ...)
- AI generátory kódu pro celé bloky nebo funkce
- Kopírování cizího kódu bez pochopení a úpravy

> **Proč toto omezení?** Maturitní zkouška ověřuje, co jste se naučili ve škole. Prokázat zvládnutí jiného jazyka, který jste ve škole neměli, je mimo rámec hodnocení. Godot je výjimka – je dostupný jako freeware, má Python-like syntaxi a lze ho nainstalovat na školní počítače.

---

## Hodnocení

### Hodnocení za kontrolní termíny

Každý žák může získat **4 hodnocení** (1 za každý termín). Hodnotí se:

| Kritérium | Termín 1 | Termín 2 | Termín 3 | Termín 4 |
|-----------|----------|----------|----------|----------|
| Splnění termínu | Menu + plán | Logika + DB | Vše propojeno | Kompletní |
| Kvalita kódu | OOP základ | Čitelnost, OOP | Testy, docstringy | Finální kvalita |
| Práce s Gitem | Pravidelnost | Smysluplnost | Průběžnost | Kompletní historie |
| Bezpečnost | – | DB, hesla | SQL injection | Celkový audit |
| Dokumentace | ER diagram, plán | README začátek | Manuál, diagramy | Finální verze |

### Hodnocení za maturitní zkoušku

Projekt 4 je **podmínkou pro přistoupení k praktické maturitní zkoušce**. Projekt musí:
- Jít spustit na školním počítači
- Obsahovat všechny povinné části (viz Funkční požadavky)
- Mít kompletní dokumentaci a Git historii

> Konkrétní kritéria praktické maturitní zkoušky jsou stanovena samostatným dokumentem.

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
│   └── manual.md
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

### Obsah `requirements.txt`
```
flask
werkzeug
pytest
```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti** (větev `main`)
- Repozitář musí být **přístupný učiteli** (přidat jako collaboratora)
- Projekt musí jít **spustit na školním počítači** bez speciálních kroků krom `pip install -r requirements.txt`
- Repozitář obsahuje: zdrojový kód (vše), `README.md`, SQL skripty, ER diagram, testy, uživatelský manuál
- Git historie ukazuje **průběžnou práci** – ne hromadné nahrání vše najednou těsně před termínem
- Finální verze je označena tagem: `git tag v1.0 && git push origin v1.0`

> **Projekt nahraný jako jeden velký commit v den odevzdání = nesplnění podmínek pro přistoupení k maturitě.**
