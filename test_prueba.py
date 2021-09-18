from unittest import TestCase, skip
from pruebas import sumatoria

class TestPruebas(TestCase):
    @skip('Demostrando los test, no sirve este test')
    def testprueba(self):
        nombre='christian'
        self.assertEqual(nombre, 'Christian')

    def testSumatoria(self):
        resultado = sumatoria(5, 6)
        self.assertEqual(resultado, 11)
        self.assertNotEqual(resultado,10)