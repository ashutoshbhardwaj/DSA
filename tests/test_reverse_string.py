import unittest
from src.reverse_string import reverse_list


class TestReverse(unittest.TestCase):
    def test_multiple_of_three(self):
        self.assertListEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
