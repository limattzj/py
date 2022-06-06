from re import I
from typing import List


def removeElement(nums: List[int], val: int) -> int:

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

if __name__ == "__main__":
    removeElement([3,2,2,3], 3)
    # removeElement([0,1,2,2,3,0,4,2], 2)
    removeElement([1], 1)
    removeElement([3, 3], 3)

