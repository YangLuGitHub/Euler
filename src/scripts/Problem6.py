# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
#
# This problem is relatively straightforward. Easy optimization can be
# performed by using the closed-form solution for summations, making the
# code extensible to much, much larger values of MAX_NUM without performance
# issues.
MAX_NUM = 100


def sum_value(start, end):
    return (start + end) * (end + 1 - start) // 2


def sum_squares(start, end):
    return (2 * start * start + 2 * start * end + 2 * end * end + end - start) * (1 + end - start) // 6


def run():
    sum_of_squares = sum_squares(1, MAX_NUM)
    sum_of_values = sum_value(1, MAX_NUM)
    square_of_sum = sum_of_values * sum_of_values
    print("square of sum - sum of squares = {0} - {1} = {2}".format(square_of_sum, sum_of_squares,
                                                                    square_of_sum - sum_of_squares))

# Sample Output:
# square of sum - sum of squares = 25502500 - 338350 = 25164150
#
# Total running time for Problem6.py is 0.00010468356314112268 seconds
