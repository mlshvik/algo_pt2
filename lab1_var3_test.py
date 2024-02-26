import unittest
import sys

sys.path.append("D:\\унік\\лаби\\lab1_var3.py")
from lab1_var3 import find_kth_element

class TestFindKthElement(unittest.TestCase):

    def test_find_kth_element(self):
        array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 4
        result_value, result_index = find_kth_element(array, k)
        self.assertEqual(result_value, 18)
        self.assertEqual(result_index, 7)

    def test_find_kth_element_with_smaller_array(self):
        array = [5, 3]
        k = 1
        result_value, result_index = find_kth_element(array, k)
        self.assertEqual(result_value, 5)
        self.assertEqual(result_index, 0)

    def test_find_kth_element_with_repeated_elements(self):
        array = [5, 5, 5, 5, 5]
        k = 3
        result_value, result_index = find_kth_element(array, k)
        self.assertEqual(result_value, 5)
        self.assertEqual(result_index, 0)  

if __name__ == '__main__':
    unittest.main()