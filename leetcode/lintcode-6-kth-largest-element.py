class Solution:

    # @param k & A a integer and an array

    # @return ans a integer

    def kthLargestElement(self, k, A):

        if not A or k < 1 or k > len(A):
            return None

        n = len(A)
        start = 0
        end = n - 1

        # 为了方便编写代码，这里将第 k 大转换成第 k 小问题。
        k = n - k

        return self.partition(A, start, end, k)

    def partition(self, nums, start, end, k):

        """

        During the process, it's guaranteed start <= k <= end

        """

        if start == end:
            return nums[k]

        left, right = start, end

        pivot = nums[(start + end) // 2]

        while left <= right:

            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]

                left, right = left + 1, right - 1

        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)

        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]


if __name__ == '__main__':
    solution = Solution()
    arr = [7, 9, 5, 1, 4]

    print(solution.kthLargestElement(3, arr))
