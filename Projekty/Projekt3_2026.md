# Projekt 3 – Webová vrstva a databáze (3. ročník / 2026)

## Cíl projektu

Navázat na práci z 1. a 2. ročníku a přidat **webovou vrstvu (Flask)** a **relační databázi (SQL)**. Na konci 3. ročníku musí projekt tvořit **funkční celek** – hra/systém z P2, webové rozhraní a databáze jsou vzájemně propojeny a sdílejí data.

> Skupiny jsou stejné jako v 1. a 2. ročníku a pracují ve **stejném repozitáři**, který rozšíří o nové složky `web/` a `db/`.

---

## Co navazuje na předchozí projekty

| Projekt | Co bylo vytvořeno | Jak to vstupuje do P3 |
|---------|------------------|----------------------|
| **P1** | Konzolová aplikace – logika, práce se soubory | Logika se přesouvá do databáze |
| **P2** | Grafická aplikace s OOP (Pygame / PyQt) | Hra/systém ukládá výsledky do DB |
| **P3** | Web + DB | Web zobrazuje data z DB, hra je napojena |

---

## Organizace práce

### Skupiny
- **Stejné skupiny jako v 1. a 2. ročníku** (3–4 členové)
- Práce pokračuje ve **stejném gitovém úložišti**
- Repozitář dostane novou větev `develop-r3` a nové složky: `web/`, `db/`

### Struktura repozitáře po P3

```
skupina-pokladna/
├── src/              ← kód z P1 a P2 (konzole + OOP)
├── game/             ← Pygame / PyQt kód z P2
├── web/              ← nové v P3 – Flask aplikace
│   ├── app.py
│   ├── templates/
│   └── static/
├── db/               ← nové v P3 – SQL skripty
│   ├── schema.sql
│   ├── seed.sql
│   └── queries.sql
├── docs/             ← dokumentace, diagramy, ER diagram
└── README.md
```

### Workflow

```
main (vždy funkční – merge pouze přes PR)
 │
 ├── develop-r3 (integrační větev 3. ročníku)
 │     │
 │     ├── feature/databaze-schema
 │     ├── feature/flask-zakladni-routes
 │     ├── feature/login-registrace
 │     └── feature/propojeni-hry-s-db
```

### Pravidla pro commity

```
✅  feat: vytvořen model User a tabulka users
✅  feat: Flask route /leaderboard zobrazuje top 10 skóre
✅  fix: opravena SQL injection v přihlašování
✅  docs: ER diagram aktualizován o tabulku score

❌  databaze hotova
❌  oprava webu
❌  update123
```

---

## Role ve skupině

Každý člen **v každém sprintu zastává jinou roli** – všichni tak do konce roku vyzkouší každou roli přesně jednou.

Za každý sprint dostane žák **1 známku** hodnocenou individuálně.

---

### 🟦 Role 1: Vedoucí projektu *(Project Lead)*

**Zodpovídá za:**
- Na začátku sprintu vytvoří **GitHub Issues**, přiřadí je členům
- Vytvoří `develop-r3`, hlídá workflow
- Merguje schválené Pull Requesty do `develop-r3`
- Na konci sprintu otevře **Release PR** a prezentuje výsledky
- Tvoří a udržuje **ER diagram** databáze
- Navrhuje, jak spolu komunikují web, hra a databáze (datové toky)

---

### 🟩 Role 2: Webový vývojář *(Web Developer)*

**Zodpovídá za:**
- Implementuje **Flask routes** (endpointy, šablony Jinja2)
- Tvoří nebo upravuje **HTML šablony** (templates/) a CSS
- Implementuje **login a registraci** uživatele
- Zobrazuje data z databáze na webových stránkách
- Dbá na **bezpečnost** – žádné SQL injection, hashování hesel

---

### 🟨 Role 3: Správce databáze *(Database Administrator)*

**Zodpovídá za:**
- Navrhuje **databázové schéma** dle ER diagramu vedoucího
- Píše DDL skripty (`CREATE TABLE`, `ALTER`, `DROP`) do `db/schema.sql`
- Plní vzorová data (`INSERT`) do `db/seed.sql`
- Píše složitější **SELECT dotazy** (JOIN, WHERE, GROUP BY, ORDER BY) do `db/queries.sql`
- Napojuje databázi na Flask aplikaci a na Pygame/PyQt aplikaci z P2

