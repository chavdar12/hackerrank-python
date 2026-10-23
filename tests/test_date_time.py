import unittest

from solutions.date_time.calendar_module import weekday_name
from solutions.date_time.time_delta import time_delta


class TestCalendarModule(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(weekday_name(8, 5, 2015), "WEDNESDAY")


class TestTimeDelta(unittest.TestCase):
    def test_same_instant_different_zones(self):
        self.assertEqual(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"), "25200")

    def test_across_years(self):
        self.assertEqual(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"), "88200")


if __name__ == "__main__":
    unittest.main()
