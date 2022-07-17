

def runningSum(nums):
        """
		Given an array nums, return the running sum of nums.

        :type nums: List[int]
        :rtype: List[int]

        Input: nums = [1,2,3,4]
		Output: [1,3,6,10]

		General Form:
		Input: nums = [a, b, c, d, ...]
		Output: [a, a+b, a+b+c, a+b+c+d, ...]
        """

        i = 0
        current_sum = 0
        n = len(nums)
        result = [0] * n 

        while i < n:
        	current_sum += nums[i]
        	result[i] = current_sum

        	i += 1

        return result


if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	result = runningSum(nums)
	print(result)
