from typing import List

class Solution:

    def partition_array(self, nums: List[int], k: int) -> int:
        """ Given an array nums of integers and an int k, partition the array 
            (i.e move the elements in "nums") such that:
                - All elements < k are moved to the left
                - All elements >= k are moved to the right
            
        Args:
            - nums: The integer array to be partitioned
            - k: The comparator as int, note that k does not have to be in nums

        Returns:
            The first index i such that nums[i] >= k

        Example:
            nums = [3,2,2,1]
            k = 2
            partition array as [1,2,2,3], and return 1 since nums[1] = 2
        """

        # if input array if empty
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # 如果 itemFromLeft 小于 k，不动
            while left <= right and nums[left] < k:
                left += 1
            
            # 如果 itemFromRight 大于等于 k, 不动
            while left <= right and nums[right] >= k:
                right -= 1

            # num[left] >= k or nums[right] < k, then swap
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left

if __name__ == '__main__':

    solution = Solution()
    arr = [3,2,2,1]
    solution.partition_array(arr, 2)
    print(arr)

