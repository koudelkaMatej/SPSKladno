-- Card Battle RPG - databáze (návrh herních dat)
-- Za běhu souboje se v paměti drží: ruka, lízací balíček, odhazovací balíček,
-- aktuální mana a efekty nepřátel. Do DB se ukládá jen trvalý stav.

PRAGMA foreign_keys = ON;

-- ============================================================
-- UŽIVATEL A HRÁČ
-- ============================================================

CREATE TABLE IF NOT EXISTS uzivatele (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno       TEXT NOT NULL UNIQUE,
    heslo_hash  TEXT NOT NULL,
    sul         TEXT NOT NULL,
    vytvoren    TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Staty hráče (1:1 s uživatelem)
CREATE TABLE IF NOT EXISTS postup (
    uzivatel_id         INTEGER PRIMARY KEY,
    skore               INTEGER NOT NULL DEFAULT 0 CHECK (skore >= 0),
    hp                  INTEGER NOT NULL DEFAULT 50,
    max_hp              INTEGER NOT NULL DEFAULT 50,
    mana                INTEGER NOT NULL DEFAULT 5,
    rychlost            INTEGER NOT NULL DEFAULT 3,
    obrana              INTEGER NOT NULL DEFAULT 1,
    utok                INTEGER NOT NULL DEFAULT 3,
    level               INTEGER NOT NULL DEFAULT 1 CHECK (level >= 1),
    exp                 INTEGER NOT NULL DEFAULT 0 CHECK (exp >= 0),
    zlato               INTEGER NOT NULL DEFAULT 0 CHECK (zlato >= 0),
    max_karet_v_balicku INTEGER NOT NULL DEFAULT 10,
    max_karet_v_ruce    INTEGER NOT NULL DEFAULT 5,
    odpocinek           INTEGER NOT NULL DEFAULT 1 CHECK (odpocinek IN (0, 1)),
    aktualizovano       TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE
);

-- Historie skóre (žebříček na webu)
CREATE TABLE IF NOT EXISTS skore (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    uzivatel_id INTEGER NOT NULL,
    body        INTEGER NOT NULL CHECK (body >= 0),
    uroven      INTEGER NOT NULL DEFAULT 1,
    datum       TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_skore_body ON skore(body DESC);

-- ============================================================
-- NEGATIVNÍ EFEKTY (číselník)
-- ============================================================

CREATE TABLE IF NOT EXISTS efekty (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev       TEXT NOT NULL UNIQUE,                              -- slow, poison, ...
    popis       TEXT NOT NULL,
    typ         TEXT NOT NULL CHECK (typ IN ('dot', 'stat_snizeni', 'ovladani')),
    hodnota     INTEGER NOT NULL DEFAULT 0                         -- poison 2 dmg/kolo, slow -1 rychlost
);

-- Aktivní efekty na hráči
CREATE TABLE IF NOT EXISTS hrac_efekty (
    uzivatel_id INTEGER NOT NULL,
    efekt_id    INTEGER NOT NULL,
    zbyva_kol   INTEGER NOT NULL CHECK (zbyva_kol > 0),
    PRIMARY KEY (uzivatel_id, efekt_id),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE,
    FOREIGN KEY (efekt_id)    REFERENCES efekty(id)
);

-- ============================================================
-- KARTY
-- ============================================================

CREATE TABLE IF NOT EXISTS karty (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev       TEXT NOT NULL UNIQUE,
    kategorie   TEXT NOT NULL CHECK (kategorie IN ('utok', 'obrana', 'leceni', 'podpora', 'kletba')),
    sila        INTEGER NOT NULL DEFAULT 1 CHECK (sila >= 0),      -- spotřeba many
    efekt_typ   TEXT NOT NULL CHECK (efekt_typ IN ('damage', 'block', 'heal', 'buff', 'debuff')),
    hodnota     INTEGER NOT NULL DEFAULT 0,                        -- např. 3 dmg, 10 hp
    efekt_id    INTEGER,                                           -- volitelně: aplikuje stav (poison...)
    popis       TEXT NOT NULL,                                     -- text pro hráče
    cena        INTEGER NOT NULL DEFAULT 0 CHECK (cena >= 0),
    FOREIGN KEY (efekt_id) REFERENCES efekty(id)
);

-- Balíček hráče: které karty a kolik kusů (součet <= max_karet_v_balicku hlídá hra)
CREATE TABLE IF NOT EXISTS hrac_balicek (
    uzivatel_id INTEGER NOT NULL,
    karta_id    INTEGER NOT NULL,
    pocet       INTEGER NOT NULL DEFAULT 1 CHECK (pocet > 0),
    PRIMARY KEY (uzivatel_id, karta_id),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE,
    FOREIGN KEY (karta_id)    REFERENCES karty(id)
);

-- Sbírka všech vlastněných karet (z ní se skládá balíček)
CREATE TABLE IF NOT EXISTS hrac_sbirka (
    uzivatel_id INTEGER NOT NULL,
    karta_id    INTEGER NOT NULL,
    pocet       INTEGER NOT NULL DEFAULT 1 CHECK (pocet > 0),
    PRIMARY KEY (uzivatel_id, karta_id),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE,
    FOREIGN KEY (karta_id)    REFERENCES karty(id)
);

-- ============================================================
-- PŘEDMĚTY, INVENTÁŘ, EQUIP
-- ============================================================

CREATE TABLE IF NOT EXISTS predmety (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev          TEXT NOT NULL UNIQUE,
    slot           TEXT CHECK (slot IN ('helma', 'torso', 'rukavice', 'nohavice', 'boty',
                                        'prsten', 'nahrdelnik', 'zbran', 'obourucni_zbran', 'stit')),
                                                                   -- NULL = nenasaditelný (lektvar, materiál)
    bonus_hp       INTEGER NOT NULL DEFAULT 0,
    bonus_mana     INTEGER NOT NULL DEFAULT 0,
    bonus_rychlost INTEGER NOT NULL DEFAULT 0,
    bonus_obrana   INTEGER NOT NULL DEFAULT 0,
    bonus_utok     INTEGER NOT NULL DEFAULT 0,
    popis          TEXT NOT NULL DEFAULT '',
    cena           INTEGER NOT NULL DEFAULT 0 CHECK (cena >= 0)
);

CREATE TABLE IF NOT EXISTS inventar (
    uzivatel_id INTEGER NOT NULL,
    predmet_id  INTEGER NOT NULL,
    pocet       INTEGER NOT NULL DEFAULT 1 CHECK (pocet > 0),
    PRIMARY KEY (uzivatel_id, predmet_id),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE,
    FOREIGN KEY (predmet_id)  REFERENCES predmety(id)
);

-- Nasazené věci: 1 řádek = 1 obsazený slot
-- (obourucni_zbran vylučuje zbran + stit - hlídá hra)
CREATE TABLE IF NOT EXISTS equip (
    uzivatel_id INTEGER NOT NULL,
    slot        TEXT NOT NULL CHECK (slot IN ('helma', 'torso', 'rukavice', 'nohavice', 'boty',
                                              'prsten_1', 'prsten_2', 'nahrdelnik',
                                              'zbran', 'obourucni_zbran', 'stit')),
    predmet_id  INTEGER NOT NULL,
    PRIMARY KEY (uzivatel_id, slot),
    FOREIGN KEY (uzivatel_id) REFERENCES uzivatele(id) ON DELETE CASCADE,
    FOREIGN KEY (predmet_id)  REFERENCES predmety(id)
);

-- ============================================================
-- NEPŘÁTELÉ
-- ============================================================

CREATE TABLE IF NOT EXISTS nepratele (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno       TEXT NOT NULL UNIQUE,
    hp          INTEGER NOT NULL CHECK (hp > 0),
    rychlost    INTEGER NOT NULL DEFAULT 1,
    obrana      INTEGER NOT NULL DEFAULT 0,
    utok        INTEGER NOT NULL DEFAULT 1,
    level       INTEGER NOT NULL DEFAULT 1 CHECK (level >= 1),     -- obtížnost
    exp         INTEGER NOT NULL DEFAULT 0                         -- odměna, např. 200
);

-- Balíček nepřítele (karty, které může hrát)
CREATE TABLE IF NOT EXISTS nepritel_balicek (
    nepritel_id INTEGER NOT NULL,
    karta_id    INTEGER NOT NULL,
    pocet       INTEGER NOT NULL DEFAULT 1 CHECK (pocet > 0),
    PRIMARY KEY (nepritel_id, karta_id),
    FOREIGN KEY (nepritel_id) REFERENCES nepratele(id) ON DELETE CASCADE,
    FOREIGN KEY (karta_id)    REFERENCES karty(id)
);

-- Odměna za porážku: zlato, předmět nebo karta (vždy právě jedno z nich)
CREATE TABLE IF NOT EXISTS nepritel_drop (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nepritel_id INTEGER NOT NULL,
    typ         TEXT NOT NULL CHECK (typ IN ('zlato', 'predmet', 'karta')),
    mnozstvi    INTEGER NOT NULL DEFAULT 1 CHECK (mnozstvi > 0),   -- u zlata částka
    predmet_id  INTEGER,
    karta_id    INTEGER,
    sance       INTEGER NOT NULL DEFAULT 100 CHECK (sance BETWEEN 1 AND 100),  -- v %
    FOREIGN KEY (nepritel_id) REFERENCES nepratele(id) ON DELETE CASCADE,
    FOREIGN KEY (predmet_id)  REFERENCES predmety(id),
    FOREIGN KEY (karta_id)    REFERENCES karty(id),
    CHECK (
        (typ = 'zlato'   AND predmet_id IS NULL     AND karta_id IS NULL) OR
        (typ = 'predmet' AND predmet_id IS NOT NULL AND karta_id IS NULL) OR
        (typ = 'karta'   AND karta_id   IS NOT NULL AND predmet_id IS NULL)
    )
);

-- ============================================================
-- VZOROVÁ DATA (INSERT OR IGNORE - bezpečné při opakovaném spuštění)
-- ============================================================

INSERT OR IGNORE INTO efekty (nazev, popis, typ, hodnota) VALUES
    ('poison', 'Každé kolo ztratí 2 HP.',   'dot',          2),
    ('slow',   'Rychlost snížena o 1.',     'stat_snizeni', 1),
    ('stun',   'Přeskočí jedno kolo.',      'ovladani',     0);

INSERT OR IGNORE INTO karty (nazev, kategorie, sila, efekt_typ, hodnota, popis, cena) VALUES
    ('Úder',        'utok',   1, 'damage', 3,  'Způsobí 3 poškození.',            10),
    ('Silný úder',  'utok',   3, 'damage', 8,  'Způsobí 8 poškození.',            40),
    ('Štít',        'obrana', 1, 'block',  4,  'Získáš 4 obrany na toto kolo.',   10),
    ('Léčení',      'leceni', 2, 'heal',   10, 'Vyléčí 10 HP.',                   30);

INSERT OR IGNORE INTO predmety (nazev, slot, bonus_utok, bonus_obrana, bonus_rychlost, cena) VALUES
    ('Dřevěný meč',  'zbran', 2, 0, 0, 20),
    ('Kožená helma', 'helma', 0, 1, 0, 15),
    ('Lehké boty',   'boty',  0, 0, 1, 15);

INSERT OR IGNORE INTO nepratele (jmeno, hp, rychlost, obrana, utok, level, exp) VALUES
    ('Slizák', 20, 1, 0, 2, 1, 50),
    ('Goblin', 35, 2, 1, 4, 2, 120);

INSERT OR IGNORE INTO nepritel_balicek (nepritel_id, karta_id, pocet)
    SELECT n.id, k.id, 3 FROM nepratele n, karty k
    WHERE n.jmeno = 'Slizák' AND k.nazev = 'Úder';

INSERT OR IGNORE INTO nepritel_balicek (nepritel_id, karta_id, pocet)
    SELECT n.id, k.id, 2 FROM nepratele n, karty k
    WHERE n.jmeno = 'Goblin' AND k.nazev IN ('Úder', 'Štít');

INSERT INTO nepritel_drop (nepritel_id, typ, mnozstvi, sance)
    SELECT id, 'zlato', 10, 100 FROM nepratele
    WHERE jmeno = 'Slizák' AND NOT EXISTS (SELECT 1 FROM nepritel_drop);
