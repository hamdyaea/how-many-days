# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from datetime import date
import unittest
from HowManyDays import days_lived

class DaysTests(unittest.TestCase):
    def test_known_dates(self):
        self.assertEqual(days_lived(date(2000, 1, 1), date(2000, 1, 2)), 1)
        self.assertEqual(days_lived(date(2000, 2, 28), date(2000, 3, 1)), 2)
    def test_same_day(self):
        self.assertEqual(days_lived(date(2020, 1, 1), date(2020, 1, 1)), 0)
    def test_future_rejected(self):
        with self.assertRaises(ValueError):
            days_lived(date(2030, 1, 1), date(2026, 1, 1))

if __name__ == "__main__":
    unittest.main()
