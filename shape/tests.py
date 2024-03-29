import unittest
from .circle import Circle
from .convex_polygon.triangle import Triangle


class TestCircle(unittest.TestCase):
    def test_area_int(self):
        c = Circle(5)
        self.assertEqual(c.area, 78.54)

    def test_area_float(self):
        c = Circle(2.5)
        self.assertEqual(c.area, 19.635)

    def test_catch_zero_radius(self):
        self.assertRaises(ValueError, Circle, 0)

    def test_catch_negative_radius(self):
        self.assertRaises(ValueError, Circle, -2)

    def test_perimeter_int(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter, 31.4, places=1)

    def test_perimeter_float(self):
        c = Circle(2.5)
        self.assertAlmostEqual(c.perimeter, 15.7, places=1)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t_int = Triangle(9, 12, 15)
        self.t_float = Triangle(3.5, 4.6, 7.9)
        self.t_1 = Triangle(60, 60, 60)
        self.t_2 = Triangle(5, 10, 7.3)
        self.t_3 = Triangle(7, 7, 13.53)

    def test_area_int(self):
        self.assertEqual(self.t_int.area, 54)

    def test_area_float(self):
        self.assertEqual(self.t_float.area, 3.499)

    def test_perimeter_int(self):
        self.assertEqual(self.t_int.perimeter, 36)

    def test_perimeter_float(self):
        self.assertAlmostEqual(self.t_float.perimeter, 16, 1)

    def test_is_right(self):
        self.assertTrue(self.t_int.is_right())

    def test_isnt_right(self):
        self.assertFalse(self.t_float.is_right())

    def test_catch_null_side(self):
        self.assertRaises(ValueError, Triangle, 0, 4, 6)

    def test_catch_all_null_sides(self):
        self.assertRaises(ValueError, Triangle, 0, 0, 0)

    def test_catch_negative_side(self):
        self.assertRaises(ValueError, Triangle, 3, 5, -2)

    def test_catch_all_negative_sides(self):
        self.assertRaises(ValueError, Triangle, -1, -3, -2.5)

    def test_catch_sum_error(self):
        self.assertRaises(ValueError, Triangle, 9, 12, 25)

    def test_catch_sum_eq_error(self):
        self.assertRaises(ValueError, Triangle, 9, 12, 21)

    def test_area_t_1(self):
        self.assertEqual(self.t_1.area, 1558.846)

    def test_perimeter_t_1(self):
        self.assertEqual(self.t_1.perimeter, 180)

    def test_area_t_2(self):
        self.assertEqual(self.t_2.area, 17.424)

    def test_perimeter_t_2(self):
        self.assertEqual(self.t_2.perimeter, 22.3)

    def test_area_t_3(self):
        self.assertEqual(self.t_3.area, 12.167)

    def test_perimeter_t_3(self):
        self.assertEqual(self.t_3.perimeter, 27.53)

if __name__ == '__main__':
    unittest.main()
