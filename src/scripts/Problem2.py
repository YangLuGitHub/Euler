# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with
# 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum
# of the even-valued terms.
#
# This requires efficient Fibonacci generation: the classical
# recursive solution of fib(n) = fib(n-1) + fib(n-2) will grow
# at O(2^n) (or more precisely, O(fib(n)) complexity).
#
# We see that the other basic solution of simply iteratively
# adding numbers will work.

UPPER_BOUND = 4000000


def run():
    even_fib_sum = 0
    fib_last = 1
    fib_current = 1

    # Loop until fibonacci numbers get too large
    while fib_current <= UPPER_BOUND:
        if fib_current % 2 == 0:
            even_fib_sum += fib_current

        fib_new = fib_last + fib_current
        fib_last = fib_current
        fib_current = fib_new

    print("The solution is {0}".format(even_fib_sum))
    # Sample Output:
    # The solution is 4613732

    # Fibonacci computed iteratively
