# Projekt 2 – Tvorba hry v Pythonu (2. ročník)

## Cíl projektu

Naprogramovat hru v Pythonu na základě návrhu z prvního ročníku. Hra bude mít grafické rozhraní, herní smyčku a základní herní mechaniky.

---

## Organizace práce

### Skupiny
- **Stejné skupiny jako v 1. ročníku** (3–4 členové)
- Práce pokračuje ve **stejném gitovém úložišti**

---

## Role ve skupině

Každý člen během roku vystřídá **3–4 role**. Za každý kontrolní termín **1 známka** – hodnocení je individuální dle aktuální role.

### 1. Vedoucí projektu
- Na začátku každé fáze vytvoří **TODO list** (seznam úkolů), jednotlivé úkoly přiřadí členům týmu a sleduje jejich plnění
- Řídí práci týmu a hlídá termíny
- Komunikuje s učitelem (zastupuje tým)
- **Prezentuje práci** při kontrolním termínu
- Pomáhá členům týmu – částečně zodpovídá za odevzdání práce ostatních
- Kontroluje, zda jsou v projektu chyby

### 2. Dokumentátor
- **Komentuje části kódu** (docstringy, inline komentáře)
- Tvoří **seznam implementovaných funkcí** hry (co už hra umí)
- Připravuje **uživatelský manuál** (z pohledu hráče – co vidí, jak se ovládá)

### 3. Vývojář (Programátor)
- Implementuje logiku hry v Pythonu
- Pracuje dle vývojových diagramů z 1. ročníku i nově nabytých znalostí
- Píše čistý, čitelný kód s rozumnou strukturou

### 4. Grafik / UI designer
- Připravuje grafiku: **sprity, tlačítka, GUI, layout**
- Navrhuje vizuální podobu herního rozhraní

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **Vývojář a Grafik se sloučí** do jedné.

---

## Kontrolní termíny

| # | Období | Co by mělo být hotové |
|---|--------|-----------------------|
| 1 | Začátek února | Základní struktura projektu, první pokusy o herní smyčku. Grafik zatím tvoří v Malování či jiném programu postavy, navrhuje hlavní menu.|
| 2 | Polovina března | Funkční menu, základní grafické prvky. Grafik stále může tvořit mimo Python. |
| 3 | Konec dubna | Propojení grafiky s kódem, základní herní mechaniky fungují. |
| 4 | Začátek června | **Více méně funkční menu hry**, připravené části kódu pro pohyb, interakce a další mechaniky. |

Při každém kontrolním termínu může učitel **změnit požadavky** (simulace reálného vývoje).

---

## Doporučený postup práce

Níže je příklad rozdělení práce pro skupinu **4 členů** (A, B, C, D). Při 3 členech se role Vývojář a Grafik sloučí.

### 1. kontrolní termín (začátek února)

| Člen | Role | Co dělá |
|-------|------|----------|
| **A** | Vedoucí | Naplánuje strukturu projektu (složky, moduly), založí issues, rozdělí úkoly, prezentuje |
| **B** | Vývojář | Začne psát **základní herní smyčku** (hlavní okno Pygame, update + render cyklus) |
| **C** | Grafik | Tvoří první grafiku **v Malování/GIMP** – sprity postav, návrh hlavního menu |
| **D** | Dokumentátor | Připraví strukturu dokumentace, začne psát seznam plánovaných funkcí, komentuje první kód |

### 2. kontrolní termín (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **B** | Vedoucí | Kontroluje funkčnost menu, řídí tým, aktualizuje issues, prezentuje |
| **C** | Vývojář | Implementuje **funkční menu** (start hry, ukončení, navigace), základní interakce |
| **D** | Grafik | Dokončuje grafiku v externím editoru – tlačítka, pozadí, další sprity |
| **A** | Dokumentátor | Komentuje nový kód, aktualizuje seznam funkcí, začíná uživatelský manuál |

