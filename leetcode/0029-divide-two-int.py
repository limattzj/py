def divide(dividend: int, divisor: int) -> int:
	"""Divides two integers without using multiplication, division, and mod

	Args:
		dividend: the numerator part of the division
		divisor: the denominator part of the division

	Returns:
		An integer that is the quotient after dividing dividend by divisor.

	>>> divide(10, 3)
	3
	>>> divide(7, -3)
	-2

	"""

	# set the sign, the sign is positive iff dividend and divisor have the
	# same operator. (Act as a AND operator) True is True and F Is False,
	# otherwise the sign is False.
	sign = (dividend < 0) is (divisor < 0)

	# changes both to abs values since positive - negative = a larger positive
	dividend = abs(dividend)
	divisor = abs(divisor)

	ans = 0

	while dividend >= divisor:
		temp = divisor
		i = 1
		while dividend >= temp:
			dividend -= temp
			ans += i
			i <<= 1
			temp <<= 1
			print(f'dividend: {dividend}, ans: {ans}, i:{i}, temp:{temp}')

	if not sign:
		ans = -ans

	return min(max(-2147483648, ans), 2147483647)


if __name__ == '__main__':
	x = divide(10, 3)
