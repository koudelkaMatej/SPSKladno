# Definice funkce
<<<<<<< HEAD
def sečti(x, y = 0):
    return x + y
# Testování pomocí unittest/ načtení knihovny
import unittest

class TestSečtiFunkce(unittest.TestCase):
    def test_sečti(self):
        # Test: sečti(2, 3) má vrátit 5
        self.assertEqual(sečti(2, 3), 5)

        # Test: sečti(-1, 1) má vrátit 0
        self.assertEqual(sečti(-1, 1), 0)

        # Test: sečti(0, 0) má vrátit 0
        self.assertEqual(sečti(0, 0), 0)

    def test_chyba(self):
        self.assertEqual(sečti(2, 3), 6) # Test: sečti(2, 3) má vrátit 5, ale já chci 6(hodí chybu) Zároveň se pustí 2 testy
=======
def sečti(x, y):
    return x + y

# Testování pomocí unittest/ načtení knihovny
import unittest

class TestSečtiFunkce(unittest.TestCase):
    def test_sečti(self):
        # Test: sečti(2, 3) má vrátit 5
        self.assertEqual(sečti(2, 3), 5)

        # Test: sečti(-1, 1) má vrátit 0
        self.assertEqual(sečti(-1.0, 1.0), 0.0)

        # Test: sečti(0, 0) má vrátit 0
        self.assertEqual(sečti(0, 0), 0)
>>>>>>> aa1dfaf9a70add6ac0675f5ecf26784820ecafa7

# Spuštění testů
if __name__ == '__main__':
    unittest.main()