

# longest palindrome string
# brute force = O(n^3)
# how to check if a string is a palindrome?
	# start from both end and check towards middle
	# b a b a d
	# ^       ^
	# or start from the middle and check outward => O(n^2)
	# b a b a d 
	#   ^
	# b a b a d  ===> bab 
	# ^   ^

	# what about even palindrome??


class Solution:
	"""
	@param s: input string
	@return: the longest palindrometic subtring
	"""
	def longest_palindrome(self, s):

		# exception handling
		if not s:
			return ""

		result = ""
		current_len = 0

		for i in range(len(s)):
			
			# odd length string
			left, right = i, i
			while left >= 0 and right < len(s) and s[left] == s[right]:

				if (right - left + 1) > current_len:
					result = s[left:right+1]
					current_len = right - left + 1

				left = left - 1
				right = right + 1

		return result

	def is_palindrome(self, s, left, right, length):

		while left >= 0 and right < length and s[left] == s[right]:
			
			left -= 1
			right += 1

		return left, right

if __name__ == '__main__':
	s = Solution()
	ss = 'aba'
	result = s.is_palindrome(ss, 1, 1, 3)
	print(result)













