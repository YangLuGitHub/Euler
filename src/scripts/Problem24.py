# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
# the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# This problem can actually be solved mathematically. We note that
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
# 10! = 3628800
#
# So the 1-millionth permutation must start with the digit floor(PERMUTATION_INDEX / 9!) = _,
# followed by remaining_digits[floor((PERMUTATION_INDEX % 9!) / 8!] = _, etc.
#
# The code reflects this solution, rather than the itertools result.
from math import factorial

PERMUTATION_INDEX = 1000000


def run():
    remaining_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    remaining = PERMUTATION_INDEX - 1
    permutation = 0
    for i in range(9, -1, -1):
        result = divmod(remaining, factorial(i))
        permutation *= 10
        permutation += remaining_digits[result[0]]
        print(str(permutation))
        remaining_digits.remove(remaining_digits[result[0]])
        remaining = result[1]
    print("The {0}th lexicographic permutation of the digits 0123456789 is {1}".format(PERMUTATION_INDEX, permutation))

# Sample Output:
# The 1000000th lexicographic permutation of the digits 0123456789 is 2783915460
#
# Total running time for Problem24.py is 0.00012720982628747603 seconds
