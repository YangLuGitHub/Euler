# Quadratic primes
# Problem 27
# Euler discovered the remarkable quadratic formula:
#
# n^2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39.
# However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly
# when n=41,41^2+41+41 is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values
# 0<=n<=79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n^2+an+b, where |a|<=1000 and |b|<=1000
#
# where |n| is the modulus/absolute value of nn
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n=0.
#
# A remarkable problem. Simplified solution lies with following constraints:
#
# b must be a positive prime, or the function will not produce a prime for n = 0
# a + b + 1 must also be prime. This limits the number of available values of a tremendously.
from Problem10 import optimized_sieve

MAXIMUM = 1000
SIEVE_SIZE = MAXIMUM * MAXIMUM


def run():
    sieve = list(optimized_sieve(SIEVE_SIZE))
    sieve_set = set(sieve)
    i = 0

    maximum_prime_count = 0
    max_a = 0
    max_b = 0

    while sieve[i] <= MAXIMUM:
        b = sieve[i]
        valid_coefficients = []
        for prime in sieve:
            coefficient = prime - b - 1
            if coefficient > MAXIMUM:
                break
            valid_coefficients.append(coefficient)

        for a in valid_coefficients:
            prime_count = 0
            for n in range(1, b):
                if n * n + a * n + b in sieve_set:
                    prime_count += 1

            if prime_count > maximum_prime_count:
                maximum_prime_count = prime_count
                max_a = a
                max_b = b
                # print("n^2 + {0}n + {1} yielded {2} primes!".format(a, b, prime_count))
                # print("a * b = {0} * {1} = {2}".format(a, b, a * b))
        i += 1
    print("n^2 + {0}n + {1} yields the most consecutive primes at {2}".format(max_a, max_b, maximum_prime_count))
    print("a * b = {0} * {1} = {2}".format(max_a, max_b, max_a * max_b))

# # Sample Output:
# n^2 + -61n + 971 yields the most consecutive primes at 582
# a * b = -61 * 971 = -59231
#
# Total running time for Problem27.py is 4.353975958923078 seconds
