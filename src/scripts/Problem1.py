# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Interestingly, the first Project Euler question seems
# to be similar in concept to "FizzBuzz", requiring the
# programmer to sum numbers that are modulo 3 or 5
#
# Notably, this problem has a simple closed-form mathematical solution.
# The sums 3 to 999, 5 to 1000, and 15 to 990 are
# (3 + 999) * 333 / 2 = 166833
# (5 + 995) * 199 / 2 = 99500
# (15 + 990) * 66 / 2 = 33165
# respectively, and the expression
# 166833 + 99500 - 33165 yields
# 233168 as expected


def run():
    divisor_sum = 0
    for x in range(1000):
        if (x % 3) == 0 or (x % 5) == 0:
            divisor_sum += x

    print("The sum of divisors is {0}".format(divisor_sum))

# Sample Output:
# The sum of divisors is 233168
#
# Total running time for Problem1.py is 0.00041155008646657056 seconds
