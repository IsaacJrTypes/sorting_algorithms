import unittest
import random
import timeit
"""
Concept

For each element in the array (starting from the second):
	Compare this element to the ones before it, moving each one step to the right until
finding the correct position for the element.
Insert the element in its correct position.
"""

def insertion_sort(arr):
    # Iterate through list, starting from second element
    for i in range(1, len(arr)):
        # Iteration values for comparison
        curr_value = arr[i]
        position = i
        # While elements before position are > curr, 
        while position > 0 and arr[position-1] >  curr_value:
            # Move greater value to current position
            arr[position] = arr[position-1]
            # Move left, loop if value left of position greater
            position -= 1
        #else, update smaller curr value to position of current iteration
        arr[position] = curr_value

    return arr
"""
Unit Tests
Create a set of test arrays with varying characteristics: [x] a small array, 
[x] a large array, 
[x] a nearly sorted array
[x] reversed array.
"""
class testing_methods(unittest.TestCase):
    def test_small_random_array_int(self):
        entries = 10
        randomArr = [ random.randint(1,100) for entry in  range(entries)]
        expectedArr = sorted(randomArr)
        self.assertEqual(insertion_sort(randomArr),expectedArr)

        # Test Execution Speed
        time = timeit.repeat(lambda:insertion_sort([ random.randint(1,100) for entry in  range(entries)]),number=1,repeat=5)
        print("Average execution of small arrays",len(time),"runs: ",sum(time)/len(time))
        
    
    def test_large_random_array_int(self):
        entries = 1000
        randomArr = [ random.randint(1,100) for entry in  range(entries)]
        expectedArr = sorted(randomArr)

        # Time Execution Speed
        self.assertEqual(insertion_sort(randomArr),expectedArr)
        time = timeit.repeat(lambda:insertion_sort([ random.randint(1,100) for entry in  range(entries)]),number=1,repeat=5)
        print("Average execution of large arrays",len(time),"runs: ",sum(time)/len(time))
   
    def test_random_size_array_int(self):
        
        # Time Execution Speed
        time = timeit.repeat(lambda:insertion_sort([ random.randint(1,100) for entry in  range(random.randint(10,100))]),number=1,repeat=5)
        print("Average execution of random sized arrays",len(time),"runs: ",sum(time)/len(time))


    def test_sorted_descending(self):
        arr = [8,7,6,5,4,3,2,1]
        expected = sorted(arr)
        self.assertEqual(insertion_sort(arr), expected)
        

    def test_nearly_sorted(self):
        arr = [1,8,6,9,7]
        expected = sorted(arr)
        self.assertEqual(insertion_sort(arr),expected)

    def test_stability(self):
        arr = [(1,'a'),(4,'a'),(1,'b'),(4,'b'),(3,'a'),(6,'a')]
        expected = [(1, 'a'), (1, 'b'), (3, 'a'), (4, 'a'), (4, 'b'), (6, 'a')]
        self.assertEqual(insertion_sort(arr),expected)
        

if __name__ == '__main__':
    unittest.main()