# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many
# letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance
# with British usage.
#
# This is a ridiculous problem, but simple enough to solve
# once patterns are established.
#
# 1-20: 1 word each
#     'one' 'four' 'three' 'eleven' 'fifteen' 'thirteen' 'seventeen'
#     'two' 'five' 'seven' 'twelve' 'sixteen' 'fourteen'
#     'six' 'nine' 'eight' 'twenty'           'eighteen'
#     'ten'                                   'nineteen'
# Letter count sum 1-9: 9 + 12 + 15 = 36
# Letter count sum 1-20: 12 + 12 + 15 + 18 + 14 + 32 + 9 = 112
#
# 21-99: 2 words
#     'forty' 'twenty' 'seventy'
#     'fifty' 'thirty'
#     'sixty' 'eighty'
#             'ninety'
# Letter count sum above: 15 + 24 + 7 = 46
# Letter count sum X0-X9: 36 + 10 * letter_count(X0)
# Letter count sum 20-99: 36 * 8 + 10 * 46 = 748
# Letter count sum 1-99: 112 + 748 - 6 = 854
#
# 100: 'one hundred'
# X00: '<> hundred'
# 101-199: 'one hundred and <>'
# X01-X99: '<> hundred and <>'
# X01-X99: (letter_count(X) + 10) * 99 + 854
# X00-X99: (letter_count(X) + 10) * 99 + 854 + (letter_count(X) + 7)
# 100-999: 10 * 99 * 9 + 36 * 99 + 854 * 9 + 36 + 7 * 9 = 20259
# 1-999: 20259 + 854 = 21113
#
# 1000: 'one thousand'
# 1-1000: 21113 + 11 = 21124
#
# Of course, this wouldn't be a Project Euler solution without
# a programmatic solution. Here, counting via a dictionary is
# employed. Slightly optimized through using a second dictionary
# to hold the integer length, rather than using expensive string
# operations.
LENGTH_HUNDRED = 7
LENGTH_AND = 3
MAX_COUNT = 1000
word_dict = {0: "",
             1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine",
             10: "ten",
             11: "eleven",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen",
             20: "twenty",
             30: "thirty",
             40: "forty",
             50: "fifty",
             60: "sixty",
             70: "seventy",
             80: "eighty",
             90: "ninety",
             1000: "onethousand"}
letter_count_dict = {}
for number in word_dict.keys():
    letter_count_dict[number] = len(word_dict[number])


# def get_english(num):
#     if num in letter_count_dict:
#         return word_dict[num]
#     else:
#         if num >= 100:
#             result = divmod(num, 100)
#             if result[1] == 0:
#                 trail = ""
#             else:
#                 trail = " and " + get_english(result[1])
#             return get_english(result[0]) + " hundred" + trail
#         else:
#             if num > 20:
#                 ones = num % 10
#                 return get_english(num - ones) + "-" + get_english(ones)
#             else:
#                 print("Something went seriously wrong parsing {0}".format(num))
#                 return "Error"


# Recursive method to get number of letters
def get_length(num):
    if num in letter_count_dict:
        return letter_count_dict[num]
    else:
        if num >= 100:
            result = divmod(num, 100)
            if result[1] == 0:
                remainder = 0
            else:
                remainder = LENGTH_AND + get_length(result[1])
            return get_length(result[0]) + LENGTH_HUNDRED + remainder
        else:
            if num > 20:
                ones = num % 10
                return get_length(num - ones) + get_length(ones)
            else:
                print("Something went seriously wrong parsing {0}".format(num))
                return 0


def run():
    total_letters = 0
    for n in range(1, MAX_COUNT + 1):
        total_letters += get_length(n)
    print("Total letters for numbers 1-{0} is {1}".format(MAX_COUNT, total_letters))

# Sample Output:
# Total letters for numbers 1-1000 is 21124
#
# Total running time for Problem17.py is 0.0021639734596378152 seconds
