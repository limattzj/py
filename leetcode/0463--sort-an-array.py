from typing import (
    List,
)


class Solution:

    def sortIntegers(self, A):

        if A is None or len(A) == 0:
            return

        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        """ QuickSort algorithm using a recursive approach.

        :param nums: List of integers to be sorted
        :param start: Starting index of the sublist to be sorted
        :param end: Ending index of the sublist to be sorted

        :return: None
        """
        
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:

            if A[left] < pivot:
                left += 1
                continue

            if A[right] > pivot:
                right -= 1
                continue

            A[left], A[right] = A[right], A[left]
            print(A)
            left += 1
            right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


if __name__ == '__main__':
    solution = Solution()
    arr = [2, 6, 5, 3, 8, 7, 1, 0]

    solution.sortIntegers(arr)
    print(arr)
