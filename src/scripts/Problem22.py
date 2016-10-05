# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order. Then working out
# the alphabetical value for each name, multiply this value by its alphabetical position in the
# list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
# 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# A hilarious problem, with a fairly simple implementation in Python.
#
# Sorting is trivial (although implementing my own sorting algorithm may
# have been a fun exercise), and there exist libraries to read CSV files.
import csv
import os

INPUT_FILE_NAME = "p022_names.txt"


def load_names(file_path):
    folder_above = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(folder_above, file_path)) as names:
        name_reader = csv.reader(names, delimiter=',', quotechar='\"')
        names = []
        for row in name_reader:
            names.extend(row)
        return names


def get_alphabetical_value(name):
    alphabetical_sum = 0
    for character in name:
        alphabetical_sum += ord(character)
    return alphabetical_sum - 64 * len(name)


def run():
    name_list = sorted(load_names(os.path.join("inputs", INPUT_FILE_NAME)))
    name_score_total = 0
    for i in range(0, len(name_list)):
        name_score_total += (i + 1) * get_alphabetical_value(name_list[i])
    # print(", ".join(name_list))
    print("The sum of all the name scores in {0} is {1}".format(INPUT_FILE_NAME, name_score_total))

# Sample Output:
# The sum of all the name scores in p022_names.txt is 871198282
#
# Total running time for Problem22.py is 0.007623108099512849 seconds
