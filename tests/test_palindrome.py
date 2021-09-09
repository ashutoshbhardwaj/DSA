import unittest
from src.palindrome import PalindromChecker


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        p = PalindromChecker()
        self.assertFalse(p.is_palindrome("Ashutosh"))
        self.assertTrue(p.is_palindrome("AssA"))
