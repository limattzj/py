from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """A function check whether every element of the array is distinct.

    Args:
        nums: an array of integers

    Returns:
        True if any value appears at least twice in the array. Else False.
    """

    hashmap = {}

    for i, value in enumerate(nums):
        if value in hashmap:
            return True
        else:
            # i not in hashmap => put i in the hashmap
            hashmap[value] = i

    return False
