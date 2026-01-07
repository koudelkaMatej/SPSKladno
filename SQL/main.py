import mysql.connector
from pripojeni import *

import mysql.connector
mydb = mysql.connector.connect(
    host = HOST
    ,user = USER
    ,password = PASSWORD
    ,database = DATABASE
) 
mycursor = mydb.cursor()

try:
    mycursor.execute("""DROP TABLE Tym;""")
    mydb.commit()
except mysql.connector.Error:
    print("Tabulka Tym neexistuje.")

try:
    mycursor.execute("""DROP TABLE Hrac;""")
    mydb.commit()
except mysql.connector.Error:
    print("Tabulka Hrac neexistuje.")

try:
    mycursor.execute("""DROP TABLE Pozice;""")
    mydb.commit()
except mysql.connector.Error:
    print("Tabulka Pozice neexistuje.")

# Vytvoříme si potřebné tabulky
mycursor.execute("""CREATE TABLE Tym
(
	id int AUTO_INCREMENT PRIMARY KEY,
	nazev char(20) NOT NULL,
	mesto char(20) NOT NULL,
	zustatek int DEFAULT 0,
	CONSTRAINT UNIKATNI_tym UNIQUE (nazev, mesto) /* UNIQUE na nazev a mesto zaroveň */
);""")

mydb.commit()

mycursor.execute("""CREATE TABLE Pozice(
	id_poz int PRIMARY KEY AUTO_INCREMENT,
	pojmenovani text NOT NULL
);""")

mydb.commit()

mycursor.execute("""CREATE TABLE Hrac(
	id int AUTO_INCREMENT PRIMARY KEY,
	jmeno text NOT NULL,
	prijmeni text NOT NULL,
	datum_narozeni DATE NOT NULL,
	tym_id int NOT NULL,
	pozice_id int NOT NULL 
    
    /* zde by se hodil ještě FOREIGN KEY, abychom měli jistotu, 
    že hráče zařazujeme do existujícího týmu */
);""")

mydb.commit()

# A zapíšeme do nich
mycursor.execute("""INSERT INTO Tym (nazev, mesto, zustatek) VALUES
	("HC Rytíři", "Kladno", 1000),
	("HC Slavie", "Praha", 5000),
	("HC Sparta", "Praha", 6000),
	("HC Sparta", "Brno", 5600);""")

mydb.commit()

mycursor.execute("""INSERT INTO Pozice(pojmenovani) VALUES
	("Utocnik"),
	("Obrana"),
	("Brankar"),
	("Zaloha");""")

mydb.commit()

mycursor.execute("""INSERT INTO Hrac (jmeno, prijmeni, datum_narozeni, tym_id, pozice_id) VALUES
	("Adam", "Prvni", '1996-06-02', 2, 2),
	("Pavel", "Druhy", '2000-09-09', 1, 3),
	("Kuba", "Treti", '1998-01-05', 3, 1),
	("Josef", "Čtvrtý", '1997-01-06', 6, 2),
	("Jirka", "Pátý", '1999-03-08', 2, 6);""")

mydb.commit()

mycursor.close()
mydb.close()



mydb = mysql.connector.connect(
    host = HOST
    ,user = USER
    ,password = PASSWORD
    ,database = DATABASE
) 
mycursor = mydb.cursor()

# bez zadané podmínky a sloupečků s hodnotami k porovnání
mycursor.execute("""SELECT prijmeni, datum_narozeni, nazev, mesto FROM Hrac INNER JOIN Tym;
""") # Tento příkaz vypíše kombinace každého hráče s každým týmem.

myresult = mycursor.fetchall()

for prijmeni, datum_narozeni, nazev, mesto in myresult:
    print(f"Hráč {prijmeni}, s datem narození {datum_narozeni} z týmu {nazev} v městě {mesto}")

print("=========")
# Tento JOIN je nám však k ničemu, protože neposkytuje žádné informace
# Takže k příkazu tedy přidáme podmínku,
# tak aby spolili pouze řádky, kde hrac.tym_id =  tym.id
mycursor.execute("""SELECT prijmeni, datum_narozeni, nazev, mesto FROM Hrac JOIN Tym
    ON Hrac.tym_id = Tym.id;
""")

myresult = mycursor.fetchall()

for prijmeni, datum_narozeni, nazev, mesto in myresult:
    print(f"Hráč {prijmeni}, s datem narození {datum_narozeni} z týmu {nazev} v městě {mesto}")
# Jak můžete vidět, tak hráč s příjmením Čtvrtý se nevypsal,
# protože k jeho tym_id není odpovídající id v tabulce Tym

print("=========")
mycursor.execute("""SELECT prijmeni, datum_narozeni, nazev, mesto FROM
    Tym LEFT JOIN Hrac ON Tym.id=Hrac.tym_id;
""")

myresult = mycursor.fetchall()

for prijmeni, datum_narozeni, nazev, mesto in myresult:
    print(f"Hráč {prijmeni}, s datem narození {datum_narozeni} z týmu {nazev} v městě {mesto}")

print("=========")

mycursor.execute("""SELECT prijmeni, datum_narozeni, nazev, mesto FROM
    Tym RIGHT JOIN Hrac ON Tym.id=Hrac.tym_id;
""")

myresult = mycursor.fetchall()

for prijmeni, datum_narozeni, nazev, mesto in myresult:
    print(f"Hráč {prijmeni}, s datem narození {datum_narozeni} z týmu {nazev} v městě {mesto}")

print("=========")
mycursor.execute("""SELECT prijmeni, datum_narozeni, nazev, mesto 
    FROM Hrac LEFT JOIN Tym ON Hrac.tym_id = Tym.id 
    UNION 
    SELECT prijmeni, datum_narozeni, nazev, mesto 
    FROM Hrac RIGHT JOIN Tym ON Hrac.tym_id = Tym.id;
""")

myresult = mycursor.fetchall()

for prijmeni, datum_narozeni, nazev, mesto in myresult:
    print(f"Hráč {prijmeni}, s datem narození {datum_narozeni} z týmu {nazev} v městě {mesto}")
mycursor.close()
mydb.close()