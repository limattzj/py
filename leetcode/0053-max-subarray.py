from typing import List


def maxSubArray(nums: List[int]) -> int:
    """Find the max sum of the contiguous subarray.

    Args:
        nums: an array of positive or negative integers

    Returns:
        the largest sum of the contiguous array

    Tags:
        - dynamic programming
        - Kadane Algorithm
        - divide and conquer

    """

    # before the loop, set both local_max and global_max to the first element
    # of the array
    max_curr = nums[0]
    max_global = nums[0]

    # starting from the second element to the end.
    for i in nums[1:]:
        # the largest of the local_max or the （local_max + current element）
        max_curr = max(i, max_curr + i)

        # update the global_max
        if max_curr > max_global:
            max_global = max_curr

    return max_global


if __name__ == '__main__':
    x = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert x == 6, f'{x} not equal to 6'

    x = maxSubArray([1])
    assert x == 1, f'{x} not equal to 1'

    x = maxSubArray([5, 4, -1, 7, 8])
    assert x == 23, f'{x} not equal to 23'

    x = maxSubArray([2, -1, 2])
    assert x == 3, f'{x} not equal to 33'
