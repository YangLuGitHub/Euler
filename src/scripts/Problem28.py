# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# For some reason, a very simple problem has shown up amidst some problems with creative solutions.
#
# Take the first innermost circle:
# 3 + 5 + 7 + 9 = 24
#
# We see that a simple formula yields the sum of the next outermost layer of the spiral,
# using the value of the last corner of the previous layer, and the side length of the
# next spiral layer:
#
# next_box_sum = (last + side_length) + (last + 2 * side_length) + (last + 3 * side_length) + (last + 4 * side_length)
#              = 4 * last + 10 * side_length
#              = 4 * 1 + 10 * 2
#              = 24
#
# We see that the next last can also be obtained easily:
# last = last + 4 * side_length
#
# There is likely a closed-form solution to this problem. A generator function is, however,
# an easier-to-implement solution to this problem, using the relation found above.
MAX_SIZE = 1001


def make_boxes(size_max):
    last = 1
    next_box_sum = 1
    side_length = 0
    while side_length <= size_max:
        yield next_box_sum
        side_length += 2
        next_box_sum = 4 * last + 10 * side_length
        last += side_length * 4


def run():
    print("Sum of diagonals for a size {0} spiral is {1}".format(MAX_SIZE, sum(make_boxes(MAX_SIZE))))

# Sample Output:
# Sum of diagonals for a size 1001 spiral is 669171001
#
# Total running time for Problem28.py is 0.0002350616355312057 seconds
