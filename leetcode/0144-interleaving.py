from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        n = len(a)
        neg_count = self.partition(a)
        pos_count = n - neg_count
        
        left = 1 if neg_count > pos_count else 0
        right = n - (2 if pos_count > neg_count else 1)
        self.interleave(a, left, right)
    
    def partition(self, a):
        left = 0
        right = len(a) - 1

        while left <= right:
            while left <= right and a[left] < 0:
                left += 1
            while left <= right and a[right] > 0:
                right -= 1
            
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        
        return left
    
    def interleave(self, a, left, right):
        while left < right:
            a[left], a[right] = a[right], a[left]
            left = left + 2
            right = right - 2



if __name__ == '__main__':

    a = [-33, -19, 30, 26, 21, -9]
    solution = Solution().rerange(a)
    print(a)

