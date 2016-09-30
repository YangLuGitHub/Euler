# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Using sieve implementation from Problem 7 to generate
# the solution seems like no-brainer, but it takes over
# a full second to execute.
#
# We can optimize it a little bit more.
from math import ceil, sqrt

SIEVE_SIZE = 2000000


# Generates a set of prime numbers less than or equal to max_num
# using Eratosthenes method. Optimized a bit from Problem7 implementation
# but could still be better.
def optimized_sieve(sieve_up_to):
    # Make sieve inclusive
    max_num = sieve_up_to + 1

    # Preliminary list holder
    result_list = list(range(max_num))
    max_sieve_element = ceil(sqrt(max_num))

    # Skip 1
    result_list[1] = 0

    # Only need to sieve up to sqrt(max_num)
    for i in range(2, max_sieve_element):
        if result_list[i]:
            # Can start at i * i since multiples of i less than
            # that have already been sieved out.
            result_list[i * i: max_num: i] = [0] * ((sieve_up_to - i * i) // i + 1)
            # The above code behaves like
            # for j in range(i * i, max_num, i):
            #     result_list[j] = 0
            # But is ~60% faster.

    # Remove entries equal to 0
    return filter(None, result_list)


def run():
    sieve = list(optimized_sieve(SIEVE_SIZE))
    print("Sum of all {0} primes under {1} is {2}".format(len(sieve), SIEVE_SIZE, sum(sieve)))

# Sample Output:
# Sum of all 148933 primes under 2000000 is 142913828922
#
# Total running time for Problem10.py is 0.23230770809706836 seconds
