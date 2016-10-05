# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Classic calendar problem. Simply a matter of implementation.
MONTH_DICTIONARY = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
MONTH_COUNT = 12
YEAR_INIT = 1900
YEAR_START = 1901
YEAR_END = 2000
WEEKDAY_START = 1


def is_leap_year(year_num):
    if year_num % 4 == 0 and (year_num % 100 != 0 or year_num % 400 == 0):
        return True


def get_month_duration(month, year_num):
    if month != 2:
        return MONTH_DICTIONARY.get(month)
    else:
        if is_leap_year(year_num):
            return MONTH_DICTIONARY.get(month) + 1
        else:
            return MONTH_DICTIONARY.get(month)


def run():
    week_counter = WEEKDAY_START
    year = YEAR_INIT
    sundays = 0
    while year < YEAR_END + 1:
        for month in range(1, MONTH_COUNT + 1):
            week_counter = week_counter + get_month_duration(month, year)
            if week_counter % 7 == 0:
                sundays += 1
        # Don't count year 1900
        if year == 1900:
            sundays = 0
        year += 1
    print("The total number of Sundays from Jan {0} to Dec {1} is {2}".format(YEAR_START, YEAR_END, sundays))
    return 0

# Sample Output:
# The total number of Sundays from Jan 1901 to Dec 2000 is 171
#
# Total running time for Problem19.py is 0.0007747151312018198 seconds
