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


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize a set to keep track of duplicate values
        # and a dictionary to store the indices of previously seen values
        duplicates = set()
        seen_values = {}

        # Initialize an empty list to store unique triplets that add up to 0
        triplets = []

        # Loop over each element in the array
        for i, x in enumerate(nums):

            # Check if x is a duplicate
            if x not in duplicates:
                duplicates.add(x)

                # Loop over the remaining elements in the array
                for j, y in enumerate(nums[i+1:]):

                    # Find the third element z such that z = -(x+y)
                    z = -(x+y)

                    # Check if we have seen z before at a previous index
                    # If z was seen at the current i-th index, we have found a triplet
                    if z in seen_values and seen_values[z] == i:

                        triplet = sorted([x, y, z])

                        # Check if the triplet is unique
                        if triplet not in triplets:
                            triplets.append(triplet)

                    # Store the index of y in the seen_indices dictionary
                    seen_values[y] = i

        # Return the list of unique triplets that add up to 0
        return triplets


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
