# Count the number of Duplicates
#
# Write a function that will return
# the count of distinct case-insensitive
# alphabetic characters and numeric digits
# that occur more than once in the input string.
# The input string can be assumed to contain
# only alphabets (both uppercase and lowercase)
# and numeric digits.
#
# Example: "aabBcde" -> 2
# 'a' occurs twice and 'b' twice (bandB)
#

from unittest import TestCase


def duplicate_count(text):

    lower_text_list = [letter.lower() for letter in text]

    duplicates = [letter for letter in lower_text_list if lower_text_list.count(letter) > 1]

    return len(set(duplicates))


class DuplicateTest(TestCase):
    def test_no_duplicates(self):
            self.assertEqual(duplicate_count("abcde"), 0)

    def test_one_duplicate(self):
            self.assertEqual(duplicate_count("indivisibility"), 1)

    def test_multiple_duplicates(self):
            self.assertEqual(duplicate_count("abcBdea"), 2)