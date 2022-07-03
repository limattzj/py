from typing import List

# Leetcode 167 majority element
# input: 	[3, 2, 3]
# output: 	-> 3
# input:	[2, 2, 1, 1, 1, 2, 2]
# output: 	-> 2
# let x be the majority element in nums, and n be the number of times x exist in nums.
# It is given that n > ( len(nums) // 2 )
 

# 方法1: 
# 排序 O(nlogn) -> 找中间的数字 O(1)
def majorityElement(nums: List[int]) -> int:
	nums.sort()
	half = len(nums) // 2
	return nums[half]

# 方法2:
# 遍历数组 -> 构建哈希
# hashmap 统计每一个 element 出现的次数 
# [2, 2, 1, 1, 2]
# key	val 
# 2  	3
# 1 	2

def majorityElement2(nums: List[int]) -> int:
	mapping = {}

	for num in nums:
		if num not in mapping:
			mapping[num] = 1

		else:
			mapping[num] += 1

	half = len(nums) // 2

	for item in mapping:
		if mapping[item] > half:
			return item

	# It would never reach this condition based on the conditions that is given.
	return -1 

# 方法3
# 分治法
# 大问题变成小问题 
# [2, 2, 1, 1, 2]
# [2, 2, 1] 和 [1, 2] 找两个里面的majoirty element
# [2], [2, 1], [1], [2]


if __name__ == "__main__":
	# nums = [2, 2, 1, 1, 2]
	nums = [3, 2, 3]
	result = majorityElement2(nums)
	print(result)
