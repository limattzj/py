from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []

    # find out the shortest of the two arrays

    shorter = nums1
    longer = nums2

    if len(nums1) > len(nums2):
        shorter = nums2
        longer = nums1

    # turn the shorter into a hashmap with key = element, and value = count
    hashmap = {}

    for element in shorter:
        if element in hashmap:  # if element already exist, then increment count
            hashmap[element] += 1
        else:
            # if the element not exist yet, add the element, and set the
            # count to 1
            hashmap[element] = 1

    # loop over the over array
    for item in longer:
        if item in hashmap and hashmap[item] > 0:
            # evaluates to True if the element is intersection of nums1 and
            # nums2 and the count of the item > 0
            res.append(item)
            hashmap[item] -= 1  # decrement the count by 1

    return res


if __name__ == '__main__':
    x = intersect([1, 2, 2, 1], nums2=[2, 2])
    print(x)

    x = intersect([4, 9, 5], nums2=[9, 4, 9, 8, 4])
    print(x)

    x = intersect([1, 2], nums2=[1, 1])
    print(x)

    x = intersect([3, 1, 2], nums2=[1, 1])
    print(x)
