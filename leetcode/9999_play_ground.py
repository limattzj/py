from typing import (
    List,
)

class Solution:
    def sort_colors(self, nums):
        self.partition_zeros(nums, 0, 0, len(nums) - 1)

    def partition_zeros(self, nums, k, start, end):
        """ Partition zeroes to the beginning of the array 

        [1, 0, 2, 0, 2] -> [0, 0, 2, 2, 1] or something equivalent
        """
        if start >= end:
            return
    
        left = start
        right = end

        while left <= right:
            while left <= right and nums[left] == k:
                left += 1
            
            while left <= right and nums[right] > k:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        self.partition_zeros(nums, k + 1, left, end)
        
if __name__ == '__main__':

    A = [1, 0, 2, 0, 2]
    result = Solution().sort_colors(A)
    print(A)
