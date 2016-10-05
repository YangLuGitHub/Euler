# Maximum path sum II
# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to
# try every route to solve this problem, as there are 299 altogether! If you could
# check one trillion (1012) routes every second it would take over twenty billion years
# to check them all. There is an efficient algorithm to solve it. ;o)
#
# Simple solution from Problem 18 works. This problem simply needs to run the same algorithm
# with the twist that input is read from a file instead of a regex'd copy-pasted input.
import os

from Problem18 import collapse_triangle


def load_input_triangle(file_path):
    folder_above = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    triangle_list = []
    with open(os.path.join(folder_above, file_path)) as triangle_file:
        for line in triangle_file:
            triangle_list.append([int(i) for i in line.split(" ")])
    return triangle_list


def run():
    print("The maximum sum of all paths through the triangle is {0}".format(
        collapse_triangle(load_input_triangle(os.path.join("inputs", "p067_triangle.txt")))))

# Sample Output:
# The maximum sum of all paths through the triangle is 7273
#
# Total running time for Problem67.py is 0.004552290900988562 seconds
