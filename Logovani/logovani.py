import logging

# Společný handler pro oba loggery
file_handler = logging.FileHandler("Logovani/logovani.txt", mode="w", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Logger pro INFO zprávy
logger_info = logging.getLogger("info_logger")
logger_info.setLevel(logging.INFO)
logger_info.addHandler(file_handler)

# Logger pro DEBUG zprávy
logger_debug = logging.getLogger("debug_logger")
logger_debug.setLevel(logging.DEBUG)
logger_debug.addHandler(file_handler)


class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.skore = 0
        logger_info.info(f"Hráč {self.jmeno} byl vytvořen.")
        logger_debug.debug(f"Vytvořen objekt Hrac(jmeno='{self.jmeno}', skore={self.skore})")

    def pridat_body(self, body):
        stary_stav = self.skore
        self.skore += body
        logger_info.info(f"Hráč {self.jmeno} získal {body} bodů. Celkem má {self.skore}.")
        logger_debug.debug(f"Změna skóre: {stary_stav} -> {self.skore}")

    def zkontrolovat_vyhru(self, limit):
        if self.skore >= limit:
            logger_info.info(f"Hráč {self.jmeno} vyhrál!")
            logger_debug.debug(f"Kontrola výhry: skore={self.skore}, limit={limit} => VYHRÁL")
            return True
        else:
            logger_debug.debug(f"Kontrola výhry: skore={self.skore}, limit={limit} => NEVYHRÁL")
            return False


# Ukázka použití
if __name__ == "__main__":
    hrac1 = Hrac("Petr")
    hrac1.pridat_body(5)
    hrac1.pridat_body(10)
    hrac1.zkontrolovat_vyhru(10)
