# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# First, we recognize that if a <= b
# then (a - 1)^2 + (b + 1)^2 = a^2 + b^2 + 2b - 2a + 2
# cannot possibly be smaller than a^2 + b^2.
#
# This fact can be used to substantially reduce wasted guesses.
#
# Algorithm can be further refined with binary searches instead of
# naive incrementing, but no need to optimize yet.
INITIAL_C_VALUE = 334


def run():
    c = INITIAL_C_VALUE
    for c in range(INITIAL_C_VALUE, 1000):
        diff = 1000 - c
        a = (diff) // 2
        b = (diff - a)

        sum_of_squares = a * a + b * b
        c_squared = c * c
        while sum_of_squares < c_squared:
            a -= 1
            b += 1
            sum_of_squares = a * a + b * b
        if sum_of_squares == c_squared:
            print("{0}^2 + {1}^2 = {2}^2 = {3}".format(a, b, c, c_squared))
            print("{0} + {1} + {2} = {3}".format(a, b, c, a + b + c))
            print("abc = {0} * {1} * {2} = {3}".format(a, b, c, a * b * c))
            return

# Sample Output:
# 200^2 + 375^2 = 425^2 = 180625
# 200 + 375 + 425 = 1000
# abc = 200 * 375 * 425 = 31875000
#
# Total running time for Problem9.py is 0.0004772338907904122 seconds
