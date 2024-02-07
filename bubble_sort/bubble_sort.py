import unittest
import random
import timeit
"""
Bubble Sort Implementation 

Concept: 
    Repeat until no swap
        for each pair of adjacent element:
            if left > right:
                swap them
    
"""
def bubble_sort(arr):
    # Get end of array
    n = len(arr) 
    # Loop every element except last element since last element is sorted 
    for i in range(n-1):
        # For each iteration of i, traverse every element except last for comparison 
        for j in range(n-1):
            # Compare if j > the next element of j
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

def optimized_bubble_sort(arr):
    # Get length of array
    n = len(arr)
    # Assume not sorted
    sorted = False
    # While not sorted, keep iterating for sorting
    while not sorted:
        # Assume sorted to break loop early
        sorted = True
        # Iterate through every element, except last sorted element
        for i in range(n - 1):
            # If i element > i element ahead, swap and array not sorted
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                sorted = False
    return arr



# print(bubble_sort([5,4,3,2,1]))
# print(optimized_bubble_sort([5,4,3,2,1]))


"""
Testing

[x] A randomly generated array of integers.
[x] An array that is already sorted in ascending order, to test the best-case scenario.
[x] An array sorted in descending order, to assess the worst-case scenario.
[x] An array where all elements are identical, to examine the algorithm's behavior with uniform input.
[x] Edge cases, such as an empty array and a single-element array.
"""
class testing_methods(unittest.TestCase):
    def test_random_array_int(self):
        entries = 100
        randomArr = [ random.randint(1,100) for entry in  range(entries)]
        expectedArr = sorted(randomArr)
        self.assertEqual(bubble_sort(randomArr),expectedArr)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(randomArr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(randomArr),number=1)
        self.assertLess(optimized_time,reg_time)
        
    def test_sorted_ascending(self):
        arr = [1,2,3,4,5,6,7,8]
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_sorted_descending(self):
        arr = [8,7,6,5,4,3,2,1]
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr), expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_elements_identical(self):
        arr = [6,6,6,6,6]
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_one_element(self):
        arr = [1]
        expected = [1]
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_negative_nums(self):
        arr = [-1,-6,-7,-3,-9,-2]
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

    def test_string_nums(self):
        arr = ['1','6','3','2']
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr),expected)

        # Test Execution Speed
        optimized_time = timeit.timeit(lambda:optimized_bubble_sort(arr),number=1)
        reg_time = timeit.timeit(lambda:bubble_sort(arr),number=1)
        self.assertLess(optimized_time,reg_time)

if __name__ == '__main__':
    unittest.main()