import unittest
def soucty_prvku(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Seznamy musí mít stejnou délku!")
    return [a + b for a, b in zip(list1, list2)]

class TestSouctyPrvku(unittest.TestCase):
    def test_spravne_scitani(self):
        self.assertEqual(soucty_prvku([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_nerovna_delka(self):
        with self.assertRaises(ValueError):
            soucty_prvku([1, 2], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
