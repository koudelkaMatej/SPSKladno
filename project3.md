# Projekt 3 – Uzavření projektu: Databáze a integrace (3. ročník)

## Cíl projektu

Dokončit hru, propojit ji s databází a aktualizovat webovou prezentaci z 1. ročníku. Na konci 3. ročníku musí projekt tvořit **funkční celek** – web, hra a databáze jsou vzájemně propojeny.

---

## Organizace práce

### Skupiny
- **Stejné skupiny jako v 1. a 2. ročníku** (3–4 členové)
- Práce pokračuje ve **stejném gitovém úložišti**

---

## Role ve skupině

Každý člen během roku vystřídá **3–4 role**. Za každý kontrolní termín **1 známka** – hodnocení je individuální dle aktuální role.

### 1. Vedoucí projektu
- Na začátku každé fáze vytvoří **TODO list** (seznam úkolů), jednotlivé úkoly přiřadí členům týmu a sleduje jejich plnění
- Řídí práci týmu a hlídá termíny
- Komunikuje s učitelem (zastupuje tým)
- Zakládá gitové úložiště (pokud ještě neexistuje)
- **Prezentuje práci** při kontrolním termínu
- Pomáhá členům týmu – částečně zodpovídá za odevzdání práce ostatních
- Kontroluje, zda jsou v projektu chyby
- **Tvorba ER diagramu** databáze

### 2. Správce dat
- Vytváří **databázi** pro ukládání herních dat
- Píše příkazy pro **připojení k databázi** z Pythonu
- Rozšiřuje webové stránky z 1. ročníku o:
  - **Login** (přihlášení uživatele)
  - **Registraci** (vytvoření účtu)
  - **Zobrazení výsledků** ze hry na webu (CREATE, SELECT, INSERT)

### 3. Vývojář (Programátor)
- Implementuje zbývající logiku hry v Pythonu
- Propojuje grafiku s klávesnicí/myší a herní logikou
- Zajišťuje plynulý chod hry

### 4. Grafik / UI designer
- Připravuje grafiku: **sprity, tlačítka, GUI, layout, postavy, překážky** apod.
- Finalizuje vizuální podobu hry

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **Správce dat a Vývojář se sloučí** do jedné.

---

## Kontrolní termíny

| # | Období | Co by mělo být hotové |
|---|--------|-----------------------|
| 1 | Začátek února | **Hra už něco dělá** – základní mechaniky fungují, postava se pohybuje |
| 2 | Polovina března | Pokročilé herní mechaniky, práce na databázi |
| 3 | Konec dubna | **Základní verze webu** s napojením na databázi |
| 4 | Začátek června | **Finální verze hry** – funguje, nepadá, je smysluplná |

Při každém kontrolním termínu může učitel **změnit požadavky**.

---

## Doporučený postup práce

Níže je příklad rozdělení práce pro skupinu **4 členů** (A, B, C, D). Při 3 členech se role Správce dat a Vývojář sloučí.

### 1. kontrolní termín (začátek února)

| Člen | Role | Co dělá |
|-------|------|----------|
| **A** | Vedoucí | Vytvoří **ER diagram** databáze, naplánuje integraci všech částí, rozdělí úkoly, prezentuje |
| **B** | Vývojář | Doprogramuje **základní herní mechaniky** – postava se pohybuje, reaguje na vstupy |
| **C** | Grafik | Dokončuje grafiku postav, překážek, prostředí – vše se zobrazuje ve hře |
| **D** | Správce dat | Vytvoří **databázi** (CREATE TABLE), připraví připojení z Pythonu, vloží vzorová data (INSERT) |

### 2. kontrolní termín (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **B** | Vedoucí | Kontroluje propojení hry s DB, řídí tým, aktualizuje ER diagram pokud třeba, prezentuje |
| **C** | Vývojář | Implementuje **pokročilé mechaniky**, propojuje hru s databází (ukládání skóre) |
| **D** | Grafik | Tvoří grafiku pro menu, tlačítka, GUI prvky hry |
| **A** | Správce dat | Píše **SELECT dotazy** (JOIN, WHERE, ORDER BY), začíná pracovat na webu – připojení k DB |

### 3. kontrolní termín (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **C** | Vedoucí | Kontroluje funkčnost webu + DB, řeší integrační problémy, prezentuje |
| **D** | Vývojář | Ladí hru – stabilita, přechody mezi scénami, hra se zeptá na jméno hráče |
| **A** | Grafik | Finální grafické úpravy, konzistentní vizuální styl celé hry |
| **B** | Správce dat | Implementuje **login + registraci** na webu, zobrazuje výsledky ze hry na webových stránkách |

### 4. kontrolní termín (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **D** | Vedoucí | Finální kontrola CELÉHO projektu (web + hra + DB), prezentuje výsledek |
| **A** | Vývojář | Finální opravy bugů, hra je **stabilní a smysluplná** |
| **B** | Grafik | Poslední vizuální úpravy, screenshoty pro web |
| **C** | Správce dat | Dokončuje SQL skripty (UPDATE, DELETE), ověřuje **normalizaci (BCNF)**, finální propojení |

> **Tip:** Od 1. fáze se pracuje na databázi paralelně s hrou. Od 3. fáze se vše začíná propojovat.

---

## Funkční požadavky

### Hra
- **Herní smyčka** (update + render)
- **Grafické rozhraní** – menu, start hry, ukončení hry
- **Interakce hráče s hrou** – klávesnice a/nebo myš
- **Ukládání dat do databáze** (např. skóre)
- **Propojení všech částí projektu** (web + hra + DB)
- Možnost ukládat výsledek jako **jméno | skóre** (hra se zeptá, kdo hrál)
- Hra musí být **funkční, stabilní a smysluplná**