---

### 🟥 Role 4: Vývojář / Tester *(Developer + QA)*

**Zodpovídá za:**
- Rozšiřuje nebo opravuje **Pygame/PyQt kód z P2** (stabilita, napojení na DB)
- Implementuje v aplikaci **ukládání výsledků do databáze** (skóre, jméno hráče)
- Testuje celý projekt: hra, web, databáze – hledá bugy
- Provádí **code review** Pull Requestů ostatních
- Schválí nebo zamítne PRy s komentáři

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **Webový vývojář a Správce databáze se sloučí** do jedné.

---

## Sprinty a kontrolní termíny

| Sprint | Období | Co se buduje | GitHub aktivita |
|--------|--------|-------------|-----------------|
| **1** | Začátek února | ER diagram, databázové schéma, základní Flask struktura | Issues, feature větve, PR |
| **2** | Polovina března | SELECT dotazy, napojení hry na DB, základní webové stránky | PRy s review, rotace rolí |
| **3** | Konec dubna | Login + registrace na webu, zobrazení dat z DB, UPDATE/DELETE | PRy, peer review |
| **4** | Začátek června | Finální propojení všeho, dokumentace, Release PR | Release PR, prezentace |

---

## Doporučený postup práce – příklad pro 4 členy (A, B, C, D)

### Sprint 1 – Databáze a základ Flasku (začátek února)

| Člen | Role | Co dělá |
|------|------|---------|
| **A** | Vedoucí | Navrhne a nakreslí **ER diagram** (tabulky, vztahy 1:N a M:N), vytvoří Issues, nastaví `develop-r3`, prezentuje |
| **B** | Webový vývojář | Nastaví strukturu Flask aplikace (`web/app.py`, `templates/`, `static/`), vytvoří základní stránku „Vítejte" |
| **C** | Správce DB | Dle ER diagramu napíše `db/schema.sql` (CREATE TABLE s PK, FK, NOT NULL, UNIQUE), nastaví SQLite/MySQL |
| **D** | Vývojář/Tester | Otestuje databázové schéma (zkusí spustit SQL skripty), zahájí refaktoring P2 pro napojení na DB |

### Sprint 2 – Napojení hry a první web (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **B** | Vedoucí | Merguje PRy, kontroluje propojení, aktualizuje ER diagram pokud třeba, prezentuje |
| **C** | Webový vývojář | Vytvoří stránky: seznam výsledků (`/leaderboard`), detail hráče; použije Jinja2 šablony |
| **D** | Správce DB | Napíše `db/seed.sql` (INSERT vzorová data), napíše SELECT dotazy s JOIN, WHERE, ORDER BY |
| **A** | Vývojář/Tester | Propojí Pygame/PyQt aplikaci s DB – po skončení hry se uloží jméno a skóre; testuje PRy |

### Sprint 3 – Login, registrace a zobrazení dat (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **C** | Vedoucí | Kontroluje funkčnost webu + DB, řeší integrační problémy, prezentuje |
| **D** | Webový vývojář | Implementuje **login a registraci** (hashování hesla pomocí `werkzeug.security`), session management |
| **A** | Správce DB | Napíše UPDATE a DELETE dotazy, ověří normalizaci (BCNF), doplní FK constrainty |
| **B** | Vývojář/Tester | Finalizuje Pygame/PyQt – hra je stabilní, zeptá se na jméno hráče před uložením skóre; testuje PRy |

### Sprint 4 – Finalizace a propojení (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|------|------|---------|
| **D** | Vedoucí | Otevře Release PR (`develop-r3` → `main`), finální kontrola celého projektu, prezentuje |
| **A** | Webový vývojář | Finální úpravy webu – přidá screenshoty ze hry, informace o projektu, konzistentní CSS |
| **B** | Správce DB | Zkompletuje SQL skripty, ověří normalizaci, přiloží aktuální ER diagram |
| **C** | Vývojář/Tester | Celkové finální testování (web, hra, DB), uzavře Issues, ověří README |

