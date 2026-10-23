import unittest

from solutions.classes.complex_numbers import Complex
from solutions.classes.torsional_angle import Points, torsional_angle


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.c = Complex(2, 1)
        self.d = Complex(5, 6)

    def test_operations(self):
        self.assertEqual(str(self.c + self.d), "7.00+7.00i")
        self.assertEqual(str(self.c - self.d), "-3.00-5.00i")
        self.assertEqual(str(self.c * self.d), "4.00+17.00i")
        self.assertEqual(str(self.c / self.d), "0.26-0.11i")
        self.assertEqual(str(self.c.mod()), "2.24+0.00i")
        self.assertEqual(str(self.d.mod()), "7.81+0.00i")

    def test_zero_parts(self):
        self.assertEqual(str(Complex(0, -2)), "0.00-2.00i")
        self.assertEqual(str(Complex(0, 0)), "0.00+0.00i")


class TestTorsionalAngle(unittest.TestCase):
    def test_sample(self):
        a, b, c, d = Points(0, 4, 5), Points(1, 7, 6), Points(0, 5, 9), Points(1, 7, 2)
        self.assertEqual("%.2f" % torsional_angle(a, b, c, d), "8.19")

    def test_vector_ops(self):
        p, q = Points(1, 0, 0), Points(0, 1, 0)
        self.assertEqual(p.dot(q), 0)
        r = p.cross(q)
        self.assertEqual((r.x, r.y, r.z), (0, 0, 1))
        self.assertEqual(Points(3, 4, 0).absolute(), 5)


if __name__ == "__main__":
    unittest.main()
