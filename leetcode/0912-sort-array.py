def mergeSort(A):

	n = len(A)
	if n == 1:
		return A

	else:
		# split array into 2 subarr with size n/2
		mid = n // 2
		left = A[:mid]
		right = A[mid:]

		# sort subarr recursively
		mergeSort(left)
		mergeSort(right)

		i = j = k = 0

		# merge 
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				A[k] = left[i]
				i += 1
			else:
				A[k] = right[j]
				j += 1

			k += 1

		while i < len(left):
			A[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			A[k] = right[j]
			j += 1
			k += 1


if __name__ == '__main__':
	A = [38, 27, 43, 3, 9, 82, 10]
	mergeSort(A)
	print(A)
