# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# There is likely a quick mathematical solution to this due to special
# properties of palindromic numbers, although here I will simply create
# palindromic numbers in descending order and check if they can be factored
# into two three-digit numbers.
from math import log


# Gets a specific digit of a number inefficiently
def digit(num, index):
    return (num // (10 ** index)) % 10


# Checks if a number is a palindrome inefficiently
def is_palindrome(num):
    max_exp = int(log(num, 10))
    for x in range((max_exp + 1) // 2):
        if digit(num, x) != digit(num, max_exp - x):
            return False
    return True


# Makes a palindrome from the input number.
# Cannot make palindromes with an odd number of digits.
def make_palindrome(input_num):
    digits = 1 + int(log(input_num, 10))
    input_reversed = 0
    for i in range(digits):
        input_reversed += digit(input_num, i) * (10 ** (digits - i - 1))
    return input_num * (10 ** digits) + input_reversed


# Checks if input_num has two three-digit factors.
# Utilizes inefficient brute-force approach.
def has_three_digit_factors(input_num):
    for divisor in range(999, 100, -1):
        result = divmod(input_num, divisor)
        if result[1] == 0:
            if 99 < result[0] < 1000:
                print(
                    "Found palindrome {0} with three-digit divisors {1} and {2}".format(input_num, result[0], divisor))
                return True
    return False


def run():
    # Creates six-digit palindromes in strictly descending order
    for source_num in range(999, 100, -1):
        if has_three_digit_factors(make_palindrome(source_num)):
            return

            # Sample Output:
            # Found palindrome 906609 with three-digit divisors 913 and 993
