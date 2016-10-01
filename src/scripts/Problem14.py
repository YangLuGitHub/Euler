# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Brute-force solution is trivial but has a long running time.
#
# Using predefined array to cache chain lengths will speed it up significantly.
#
# Sample running rimes:
# 51.89253616457898 seconds - Naive
# 8.987725339066984 seconds - Array-Cached (cache size 100000)
# 4.022678359752248 seconds - Array-Cached (cache size 100000, backed by dictionary)
# 3.352552175006286 seconds - Array-Cached (cache size 1000000)
# 3.305682162228734 seconds - Dictionary-Cached
#
# Pure Python solution to Problem 14 is unlikely to run any faster.


def run():
    chain_dictionary = {}

    max_chain_source = 1
    max_chain_length = 1
    for n in range(1, 1000000):
        seed = n
        chain_length = 0

        while seed != 1:
            if seed in chain_dictionary:
                chain_length += chain_dictionary[seed]
                break

            chain_length += 1
            if seed % 2 == 0:
                seed //= 2
            else:
                seed = seed * 3 + 1

        # Cache chain length value
        chain_dictionary[n] = chain_length

        if chain_length > max_chain_length:
            max_chain_length = chain_length
            max_chain_source = n
    print("Max chain length is {0} from number {1}".format(max_chain_length + 1, max_chain_source))

# Sample Output:
# Max chain length is 525 from number 837799
#
# Total running time for Problem14.py is 3.305682162228734 seconds
