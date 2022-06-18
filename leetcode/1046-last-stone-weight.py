from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    # init a max heap with all stones
    stones = [-i for i in stones]
    heapq.heapify(stones)
    # print(stones)
    # while length of array > 1, extract 2 largest stones.

    while len(stones) > 1:
        # let x be the first item extracted, and y be the second item
        # then we know that x >= y.
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)

        if x != y:
            #   if x != y, then x - y and put back into heap
            temp = x - y
            heapq.heappush(stones, temp)
        else:
            #   if x == y, then continue to next iteration.
            continue

    return -stones[0] if len(stones) >= 1 else 0


if __name__ == '__main__':
    x = lastStoneWeight(stones=[2, 7, 4, 1, 8, 1])
    print(x)

    x = lastStoneWeight(stones=[1])
    print(x)

