# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Simple factorization problem.
#
# Naive algorithm will work for small integer like 600851475143.
#
# More efficient algorithms involving prime-sieving and
# congruence-of-squares probabilistic factorization exist
# but are not implemented here due to a lack of need for
# optimization.
TO_FACTOR = 600851475143


# Unoptimized. Simple prime sieve will speed up tremendously.
def naive_factorize(num):
    n = 2
    while n * n <= num:
        if num % n == 0:
            num //= n
            yield n
        else:
            n += 1
    yield num


def run():
    for prime_factor in naive_factorize(TO_FACTOR):
        print("Found factor {0}".format(prime_factor))

# Sample Output:
# Found factor 71
# Found factor 839
# Found factor 1471
# Found factor 6857
#
# Total running time for Problem3.py is 0.000626561914682896 seconds
