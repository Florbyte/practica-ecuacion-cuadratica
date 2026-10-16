# test_ecuacion.py
import unittest
from ecuacion import resolver_ecuacion

class TestResolverEcuacion(unittest.TestCase):

    def test_dos_soluciones_reales(self):
        """x^2 - 5x + 6 = 0 => x=3, x=2"""
        res = resolver_ecuacion(1, -5, 6)
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertAlmostEqual(res["soluciones"][0], 3.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)

    def test_una_solucion(self):
        """x^2 - 2x + 1 = 0 => x=1"""
        res = resolver_ecuacion(1, -2, 1)
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertAlmostEqual(res["soluciones"][0], 1.0)  

    def test_sin_solucion_real(self):
        """x^2 + 1 = 0 => sin solucion real"""
        res = resolver_ecuacion(1, 0, 1)
        self.assertEqual(res["tipo"], "sin_solucion_real")
        self.assertEqual(res["soluciones"], [])

    def test_ecuacion_lineal(self):
        """0x^2 + 2x + 4 = 0 => x = -2 (lineal)"""
        res = resolver_ecuacion(0, 2, 4)
        self.assertEqual(res["tipo"], "lineal")
        self.assertAlmostEqual(res["soluciones"][0], -2.0)

    def test_coeficientes_invalidos(self):
        """a=0, b=0 => ValueError"""
        with self.assertRaises(ValueError):
            resolver_ecuacion(0, 0, 5)

    def test_multiples_casos_con_subTest(self):
        """Varios casos parametrizados con subTest."""
        casos = [
            (1, 0, -4, "dos_soluciones", [2.0, -2.0]),
            (2, -4, 2, "una_solucion", [1.0]),  # Corregido: [1.0] dentro de lista
            (1, 2, 5, "sin_solucion_real", []),
        ]
        for a, b, c, tipo_esp, sol_esp in casos:
            with self.subTest(a=a, b=b, c=c):
                res = resolver_ecuacion(a, b, c)
                self.assertEqual(res["tipo"], tipo_esp)
                for obt, esp in zip(
                    res["soluciones"], sol_esp
                    ):
                    self.assertAlmostEqual(obt, esp)
        else:
            self.assertAlmostEqual(
                res["soluciones"], sol_esp
            )
# Pruebas nuevas

    def test_coeficientes_grandes_sin_error(self):
        """Coeficientes grandes: el programa devuelve un resultado válido."""
        res = resolver_ecuacion(1000000, 1000000, 1000000)
        self.assertEqual(res["tipo"], "sin_solucion_real")
        self.assertEqual(res["soluciones"], [])

    def test_ecuacion_x_cuadrado_igual_cero(self):
        """x^2 = 0 debe devolver una raíz doble igual a cero."""
        res = resolver_ecuacion(1, 0, 0)
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertAlmostEqual(res["soluciones"][0], 0.0, places=10)

    def test_coeficiente_a_negativo(self):
        """-x^2 + 4 = 0 -> x=2 y x=-2."""
        res = resolver_ecuacion(-1, 0, 4)
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertAlmostEqual(res["soluciones"][0], -2.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)


if __name__ == '__main__':
 unittest.main()
