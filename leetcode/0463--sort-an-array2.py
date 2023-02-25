from typing import (
    List,
)


class Solution:

    def sort_integers(self, a: List[int]):
        """
       @param a: an integer array
       @return: nothing
       """
        self.quickSort(a, 0, len(a) - 1)

    def quickSort(self, arr, start, end):
        """ QuickSort algorithm using a recursive approach.

       :param arr: List of integers to be sorted
       :param start: Starting index of the sublist to be sorted
       :param end: Ending index of the sublist to be sorted

       :return: None
       """
        if start >= end:
            return
        # find the pivot, and partition elements left of pivot to be smaller
        # than pivot, elements right of pivot to be larger than pivot.
        # then recursively sort left_subarray and right_subarray

        pivot_index = self.partition(arr, start, end)
        self.quickSort(arr, start, pivot_index - 1)
        self.quickSort(arr, pivot_index + 1, end)

    def partition(self, arr, start, end):
        """ Partitions list by selecting a pivot and rearranging the elements

        :param arr: List of integers to be sorted
        :param start: Starting index of the sublist to be partitioned
        :param end: Ending index of the sublist to be partitioned

        :return: Final index of the pivot element after partitioning
        """

        pivot = arr[start]

        left = start + 1
        right = end

        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1

            while left <= right and arr[right] > pivot:
                right -= 1

            # if arr[left] > pivot or arr[right] < pivot, then swap
            # and bring closer both ptrs
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            # left += 1
            # right -= 1

        # swap pivot into appropriate place
        arr[start], arr[right] = arr[right], arr[start]

        return right
