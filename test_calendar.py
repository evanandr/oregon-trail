from unittest import TestCase
from oregon import Calendar
from datetime import date
from datetime import timedelta


class TestCalendar(TestCase):
    def test_construction(self):
        cal = Calendar()
        self.assertFalse(cal.is_final_turn())
        self.assertEqual(cal.date, date(2016, 3, 29))
        self.assertEqual(cal.total_turn_count, 18)

    def test_advance_date(self):
        cal = Calendar()
        cal.advance_date()
        self.assertEqual(cal.date, date(2016, 3, 29) + timedelta(days=14))

    def test_rollback_date(self):
        cal = Calendar()
        cal.rollback_date(1)
        self.assertEqual(cal.date, date(2016, 3, 29) - timedelta(days=1))

    def test_is_final_turn(self):
        cal = Calendar()
        for i in range(1, cal.total_turn_count):
            cal.advance_date()
        self.assertEqual(cal.date, date(2016, 11, 22))
        self.assertTrue(cal.is_final_turn())