---

## Funkční požadavky

### Webová stránka (Flask)

| Požadavek | Detail |
|-----------|--------|
| **Minimálně 4 stránky** | Hlavní stránka, přihlášení, registrace, žebříček výsledků |
| **Login a registrace** | Uživatel se může registrovat a přihlásit; heslo je **hashované** (`werkzeug.security`) |
| **Zobrazení dat z DB** | Stránka se žebříčkem zobrazuje výsledky ze hry načtené z databáze |
| **Jinja2 šablony** | HTML šablony s dědičností (`{% extends %}`, `{% block %}`) |
| **CSS** | Minimálně 1 vlastní CSS soubor pro konzistentní vizuál |
| **Session** | Přihlášený uživatel je rozpoznán napříč stránkami |

### Databáze (SQL)

| Požadavek | Detail |
|-----------|--------|
| **ER diagram** | Nakreslen a přiložen v `docs/er_diagram.png` |
| **Vztahy** | Databáze využívá vztahy 1:N **i** M:N (tedy alespoň 3 tabulky) |
| **DDL** | `CREATE TABLE` s: datový typ, `UNIQUE`, `NOT NULL`, `AUTO_INCREMENT`, `PRIMARY KEY`, `FOREIGN KEY`, `DEFAULT` |
| **DML** | `INSERT` – min. 3 vzorové záznamy do každé tabulky |
| **SELECT** | Dotazy s `JOIN`, `WHERE`, `ORDER BY`, `GROUP BY`, `LIKE`, agregační funkce |
| **DML úpravy** | `UPDATE` a `DELETE` příkazy jsou přiloženy ve skriptech |
| **Normalizace** | Minimálně po **Boyceho-Coddovu normální formu (BCNF)** |

### Propojení (hra ↔ DB ↔ web)

| Požadavek | Detail |
|-----------|--------|
| **Hra ukládá do DB** | Po skončení hry/systému se uloží výsledek (jméno, skóre/výsledek) do databáze |
| **Web čte z DB** | Webová stránka zobrazuje data uložená hrou |
| **Sdílená DB** | Hra i web přistupují ke stejné databázi |

### Dokumentace

- Z **Git historie** musí být patrné, kdo co napsal
- Každá **Flask route** má komentář popisující účel
- Každá **třída a metoda** (Python) má docstring
- `README.md` obsahuje: jak spustit webovou aplikaci, jak nastavit databázi, jak spustit hru
- Přiloženy: ER diagram, SQL skripty, seznam endpointů

---

## Bezpečnostní požadavky

> Toto jsou minimální bezpečnostní praktiky – porušení bude bráno jako chyba při peer review.

| Riziko | Opatření |
|--------|----------|
| **SQL injection** | Používejte parametrizované dotazy (`cursor.execute("... WHERE id = ?", (id,))`) – nikdy f-string s uživatelským vstupem v SQL |
| **Hashování hesel** | Nikdy neukládejte heslo jako prostý text – použijte `werkzeug.security.generate_password_hash` |
| **Session fixation** | Používejte `flask.session` správně, nastavte `SECRET_KEY` v konfiguraci |
| **Přístup bez přihlášení** | Stránky s daty chráňte podmínkou: `if 'user_id' not in session: return redirect(url_for('login'))` |

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **Python 3** + OOP
- **Pygame** nebo **PyQt6** (ze sprintu P2)
- **Flask** (webový framework – probíraný ve výuce)
- **Jinja2** (šablonovací jazyk – součást Flask)
- **HTML 5** + **CSS 3** (vlastní, bez frameworků)
- **SQL** – MySQL / MariaDB nebo SQLite (dle toho, co se probírá ve výuce)
- **Git** + **GitHub**
- Standardní knihovny Pythonu

### ❌ Zakázáno
- Jiné webové frameworky (Django, FastAPI, Express apod.)
- CSS frameworky (Bootstrap, Tailwind apod.)
- ORM knihovny (SQLAlchemy apod.) – SQL dotazy pište ručně
- NoSQL databáze (MongoDB apod.)
- Frontend frameworky (React, Vue, Angular apod.)
- Jiné programovací jazyky
- AI generátory celých bloků kódu
- Kopírování cizího kódu bez pochopení

