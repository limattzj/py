from typing import List


class Solution:
    """ Find the indices of the two numbers such that they add up to the
        target.

    Args:
        nums: an array of integers
        target: an integer

    Returns:
        A  list of the two indices which their corresponding value adds
        to the target
    """

    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """ We implement using brute force with overall complexity O(n^2)
        """

        i = 0
        n = len(nums)

        while i < n:
            j = i + 1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

    def two_sum_sort(self, nums: List[int], target: int) -> List[int]:
        """ We implement by first sorting the array O(nlogn), and use two pointers
            i going from left to right and j going from right to left.
        """
        # sort the array from small to large and keep the original index
        nums = [(number, i) for i, number in enumerate(nums)]
        nums = sorted(nums)  # O(nlogn)

        # 排序后，两个指针 i, j 从两边往中间移动, and sum = nums[i] + nums[j]
        # if sum > target => j 减 1 
        # if sum < target => i 加 1
        # if sum == target => (i, j) 就是一组 solution

        left = 0
        right = len(nums) - 1
    
        while left < right:
            sum = nums[left][0] + nums[right][0]

            if sum == target:
                return sorted([nums[left][1], nums[right][1]])
    
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        # if not found, return [-1, -1]
        return [-1, -1]

    def two_sum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """ We implement using hashtable thus each access should be O(1) and
            overall complexity should be O(n) (at most n access)
        """

        hashmap = {}
        i = 0
        n = len(nums)

        while i < n:
            value = nums[i]  # the current value

            diff = target - value
            # find the difference between the target and the current number

            if diff in hashmap:  # look up in dictionary in O(1)
                # if the difference is in the hash table, return the index of
                # the current number and the index of the diff
                return [hashmap[diff], i]

            # else: the difference not in hash table, then we add to the hash
            # table and go to the next iteration
            hashmap[value] = i
            i += 1


if __name__ == '__main__':
    
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected_output1 = [0, 1]
    # test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected_output2 = [1, 2]
    
    # test case 3
    nums3 = [3, 3]
    target3 = 6
    expected_output3 = [0, 1]

    assert solution.two_sum_hashmap(nums1, target1) == expected_output1
    assert solution.two_sum_hashmap(nums2, target2) == expected_output2
    assert solution.two_sum_hashmap(nums3, target3) == expected_output3
    assert solution.two_sum_sort(nums1, target1) == expected_output1
    assert solution.two_sum_sort(nums2, target2) == expected_output2
    assert solution.two_sum_sort(nums3, target3) == expected_output3



