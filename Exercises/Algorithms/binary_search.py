# Given a sorted array arr[] of n elements,
# write a function to search a given element x in arr[]
# if the element is in the array return True otherwise return False

from unittest import TestCase

def binary_search(element, arr):

    if len(arr) == 0:
        return False
    else:
        middle = len(arr) // 2

        if element == arr[middle]:
            return True
        else:
            if element > arr[middle]:
                return binary_search(element, arr[middle + 1:])
            else:
                return binary_search(element, arr[:middle])


class BinarySearchTest(TestCase):

    def test_element_in_array(self):

        array = [1, 6, 9, 14, 20]
        element = 20

        self.assertEqual(binary_search(element, array), True)

    def test_element_not_in_array(self):

        array = [1, 6, 9, 14, 20, 99, 101, 36]
        element = 37

        self.assertEqual(binary_search(element, array), False)


