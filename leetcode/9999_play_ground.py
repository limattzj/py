from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        """Three approaches:
        Brute-force: O(n^2)
        two pointers: O(n*logn)
        hashmap: O(n)
        """

        # list of tuple (number, index)
        nums = [(number, index) for index, number in enumerate(numbers)]

        # sort in O(n*logn), and old indices can still be accessed
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            two_sum = nums[left][0] + nums[right][0]
            if two_sum == target:
                return sorted([nums[left][1], nums[right][1]])
            elif two_sum > target:
                right -= 1
            else:
                left += 1
        
        return [-1, -1]

        
if __name__ == '__main__':

    A = [15,2,7,11]
    result = Solution().two_sum(A, 9)
    print(result)
