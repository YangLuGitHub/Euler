# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# This actually requires knowledge of group theory for a mathematical solution, related to the Fermat quotient.
#
# The details are beyond the scope of this exercise, which will simply track remainders using the python divmod()
# function - taking advantage of the fact that when a remainder repeats, the repeating fraction will increase.
MAX_RANGE = 1000
RADIX = 10


def run():
    max_digits = 0
    max_index = 0
    for i in range(1, MAX_RANGE):
        remainders = []
        base = divmod(1, i)[1]
        digits = 0
        while base not in remainders and base != 0:
            remainders.append(base)
            # Long division with remainder
            while base < i:
                base *= RADIX
                digits += 1
            result = divmod(base, i)
            base = result[1]

        # Trim non-repeating leading digits
        if base != 0:
            index = 0
            # Stop when repeating bit found
            while remainders[index] != base:
                index += 1
                digits -= 1
        if base != 0:
            # print("Found repeating fraction 1/{0} with {1} digits".format(i, digits))
            if digits > max_digits:
                max_digits = digits
                max_index = i
                # else:
                #     print("Found terminating fraction 1/{0} with {1} digits".format(i, digits))

    print("The longest recurring cycle appears with fraction 1/{0} with length {1}".format(max_index, max_digits))

# Sample Output:
# The longest recurring cycle appears with fraction 1/983 with length 982
#
# Total running time for Problem26.py is 0.2719813246493532 seconds
