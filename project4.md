# Projekt 4 – Samostatný projekt (4. ročník / maturitní)

## Cíl projektu

Samostatně vytvořit kompletní projekt, který obsahuje **všechny části** zpracovávané ve skupinách během předchozích 3 let: **webovou prezentaci, hru a databázi** – vše vzájemně propojené. Tento projekt je **podmínkou pro přistoupení k praktické maturitní zkoušce**.

---

## Organizace práce

### Práce je **individuální**
- Každý žák pracuje **sám**
- Žák založí **vlastní gitové úložiště** a přidá učitele jako spolupracovníka
- **Doporučení:** veřejný repozitář ušetří starosti s přístupy

### Volba jazyka
- Projekt **může být v jiném jazyce než Python**, ale:
  - Na **začátku školního roku** je nutné ověřit, že projekt **půjde spustit v učebně VT6**
  - Pokud potřebujete nainstalovat freeware software, **zažádejte nejpozději do konce října**
  - Pokud se projekt nepodaří spustit na školních PC, je nutné **změnit prostředí/jazyk**

---

## Kontrolní termíny

| # | Období | Co by mělo být hotové |
|---|--------|-----------------------|
| 1 | **Začátek listopadu** | Výběr tématu, funkční menu, návrh rozložení projektu (datové toky – co-kde-kam-odkud), návrh databáze, ER diagram |
| 2 | **Konec ledna** | Základní pohyb a logika hry, práce s databází, komunikace DB s webovou stránkou a hrou |
| 3 | **Konec března** | Dodělávání detailů a oprava chyb, vylepšení na základě zpětné vazby vyučujících |
| 4 | **14 dní před praktickou maturitní zkouškou** | **Finální odevzdání** – kompletní, funkční projekt |

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

### 2. fáze (listopad – konec ledna)

| Oblast | Co dělat |
|--------|-----------|
| **Hra** | **Základní pohyb a logika** – postava se pohybuje, reaguje na vstupy, herní smyčka funguje |
| **Databáze** | Vložit vzorová data (INSERT), napsat SELECT dotazy (JOIN, WHERE, ORDER BY) |
| **Propojení** | Hra ukládá skóre do DB, web čte data z DB |
| **Web** | Implementovat **login + registraci**, zobrazit herní výsledky z databáze |
| **Dokumentace** | Komentovat kód průběžně, začít uživatelský manuál |

### 3. fáze (leden – konec března)

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

### 2. Hra
- **Herní smyčka** (update + render)
- **Grafické rozhraní** – menu, start, ukončení hry
- **Interakce hráče** s hrou (klávesnice/myš)
- **Ukládání výsledků** do databáze (jméno | skóre)
- Hra se na začátku nebo na konci **zeptá, kdo hrál**
- Hra je **funkční, stabilní a smysluplná** – nesmí padat

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
- Všechny tři části (web + hra + DB) musí **spolu komunikovat**
- Web zobrazuje data z databáze
- Hra ukládá data do databáze

### 5. Automatizované testy (NAVÍC oproti skupinovému projektu)
- Minimálně **2 automatizované testy**
- Testy musí být zaměřeny na **důležité funkce projektu**
- Testy musí jít spustit a musí procházet

### 6. Dokumentace
- Z historie Gitu musí být patrné, **co kdy bylo nahráno**
- Kód obsahuje **komentáře** popisující jednotlivé bloky
- **Všechny třídy a funkce/metody** musí mít popisný komentář
- Uživatelský manuál (jak hru spustit, jak hrát)
- Vývojové diagramy klíčových herních mechanik

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce** (případně jiný jazyk po dohodě s učitelem – viz sekce Volba jazyka).

### ✅ Povoleno
- **Python 3** + **Pygame** (hra) – nebo jiný jazyk po dohodě s učitelem
- **HTML 5** + **CSS 3** (webová prezentace)
- **SQL** (MySQL / MariaDB / SQLite – dle toho, co se probírá ve výuce)
- **PHP** nebo jiný serverový jazyk probíraný ve výuce
- **Git** (GitHub / GitLab)
- Standardní knihovny zvoleného jazyka
- Grafické editory pro tvorbu spritů
- Testovací frameworky probírané ve výuce (pytest, unittest apod.)

### ❌ Zakázáno
- Herní enginy (Unity, Unreal, Godot apod.) – pokud nebyly dohodnuty s učitelem
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
- **Kompletnost** – projekt obsahuje VŠECHNY části (web, hru, databázi a jejich propojení)
- **Funkčnost** – vše běží, nic nepadá
- **Kvalita kódu** – čitelnost, struktura, komentáře
- **Kvalita SQL** – normalizace, správné použití dotazů
- **Testy** – automatizované testy existují a procházejí
- **Dokumentace** – komentáře, manuál, diagramy
- **Práce s Gitem** – pravidelné commity, smysluplné zprávy
- **Komunikace s učitelem** – reakce na zpětnou vazbu
- **Celkový dojem** – smysluplnost, přehlednost, úroveň zpracování

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
- Učitel musí mít přístup k repozitáři
- Projekt musí jít **spustit na školních PC v učebně VT6**
- SQL skripty přiloženy v repozitáři
- ER diagram přiložen v repozitáři
- Testy musí jít spustit
- **Deadline: 14 dní před praktickou maturitní zkouškou**
