import unittest

def secti(x, y):
    return x + y

class TestSectiFunkce(unittest.TestCase):
    def test_spravny(self):
        self.assertEqual(secti(2, 3), 5)  # ✅ projde

    def test_chybny(self):
        self.assertNotEqual(secti(2, 3), 6)  # ❌ selže — 2+3 = 5, ne 6!


# Spuštění testů v Jupyter Notebooku (náhrada za unittest.main())
unittest.main()