from typing import List

class Solution:

    def partition_array(self, nums: List[int], k: int) -> int:
        """ Given an array nums of integers and an int k, partition the array 
            (i.e move the elements in "nums") such that:
                - All elements < k are moved to the left
                - All elements >= k are moved to the right
            
        Args:
            - nums: The integer array you should partition
            - k: The comparator as int

        Returns:
            The first index i such that nums[i] >= k

        Example:
            nums = [3,2,2,1]
            k = 2
            partition array as [1,2,2,3], and return 1 since nums[1] = 2
        """

        A = nums
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            #如果 itemFromLeft 小于 k，放那儿不动
            while left <= right and A[left] < k:
                left += 1
            
            #如果 itemFromRight 大于等于 k, 也放那儿不动
            while left <= right and A[right] >= k:
                right -= 1

            #如果 itermFromLeft 大于 k 或者 itemFromRight 大于k
            #swap
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        return left

if __name__ == '__main__':

    solution = Solution()
    arr = [3,2,2,1]
    solution.partition_array(arr, 2)
    print(arr)

