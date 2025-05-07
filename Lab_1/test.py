import unittest
from mycode import *


class TestString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_single_string(self):
        self.assertEqual(Add("1"), 1)

    def test_double_string(self):
        self.assertEqual(Add("2,3"), 5)
        self.assertEqual(Add("3,4"), 7)

    def test_multiple_strings(self):
        self.assertEqual(Add("1,2,3"), 6)

    def test_lines_string(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
