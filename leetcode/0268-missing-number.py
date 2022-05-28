from typing import List


def missing_number(nums: List[int]) -> int:
    """Find the missing integer from n distinct numbers in the range [0, n].

    >>> missing_number([3,0,1])
    2
    >>> missing_number([0,1])
    2
    >>> missing_number([9,6,4,2,3,5,7,0,1])
    8

    Args:
        nums: an array of integers from a range 0 to len(nums)

    Returns: The missing integer that should be in the range.
    """
    n = len(nums)

    # compute the sum of [0,n] - the sum of existing number, thus yielding
    # the missing number we are looking for
    return (n*(n+1)//2) - sum(nums)


def main():
    """Function that compute the time for the functions

    """
    import timeit

    setup_code1 = """from __main__ import missing_number"""
    stmt_code1 = "missing_number([9,6,4,2,3,5,7,0,1])"
    times1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number=100000,
                           repeat=5)

    print(f'Time taken by missing_number is { min(times1) }')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # time of missing_number using while-loop to accumulate total = 0.0508
    # time of missing_number using built-in sum() = 0.0196
    main()

