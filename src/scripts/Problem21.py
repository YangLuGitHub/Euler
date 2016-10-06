# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Fairly simple to find all proper divisors of a number by factorizing the number into primes,
# then generating all combinations of such primes and summing them.
#
# Much faster than naive solutions of integer factorization.
from Problem10 import optimized_sieve

MAX_NUM = 10000


def factorize(num, prime_sieve):
    factors = {}
    for prime in prime_sieve:
        exponent_count = 0
        while num % prime == 0:
            exponent_count += 1
            num //= prime
        if exponent_count > 0:
            factors[prime] = exponent_count
        if num <= 1:
            return factors
        if prime * prime > num:
            factors[num] = 1
            return factors


def sum_divisors(num, prime_sieve):
    prime_factors_dictionary = factorize(num, prime_sieve)
    divisors = [1]
    for entry in prime_factors_dictionary.keys():
        new_divisors = []
        for i in range(1, prime_factors_dictionary[entry] + 1):
            for existing_divisor in divisors:
                new_divisors.append((entry ** i) * existing_divisor)
        for value in new_divisors:
            divisors.append(value)
    return sum(divisors) - num


def run():
    prime_sieve = list(optimized_sieve(MAX_NUM))

    sum_of_factors_dictionary = {}
    amicable_sum = 0
    for i in range(1, MAX_NUM):
        sum_of_factors_dictionary[i] = sum_divisors(i, prime_sieve)

    # Use dictionary to avoid computing sum of factors twice
    for num in sum_of_factors_dictionary.keys():
        if sum_of_factors_dictionary[num] in sum_of_factors_dictionary:
            # Check if sum of factors of the sum of factors equals the number, and that the sum of factors
            # does not equal the number itself.
            if sum_of_factors_dictionary[sum_of_factors_dictionary[num]] == num and \
                            num != sum_of_factors_dictionary[num]:
                if sum_of_factors_dictionary[num] > num:
                    print("Found amicable pair {0}, {1}".format(num, sum_of_factors_dictionary[num]))
                amicable_sum += num

    print("The sum of all amicable numbers under {0} is {1}".format(MAX_NUM, amicable_sum))

# Sample Output:
# Found amicable pair 220, 284
# Found amicable pair 1184, 1210
# Found amicable pair 2620, 2924
# Found amicable pair 5020, 5564
# Found amicable pair 6232, 6368
# The sum of all amicable numbers under 10000 is 31626
#
# Total running time for Problem21.py is 0.08649122508988638 seconds
