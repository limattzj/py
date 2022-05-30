from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """A function that remove duplicate (in-place) of a sorted non-decreasing
    array.

    Args:
        nums: an array of integers in sorted non-decreasing order.

    Returns:
        an integer k such that the index up to k contains no duplicates.

    Precondition:
        - nums is sorted in non-decreasing order.
        - -100 <= nums[i] <= 100
        - 1 <= nums.length <= 3 * 10^4

    """

    i = 0
    j = 1
    n = len(nums)

    while j < n:
        if nums[i] < nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1

    return i + 1
