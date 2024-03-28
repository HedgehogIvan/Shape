import unittest
from .circle import Circle
from .convex_polygon.triangle import Triangle


class TestCircle(unittest.TestCase):
    def test_area_int(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area, 78.5, places=1)

    def test_area_float(self):
        c = Circle(2.5)
        self.assertAlmostEqual(c.area, 19.63495, places=5)

    def test_perimeter_int(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter, 31.4, places=1)

    def test_perimeter_float(self):
        c = Circle(2.5)
        self.assertAlmostEqual(c.perimeter, 15.7, places=1)


class TestTriangle(unittest.TestCase):
    def test_area_int(self):
        t = Triangle(9, 12, 15)
        self.assertEqual(t.area, 54)

    def test_area_float(self):
        t = Triangle(3.5, 4.6, 7.9)
        self.assertAlmostEqual(t.area, 3.49857, places=5)

    def test_perimeter_int(self):
        t = Triangle(9, 12, 15)
        self.assertEqual(t.perimeter, 36)

    def test_perimeter_float(self):
        t = Triangle(3.5, 4.6, 7.9)
        self.assertAlmostEqual(t.perimeter, 16, 1)

    def test_is_right(self):
        t = Triangle(9, 12, 15)
        self.assertTrue(t.is_right())

    def test_isnt_right(self):
        t = Triangle(3.5, 4.6, 7.9)
        self.assertFalse(t.is_right())

if __name__ == '__main__':
    unittest.main()
