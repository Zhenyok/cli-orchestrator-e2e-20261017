import unittest

from greeting import greet


class GreetTests(unittest.TestCase):
    def test_ada(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_trims_surrounding_whitespace(self):
        self.assertEqual(greet("  Ada \t\n"), "Hello, Ada!")

    def test_unicode_name(self):
        self.assertEqual(greet(" Zoë "), "Hello, Zoë!")
        self.assertEqual(greet("李雷"), "Hello, 李雷!")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_whitespace_only_name_raises(self):
        with self.assertRaises(ValueError):
            greet(" \t\n ")


if __name__ == "__main__":
    unittest.main()
