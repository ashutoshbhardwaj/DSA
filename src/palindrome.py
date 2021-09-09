"""To check if the provided word is palindrome or not
"""


class PalindromChecker:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]


test_palindrome = """
>>> p = PalindromChecker()
>>> p.is_palindrome('ashu')
False
>>> p.is_palindrome('assa')
True
"""
__test__ = {key: value for key, value in locals().items() if key.startswith("test_")}
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
