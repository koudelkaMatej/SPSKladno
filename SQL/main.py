from pripojeni import *
import mysql.connector

# tento příkaz nás připojí do databáze
mydb = mysql.connector.connect(
    host = HOST
    ,user = USER
    ,password = PASSWORD
    ,database = DATABASE
) 

mycursor = mydb.cursor() # proměnnou mycursor si můžeme představit jako myš a klávesnici, kterými zadáváme hodnoty do databáze a potvrzujeme příkazy


# mycursor.execute("""DROP TABLE Automobil """)
mycursor.execute("""CREATE TABLE Automobil2025(
    id int PRIMARY KEY AUTO_INCREMENT,  /* Vlastní klíč - může být jen jeden v tabulce */
    spz char(7) NOT NULL UNIQUE,        /* UNIQUE - v tabulce se nemůže opakovat spz, NOT NULL - spz musí být vyplněna*/
    pocet_sedadel int NOT NULL,         /* NOT NULL - počet sedadel musí být vyplněn */
    max_rychlost int,
    nosnost int,
    nutna_kvalifikace text NOT NULL DEFAULT "B",  /* DEFAULT - pokud nezadáme hodnotu doplní se "B", NOT NULL - nutná klasifikace musí být vyplněna - tedy nemůžeme manuálně vložit NULL*/
    datum_vyroby date
);""")

mydb.commit()
mycursor.close()
mydb.close()
