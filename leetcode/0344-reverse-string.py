from typing import List


def reverseString(s: List[str]) -> None:
    """A function that reserves a string using the opposite directional
    two-pointer approach (in-place)

    Args:
        s: an array of characters.

    Returns:
        None.

    Preconditions:
        - 1 <= s.length <= 10^5

    >>> s = ["h","e","l","l","o"]
    >>> reverseString(s)
    >>> assert s == ["o","l","l","e","h"], "reverse Incorrectly"


    """

    # let i be the pointer to the first element of s and j be the pointer to
    # the last element of s
    i = 0
    j = len(s) - 1

    while i < j:

        # simultaneous assignment, the expression on the right side are all
        # evaluated before any new values are assigned.
        s[i], s[j] = s[j], s[i]

        # at end of each iteration, i increment by one (points to the next
        # element), while j decrement by one (points to the previous element)
        i += 1
        j -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
