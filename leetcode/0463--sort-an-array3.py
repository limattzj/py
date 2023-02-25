# Merge Sort

class Solution:

    def sortIntegers(self, A):

        if A is None or len(A) == 0:
            return

        tmp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, tmp)

    def mergeSort(self, A, start, end, tmp):

        if start >= end:
            return

        self.mergeSort(A, start, (start + end) // 2, tmp)
        self.mergeSort(A, (start + end) // 2 + 1, end, tmp)
        self.merge(A, start, end, tmp)

    def merge(self, nums, start, end, tmp):

        mid = (start + end) // 2

        left = start
        right = mid + 1
        index = left

        # merge two halves of the array
        while left <= mid and right <= end:

            # if element on the left is smaller or equal, then copy it
            # temporary array and increment left pointer
            if nums[left] <= nums[right]:
                tmp[index] = nums[left]
                left += 1

            # otherwise element on right is smaller, then copy it to
            # temporary array and increment right pointer
            else:
                tmp[index] = nums[right]
                right += 1

            # increment the index pointer
            index += 1

        # copy the remaining elements from left half of the array to
        # the temporary array
        while left <= mid:
            tmp[index] = nums[left]
            index += 1
            left += 1

        # copy the remaining elements from right half of the array to
        # the temporary array
        while right <= end:
            tmp[index] = nums[right]
            index += 1
            right += 1

        # Copy the sorted elements from the temporary array back
        # to the original array
        for index in range(start, end + 1):
            nums[index] = tmp[index]


if __name__ == '__main__':
    solution = Solution()
    arr = [2, 8, 5, 3, 9, 4, 1, 7]

    solution.sortIntegers(arr)
    print(arr)
