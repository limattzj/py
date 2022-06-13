from typing import List
from collections import defaultdict


def containsDuplicate_v1(nums: List[int]) -> bool:
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


def containsDuplicate_v2(nums: List[int]) -> bool:
    """A function check whether every element of the array is distinct.

    Args:
        nums: an array of integers

    Returns:
        True if any value appears at least twice in the array. Else False.
    """

    set_seq = set(nums)

    return len(set_seq) != len(nums)


def containsDuplicate_v3(nums: List[int]) -> bool:
    d = defaultdict()

    for num in nums:
        if num in d:
            return True
        else:
            d[num] = 0

    return False


def main():
    import timeit

    setup_code1 = """from __main__ import containsDuplicate_v1"""
    stmt_code1 = "containsDuplicate_v1(nums = [1,1,1,3,3,4,3,2,4,2])"
    times1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number=100000,
                           repeat=5)

    print(f'Time taken by containsDuplicate_v1 is {min(times1)}')

    setup_code1 = """from __main__ import containsDuplicate_v3"""
    stmt_code1 = "containsDuplicate_v3(nums = [1,1,1,3,3,4,3,2,4,2])"
    times1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number=100000,
                           repeat=5)

    print(f'Time taken by containsDuplicate_v3 is {min(times1)}')


if __name__ == "__main__":
    main()
