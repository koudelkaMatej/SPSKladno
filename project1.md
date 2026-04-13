# Projekt 1 – Webová prezentace projektu (1. ročník)

## Cíl projektu

Vytvořit webovou prezentaci vaší budoucí hry. Stránky budou sloužit jako veřejná tvář projektu po celou dobu jeho existence (1.–3. ročník).

---

## Organizace práce

### Skupiny
- **3–4 členové** (dle počtu žáků ve třídě)
- Skupiny jsou **neměnné po celé 3 roky** (1.–3. ročník)

### Zahájení práce
1. **Učitel** založí skupinu **gitové úložiště** (GitHub) buď: 
    - celé třídě s názvem skupiny např. Skupinový projekt 2025-2027 -> skupiny Snake | Flappy 
    - Jednotlivé skupiny zvlášť např. Skupinový projekt 2025-2027 Snake | Skupinový projekt 25-27 HrdliSeberVetroPech apod.
2. Přidá **žáky** jako spolupracovníka do projektu
3. **Doporučení:** veřejný repozitář vám ušetří práci s přístupy
4. V každé složce s projektem bude soubor Issues.txt, který bude sloužit pro zápis nalezených chyb.

---

## Role ve skupině

Každý člen během roku vystřídá **3–4 role** (dle velikosti skupiny). Za každý kontrolní termín dostane žák **1 známku** – hodnotí se individuálně podle aktuální role.

### 1. Vedoucí projektu
- Na začátku každé fáze vytvoří **TODO list** (seznam úkolů), jednotlivé úkoly přiřadí členům týmu a sleduje jejich plnění
- Řídí práci týmu a hlídá termíny
- Komunikuje s učitelem (zastupuje tým)
- Hlídá práci ve větvých a Merguje změny do hlavní větve před kontrolním termínem
- **Prezentuje práci** při kontrolním termínu
- Pomáhá členům týmu – částečně zodpovídá za odevzdání práce ostatních
- Kontroluje, zda jsou v projektu chyby

### 2. Designér
- Navrhuje grafické rozhraní webových stránek
- Každý designér navrhne **1 stránku**, která musí vizuálně navazovat na ostatní (jednotný vzhled celého webu)
- Návrh může být ve formě wireframe, skicy, nebo mockupu (např. v Malování, Figma, na papíře)

### 3. Copy-writer
- Zodpovídá za **textový obsah** stránek (popisy, pravidla, informace)
- Vytváří **vývojové diagramy** základních herních mechanik

### 4. Vývojář
- Tvoří webovou stránku **na základě designu** od designéra
- Implementuje HTML strukturu a CSS styly

> **Pozn.:** Pokud jsou ve skupině pouze 3 lidé, role **designér a vývojář se sloučí** do jedné.

---

## Kontrolní termíny

| # | Období | Role (cca) | Poznámka |
|---|--------|------------|----------|
| 1 | Začátek února | 1.–2. rotace | Zpětná vazba učitele, případné změny požadavků |
| 2 | Polovina března | 2.–3. rotace | Zpětná vazba učitele, případné změny požadavků |
| 3 | Konec dubna | 3.–4. rotace | Zpětná vazba učitele, případné změny požadavků |
| 4 | Začátek června | Závěrečná | Finální odevzdání |

