# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
# 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
# the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
# any further by analysis even though it is known that the greatest number that cannot be expressed as the sum
# of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# A very interesting question. Thankfully efficient factor summing method was already written for Problem 21,
# and is generally usable with minimal modifications.
#
# Micro-optimizations can be performed by noting things such as only needing to iterate up to (28123 - 12),
# but as they have negligible performance impact at the cost of difficult-to-read code, they are not performed.
#
# sum_divisors() could perhaps be made faster.
from Problem10 import optimized_sieve
from Problem21 import sum_divisors

MAX_NUM = 28123


def run():
    prime_sieve = list(optimized_sieve(MAX_NUM))
    abundant_numbers = set(i for i in range(1, MAX_NUM) if sum_divisors(i, prime_sieve) > i)

    def is_abundant_sum(input_num):
        return any(input_num - num in abundant_numbers for num in abundant_numbers)

    non_abundant_sum = sum(i for i in range(1, MAX_NUM) if not is_abundant_sum(i))

    print("The sum of integers under {0} that cannot be abundantly summed is {1}".format(MAX_NUM, non_abundant_sum))

# Sample Output:
# The sum of integers under 28123 that cannot be abundantly summed is 4179871
#
# Total running time for Problem23.py is 1.7978987465091372 seconds
