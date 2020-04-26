"""
Given a positive integer n, calculate the following sum:
25  =>  25 + 12 + 6 + 3 + 1 = 47
        |   n       |   total       |   n>=1    |
        |     25    |       25      |   False   |
        |    12     |       37      |   False   |
        |     6     |       43      |   False   |
        |     3     |       46      |   False   |
        |   1       |       47      |   True    |

"""


def halving_sum(n):
	total = n
	while n >= 1:
		n = int(n/2)
		total += n
	return total


print(halving_sum(25))