# Projekt 4 – Samostatný projekt (4. ročník / maturitní)

Samostatně vytvořit kompletní projekt propojující **web, hru/aplikaci a databázi**. Projekt je **podmínkou pro přistoupení k praktické maturitní zkoušce**.

---

## Organizace práce

- Práce je **individuální** – každý žák pracuje sám
- Žák se přidá ke **gitovému úložišti** vytvořenému učitelem
- AI lze použít **pouze** pro inspiraci, generování textů, komentování a pomoc s dílčími problémy – **ne pro generování celých bloků kódu**
- Projekt musí být v technologiích probíraných ve výuce; Godot (GDScript) možný po dohodě s učitelem

---

## Kontrolní termíny

| # | Kdy | Co musí být hotové |
|---|-----|--------------------|
| 1 | Začátek listopadu | Téma, funkční menu, návrh datových toků, ER diagram |
| 2 | Začátek ledna | Základní logika hry/aplikace, DB s daty, propojení DB↔web↔hra |
| 3 | Konec února | Oprava chyb, testy, dokončení dokumentace |
| 4 | 14 dní před maturitou | **Finální odevzdání** + prezentace ve třídě + peer review |

> Termíny 3 a 4 se mohou krýt → žák může dostat **3 známky místo 4**.

---

## Funkční požadavky

Projekt musí obsahovat **VŠECHNY** následující části:

### 1. Web (min. 4 HTML stránky + 1 CSS)
- Navigační lišta, informace o projektu, vývojové diagramy
- **Login a registrace** uživatele
- **Zobrazení dat z databáze** (výsledky, záznamy)

### 2. Hra / Desktopová aplikace
- Hlavní smyčka (event loop / update + render), menu, spuštění, ukončení
- Interakce uživatele (klávesnice/myš, formuláře, tlačítka)
- Identifikace uživatele (jméno hráče / přihlášení)
- Ukládání dat do DB (skóre / CRUD operace)
- Projekt **nesmí padat**

> 💡 **Příklad alternativy – Skladovací systém (PyQt6):**
>
> | Herní požadavek | Ekvivalent v aplikaci |
> |---|---|
> | Herní smyčka | Qt event loop |
> | Menu + ukončení | Hlavní okno s navigací |
> | Interakce hráče | Formuláře, tabulky, filtry |
> | Ukládání skóre | CRUD operace v DB |
> | Kdo hrál | Přihlášení / výběr uživatele |


### 3. Databáze

| Požadavek | Detail |
|-----------|--------|
| ER diagram | Zakreslen a přiložen |
| Vztahy | 1:N i M:N (JOIN při čtení) |
| DDL | CREATE TABLE: datový typ, UNIQUE, NOT NULL, AUTO_INCREMENT, PK, FK, DEFAULT |
| DML | INSERT – min. 3 záznamy do každé tabulky |
| SELECT | JOIN, WHERE, ORDER BY, GROUP BY, LIKE |
| Úprava dat | UPDATE a DELETE |
| Normalizace | Min. BCNF |
| Komunikace | Web (PHP/Flask/JS) i hra (Python) čtou/zapisují do DB |

### 4. Propojení
- Minimálně 2 ze 3 částí spolu komunikují (DB↔hra, DB↔web, web↔hra)

### 5. Automatizované testy
- Min. **2 testy** na důležité funkce, musí jít spustit a procházet

### 6. Dokumentace

**Kód:**
- Komentáře u všech bloků, tříd a funkcí/metod
- Min. **5 commitů na fázi** s popisnými zprávami (`feat:`, `fix:`, `docs:`, `update:`)
- 3× vývojový diagram klíčové mechaniky

**Povinné soubory** (každý jako samostatný soubor – `.md`, `.pdf`, `.docx`, `.pptx` nebo HTML stránka):

| Soubor | Obsah |
|--------|-------|
| `dokumentace.*` | Účel, technologie, struktura projektu, spuštění, závislosti, omezení |
| `manual.*` | Postup spuštění, popis UI, příklady použití, chybové stavy |
| `prezentace.*` | Problém, řešení, cílová skupina, přínos, ukázka, možnosti rozvoje |
| `prehled.*` | Struktura kódu, datové toky, technologie, jak začít s vývojem, rizika |

---

## Povolené technologie

✅ Python 3 + Pygame · HTML5 + CSS3 · SQL (MySQL/MariaDB/SQLite) · PHP / JS / Flask · Git · pytest/unittest · Grafické editory

❌ Herní enginy (Unity, Unreal) · React/Vue/Angular/Django · Bootstrap/Tailwind · ORM · MongoDB · AI generátory kódu pro celé bloky · cizí kód bez pochopení

---

## Hodnocení

### Známky
- Až **4 známky** (1 za každý kontrolní termín); při sloučení termínů 3+4 → **3 známky**
- Kompletní projekt v posledním termínu **začíná na stupni 4** a zlepšuje se dle kvality

### Co se hodnotí

| Kritérium | Váha |
|-----------|:----:|
| Kompletnost (obsahuje všechny části) | 3 |
| Funkčnost (běží, nepadá) | 3 |
| Kvalita kódu (čitelnost, komentáře, struktura) | 2 |
| Kvalita SQL (normalizace, dotazy, DDL/DML) | 2 |
| Dokumentace (4 soubory, diagramy, komentáře v kódu) | 2 |
| Celkový dojem (smysluplnost, přehlednost) | 2 |
| Testy (existují, procházejí) | 1 |
| Práce s Gitem (pravidelné commity, zprávy) | 1 |
| Komunikace s učitelem (reakce na zpětnou vazbu) | 1 |

### Peer review

Žáci si navzájem kontrolují projekty a hledají chyby.

- **Chyby ve VAŠEM projektu:** za každých 5 chyb → **známka 5** (váha 1)
- **Chyby v CIZÍM projektu:** za každé 2 nalezené chyby → **známka 1** (váha 1)

Chyby se zapisují do **Issues.txt** v gitovém úložišti kontrolovaného projektu. Commit s chybou musí být odeslán do konce hodiny – kdo první, má přednost.

```
# Issues.txt – příklad
1. Hra padá po 30 sekundách – nekontrolovaná výjimka v herní smyčce (Koudelka)
2. Registrace neumožňuje heslo delší než 8 znaků (Novák)
```
```
git commit -m "Issue: hra padá po 30 sekundách – nekontrolovaná výjimka"
```

### Podmínka pro maturitu
> Bez odevzdaného projektu žák **nemůže přistoupit k praktické maturitní zkoušce v řádném termínu**.

---

## Odevzdání

- Veškerá práce v **gitovém repozitáři**
- Projekt spustitelný **na školních PC ve VT6**
- SQL skripty, ER diagram a testy přiloženy v repozitáři
- **Deadline: 14 dní před praktickou maturitní zkouškou**
