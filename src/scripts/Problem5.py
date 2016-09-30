# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
#
# Naive solution would be brute-force dividing numbers by
# 1-20 and checking for remainder, but that is inefficient.
#
# Can mathematically solve this by finding the largest
# prime factors and exponents for 1-20 and finding a
# product, which is automated below.
from math import sqrt, ceil, log

MAX_DIVISOR = 20


# Generates a set of prime numbers less than or equal to max_num
# using Eratosthenes method. Could be optimized a bit more, but
# fast enough for current purposes.
def prime_sieve(sieve_up_to):
    # Make sieve inclusive
    max_num = sieve_up_to + 1
    sieve = [True] * max_num

    # Result is an unordered set since order doesn't matter
    result = set()
    max_sieve_element = ceil(sqrt(max_num))

    # Only need to sieve up to sqrt(max_num)
    i = 2
    for i in range(2, max_sieve_element):
        if sieve[i]:
            result.add(i)
            sieve_iterator = i * 2
            while sieve_iterator < max_num:
                sieve[sieve_iterator] = False
                sieve_iterator += i
    for j in range(i + 1, max_num):
        if sieve[j]:
            result.add(j)
    return result


# Replaces all sieve members with their largest exponent
# that is still less than or equal to max_value.
#
# Useful in the context of this problem to obtain
# the maximum exponents of all prime divisors
# less than or equal to MAX_DIVISOR
def adjust_sieve(sieve, max_value):
    result = set()
    for element in sieve:
        result.add(element ** int(log(max_value, element)))
    return result


def run():
    sieve = prime_sieve(MAX_DIVISOR)
    # print("Prime sieve {0}".format(sieve))
    adjusted_sieve = adjust_sieve(sieve, MAX_DIVISOR)
    # print("Adjusted factors {0}".format(adjusted_sieve))

    product = 1
    for element in adjusted_sieve:
        product *= element

    print("Product of all maximum prime factors under {0} is {1}".format(MAX_DIVISOR, product))

    for i in range(1, MAX_DIVISOR + 1):
        div_result = divmod(product, i)
        # print("{0} / {1} = {2} with remainder {3}".format(product, i, div_result[0], div_result[1]))

        # Sample Output with all debugging messages:
        # Prime sieve {2, 3, 5, 7, 11, 13, 17, 19}
        # Adjusted factors {5, 7, 9, 11, 13, 16, 17, 19}
        # Product of all maximum prime factors under 20 is 232792560
        # 232792560 / 1 = 232792560 with remainder 0
        # 232792560 / 2 = 116396280 with remainder 0
        # 232792560 / 3 = 77597520 with remainder 0
        # 232792560 / 4 = 58198140 with remainder 0
        # 232792560 / 5 = 46558512 with remainder 0
        # 232792560 / 6 = 38798760 with remainder 0
        # 232792560 / 7 = 33256080 with remainder 0
        # 232792560 / 8 = 29099070 with remainder 0
        # 232792560 / 9 = 25865840 with remainder 0
        # 232792560 / 10 = 23279256 with remainder 0
        # 232792560 / 11 = 21162960 with remainder 0
        # 232792560 / 12 = 19399380 with remainder 0
        # 232792560 / 13 = 17907120 with remainder 0
        # 232792560 / 14 = 16628040 with remainder 0
        # 232792560 / 15 = 15519504 with remainder 0
        # 232792560 / 16 = 14549535 with remainder 0
        # 232792560 / 17 = 13693680 with remainder 0
        # 232792560 / 18 = 12932920 with remainder 0
        # 232792560 / 19 = 12252240 with remainder 0
        # 232792560 / 20 = 11639628 with remainder 0
