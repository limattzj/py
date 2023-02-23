def maxSubarray(A):

    if len(A) == 1:
        return A[0]

    mid = len(A) // 2
    curr = best_left_sum = best_right_sum = 0

    i = mid -1
    while i >= 0:
        curr += A[i]
        best_left_sum = max(curr, best_left_sum)
        i -= 1

    j = mid + 1
    curr = 0

    while j < len(A):
        curr += A[j]
        best_right_sum = max(curr, best_right_sum)
        j += 1

    cross = best_left_sum + A[mid] + best_right_sum

    left_half = maxSubarray(A[:mid])
    right_half = maxSubarray(A[mid:])

    return max(left_half, cross, right_half)

A = [-2,1,-3,4,-1,2,1,-5,4]
maxSubarray(A)
