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

### 6. Vypnutí Credential Manageru (žádné vyskakovací okno při sync)

Portable Git ve škole používá **Git Credential Manager**, který při každém sync vyskočí s přihlašovacím oknem. Aby se credentials uložily natrvalo a okno už nevyskočilo, zadej v **Git Bash Portable**:

```bash
git config --global credential.helper store
```

Při **prvním** git sync/push se tě ještě zeptá na přihlášení – zadej:
- **Username:** tvůj GitHub username
- **Password:** tvůj **Personal Access Token** (ne heslo k účtu!)

Od té chvíle se credentials uloží a okno se už **nikdy nezobrazí**.

#### Jak vytvořit Personal Access Token (PAT)

1. Na GitHubu jdi do **Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Klikni **Generate new token (classic)**
3. Zaškrtni oprávnění **repo** (celý blok)
4. Vygeneruj token a **ihned si ho zkopíruj** (zobrazí se jen jednou)
5. Tento token použij místo hesla při prvním přihlášení

> ⚠️ Token se uloží jako plain text v souboru `~/.git-credentials`. Ve školním prostředí to je přijatelné řešení.

---

### Shrnutí pořadí kroků
 
| # | Co udělat | Kde |
|---|-----------|-----|
| 1 | Vytvořit venv | PowerShell terminál |
| 2 | Povolit spouštění skriptů | PowerShell terminál |
| 3 | Aktivovat venv | PowerShell terminál |
| 4 | Nastavit `settings.json` | VS Code – User Settings (JSON) |
| 5 | Nastavit Git identitu | Git Bash Portable terminál |
| 6 | Vypnout Credential Manager | Git Bash Portable terminál |
