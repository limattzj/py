class Node:

    def __init__(self, min_left=1000000, min_right=1000000, min_sum=1000000, total_sum=1000000):
        self.min_sum = min_sum
        self.min_left = min_left
        self.min_right = min_right
        self.total_sum = total_sum

def minSubarraySum(A):

    if len(A) == 1: 
        return Node(A[0], A[0], A[0], A[0])

    mid = len(A) // 2

    left = minSubarraySum(A[:mid])
    right = minSubarraySum(A[mid:])
    
    result = Node()

    result.min_left = min(left.min_left, 
                        left.total_sum+right.min_left, 
                        left.total_sum+right.total_sum)

    result.min_right = min(right.min_right, 
                            right.total_sum + left.min_right, 
                            left.total_sum+right.total_sum)

    result.total_sum = left.total_sum + right.total_sum

    result.min_sum = min(left.min_sum, 
                        right.min_sum, 
                        left.min_right + right.min_left,
                        result.total_sum,
                        result.min_left,
                        result.min_right,
                        )

    return result

ar = [-2,1,-3,4,-1,2,1,-5,4]
n = len(ar)
ans = minSubarraySum(ar)
print(ans.min_sum)
