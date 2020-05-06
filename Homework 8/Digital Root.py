"""
Time complexity: O(n)
Space Complexity: O(1)
"""


def digital_root(number):
	while not 0 < number <= 9:
		number = sum([int(i) for i in str(number)])
		print(number)
	return number


digital_root(456)