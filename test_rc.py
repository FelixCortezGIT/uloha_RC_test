import unittest
from main import validate


class TestRCValidator(unittest.TestCase):
    def test_valid_rc(self):
        self.assertEqual(validate("8004309412"))
    def test_invalid_date(self):
        self.assertFalse(validate("9913320000"))
    def test_invalid_length(self):
        self.assertFalse(validate("010101000"))
    def test_not_divide_by_11(self):
        self.assertFalse(validate("0101010001"))
    def test_female_rc(self):
        self.assertTrue(validate("0151010000"))
    def test_non_numeric(self):
        self.assertFalse(validate("abcd123456"))


if __name__ == '__main__':
    unittest.main()
