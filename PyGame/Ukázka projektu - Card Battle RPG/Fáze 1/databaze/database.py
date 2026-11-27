"""Práce s databází (SQLite) - registrace, přihlášení, postup a skóre."""
import hashlib
import hmac
import os
import sqlite3

DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DIR, "hra.db")
SCHEMA_PATH = os.path.join(DIR, "schema.sql")


def pripojit():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializovat():
    """Vytvoří tabulky, pokud neexistují."""
    with pripojit() as conn, open(SCHEMA_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())


def _hash(heslo, sul):
    return hashlib.pbkdf2_hmac("sha256", heslo.encode(), bytes.fromhex(sul), 100_000).hex()


def registrovat(jmeno, heslo):
    """Vrátí id nového uživatele, nebo None pokud jméno už existuje."""
    sul = os.urandom(16).hex()
    try:
        with pripojit() as conn:
            cur = conn.execute(
                "INSERT INTO uzivatele (jmeno, heslo_hash, sul) VALUES (?, ?, ?)",
                (jmeno, _hash(heslo, sul), sul),
            )
            conn.execute("INSERT INTO postup (uzivatel_id) VALUES (?)", (cur.lastrowid,))
            return cur.lastrowid
    except sqlite3.IntegrityError:
        return None


def prihlasit(jmeno, heslo):
    """Vrátí id uživatele, nebo None při špatných údajích."""
    with pripojit() as conn:
        r = conn.execute(
            "SELECT id, heslo_hash, sul FROM uzivatele WHERE jmeno = ?", (jmeno,)
        ).fetchone()
    if r and hmac.compare_digest(r["heslo_hash"], _hash(heslo, r["sul"])):
        return r["id"]
    return None


STAT_SLOUPCE = {
    "skore", "hp", "max_hp", "mana", "rychlost", "obrana", "utok", "level", "exp",
    "zlato", "max_karet_v_balicku", "max_karet_v_ruce", "odpocinek",
}


def nacist_postup(uzivatel_id):
    """Vrátí řádek se staty hráče (sqlite3.Row), nebo None."""
    with pripojit() as conn:
        return conn.execute(
            "SELECT * FROM postup WHERE uzivatel_id = ?", (uzivatel_id,)
        ).fetchone()


def ulozit_postup(uzivatel_id, **staty):
    """Např. ulozit_postup(1, level=2, exp=30, zlato=100)."""
    neplatne = set(staty) - STAT_SLOUPCE
    if neplatne or not staty:
        raise ValueError(f"Neplatné staty: {neplatne or 'žádné'}")
    sloupce = ", ".join(f"{k} = ?" for k in staty)
    with pripojit() as conn:
        conn.execute(
            f"UPDATE postup SET {sloupce}, aktualizovano = datetime('now') WHERE uzivatel_id = ?",
            (*staty.values(), uzivatel_id),
        )


def pridat_skore(uzivatel_id, body, uroven=1):
    with pripojit() as conn:
        conn.execute(
            "INSERT INTO skore (uzivatel_id, body, uroven) VALUES (?, ?, ?)",
            (uzivatel_id, body, uroven),
        )


def zebricek(limit=10):
    with pripojit() as conn:
        return conn.execute(
            "SELECT u.jmeno, MAX(s.body) AS body, MAX(s.uroven) AS uroven "
            "FROM skore s JOIN uzivatele u ON u.id = s.uzivatel_id "
            "GROUP BY u.id ORDER BY body DESC LIMIT ?",
            (limit,),
        ).fetchall()


if __name__ == "__main__":
    inicializovat()
    print("Databáze vytvořena:", DB_PATH)
