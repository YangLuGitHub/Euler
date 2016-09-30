# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
#
# Using a slightly modified sieve implementation from Problem 5,
# but returning a list instead of set, this is simple to do.
#
# Can guess size of sieve needed by utilizing approximation of
# prime-counting function pi(x) ~ x/(ln(x) - 1)
#
# 10001 = x / (ln(x) - 1)
# x = 105694
# Use 110000 to account for margin of error in estimation
from math import sqrt, ceil

SIEVE_SIZE = 110000


# Generates a set of prime numbers less than or equal to max_num
# using Eratosthenes method. Could be optimized a bit more, but
# fast enough for current purposes.
def prime_sieve(sieve_up_to):
    # Make sieve inclusive
    max_num = sieve_up_to + 1
    sieve = [True] * max_num

    # Result is an unordered set since order doesn't matter
    result = []
    max_sieve_element = ceil(sqrt(max_num))

    # Only need to sieve up to sqrt(max_num)
    i = 2
    for i in range(2, max_sieve_element):
        if sieve[i]:
            result.append(i)
            sieve_iterator = i * 2
            while sieve_iterator < max_num:
                sieve[sieve_iterator] = False
                sieve_iterator += i
    for j in range(i + 1, max_num):
        if sieve[j]:
            result.append(j)
    return result


def run():
    sieve = prime_sieve(SIEVE_SIZE)
    print("Prime numbers in size {0} sieve: {1}".format(SIEVE_SIZE, len(sieve)))
    i = 10000
    print("sieve[{0}]: {1}".format(i, sieve[i]))

    # Sample Output:
    # Prime numbers in size 110000 sieve: 10453
    # sieve[10000]: 104743
