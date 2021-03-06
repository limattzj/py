

def findTheDifference(s: str, t: str) -> str:
	""" Given two string s and t, such that t is generated by 
	random shuffling string s and then add one more letter at
	random position. 

	Args:
		s: a string that is given
		t: A string s.t shuffled s and add a letter at random pos

	Returns:
		the difference between s and t. 

	"""

	mapping = {}

	# iterate over each letter in s and put s in a hashtable
	# key, value : char, number of occurrences
	for letter in s:
		if letter not in mapping:
			mapping[letter] = 1

		else:
			mapping[letter] += 1

	# iterate over t, if char in hashtable, reduce the number of occurences,
	# if char not in hashtable, we have found the difference.

	for letter in t:
		if letter not in mapping or mapping[letter] == 0:
			return letter

		else:
			mapping[letter] -= 1


if __name__ == "__main__":
	s = ""
	t = "y"

	result = findTheDifference(s, t)
	print(result)
