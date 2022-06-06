import heapq


def kth_largest(a, k):

    # split the list into two parts and only heapify the first part
    pq = a[0:k]

    heapq.heapify(pq)
    print(pq)

    # repeatedly perform extract_min and insert, and after n times, the item
    # at the root of the heap would be the k-th largest, the heap invariant is
    # that the heap size always maintained at k.
    for i in range(k, len(a)):

        # compare the root with the current element, if the current > the root
        # then pop root and add the current element.
        if a[i] > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, a[i])

    return pq[0]


if __name__ == '__main__':
    x = kth_largest([2, 1], 2)  # expected 1
    print(x)