---

## Hodnocení

### Známky za sprinty – individuální

Každý žák získá **4 známky** (1 za každý sprint). Hodnotí se aktuální role:

| Kritérium | Vedoucí | Web. vývojář | Správce DB | Vývojář/Tester |
|-----------|---------|--------------|------------|----------------|
| Splnění role | ✅ | ✅ | ✅ | ✅ |
| Kvalita výstupu | ER diagram + Issues | Routes, šablony, CSS | SQL skripty, normalizace | Stabilita kódu, testy |
| Práce s Gitem | Merge, Release PR | Commity web kódu | Commity SQL | Feature větve, review |
| Bezpečnost | Datové toky | SQL injection, hesla | Normalizace, FK | Testování edge cases |
| Prezentace | ✅ | – | – | – |

### Vzájemné hodnocení skupin (peer review)

Při kontrolních termínech si skupiny navzájem **kontrolují projekty ostatních skupin** a hledají chyby.

#### Nalezené chyby ve VAŠEM projektu *(motivace dělat kvalitně)*
- Za každých **5 nalezených chyb** ve vašem projektu dostane **celý tým známku 5** (váha 1)

#### Nalezení chyb v CIZÍM projektu *(motivace pečlivě testovat)*
- Za každé **2 nalezené chyby** v projektu jiné skupiny dostane **jednotlivec, který chybu našel, známku 1** (váha 1)

> **Pravidla peer review:**
> - Chyba musí být **reálná a ověřitelná** – učitel rozhoduje sporné případy
> - Duplicitní hlášení stejné chyby se nepočítá
> - Chyby se zapisují **jako GitHub Issue** (label: `peer-review`)
> - Issue musí být vytvořeno **do konce hodiny** po odprezentování
>
> **Formát GitHub Issue:**
> - **Název:** `[Peer review] Stručný popis chyby`
> - **Popis:** Co se stane, jak to reprodukovat, co se očekávalo
> - **Label:** `peer-review`
>
> Příklady:
> ```
> [Peer review] SQL dotaz na stránce výsledků vrací chybu – špatný JOIN
> [Peer review] Login umožňuje přihlášení s libovolným heslem – SQL injection
> [Peer review] Hra neukládá skóre do databáze po skončení
> [Peer review] Hesla jsou uložena jako prostý text, bez hashování
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti** (větev `main`)
- Webová aplikace musí jít **spustit na školních počítačích**
- SQL skripty musí být přiloženy v `db/` (schema.sql, seed.sql, queries.sql)
- ER diagram musí být přiložen v `docs/`
- Z **Git historie a PR** musí být patrné, kdo co dělal

---

---

# 🗺️ Roadmapa Sprintu 1 – krok za krokem

> Tato sekce ukazuje **přesně co, kdy a jak** by měl každý člen týmu udělat během prvního sprintu.  
> Příklad je pro skupinu „Pokladna" (SQLite + Flask).  
> A = Vedoucí, B = Webový vývojář, C = Správce DB, D = Vývojář/Tester.  
> Časový rámec: **2–3 týdny**.

---

## 📅 Den 1 – Kick-off

### Celý tým společně:
- [ ] Projít projekt z P2, domluvit se **co jde do databáze** (co bylo v souborech)
- [ ] Stáhnout repozitář a přepnout na novou větev:
  ```bash
  git checkout main
  git pull
  git checkout -b develop-r3
  git push -u origin develop-r3
  ```

### 🟦 Vedoucí (A) – den 1:
- [ ] Nakreslit **ER diagram** (aspoň 3 tabulky, vztahy 1:N a M:N):

  ```
  users (id, username, password_hash, created_at)
      1 ─────────────────── N
  scores (id, user_id, score, played_at)
  
  items (id, nazev, cena)
      M ─────────────────── N
  scores (přes tabulku score_items)
  score_items (score_id, item_id, mnozstvi)
  ```

- [ ] Uložit jako `docs/er_diagram.png`
- [ ] Vytvořit Issues pro sprint 1:

  | # | Název | Přiřazeno |
  |---|-------|-----------|
  | 8 | `ER diagram a datové toky` | A (Vedoucí) |
  | 9 | `Flask – základní struktura a stránka index` | B (Webový vývojář) |
  | 10 | `DB schema – CREATE TABLE dle ER diagramu` | C (Správce DB) |
  | 11 | `Refaktoring P2 – příprava napojení na DB` | D (Vývojář/Tester) |

---

## 📅 Dny 2–5 – Webový vývojář zakládá Flask projekt

### 🟩 Webový vývojář (B):

**Krok 1 – Větev a struktura projektu:**
```bash
git checkout develop-r3
git checkout -b feature/flask-zaklad
mkdir -p web/templates web/static/css web/static/images
```

**Krok 2 – Základní Flask aplikace** (`web/app.py`):

```python
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "NAHRADTE_BEZPECNYM_KLICEM"  # V produkci používejte env proměnnou!


