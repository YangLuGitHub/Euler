# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# Problem is trivial in Python thanks to its support of arbitrarily large integers.
#
# The method demonstrated in Problem 13 for a primitive unoptimized array-based
# integer container can also be used to solve this problem. To avoid repetition,
# the trivial solution is used here, written as a single expression.
from math import factorial

FACTORIAL_BASE = 100


def run():
    print("The sum of all the digits in {0}! is {1}".format(FACTORIAL_BASE, sum(
        int(digit) for digit in str(factorial(FACTORIAL_BASE)))))

# Sample Output:
# The sum of all the digits in 100! is 648
#
# Total running time for Problem20.py is 0.00011891343931246698 seconds
