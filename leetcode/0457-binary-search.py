class Solution:
   
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):

        # check for empty string
        if not nums:
            return -1

        start = 0 # 起点
        end = len(nums) - 1 # 终点

        while start + 1 < end:
            mid = (start + end) // 2  # 中间点 

            if nums[mid] < target: # 说明target在右区间
                start = mid

            elif nums[mid] == target: # 如果有多个target，找最后一个target
                start  = mid
            
            else: # nums[mid] > target => 说明target在左区间
                end = mid
        
        if nums[end] == target:
            return end 

        if nums[start] == target:
            return start

        # 如果target不在这里数组里        
        return -1;
                 
if __name__ == '__main__':
    A = [1, 3, 7, 11, 12, 19]
    solution = Solution()
    result = solution.findPosition(A, 15)

    print(f"The index of the target is at: {result}")


    A = [1, 1, 1, 1, 1]
    solution = Solution()
    result = solution.findPosition(A, 1)

    print(f"The index of the target is at: {result}")
