# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import re

RADIX = 10
POWER = 5


def run():
    powers = [i ** POWER for i in range(0, RADIX)]
    total_sum = 0
    for i in range(RADIX, ((RADIX - 1) ** POWER) * (POWER + 1)):
        remainder = i
        digit_power_sum = 0
        while remainder > 0:
            result = divmod(remainder, RADIX)
            remainder = result[0]
            digit_power_sum += powers[result[1]]
        if i == digit_power_sum:
            print("{0} = {1}".format(i, re.sub(r' ([0-9])', r' + \1', re.sub(r'([0-9])', r'\1^{0} ', str(i))))
                  .format(POWER))
            total_sum += i
    print("The sum of all {0}-digit numbers that can be written as the {0}th power of its digits is {1}"
          .format(POWER, total_sum))

# Sample Output:
# 4150 = 4^5 + 1^5 + 5^5 + 0^5
# 4151 = 4^5 + 1^5 + 5^5 + 1^5
# 54748 = 5^5 + 4^5 + 7^5 + 4^5 + 8^5
# 92727 = 9^5 + 2^5 + 7^5 + 2^5 + 7^5
# 93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5
# 194979 = 1^5 + 9^5 + 4^5 + 9^5 + 7^5 + 9^5
# The sum of all 5-digit numbers that can be written as the 5th power of its digits is 443839
#
# Total running time for Problem30.py is 0.6594186036864775 seconds
