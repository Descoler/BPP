import unittest
import operaciones

class PruebasUnitarias (unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones.suma(10,2),12)
    def test_resta(self):
        self.assertEqual(operaciones.resta(10,5),5)
    def test_primo(self):
        self.assertTrue(operaciones.es_primo(3))
        self.assertFalse(operaciones.es_primo(8))

if __name__ =='__main__':
    unittest.main()