@app.route("/")
def index():
    """Hlavní stránka – uvítací obrazovka."""
    return render_template("index.html")


@app.route("/leaderboard")
def leaderboard():
    """Zobrazí žebříček výsledků ze hry."""
    # TODO: načíst data z databáze
    vysledky = []
    return render_template("leaderboard.html", vysledky=vysledky)


if __name__ == "__main__":
    app.run(debug=True)
```

**Krok 3 – Základní šablony** (`web/templates/base.html`):

```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Pokladna{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Domů</a>
        <a href="{{ url_for('leaderboard') }}">Výsledky</a>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**Krok 4 – Commit a PR do `develop-r3`**, closes #9

---

## 📅 Dny 2–5 – Správce DB vytváří schéma

### 🟨 Správce DB (C):

**Krok 1 – Větev:**
```bash
git checkout develop-r3
git checkout -b feature/databaze-schema
```

**Krok 2 – Schéma** (`db/schema.sql`):

```sql
-- Tabulka uživatelů
CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabulka výsledků hry
CREATE TABLE IF NOT EXISTS scores (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER      NOT NULL,
    score       INTEGER      NOT NULL DEFAULT 0,
    played_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabulka položek (z P1/P2)
CREATE TABLE IF NOT EXISTS items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev       VARCHAR(100) NOT NULL UNIQUE,
    cena        DECIMAL(10,2) NOT NULL CHECK (cena >= 0)
);
```

**Krok 3 – Vzorová data** (`db/seed.sql`):

```sql
INSERT INTO users (username, password_hash) VALUES
    ('admin',  'hash_placeholder_1'),
    ('novak',  'hash_placeholder_2'),
    ('dvorak', 'hash_placeholder_3');

INSERT INTO items (nazev, cena) VALUES
    ('Rohlík',  2.50),
    ('Máslo',  45.00),
    ('Mléko',  25.90);

INSERT INTO scores (user_id, score) VALUES
    (1, 150),
    (2, 230),
    (1, 180);
```

**Krok 4 – Commit a PR**, closes #10

---

## 📅 Dny 3–7 – Vývojář/Tester připravuje P2 pro napojení

### 🟥 Vývojář/Tester (D):

- [ ] Přidat do Pygame/PyQt aplikace funkci `uloz_skore_do_db(jmeno, skore)` – zatím jen stub
- [ ] Otestovat spuštění SQL skriptů: `sqlite3 db/hra.db < db/schema.sql`
- [ ] Provést code review PRů #9 a #10 – komentáře, schválení nebo zamítnutí

---

## 📅 Den 10–14 – Vedoucí merguje a uzavírá sprint

### 🟦 Vedoucí (A):

- [ ] Mergovat PR z `feature/flask-zaklad` → `develop-r3`
- [ ] Mergovat PR z `feature/databaze-schema` → `develop-r3`
- [ ] Otevřít Release PR: `develop-r3` → `main`
  - Název: `Release Sprint 1 – Flask základ + DB schéma`
- [ ] Prezentovat výsledky sprint 1

> **Sprint 1 je hotov, když:** Flask aplikace jde spustit, SQL schema se spustí bez chyb, ER diagram je v docs a Release PR je mergnut.
