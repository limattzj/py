
from typing import List


def pivotIndex(nums: List[int]):

	"""
	Calculate the pivot index of the array nums, such that sum_left of pivot 
	equals to the sum_right of pivot
	:type nums: List[int]
	:rtype: int
	"""

	
	sum_left = 0
	sum_right = sum(nums[1:])
	n = len(nums)

	pivot = 0

	while pivot < n:

		if sum_left == sum_right:
			return pivot

		sum_left += nums[pivot]
		pivot += 1
		if pivot < n:
			sum_right -= nums[pivot]

	return -1

if __name__ == '__main__':
	result = pivotIndex(nums = [1, 7, 3, 6, 5, 6])
	print(result)
