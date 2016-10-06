# 1000-digit Fibonacci number
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#
# Naive solution is trivial in Python, again, thanks to support for big integers.
#
# Fibonacci numbers given by closed-form formula can be solved mathematically for solution in
# constant time for arbitrarily large digit counts, if needed.
from math import log10

DIGIT_COUNT_REQUIRED = 1000


def run():
    fib_last = 1
    fib_current = 1
    fib_index = 2

    # Loop until fibonacci numbers get too large
    # Fibonacci computed iteratively
    while log10(fib_current) < DIGIT_COUNT_REQUIRED - 1:
        fib_new = fib_last + fib_current
        fib_last = fib_current
        fib_current = fib_new
        fib_index += 1
    print("The first Fibonacci number to exceed {0} digits has index {1}".format(DIGIT_COUNT_REQUIRED, fib_index))

# Sample Output:
# The first Fibonacci number to exceed 1000 digits has index 4782
#
# Total running time for Problem25.py is 0.00294952969895123 seconds
