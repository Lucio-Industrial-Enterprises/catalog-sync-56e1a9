import unittest

from warehouse.quantity import parse_quantity


class ParseQuantityTests(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(parse_quantity("3"), 3)

    def test_strips_whitespace(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("0")

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-5")

    def test_non_numeric_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("abc")
