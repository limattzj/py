from typing import List, Tuple


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

            elif total > 0:
                k -= 1

            else:  # total < 0
                j += 1
    return res


if __name__ == '__main__':
    # result = threeSum(nums=[-1, 0, 1, 2, -1, -4])
    # result = threeSum(nums=[0, 0, 0, 0])
    result = threeSum(
        nums=[34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21,
              -43, 57, -6, 86, 56, 94, 74, 83, -14, 28, -66, 46, -49, 62, -11,
              43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29,
              36, -29, 10, -70, 69, 17, 49]
    )
    print(result)
