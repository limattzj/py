from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find the indices of the two numbers such that they add up to the
    target. We implement using hashtable thus each access should be O(1) and
    overall complexity should be O(n) (at most n access)

    >>> two_sum(nums = [2,7,11,15], target = 9)
    [0, 1]
    >>> two_sum(nums = [3,2,4], target = 6)
    [1, 2]

    Args:
        nums: an array of integers
        target: an integer

    Returns: A list of the two indices which their corresponding value adds
    to the target
    """

    hashmap = {}
    i = 0
    n = len(nums)

    while i < n:
        value = nums[i]  # the current value

        diff = target - value
        # find the difference between the target and the current number

        if diff in hashmap:  # look up in dictionary in O(1)
            # if the difference is in the hash table, return the index of the
            # current number and the index of the diff
            return [hashmap[diff], i]

        # else: the difference not in hash table, then we add to the hash table
        # and go to the next iteration
        hashmap[value] = i
        i += 1


def main():
    """Function that compute the time for the functions

    """
    import timeit

    setup_code1 = """from __main__ import two_sum"""
    stmt_code1 = "two_sum([2, 7, 11, 15], 9)"
    times1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number=100000,
                           repeat=5)

    print(f'Time taken by two_sum is {min(times1)}')


if __name__ == '__main__':
    main()
    # while-loop with 100,000 runs ~= 0.0249
    # enumerated with 100,000 runs ~= 0.0265
