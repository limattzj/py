from typing import List

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        # Sort the input array in ascending order
        s.sort()
        # Initialize a variable to keep track of the number of valid triplets
        count = 0
        # Set i to the index of the largest element in s
        i = len(s) - 1

        # Iterate through each element in s from last to first
        while i >= 0:
            # Initialize left and right pointers to the leftmost and rightmost elements of the subarray s[0:i]
            left = 0
            right = i - 1
            
            # Iterate through each pair of elements (s[left], s[right]) in the subarray s[0:i]
            
            while left < right:
                
                # Check if s[left] + s[right] is greater than s[i]    
                # If so, add (right - left) to the count, 
                # since all elements to the left of right also satisfy the triangle inequality

                if s[left] + s[right] > s[i]:
                    
                    count += (right - left)
                    # Decrement right to move it closer to left
                    right -= 1
                else:
                    # If not, increment left to move it closer to right
                    left += 1

            # Decrement i to move to the next largest element in s
            i -= 1
        
        # Return the final value of count as the answer
        return count
