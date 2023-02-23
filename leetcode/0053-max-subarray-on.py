class Node:

    def __init__(self, x):
        self.max_sum = x
        self.max_prefix = x
        self.max_suffix = x
        self.total_sum = x

# Function to merge the 2 nodes left and right
def merg(left, right):

    # Creating node ans
    ans = Node(0)

    # The max prefix sum of ans Node is maximum of
    # a) max prefix sum of left Node
    # b) sum of left Node + max prefix sum of right Node
    # c) sum of left Node + sum of right Node
    ans.max_prefix = max(left.max_prefix, 
                        left.total_sum+right.max_prefix, 
                        left.total_sum+right.total_sum)

    # The max suffix sum of ans Node is maximum of
    # a) max suffix sum of right Node
    # b) sum of right Node + max suffix sum of left Node
    # c) sum of left Node + sum of right Node
    ans.max_suffix = max(right.max_suffix, 
                    right.total_sum+left.max_suffix, 
                    left.total_sum+right.total_sum)

    # Total sum of ans Node = total sum of
    # left Node + total sum of right Node
    ans.total_sum = left.total_sum + right.total_sum

    # The max sum of ans Node stores the answer
    # which is the maximum value among:
    # prefix sum of ans Node
    # suffix sum of ans Node
    # maximum value of left Node
    # maximum value of right Node
    # prefix value of left Node + suffix value of right Node
    ans.max_sum = max(ans.max_prefix, 
                    ans.max_suffix, 
                    ans.total_sum,
                    left.total_sum, 
                    right.total_sum, 
                    left.max_suffix+right.max_prefix
                )

    # Return the ans Node
    return ans

# Function for calculating the
# max_sum_subArray using divide and conquer
def getMaxSumSubArray(A):

    if len(A) == 1: 
        return Node(A[0])

    mid = len(A) // 2

    # Call method to return left Node:
    left = getMaxSumSubArray(A[:mid])

    # Call method to return right Node:
    right = getMaxSumSubArray(A[mid:])

    # Return the merged Node:
    return merg(left, right)

# Driver code

ar = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(ar)
ans = getMaxSumSubArray(ar)
print("Answer is", ans._max)
