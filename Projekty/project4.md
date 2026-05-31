# Projekt 4 – Samostatný projekt (4. ročník / maturitní)

## Cíl projektu

Samostatně vytvořit kompletní projekt, který obsahuje **všechny části** zpracovávané ve skupinách během předchozích 3 let: **webovou prezentaci, hru a databázi** – vše vzájemně propojené. Tento projekt je **podmínkou pro přistoupení k praktické maturitní zkoušce**.

---

## Organizace práce

### Práce je **individuální**
- Každý žák pracuje **sám**
- Žák se přidá k **existujícímu gitovému úložišti založené učitelem** a přidá se jako spolupracovník
- Žák použije znalosti získané během výuky a **všechny části projektu vytvoří sám** (web, hra, databáze)
- Žák **nevyužil AI** pro **generování celých bloků kódu**, ale **pouze pro inspiraci, komentování, generování textu a pomoc s konkrétními problémy**

### Volba jazyka
- Projekt **může být pouze v technologiích probíraných v rámci výuky (převážně Python)**, ale:
  - Je možné použít engine Godot (s GDScript) – po dohodě s učitelem


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
| **Databáze** | Navrhnout a zakreslit **ER diagram**, vytvořit CREATE TABLE skripty |
| **Hra** | Funkční **hlavní menu** (start, ukončení), základní okno Pygame |
| **Web** | Založit strukturu HTML souborů, základní navigace |
| **Git** | Založit repozitář, pravidelně commitovat |

### 2. fáze (listopad – začátek ledna)

| Oblast | Co dělat |
|--------|-----------|
| **Hra** | **Základní pohyb a logika** – postava se pohybuje, reaguje na vstupy, herní smyčka funguje |
| **Databáze** | Vložit vzorová data (INSERT), napsat SELECT dotazy (JOIN, WHERE, ORDER BY) |
| **Propojení** | Hra ukládá skóre do DB, web čte data z DB |
| **Web** | Implementovat **login + registraci**, zobrazit herní výsledky z databáze |
| **Dokumentace** | Komentovat kód průběžně, začít uživatelský manuál |

### 3. fáze (začátek ledna – konec února)

| Oblast | Co dělat |
|--------|-----------|
| **Hra** | Doladit mechaniky, opravit bugy, hra se zeptá na jméno hráče |
| **Databáze** | Doplnit UPDATE, DELETE, ověřit **normalizaci (BCNF)** |
| **Web** | Aktualizovat obsah, přidat screenshoty ze hry, vývojové diagramy |
| **Testy** | Napsat minimálně **2 automatizované testy** na důležité funkce |
| **Dokumentace** | Dokončit komentáře u všech tříd/funkcí, finalizovat manuál |

### 4. fáze (březen – 14 dní před maturitou)

| Oblast | Co dělat |
|--------|-----------|
| **Vše** | Finální testování – hra nepadá, web funguje, DB odpovídá, vše je propojené |
| **Dokumentace** | Všechny SQL skripty přiloženy, ER diagram aktuální, manuál hotový |
| **Git** | Vyčistit repozitář, zkontrolovat historii commitů |
| **Kvalita** | Zpětná vazba učitele zapracována, kód čitelný a komentovaný |

> **Tip:** Pracujte průběžně a pravidelně commitujte. Nenechávejte vše na poslední chvíli – projekt je rozsáhlý a musí obsahovat všechny části.

---

## Funkční požadavky

### Projekt musí obsahovat VŠECHNY následující části:

### 1. Webová prezentace
- Minimálně **4 HTML stránky** s navigační lištou
- **1 CSS soubor** pro jednotný design
- Obsahuje informace o hře, vývojové diagramy, pravidla, informace o autorovi
- **Login a registrace** uživatele
- **Zobrazení herních výsledků** z databáze
- Komunikuje s databází přes připravené dotazy

### 2. Hra / Desktopová aplikace
- **Herní smyčka / hlavní smyčka aplikace** (event loop nebo update + render)
- **Grafické rozhraní** – menu / hlavní okno, start/spuštění, ukončení
- **Interakce uživatele** (klávesnice/myš, formuláře, tlačítka)
- **Ukládání dat** do databáze (hra: jméno | skóre; aplikace: CRUD operace)
- Aplikace identifikuje uživatele – hra se zeptá na jméno, aplikace má přihlášení nebo výběr uživatele
- Projekt je **funkční, stabilní a smysluplný** – nesmí padat

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
>


