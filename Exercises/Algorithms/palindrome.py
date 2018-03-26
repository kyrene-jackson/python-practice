# Write a function that returns True
# if the word is a palindrome
from unittest import TestCase


def is_a_palindrome(word):
    word = word.lower()
    reversed_word = reversed(word)
    if list(word) == list(reversed_word):
        return True
    else:
        return False


class PalindromeTest(TestCase):
    def test_is_a_palindrome_same_case(self):
        self.assertEqual(is_a_palindrome("racecar"), True)

    def test_is_a_palindrome_mixed_case(self):
        self.assertEqual(is_a_palindrome("RaCeCaR"), True)

    def test_is_not_a_palindrome(self):
        self.assertEqual(is_a_palindrome("dinosaur"), False)
