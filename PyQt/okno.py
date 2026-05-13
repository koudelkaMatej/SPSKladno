from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class HlavniOkno(QWidget):
    """Hlavní okno naší aplikace.

    Args:
        QWidget (class): Tento argument přidáváme,
        abychom rozšířili, to co naše třída umí.
        Říkáme tím, že naše HlavniOkno je QWidget (tedy umí vše, co umí QWidget)
        a může k němu přidat i něco navíc
    """

    def __init__(self):
        """Tato funkce se zavolá v momentě,
        kdy vytvoříme instanci třídy HlavniOkno (zapíšeme, že chceme vytvořit objekt typu HlavniOkno).
        Do této funkce dáme vše co jsme u aplikací určovali:
        * rozložení atributů
        * přidávání atributů
        * přiřazování funkcí k atributům
        """
        QWidget.__init__(self) # vytoříme QWidget
        # a přidáme naše prvky
        self.rozlozeni = QVBoxLayout()
        self.tlacitko = QPushButton("Stiskni pro nové okno")
        self.rozlozeni.addWidget(self.tlacitko)
        self.setLayout(self.rozlozeni)
        self.tlacitko.clicked.connect(self.vyrob_nove_okno)

    def vyrob_nove_okno(self):
        """Tato funkce je zodpovědná za vytvoření a zobrazení,
        nového okna. V tomto případě okna třídy (typu) VedlejsiOkno.
        """
        self.okno = VedlejsiOkno()
        self.okno.show()


class VedlejsiOkno(QWidget):
    """Vedlejší okno naší aplikace.
    Instance této třídy se vytvoří, až poté co klikneme na tlačítko v hlavním okně

    Args:
        QWidget (class): Tento argument přidáváme,
        abychom rozšířili, to co naše třída umí.
        Říkáme tím, že naše VedlejsiOkno je QWidget (tedy umí vše, co umí QWidget)
        a může k němu přidat i něco navíc
    """

    def __init__(self):
        """Tato funkce se zavolá v momentě,
        kdy vytvoříme instanci třídy VedlejsiOkno.
        Do této funkce dáme všechno co jsme u aplikací určovali:
        * rozložení atributů
        * přidávání atributů
        * přiřazování funkcí k atributům
        """
        QWidget.__init__(self)
        self.rozlozeni = QVBoxLayout()
        self.text = QLabel("Nové okno")
        self.rozlozeni.addWidget(self.text)
        self.setLayout(self.rozlozeni)


# jediné co zbývá je vytvořit aplikaci a instanci (objekt) hlavního okna
app = QApplication([])
okno = HlavniOkno()
okno.show()
app.exec()