Při každém kontrolním termínu může učitel (jako „zadavatel") **změnit požadavky** – to simuluje reálné prostředí vývoje.

---
## Doporučený postup práce

Níže je příklad rozdělení práce pro skupinu **4 členů** (A, B, C, D). Při 3 členech se role designér a vývojář sloučí.

### 1. kontrolní termín (začátek února)

| Člen | Role | Co dělá |
|-------|------|----------|
| **A** | Vedoucí | Založí issues pro celou 1. fázi, rozdělí úkoly, nastaví strukturu složek v repozitáři, připraví prezentaci práce |
| **B** | Designér | Navrhne wireframe/mockup **hlavní stránky** (vzhled, rozložení, barevné schéma – určuje směr designu celého webu) |
| **C** | Copy-writer | Napíše texty pro hlavní stránku + vytvoří **1. vývojový diagram** herní mechaniky |
| **D** | Vývojář | Nakóduje **hlavní stránku** v HTML + vytvoří základní CSS soubor dle návrhu designéra |

### 2. kontrolní termín (polovina března) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **B** | Vedoucí | Řídí 2. fázi, aktualizuje issues, kontroluje kvalitu dosavadní práce, prezentuje |
| **C** | Designér | Navrhne wireframe stránky **„O hře“** (naváže na design z 1. fáze) |
| **D** | Copy-writer | Napíše texty pro stránku „O hře“ + vytvoří **2. vývojový diagram** |
| **A** | Vývojář | Nakóduje stránku **„O hře“** v HTML + rozšíří CSS |

### 3. kontrolní termín (konec dubna) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **C** | Vedoucí | Řídí 3. fázi, kontroluje konzistenci webu, prezentuje |
| **D** | Designér | Navrhne wireframe stránky **„Vývojové diagramy“** |
| **A** | Copy-writer | Napíše texty pro stránku s diagramy + vytvoří **3. vývojový diagram** |
| **B** | Vývojář | Nakóduje stránku **„Vývojové diagramy“** + ladí CSS |

### 4. kontrolní termín (začátek června) – rotace rolí

| Člen | Role | Co dělá |
|-------|------|----------|
| **D** | Vedoucí | Finální kontrola celého webu, prezentuje výsledek, řeší poslední issues |
| **A** | Designér | Navrhne wireframe stránky **„O nás“** + zkontroluje jednotnost designu |
| **B** | Copy-writer | Napíše texty pro stránku „O nás“ + vytvoří **4. vývojový diagram** |
| **C** | Vývojář | Nakóduje stránku **„O nás“** + finální úpravy CSS, navigace |

> **Tip:** Každý člen tak během roku vyzkouší všechny role a každý přispěje 1 vývojovým diagramem.

---
## Funkční požadavky na webovou stránku

### Struktura
- **Minimálně 4 HTML soubory** propojené navigační lištou
- **1 společný CSS soubor** pro jednotný design celého webu
- **stránky jsou responzivní a chovají se jinak na mobilu, tabletu a PC (platí až pro kontrolní termín, ve kterém se tato problematika vysvětluje)**

### Povinné stránky

| Stránka | Obsah |
|---------|-------|
| **Hlavní stránka** | Základní informace o hře/projektu, úvod, shrnutí |
| **Vývojové diagramy** | Každý člen vytvoří **1 vývojový diagram** základní herní mechaniky v průběhu 4 rotací (1 období = 1 diagram)|
| **O hře** | Podrobné informace – funkční a technické požadavky, pravidla hry |
| **O nás** | Informace o tvůrcích, kontaktní informace, rozdělení rolí |

---

## Povolené technologie

> **Používejte VÝHRADNĚ technologie probírané ve výuce.**

### ✅ Povoleno
- **HTML 5**
- **CSS 3**
- **Git** (GitHub / GitLab) pro správu verzí
- Grafické editory pro návrhy (Malování, GIMP, Figma – pro wireframy)
- Nástroje pro vývojové diagramy (draw.io, ruční nákres)

### ❌ Zakázáno
- JavaScript a jakékoliv skriptovací jazyky na straně klienta
- CSS frameworky (Bootstrap, Tailwind apod.)
- HTML šablony a generátory stránek
- Jakékoliv backendové technologie (PHP, Node.js apod.)
- AI generátory celých stránek
- Kopírování cizích šablon

> **Porušení tohoto pravidla bude mít vliv na hodnocení. Cílem je prokázat vlastní zvládnutí základů HTML a CSS.**

---

## Hodnocení

### Známky za kontrolní termíny
Každý žák získá **4 známky** (1 za každý kontrolní termín). Hodnotí se:

- **Splnění role** – jak kvalitně žák plnil úkoly své aktuální role
- **Kvalita výstupu** – funkčnost, přehlednost, vizuální úroveň
- **Práce s Gitem** – viditelné commity, smysluplné zprávy
- **Týmová spolupráce** – komunikace, dodržování termínů
- **Prezentace** (vedoucí) – srozumitelnost, připravenost

### Vzájemné hodnocení skupin (peer review)

Při kontrolních termínech si skupiny navzájem **kontrolují projekty ostatních skupin** a hledají chyby (nefunkční odkazy, překlepy, chybějící obsah, rozbitý layout apod.).

#### Nalezené chyby ve VAŠEM projektu (trest za špatnou kvalitu)
- Za každých **5 nalezených chyb** ve vašem projektu dostane **celý tým známku 5** (váha 1)
- Motivace: odevzdávejte kvalitní práci a testujte si projekt před odevzdáním

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
> 1. Stránka "O hře" má špatný kontrast a nejde dobře přečíst (Koudelka)
> 2. Na stránce "O nás" nefunguje odkaz na hlavní stránku (Novák)
> 3. Chybí navigační lišta na stránce "Vývojové diagramy" (Dvořáková)
> ```
>
> **Formát commit zprávy:**
> ```
> git commit -m "Issue: špatný kontrast na stránce O hře"
> ```

---

## Odevzdání

- Veškerá práce musí být v **gitovém úložišti**
- Žáci využívají větve pro práci na projektu jako je např:
    * Development_Snake | Design_Snake | Leader_Snake | CopyWriter_Snake apod.
- Z historie commitů musí být patrné, **kdo na čem pracoval**