### 3. kontrolní termín (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **C** | Vedoucí | Kontroluje propojení grafiky s kódem, řeší bugy, prezentuje |
| **D** | Vývojář | **Propojuje grafiku s herní logikou** – sprity se zobrazují, základní mechaniky fungují |
| **A** | Grafik | Doplňuje chybějící grafické prvky, přímo v Pygame testuje zobrazení |
| **B** | Dokumentátor | Dokončuje komentáře u všech tříd/funkcí, aktualizuje manuál |

### 4. kontrolní termín (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **D** | Vedoucí | Finální kontrola – vše funguje, nechybí závislosti, prezentuje výsledek |
| **A** | Vývojář | Implementuje **ukládání skóre do souboru**, ladí pohyb a interakce |
| **B** | Grafik | Finální leštění grafiky, zajistí konzistenci vizuálu |
| **C** | Dokumentátor | Finální verze dokumentace, kontrola všech komentářů, hotový uživatelský manuál |

> **Tip:** Grafik v prvních 2 fázích tvoří grafiku mimo Python (Malování, GIMP). Od 3. fáze se grafika začíná propojovat s kódem.

---

## Funkční požadavky na hru

### Povinné prvky
- **Herní smyčka** (update + render cyklus)
- **Grafické rozhraní** – hlavní menu, tlačítko pro start hry, ukončení hry
- **Interakce s menu** – ovládání klávesnicí a/nebo myší
- **Jednoduché ukládání dat** – např. skóre do souboru (textový soubor, CSV, JSON)
- **Implementace algoritmů** na základě vývojových diagramů z 1. ročníku

### Dokumentace (povinná součást)
- Z historie Gitu musí být patrné, **kdo co nahrál**
- Kód obsahuje **komentáře** vysvětlující nebo popisující jednotlivé bloky
- Komentáře mohou obsahovat jméno autora dané části
- **Všechny třídy a funkce/metody** musí mít popisný komentář (co dělají, parametry, návratová hodnota)

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **Python 3** (hlavní jazyk hry)
- **Pygame** (pro grafické rozhraní a herní smyčku)
- **Standardní knihovny Pythonu** (os, json, csv, random, math apod.)
- **Git** (GitHub / GitLab) pro správu verzí
- Grafické editory pro tvorbu spritů (Malování, GIMP, Piskel apod.)

### ❌ Zakázáno
- Herní enginy (Unity, Unreal, Godot apod.)
- Jiné programovací jazyky než Python
- Externí Python frameworky mimo Pygame (Arcade, Pyglet, Kivy apod.) – pokud nebyly probírány ve výuce
- AI generátory kódu pro celé bloky
- Kopírování cizího kódu bez pochopení a úpravy

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí programování v Pythonu.**

---

## Hodnocení

### Známky za kontrolní termíny
Každý žák získá **4 známky** (1 za každý kontrolní termín). Hodnotí se:

- **Splnění role** – kvalita práce v aktuální roli
- **Funkčnost kódu** – hra jde spustit, nechybí závislosti
- **Kvalita kódu** – čitelnost, struktura, komentáře
- **Práce s Gitem** – pravidelné commity, smysluplné zprávy
- **Dokumentace** – komentáře, uživatelský manuál
- **Týmová spolupráce** – komunikace, dodržování termínů

### Vzájemné hodnocení skupin (peer review)

Při kontrolních termínech si skupiny navzájem **kontrolují projekty ostatních skupin** a hledají chyby (nefunkční herní mechaniky, chyby v kódu, chybějící komentáře, pády hry apod.).

#### Nalezené chyby ve VAŠEM projektu (trest za špatnou kvalitu)
- Za každých **5 nalezených chyb** ve vašem projektu dostane **celý tým známku 5** (váha 1)
- Motivace: testujte svůj kód důkladně před odevzdáním

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
> 1. Hra padá při spuštění – chybí import pygame (Koudelka)
> 2. Funkce pohyb_hrace() nemá žádný komentář (Novák)
> 3. Menu nejde ovládat klávesnicí, pouze myší (Dvořáková)
> ```
>
> **Formát commit zprávy:**
> ```
> git commit -m "Issue: hra padá při spuštění – chybí import pygame"
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti**
- Hra musí jít **spustit** na školních počítačích
- Z historie commitů musí být patrné, **kdo na čem pracoval**