### Webová stránka
- Aktualizovaná prezentace z 1. ročníku
- Slouží jako **prezentační nástroj** – ukazuje ukázky ze hry a vysvětluje ji
- Obsahuje **login, registraci a zobrazení herních výsledků**
- Komunikuje s databází přes webové rozhraní

### Databáze

| Požadavek | Detail |
|-----------|--------|
| **ER diagram** | Zakreslen a přiložen k projektu |
| **Vztahy** | Využívá 1:N i M:N (tedy i JOIN při čtení dat) |
| **DDL skripty** | CREATE TABLE s atributy: datový typ, UNIQUE, NOT NULL, AUTO_INCREMENT, PK, FK, DEFAULT |
| **DML skripty** | INSERT – min. 3 vzorové záznamy do každé tabulky |
| **SELECT dotazy** | Včetně JOIN, filtrování (WHERE), řazení (ORDER BY), seskupování (GROUP BY), vyhledávání (LIKE) |
| **Úprava dat** | UPDATE a DELETE příkazy |
| **Normalizace** | Minimálně po **Boyceho-Coddovu normální formu (BCNF)** |
| **Komunikace** | S databází se komunikuje přes webové rozhraní (webové stránky), i přes Python (hra) |

### Dokumentace
- Z historie Gitu musí být patrné, **kdo co nahrál**
- Kód obsahuje **komentáře** vysvětlující jednotlivé bloky
- **Všechny třídy a funkce/metody** musí mít popisný komentář

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **Python 3** + **Pygame** (hra)
- **HTML 5** + **CSS 3** (webová prezentace)
- **SQL** (MySQL / MariaDB / SQLite – dle toho, co se probírá ve výuce)
- **PHP** nebo jiný serverový jazyk probíraný ve výuce (pro propojení webu s DB)
- **Git** (GitHub / GitLab)
- Standardní knihovny Pythonu
- Grafické editory pro tvorbu spritů

### ❌ Zakázáno
- Herní enginy (Unity, Unreal, Godot apod.)
- Jiné programovací jazyky než Python pro herní logiku
- Webové frameworky (React, Vue, Angular, Django, Flask apod.) – pokud nebyly probírány ve výuce
- CSS frameworky (Bootstrap, Tailwind apod.)
- ORM knihovny – SQL dotazy pište ručně
- NoSQL databáze (MongoDB apod.)
- AI generátory kódu pro celé bloky
- Kopírování cizího kódu bez pochopení a úpravy

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí všech technologií.**

---

## Hodnocení

### Známky za kontrolní termíny
Každý žák získá **4 známky** (1 za každý kontrolní termín). Hodnotí se:

- **Splnění role** – kvalita práce v aktuální roli
- **Funkčnost** – hra běží, web funguje, databáze odpovídá
- **Propojení** – všechny části projektu spolu komunikují
- **Kvalita kódu a SQL** – čitelnost, struktura, komentáře, normalizace
- **Práce s Gitem** – pravidelné commity, smysluplné zprávy
- **Týmová spolupráce** – komunikace, dodržování termínů

### Vzájemné hodnocení skupin (peer review)

Při kontrolních termínech si skupiny navzájem **kontrolují projekty ostatních skupin** a hledají chyby (nefunkční prvky hry, SQL chyby, rozbitý web, chybějící dokumentace, bezpečnostní problémy apod.).

#### Nalezené chyby ve VAŠEM projektu (trest za špatnou kvalitu)
- Za každých **5 nalezených chyb** ve vašem projektu dostane **celý tým známku 5** (váha 1)
- Motivace: testujte všechny části projektu důkladně před odevzdáním

#### Nalezení chyb v CIZÍM projektu (odměna za pečlivost)
- Za každé **2 nalezené chyby** v projektu jiné skupiny dostane **jednotlivec, který chybu našel, známku 1** (váha 1)
- Motivace: pečlivě kontrolujte práci ostatních – pomáháte jim i sobě

> **Pravidla peer review:**
> - Chyba musí být **reálná a ověřitelná** (učitel rozhoduje sporné případy)
> - Duplicitní hlášení stejné chyby se nepočítá
> - Chyby se zapisují do souboru **Issues.txt** v gitovém úložišti kontrolované skupiny
> - **Commit** s nalezenou chybou musí být odeslán **do konce hodiny** po odprezentování ve třídě
> - Kdo pošle commit jako **první**, má přednost v případě nalezení stejné chyby
>
> **Formát zápisu do Issues.txt:**
> ```
> 1. SQL dotaz na stránce výsledků vrací chybu – špatný JOIN (Koudelka)
> 2. Login neověřuje heslo, pustí kohokoli (Novák)
> 3. Hra neukládá skóre do databáze po skončení hry (Dvořáková)
> ```
>
> **Formát commit zprávy:**
> ```
> git commit -m "Issue: SQL dotaz na stránce výsledků vrací chybu"
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti**
- Učitel musí mít přístup k repozitáři
- Hra musí jít **spustit** na školních počítačích
- Webová stránka musí být **funkční** (včetně napojení na DB)
- SQL skripty musí být přiloženy v repozitáři (CREATE, INSERT, SELECT, UPDATE, DELETE)
- ER diagram musí být přiložen v repozitáři
- Z historie commitů musí být patrné, **kdo na čem pracoval**
