# Interestingly, the first Project Euler question seems
# to be similar in concept to "FizzBuzz", requiring the
# programmer to sum numbers that are modulo 3 or 5


def run():
    divisor_sum = 0
    for x in range(1000):
        if (x % 3) == 0 or (x % 5) == 0:
            divisor_sum += x

    print("The solution is %d" % divisor_sum)
    # Sample Output:
    # The solution is 233168

# Notably, this problem has a closed-form mathematical solution.
# The sums 3 to 999, 5 to 1000, and 15 to 990 are
# (3 + 999) * 333 / 2 = 166833
# (5 + 995) * 199 / 2 = 99500
# (15 + 990) * 66 / 2 = 33165
# respectively, and the expression
# 166833 + 99500 - 33165 yields
# 233168 as expected
