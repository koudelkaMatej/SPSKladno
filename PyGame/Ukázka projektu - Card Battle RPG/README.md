# Card Battler

## Stručný cíl projektu
**Card Battler** je singleplayer karetní RPG hra proti počítači.  
Cílem je porážet nepřátele pomocí karet s různými efekty, správně pracovat s manou a využívat kombinace karet.

## Autor / tým
- Autor: *Doplň jméno*
- Třída: *Doplň třídu*  
*(Pokud je tým: doplň seznam členů a role.)*

## Použité technologie
- **Jazyk:** Python 3
- **Knihovna:** Pygame
- **Nástroje:** Git, VS Code

## Herní princip
- Hráč bojuje v tahových soubojích proti AI.
- Každá karta má:
  - cenu many,
  - efekt (útok, obrana, buff/debuff, speciální akce),
  - možnost kombinací s jinými kartami.
- Za poražené nepřátele hráč získává **EXP**.
- Po levelování získává nové karty.
- Každý 5. level je dostupný **obchod** pro vylepšení balíčku.

## Požadavky pro spuštění
- Python **3.10+**
- Nainstalovaný balíček `pygame`
- OS: Windows / Linux / macOS

## Instalace a spuštění

1. Klonování repozitáře:
   ```bash
   git clone <URL_REPO>
   cd "<složka_projektu>"
   ```

2. (Doporučeno) vytvoření virtuálního prostředí:
   ```bash
   python -m venv .venv
   ```

3. Aktivace virtuálního prostředí:
   - Windows (PowerShell):
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

4. Instalace závislostí:
   ```bash
   pip install pygame
   ```

5. Spuštění hry:
   ```bash
   python main.py
   ```

## Ovládání
- Myš: výběr a zahrání karty
- Klávesnice: dle implementace menu/souboje (doplň konkrétní klávesy)

## Ukázky / screenshoty
- Přidej screenshoty do složky `screenshots/`
- Vlož je sem, např.:
  - ![Souboj](screenshots/battle.png)
  - ![Deck builder](screenshots/deckbuilder.png)
  - ![Obchod](screenshots/shop.png)

## Známá omezení
- Vyvážení některých karet ještě není finální.
- AI nepřítele používá základní rozhodování.
- Obsah obchodu je zatím omezený.
- Ukládání postupu je ve vývoji / základní verze.

## Plán rozvoje
- Lepší AI (pokročilé taktiky).
- Více typů karet a synergických balíčků.
- Bossové a speciální eventy.
- Rozšířený obchod a relic systém.
- Trvalé ukládání kampaně.