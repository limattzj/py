class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        result = []

        self.dfs(nums, 0, [], result)

        return result
        
    def dfs(self, nums, index, subset, results):
        results.append(list(subset))
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            
            self.dfs(nums, i + 1, subset, results)
            
            subset.pop()

if __name__ == "__main__":
    a = [1, 2, 3]
    result = Solution().subsets(a)
    print(result)
