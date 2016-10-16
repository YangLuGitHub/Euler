# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
#
# Easy recursive tree-traversing algorithm.
COIN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1]
CUTOFF = len(COIN_VALUES) - 2


def sum_coin_counts(coin_level, remaining_amount):
    if coin_level == CUTOFF:
        return 1 + remaining_amount // 2
    else:
        return sum(sum_coin_counts(coin_level + 1, remaining_amount - coin_count * COIN_VALUES[coin_level])
                   for coin_count in range(0, 1 + remaining_amount // COIN_VALUES[coin_level]))


def run():
    print("The total number of ways that 2 pounds can be made with coins is {0}".format(sum_coin_counts(0, 200)))

# Sample Output:
# The total number of ways that 2 pounds can be made with coins is 73682
#
# Total running time for Problem31.py is 0.0022060281774272435 seconds
