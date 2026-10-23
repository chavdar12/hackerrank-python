import unittest

from solutions.maths.find_angle_mbc import angle_mbc
from solutions.maths.integers_come_in_all_sizes import big_power_sum
from solutions.maths.mod_divmod import mod_divmod
from solutions.maths.polar_coordinates import polar
from solutions.maths.power_mod_power import power_mod
from solutions.maths.triangle_quest import triangle
from solutions.maths.triangle_quest_2 import palindromic_triangle


class TestPolarCoordinates(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(polar("1+2j"), (2.236, 1.107))


class TestFindAngleMBC(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(angle_mbc(10, 10), "45°")

    def test_rounds_to_nearest(self):
        self.assertEqual(angle_mbc(1, 100), "1°")


class TestTriangleQuest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(triangle(5), [1, 22, 333, 4444])


class TestTriangleQuest2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(palindromic_triangle(5), [1, 121, 12321, 1234321, 123454321])


class TestModDivmod(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(mod_divmod(177, 10), (17, 7, (17, 7)))


class TestPowerModPower(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(power_mod(3, 4, 5), (81, 1))


class TestIntegersComeInAllSizes(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(big_power_sum(9, 29, 7, 27), 4710194409608608369201743232)


if __name__ == "__main__":
    unittest.main()
