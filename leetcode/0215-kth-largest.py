from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    # split the list into two parts and only heapify the first part
    pq = nums[0:k]

    heapq.heapify(pq)

    # repeatedly perform extract_min and insert, and after n times, the item
    # at the root of the heap would be the k-th largest, the heap invariant is
    # that the heap size always maintained at k.
    for i in range(k, len(nums)):

        # compare the root with the current element, if the current > the root
        # then pop root and add the current element.
        if nums[i] > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, nums[i])

    return pq[0]


if __name__ == '__main__':
    k = findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
    assert k == 5, print('not 5')

    k = findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    assert k == 4, print('not 4')
