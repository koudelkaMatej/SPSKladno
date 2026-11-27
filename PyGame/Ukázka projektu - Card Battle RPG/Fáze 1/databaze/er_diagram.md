# ER diagram

```mermaid
erDiagram
    UZIVATELE ||--|| POSTUP : "staty hráče"
    UZIVATELE ||--o{ SKORE : "historie"
    UZIVATELE ||--o{ HRAC_BALICEK : "balíček"
    UZIVATELE ||--o{ HRAC_SBIRKA : "sbírka"
    UZIVATELE ||--o{ INVENTAR : "inventář"
    UZIVATELE ||--o{ EQUIP : "nasazeno"
    UZIVATELE ||--o{ HRAC_EFEKTY : "efekty"

    KARTY ||--o{ HRAC_BALICEK : ""
    KARTY ||--o{ HRAC_SBIRKA : ""
    KARTY ||--o{ NEPRITEL_BALICEK : ""
    KARTY }o--o| EFEKTY : "aplikuje"
    EFEKTY ||--o{ HRAC_EFEKTY : ""

    PREDMETY ||--o{ INVENTAR : ""
    PREDMETY ||--o{ EQUIP : ""

    NEPRATELE ||--o{ NEPRITEL_BALICEK : "hraje"
    NEPRATELE ||--o{ NEPRITEL_DROP : "dropuje"
    NEPRITEL_DROP }o--o| PREDMETY : ""
    NEPRITEL_DROP }o--o| KARTY : ""

    UZIVATELE {
        int id PK
        text jmeno UK
        text heslo_hash
        text sul
    }
    POSTUP {
        int uzivatel_id PK,FK
        int skore
        int hp
        int max_hp
        int mana
        int rychlost
        int obrana
        int utok
        int level
        int exp
        int zlato
        int max_karet_v_balicku
        int max_karet_v_ruce
        int odpocinek
    }
    SKORE {
        int id PK
        int uzivatel_id FK
        int body
        int uroven
    }
    KARTY {
        int id PK
        text nazev UK
        text kategorie
        int sila "cena v mane"
        text efekt_typ
        int hodnota
        int efekt_id FK
        text popis
        int cena
    }
    EFEKTY {
        int id PK
        text nazev UK
        text typ
        int hodnota
    }
    HRAC_EFEKTY {
        int uzivatel_id PK,FK
        int efekt_id PK,FK
        int zbyva_kol
    }
    HRAC_BALICEK {
        int uzivatel_id PK,FK
        int karta_id PK,FK
        int pocet
    }
    HRAC_SBIRKA {
        int uzivatel_id PK,FK
        int karta_id PK,FK
        int pocet
    }
    PREDMETY {
        int id PK
        text nazev UK
        text slot
        int bonus_hp
        int bonus_mana
        int bonus_rychlost
        int bonus_obrana
        int bonus_utok
        int cena
    }
    INVENTAR {
        int uzivatel_id PK,FK
        int predmet_id PK,FK
        int pocet
    }
    EQUIP {
        int uzivatel_id PK,FK
        text slot PK
        int predmet_id FK
    }
    NEPRATELE {
        int id PK
        text jmeno UK
        int hp
        int rychlost
        int obrana
        int utok
        int level
        int exp
    }
    NEPRITEL_BALICEK {
        int nepritel_id PK,FK
        int karta_id PK,FK
        int pocet
    }
    NEPRITEL_DROP {
        int id PK
        int nepritel_id FK
        text typ "zlato/predmet/karta"
        int mnozstvi
        int predmet_id FK
        int karta_id FK
        int sance
    }
```

## Co je v DB a co jen v paměti hry

| Údaj | Kde | Proč |
|---|---|---|
| Staty hráče (HP, útok, level, zlato…) | DB `postup` | trvalé |
| Sbírka a balíček karet | DB `hrac_sbirka`, `hrac_balicek` | trvalé; balíček = výběr ze sbírky |
| Inventář, equip | DB `inventar`, `equip` | trvalé |
| Efekty na hráči | DB `hrac_efekty` | jen pokud se ukládá hra uprostřed souboje |
| **Ruka, lízací balíček, odhazovací balíček** | **paměť hry** | existují jen během souboje; na jeho začátku se lízací balíček vytvoří z `hrac_balicek` a zamíchá |
| Aktuální mana v souboji | paměť hry | na začátku kola se doplní na hodnotu `postup.mana` |
| Efekty a HP nepřítele v souboji | paměť hry | nepřítel se vytvoří kopií řádku z `nepratele` |

## Poznámky k návrhu

- **Mana** v `postup` je maximum (default 5); aktuální hodnota je jen v souboji. `karty.sila` je cena many.
- **Popis efektu karty** je rozdělen na strojově čitelné `efekt_typ` + `hodnota` (pro logiku hry) a `popis` (text pro hráče).
- **Equip**: každý slot má max. jednu věc. Prsteny mají sloty `prsten_1`, `prsten_2`. Obouruční zbraň vylučuje `zbran` a `stit` (kontroluje hra).
- **Limity** `max_karet_v_balicku` a `max_karet_v_ruce` jsou ve `postup`, aby šly zvyšovat předměty/levelem; součet `hrac_balicek.pocet` hlídá hra.
- **Drop** má `sance` v % a omezení, že řádek odkazuje právě na zlato, předmět, nebo kartu.
- **Bonusy předmětů** se při souboji sčítají ze všech řádků `equip`.
- **Rychlost** může určovat, kdo hraje v kole první.
