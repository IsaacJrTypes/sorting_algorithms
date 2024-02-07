import unittest
import random

"""
Concept
traversing array, selecting min or max of unsorted element, then moving element to sorted section
"""
def selection_sort(arr):
    # Iterate through array
    for i in range(len(arr)) :
        # Assume first index is minimum value
        min_value = i
        # Iterate through array starting one value ahead of outer loop iteration. This loop finds smallest element. 
        for j in range(i + 1, len(arr) ):
            # If j element < min_index element, j becomes new min_index
            if arr[j] < arr[min_value]:
                min_value = j
        # If min_value not same as i iteration, swap values 
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr
"""
Unit Tests
"""
class testing_methods(unittest.TestCase):
    def test_random_array_int(self):
        entries = 100
        randomArr = [ random.randint(1,100) for entry in  range(entries)]
        expectedArr = sorted(randomArr)
        self.assertEqual(selection_sort(randomArr),expectedArr)

        
    def test_sorted_ascending(self):
        arr = [1,2,3,4,5,6,7,8]
        expected = sorted(arr)
        self.assertEqual(selection_sort(arr),expected)

       

    def test_sorted_descending(self):
        arr = [8,7,6,5,4,3,2,1]
        expected = sorted(arr)
        self.assertEqual(selection_sort(arr), expected)
        

    def test_elements_identical(self):
        arr = [6,6,6,6,6]
        expected = sorted(arr)
        self.assertEqual(selection_sort(arr),expected)
        

    def test_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(selection_sort(arr),expected)
        

    def test_one_element(self):
        arr = [1]
        expected = [1]
        self.assertEqual(selection_sort(arr),expected)
        

    def test_negative_nums(self):
        arr = [-1,-6,-7,-3,-9,-2]
        expected = sorted(arr)
        self.assertEqual(selection_sort(arr),expected)
        

    def test_string_nums(self):
        arr = ['1','6','3','2']
        expected = sorted(arr)
        self.assertEqual(selection_sort(arr),expected)
        

if __name__ == '__main__':
    unittest.main()