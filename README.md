# Table of Contents
1. [Bubble Sort Report](#bubble-sort-report)
1. [Selection Sort Report](#selection-sort-report)
1. [Insertion Sort Report](#insertion-sort-report)

# Bubble Sort Report

## Observations

- The optimized version of bubble sort uses a boolean flag to detect if a swap occurred. If a value is found to be unsorted, we swap the values and assign sorted to False. This allows for continuous iteration of sorting the array until no swap are detected. Once sorted stays false, meaning all elements are sorted, the loop will terminate right away. Using the while loop to detect if array is sorted allows the algorithm to terminate early if a portion of the array is already sorted.
- The outer loop in the un-optimized version will force the algorithm to iterate every element, even if array is partially sorted.
- Differences in regular vs optimized code of bubble sort made an observable impact in performance testing

## Unit Tests

- Performance testing using libraries: `unittest` and `timeit`

| Test Case               | Observations                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Random Numbers          | Testing random array of integers. Optimized won performance test.                        |
| Sorted Ascending Array  | Testing an array already sorted in ascending order. Optimized won performance test.      |
| Sorted Descending Array | Testing an array sorted in descending order. Optimized won performance test.             |
| Elements Identical      | Testing an array where all elements are identical. Optimized won performance test.       |
| Empty Array             | Testing edge case: an empty array. No significant performance difference                 |
| Array with One Element  | Testing edge case: an array with a single element. No significant performance difference |
| Negative Numbers        | Testing an array with negative numbers. Optimized won performance test                   |
| String Numbers          | Testing an array of strings representing numbers. Optimized won performance test         |

## Final Thoughts

- The Space complexity of does not change in optimized version. Since both algorithms are swapping elements using variables, space complexity stays at O(1). Time complexity at best can be O(n) but the average to worst will be O(n^2)
- The algorithm allow repeated elements to stay relatively in order. This feature makes bubble sort stable which can be an important factor depending on the context of a problem.

# Selection Sort Report

## Observations

- Selection sort places either the minimum or maximum value at the beginning of the list. As the outer loop iterates, the inner loop will start from outer loop's index and iterate till a value is smaller than outer loop's value. This causes two sub-lists to emerge. As the algorithm runs, the left side of outer iterator will be sorted while the right side will be unsorted.

## Unit Tests

- Performance testing using library: `unittest`

| Test Case               | Observations                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Random Numbers          | Testing random array of integers.                                                        |
| Sorted Ascending Array  | Testing an array already sorted in ascending order. Optimized won performance test.      |
| Sorted Descending Array | Testing an array sorted in descending order.                                             |
| Elements Identical      | Testing an array where all elements are identical.                                       |
| Empty Array             | Testing edge case: an empty array. No significant performance difference                 |
| Array with One Element  | Testing edge case: an array with a single element. No significant performance difference |
| Negative Numbers        | Testing an array with negative numbers.                                                  |
| String Numbers          | Testing an array of strings representing numbers.                                        |

## Final Thoughts

- Since the algorithm is creating a sorted list in place as it iterates, it is much more efficient at sorting. The time complexity will still stay O(n^2). Space complexity will be O(1) since we are sorting in place
- The algorithm is not stable as repeated numbers will not stay in relative order.

# Insertion Sort Report

## Observations

- Insertion sort is a very interesting algorithm. I found it more difficult to implement than the other algorithms. This algorithm like the bubble sort is stable which keeps the order of repeated elements relative to each other.

## Unit Tests

- Performance testing using library: `unittest`

| Test Case             | Observations                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| Small Random Numbers  | Testing small random array of integers. Performed well over the other two speed tests.                    |
| Large Random Numbers  | Testing Large random array of integers. Performed worst over the other two speed tests.                   |
| Random Size of Arrays | Testing random size of array with random integers. Performed right between the the other two speed tests. |
| Stability             | Testing algorithms ability to retain relative order of repeated numbers. Passed stability test.           |

## Final Thoughts

- The algorithm performed vastly different with large and small sized arrays. Compared to the other algorithms, implementation is trickier, yet it tends to perform faster than the other two.
- Time complexity at best is O(n) and O(n^2) at average to worst. The Space complexity like the others stays at O(1) because only variables are used to sort in-place.
- Since insertion sort and selection sort perform at best case time complexity O(n), insertion's ability to be stable makes this algorithm the best out of all three I covered.  
- It is not surprising why insertion sort is used in merge sort for a hybrid approach to sorting. Merge sort can break down the array to smaller sub-arrays and apply insertion sort to the sub-arrays. Creative mix of sorting techniques to help come up with an efficient solution.