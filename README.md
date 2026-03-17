# SPSKladno

## Nastavení VS Code a GIT ve školním prostředí

Ve škole je Python, Git i VS Code nainstalováno jako **portable verze na serveru**. Aby vše správně fungovalo, je potřeba provést následující kroky.

---

### 1. Vytvoření a otevření složky projektu

Nejdřív si vytvoř složku pro svůj projekt (např. na ploše nebo na disku) a otevři ji ve VS Code:

1. **File → Open Folder…** (`Ctrl + K, Ctrl + O`)
2. Vyber nebo vytvoř novou složku pro svůj projekt
3. Potvrď otevření složky

> 💡 Vždy pracuj v otevřené složce – VS Code tak správně rozpozná projekt, Git i virtuální prostředí.

---

### 2. Vytvoření virtuálního prostředí (venv)

V terminálu VS Code spusť:

```powershell
& "G:/win32app/Portable Python-3.13.3 x64/python.exe" -m venv venv
```

### 3. Povolení spouštění skriptů

Školní politika může blokovat aktivaci venv. Povol spouštění skriptů:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 4. Aktivace virtuálního prostředí

```powershell
.\venv\Scripts\activate
```

---

### 5. Nastavení VS Code (settings.json)

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

---

### 6. Nastavení Git identity

Otevři terminál **Git Bash Portable** (v dolní liště VS Code vyber profil terminálu) a zadej:

```bash
git config --global user.email "tvuj@email.cz"
git config --global user.name "TvujNick"
git config --global credential.helper store
```

> 🔁 Nahraď `"tvuj@email.cz"` a `"TvujNick"` svými skutečnými údaji (např. z GitHubu).

---

### 7. Instalace rozšíření (Extensions)

VS Code potřebuje rozšíření pro práci s Pythonem a Jupyter notebooky. V levém panelu klikni na ikonu **Extensions** (`Ctrl + Shift + X`) a nainstaluj:

- **Python** (`ms-python.python`) – podpora pro Python (IntelliSense, linting, debugging)
- **Jupyter** (`ms-toolsai.jupyter`) – podpora pro Jupyter notebooky (.ipynb)

> 💡 Stačí do vyhledávání zadat „Python" nebo „Jupyter" a nainstalovat rozšíření od **Microsoftu**.

---

### 8. Naklonování Git repozitáře

V terminálu (PowerShell nebo Git Bash) se přesuň do své složky projektu a naklonuj repozitář:

```Git Bash Portable
git clone https://github.com/uzivatel/nazev-repozitare.git .
```

> ⚠️ Tečka `.` na konci znamená, že se obsah naklonuje **přímo do aktuální složky** (nevytvoří se podsložka).

Případně můžeš klonovat přes VS Code:
1. Otevři příkazovou paletu (`Ctrl + Shift + P`)
2. Zadej **"Git: Clone"**
3. Vlož URL repozitáře a vyber cílovou složku

> 🔁 Nahraď `https://github.com/uzivatel/nazev-repozitare.git` skutečnou URL svého repozitáře z GitHubu.

---

### Shrnutí pořadí kroků
 
| # | Co udělat | Kde |
|---|-----------|-----|
| 1 | Vytvořit a otevřít složku projektu | VS Code – File → Open Folder |
| 2 | Vytvořit venv | PowerShell terminál |
| 3 | Povolit spouštění skriptů | PowerShell terminál |
| 4 | Aktivovat venv | PowerShell terminál |
| 5 | Nastavit `settings.json` | VS Code – User Settings (JSON) |
| 6 | Nastavit Git identitu | Git Bash Portable terminál |
| 7 | Nainstalovat rozšíření Python + Jupyter | VS Code – Extensions |
| 8 | Naklonovat Git repozitář | Terminál nebo VS Code – Git: Clone |
