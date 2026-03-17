# SPSKladno

## Nastavení VS Code a GIT ve školním prostředí

Ve škole je Python, Git i VS Code nainstalováno jako **portable verze na serveru**. Aby vše správně fungovalo, je potřeba provést následující kroky.

---

### 1. Vytvoření virtuálního prostředí (venv)

V terminálu VS Code spusť:

```powershell
& "G:/win32app/Portable Python-3.13.3 x64/python.exe" -m venv venv
```

### 2. Povolení spouštění skriptů

Školní politika může blokovat aktivaci venv. Povol spouštění skriptů:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3. Aktivace virtuálního prostředí

```powershell
.\venv\Scripts\activate
```

---

### 4. Nastavení VS Code (settings.json)

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

### 5. Nastavení Git identity

Otevři terminál **Git Bash Portable** (v dolní liště VS Code vyber profil terminálu) a zadej:

```bash
git config --global user.email "tvuj@email.cz"
git config --global user.name "TvujNick"
```

> 🔁 Nahraď `"tvuj@email.cz"` a `"TvujNick"` svými skutečnými údaji (např. z GitHubu).

---

### Shrnutí pořadí kroků

| # | Co udělat | Kde |
|---|-----------|-----|
| 1 | Vytvořit venv | PowerShell terminál |
| 2 | Povolit spouštění skriptů | PowerShell terminál |
| 3 | Aktivovat venv | PowerShell terminál |
| 4 | Nastavit `settings.json` | VS Code – User Settings (JSON) |
| 5 | Nastavit Git identitu | Git Bash Portable terminál |
