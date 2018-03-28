# DISEMVOWEL
#
# Your task is to write a function that takes a string and
# return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become
# "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

from unittest import TestCase


def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    string_list = list(string)

    vowels_in_string = [letter for letter in string if letter.lower() in vowels]

    for letter in string_list:
        if letter in vowels_in_string:
            string_list.remove(letter)
    return "".join(string_list)


class DisemvowelTest(TestCase):
    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"),
                           "Ths wbst s fr lsrs LL!")