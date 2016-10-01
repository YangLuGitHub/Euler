# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only
# being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
# This seems more like a math problem than a computational one.
#
# Combinatorics reveals solution to be 40 choose 20, also written
# 40! / (20!20!). It's only necessary to compute the result, which
# I assume overflows a 32-bit integer - but Python does not have
# that problem.
#
# A recursive programmatic solution may have worked - but if poorly
# implemented, it can easily blow the call stack.
HEIGHT = 20
WIDTH = 20


def a_choose_b(a, b):
    product = 1
    if b < a / 2:
        b = a - b
    for x in range(a, b, -1):
        product *= x
    denominator = 1
    for y in range(a - b, 0, -1):
        denominator *= y
    return product // denominator


def run():
    print("The number of paths through a {0}x{1} grid is {2}".format(HEIGHT, WIDTH, a_choose_b(WIDTH + HEIGHT, HEIGHT)))

# Sample Output:
# The number of paths through a 20x20 grid is 137846528820
#
# Total running time for Problem15.py is 0.00011545981228800295 seconds
