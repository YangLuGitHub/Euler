# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?
#
# Again, a problem that is trivially implemented in Python thanks
# to its handling of arbitrarily large integers:
#
# print("The sum of digits in 2^{0} is {1}".format(EXPONENT, sum(int(digit) for digit in str(2**EXPONENT))))
#
# A simple solution that falls within the spirit of this problem
# does exist, however, by implementing the number as an array of
# digits.
#
# As the challenge of Problem16 seems to be the creation of an algorithm
# that can go arbitrarily high, without relying on library functions like
# bigint or natively infinite precision integer types like Python,
# this solution was used instead of the one-liner involving 2**1000.
#
# It's obviously inefficient as far as algorithms go, but it shows
# the process of addition with carry clearly.
from math import ceil, log

EXPONENT = 1000
DIGIT_COUNT = ceil(EXPONENT * log(2, 10)) + 1


def run():
    digit_list = [0] * DIGIT_COUNT
    digit_list[0] = 1
    digits = 1
    for x in range(EXPONENT):
        for digit in range(digits - 1, -1, -1):
            digit_list[digit] *= 2
            if digit_list[digit] > 9:
                if digit + 1 == digits:
                    digit_list.append(0)
                    digits += 1
                digit_list[digit] %= 10
                digit_list[digit + 1] += 1

    result = sum(digit_list)
    print("The sum of digits in 2^{0} is {1}".format(EXPONENT, result))

# Sample Output:
