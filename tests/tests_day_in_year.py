import unittest
from day_in_year import DayInYear


class TestDayInYear(unittest.TestCase):
    """TestDayInYear."""

    def test_instance_day_in_year(self):
        day_year = DayInYear(2022, 6, 17)
        self.assertIsInstance(day_year, DayInYear)

    def test_exception_set_args_year_string(self):
        with self.assertRaises(Exception):
            DayInYear('7', 2, 3)

    def test_exception_set_args_day_float(self):
        with self.assertRaises(Exception):
            DayInYear(2022, 6, float(2))

    def test_exception_set_args_year_less_than_1970(self):
        with self.assertRaises(Exception):
            DayInYear(1969, 2, 3)

    def test_exception_set_arg_month_less_than_1(self):
        with self.assertRaises(Exception):
            DayInYear(1970, 0, 1)

    def test_exception_set_arg_month_greater_than_12(self):
        with self.assertRaises(Exception):
            DayInYear(1970, 13, 2)

    def test_exception_set_arg_day_less_than_1(self):
        with self.assertRaises(Exception):
            DayInYear(1970, 1, 0)

    def test_exception_set_arg_day_greater_than_31(self):
        with self.assertRaises(Exception):
            DayInYear(1970, 2, 32)

    def test_exception_set_arg_day_out_range_for_month(self):
        with self.assertRaises(Exception):
            DayInYear(2023, 2, 29)

    def test_property_date_in_the_year_to_int(self):
        day_in_year = DayInYear(2022, 1, 12)
        self.assertEqual(day_in_year.date_in_the_year_to_int, 12)

        day_in_year = DayInYear(2024, 12, 31)
        self.assertEqual(day_in_year.date_in_the_year_to_int, 366)

        day_in_year = DayInYear(2023, 12, 31)
        self.assertEqual(day_in_year.date_in_the_year_to_int, 365)


if __name__ == '__main__':
    unittest.main()
