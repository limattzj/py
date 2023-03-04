from typing import List, Tuple

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # sort the input list O(n*logn)

        # the outer-loop takes O(n) and inner-loop takes O(n)
        # together O(n^2)
        for i, num in enumerate(nums):
            # avoid duplicates in the input
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1 # set the left pointer to the next index
            right = n - 1 # set the right pointer to the last index

            # two-sum algorithm O(n), 
            # loop-invariant: left pointer < right pointer
            while left < right:
                # calculate the current three-sum
                total = nums[i] + nums[left] + nums[right] 

                # if sum > 0,   move the right pointer to the left
                # if sum < 0,   move the left pointer to the right
                # if sum == 0,  append the triplet to the result list 
                if total > 0: right -= 1
                    
                elif total < 0: left += 1
                    
                else: # three_sum == 0 
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # move the left pointer to the right
                    # and avoid duplicates in the input
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return result


    def three_sum_hash(self, nums: List[int]) -> List[List[int]]:

        # Initialize sets to store result triplets and duplicate values
        # Initialize dictionary to store seen values and their indices
        result, duplicates = set(), set()
        seen = {}
        
        # Iterate through each value in the input array "nums"
        for i, x in enumerate(nums):

            # Check if nums[i] has already been processed before
            # If not, add it to the "dups" set to prevent duplicates
            if x not in duplicates:
                duplicates.add(x)
                
                # Iterate through remaining values in "nums" 
                # such that first + second + third = 0 => third = - first - second = -(first + second)
                for _, y in enumerate(nums[i + 1: ]):
                    z = -(x + y)

                    # Check if the complement has been seen before and if it was seen for x
                    if z in seen and seen[z] == i:
                        
                        # If so, add the triplet (x, y, complement) to result
                        result.add(tuple(sorted((x, y, z))))
                    
                    # Update the "seen" dictionary with the current "y" and its index "i"
                    seen[y] = i
        
        # Return the "res" set as a list of lists
        return result


if __name__ == '__main__':
    result = Solution().three_sum([-1, 0, 1, 2, -1, -4])
    # result = threeSum(nums=[0, 0, 0, 0])
    # result = Solution().three_sum(
    #     [34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21,
    #           -43, 57, -6, 86, 56, 94, 74, 83, -14, 28, -66, 46, -49, 62, -11,
    #           43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29,
    #           36, -29, 10, -70, 69, 17, 49]
    # )
    print(result)
