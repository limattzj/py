from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    i = 0
    j = len(nums) - 1

    while i <= j:
        p = (i + j) // 2

        if nums[p] == target:
            return p

        if target < nums[p]:
            j = p - 1
        else:
            i = p + 1

    return i


if __name__ == '__main__':
    x = searchInsert(nums=[1, 3, 5, 6], target=5)
    y = searchInsert(nums=[1, 3, 5, 6], target=2)
    z = searchInsert(nums=[1, 3, 5, 6], target=7)
    a = searchInsert(nums=[1, 3, 5, 6], target=0)
    b = searchInsert(nums=[1, 3], target=0)
    c = searchInsert(nums=[3, 5, 7, 9, 10], target=8)
    d = searchInsert(nums=[1, 2, 7, 8, 10, 11, 12], target=9)

    print(d)