### 3. Databáze

| Požadavek | Detail |
|-----------|--------|
| **ER diagram** | Zakreslen a přiložen k projektu |
| **Vztahy** | Využívá 1:N i M:N (tedy i JOIN při čtení dat) |
| **DDL skripty** | CREATE TABLE s atributy: datový typ, UNIQUE, NOT NULL, AUTO_INCREMENT, PK, FK, DEFAULT |
| **DML skripty** | INSERT – min. 3 vzorové záznamy do každé tabulky |
| **SELECT dotazy** | Včetně JOIN, filtrování (WHERE), řazení (ORDER BY), seskupování (GROUP BY), vyhledávání (LIKE) |
| **Úprava dat** | UPDATE a DELETE příkazy |
| **Normalizace** | Minimálně po **Boyceho-Coddovu normální formu (BCNF)** |
| **Komunikace** | S databází komunikuje web (přes PHP/jiný serverový jazyk) i hra (přes Python) |

### 4. Propojení
- Všechny tři části (web + hra + DB) musí **spolu komunikovat** min. vždy 2 mezi sebou např. DB a hra, DB a web, web a hra
- Web zobrazuje data z databáze
- Hra ukládá data do databáze

### 5. Automatizované testy (NAVÍC oproti skupinovému projektu)
- Minimálně **2 automatizované testy**
- Testy musí být zaměřeny na **důležité funkce projektu**
- Testy musí jít spustit a musí procházet

### 6. Dokumentace
- Z historie Gitu musí být patrné, **co kdy bylo nahráno**
- Každá fáze bude obsahovat minimálně **5 commitů** s popisnými zprávami (feat: Nová funkce sčítání, fix: oprava for cyklu, docs: přidání komentářů pro vytvoření postavy, update: vylepšení funkce o sčítání více čísel atd.)
- Kód obsahuje **komentáře** popisující jednotlivé bloky
- **Všechny třídy a funkce/metody** musí mít popisný komentář
- 3× Vývojové diagramy klíčových mechanik aplikace/hry

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

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce** (případně jiný jazyk po dohodě s učitelem – viz sekce Volba jazyka).

### ✅ Povoleno
- **Python 3** + **Pygame** (hra) – nebo jiný jazyk po dohodě s učitelem
- **HTML 5** + **CSS 3** (webová prezentace)
- **SQL** (MySQL / MariaDB / SQLite – dle toho, co se probírá ve výuce)
- **PHP / JS / Flask** nebo jiný serverový jazyk probíraný ve výuce
- **Git** (GitHub / GitLab)
- Standardní knihovny zvoleného jazyka
- Grafické editory pro tvorbu spritů
- Testovací frameworky probírané ve výuce (pytest, unittest apod.)

### ❌ Zakázáno
- Herní enginy (Unity, Unreal, apod.) – pokud nebyly dohodnuty s učitelem
- Webové frameworky (React, Vue, Angular, Django, Flask apod.) – pokud nebyly probírány ve výuce
- CSS frameworky (Bootstrap, Tailwind apod.)
- ORM knihovny – SQL dotazy pište ručně
- NoSQL databáze (MongoDB apod.)
- AI generátory kódu pro celé bloky
- Kopírování cizího kódu bez pochopení a úpravy

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí všech technologií.**

---

## Hodnocení

### Známky
- Žák získá **až 4 známky** (1 za každý kontrolní termín)
- Pokud se termíny 3 a 4 kryjí, mohou být známky jen **3**

### Co se hodnotí

| Kritérium | Váha | Popis |
|-----------|:----:|---------|
| **Kompletnost** | 3 | Projekt obsahuje VŠECHNY části (web, aplikaci/hru, databázi a jejich propojení) |
| **Funkčnost** | 3 | Vše běží, nic nepadá, projekt lze spustit na školních PC |
| **Kvalita kódu** | 2 | Čitelnost, struktura, komentáře u všech tříd a funkcí |
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

Hodnocení kompletního projektu v posledním termínu **začíná na stupni 4 (dostatečný)** – tím, že projekt obsahuje všechny části. Dále se hodnocení zlepšuje dle kvality zpracování na základě uvážení vyučujícího.

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti**
- Projekt musí jít **spustit na školních PC v učebně VT6**
- SQL skripty přiloženy v repozitáři či kódu
- ER diagram přiložen v repozitáři či webu
- Testy musí jít spustit
- **Deadline: 14 dní před praktickou maturitní zkouškou**
