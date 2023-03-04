from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        """Given two sorted A, B
        A:[     ] 
        B:[     ]
        initialize two pointers, left & right such that left points at 
        first index of A, and right points at first index of B.
        iterate over two arrays at the same time and compare a[left] with b[right], 
        and put the smaller element into result, and increment that pinter.

        loop invariant (left <= len(A) - 1) and (right <= len(B) -1)

        Time complexity: O(n+m)
        Space complexity: O(n+m) since we need a new array result.
        """

        n = len(a)
        m = len(b)
        result = [0] * (len(a) + len(b))
        left = 0   # used to point at a
        right = 0  # used to point at b
        index = 0  # used to point at result

        while left <= n - 1 and right <= m - 1:
            if a[left] <= b[right]:
                result[index] = a[left]
                left += 1
            else: # a[left] > b[right]
                result[index] = b[right]
                right += 1
            
            index += 1
        
        # after the while loop at line 33, one of array a or b is exhausted.
        # we need add the rest of the elemnents from a or b into result
        while left <= n - 1:
            result[index] = a[left]
            index += 1
            left += 1
        
        while right <= m - 1:
            result[index] = b[right]
            index += 1
            right += 1
        
        return result




