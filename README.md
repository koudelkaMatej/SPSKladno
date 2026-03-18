# SPSKladno

## Nastavení VS Code a GIT ve školním prostředí

Ve škole je Python, Git i VS Code nainstalováno jako **portable verze na serveru**. Aby vše správně fungovalo, je potřeba provést následující kroky.

Návod je rozdělen na dvě části:
- **Část A** – jednorázové nastavení (stačí udělat jednou na školním PC)
- **Část B** – kroky pro každý nový projekt (i po restartu PC)

---

## Část A – Jednorázové nastavení (udělej jen poprvé)

### 1. Nastavení VS Code (settings.json)

Otevři příkazovou paletu (`Ctrl + Shift + P`) → zadej **"Open User Settings (JSON)"** a vlož následující konfiguraci:

```json
{
  "terminal.integrated.profiles.windows": {
    "Git Bash Portable": {
      "path": "G:/win32app/git_portable/bin/bash.exe",
      "args": ["--login", "-i"]
    }
  },
  "git.path": "G:/win32app/git_portable/cmd/git.exe",
  "git.enabled": true,
  "files.autoSave": "afterDelay",
  "git.enableSmartCommit": true,
  "git.autofetch": "all"
}
```

> ⚠️ Pokud už v souboru nějaké nastavení máš, přidej pouze jednotlivé položky – neduplikuj vnější složené závorky `{}`.

### 2. Nastavení Git identity

Otevři terminál **Git Bash Portable** (v dolní liště VS Code vyber profil terminálu - vedle pluska malý zobáček dolů) a zadej:

```bash
git config --global user.email "tvuj@email.cz"
git config --global user.name "TvujNick"
git config --global credential.helper store
```

> 🔁 Nahraď `"tvuj@email.cz"` a `"TvujNick"` svými skutečnými údaji (např. z GitHubu).

### 3. Instalace rozšíření (Extensions)

VS Code potřebuje rozšíření pro práci s Pythonem a Jupyter notebooky. V levém panelu klikni na ikonu **Extensions** (`Ctrl + Shift + X`) a nainstaluj:

- **Python** (`ms-python.python`) – podpora pro Python (IntelliSense, linting, debugging)
- **Jupyter** (`ms-toolsai.jupyter`) – podpora pro Jupyter notebooky (.ipynb)

> 💡 Stačí do vyhledávání zadat „Python" nebo „Jupyter" a nainstalovat rozšíření od **Microsoftu**.

---

## Část B – Pro každý nový projekt (nebo po restartu PC)

### 4. Vytvoření a otevření složky projektu

Nejdřív si vytvoř složku pro svůj projekt (např. na ploše nebo na disku) a otevři ji ve VS Code:

1. **File → Open Folder…** (`Ctrl + K, Ctrl + O`)
2. Vyber nebo vytvoř novou složku pro svůj projekt
3. Potvrď otevření složky

> 💡 Vždy pracuj v otevřené složce – VS Code tak správně rozpozná projekt, Git i virtuální prostředí.

### 5. Naklonování Git repozitáře

V terminálu (PowerShell nebo Git Bash Portable) se přesuň do své složky projektu a naklonuj repozitář:

```bash
git clone https://github.com/uzivatel/nazev-repozitare.git 
```
Nebo 
```bash
git clone https://github.com/uzivatel/nazev-repozitare.git .
```

> ⚠️ Tečka `.` na konci znamená, že se obsah naklonuje **přímo do aktuální složky** (nevytvoří se podsložka).

Případně můžeš klonovat přes VS Code:
1. Otevři příkazovou paletu (`Ctrl + Shift + P`)
2. Zadej **"Git: Clone"**
3. Vlož URL repozitáře a vyber cílovou složku

> 🔁 Nahraď `https://github.com/uzivatel/nazev-repozitare.git` skutečnou URL svého repozitáře z GitHubu.

### 6. Povolení spouštění skriptů

Školní politika resetuje toto nastavení po každém restartu PC. **Musíš to spustit pokaždé znovu, pokud budeš chtít upravovat venv:**

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 7. Vytvoření virtuálního prostředí (venv)

V terminálu VS Code spusť:

```powershell
& "G:/win32app/Portable Python-3.13.3 x64/python.exe" -m venv venv
```

### 8. Aktivace virtuálního prostředí

```powershell
.\venv\Scripts\activate
```

### 9. Instalace balíčků (pip install)

Po aktivaci virtuálního prostředí můžeš instalovat Python balíčky pomocí `pip`:

```powershell
pip install "nazev-balicku"
```

Příklady:

```powershell
pip install flask
pip install pandas matplotlib
pip install pygame
```

Pokud projekt obsahuje soubor `requirements.txt` (např. po naklonování z GitHubu), nainstaluj všechny balíčky najednou:

```powershell
pip install -r requirements.txt
```

---

### 10. Uložení závislostí (pip freeze)

Příkaz `pip freeze` vypíše **všechny nainstalované balíčky** ve tvém virtuálním prostředí i s jejich verzemi:

```powershell
pip freeze
```

Výstup vypadá například takto:

```
flask==3.1.0
Jinja2==3.1.6
pandas==2.2.3
```

#### Uložení do souboru requirements.txt

Aby si spolužáci nebo učitel mohli tvůj projekt spustit, ulož seznam balíčků do souboru:

```powershell
pip freeze > requirements.txt
```

Tento soubor pak **commitni do Gitu** spolu s projektem. Kdokoliv si pak nainstaluje stejné balíčky příkazem:

```powershell
pip install -r requirements.txt
```

> 💡 **Doporučení:** Vždy po instalaci nového balíčku aktualizuj `requirements.txt` příkazem `pip freeze > requirements.txt`.

---

### Shrnutí pořadí kroků

#### Část A – Jednorázové nastavení

| # | Co udělat | Kde |
|---|-----------|-----|
| 1 | Nastavit `settings.json` | VS Code – User Settings (JSON) |
| 2 | Nastavit Git identitu | Git Bash Portable terminál |
| 3 | Nainstalovat rozšíření Python + Jupyter | VS Code – Extensions |

#### Část B – Pro každý nový projekt (i po restartu PC)

| # | Co udělat | Kde |
|---|-----------|-----|
| 4 | Vytvořit a otevřít složku projektu | VS Code – File → Open Folder |
| 5 | Naklonovat Git repozitář | Terminál nebo VS Code – Git: Clone |
| 6 | Povolit spouštění skriptů | PowerShell terminál |
| 7 | Vytvořit venv | PowerShell terminál |
| 8 | Aktivovat venv | PowerShell terminál |
| 9 | Nainstalovat balíčky (`pip install`) | PowerShell terminál (s aktivním venv) |
| 10 | Uložit závislosti (`pip freeze`) | PowerShell terminál (s aktivním venv) |
