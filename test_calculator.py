import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): #? Esta es la función que testea la función «add», Siempre hay que llamarlas con «test», de lo contrario Python se salta esa prueba.
        self.assertEqual(add(1, 2), 3) #TODO Aquí se insertan las distintas pruebas de la función a probar con los valores y el resultado que esperamos.
        self.assertEqual(add(-1, 2), 1)

    def test_substract(self):
        self.assertEqual(substract(2, 3), -1)
        self.assertEqual(substract(5, 2), 3)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(5, 4), 20)
    
    def test_divide(self):
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(10, 5), 2)

if __name__ == '__main__': #? Estas líneas de código son para que las pruebas solo se lleven a cabo cuando se ejecute este archivo de Python en concreto. 
    unittest.main()