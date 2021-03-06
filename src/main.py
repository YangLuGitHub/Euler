# Generic benchmarking code
# perf_counter() used for high precision
import os
from time import perf_counter

# Constant Declarations
MAX_SOLVED = 67  # Max number of Euler problems solved
BORDER = "-----"  # Border string printed around execution output of Problem#.py
DEFAULT = str(MAX_SOLVED)  # Defaults to highest solved problem2


# Print error message for invalid inputs
def print_input_err():
    print("Input not in the range 1-{0}. Using solution for Problem #{0}.".format(MAX_SOLVED))


# Function to validate input
def isint(value):
    try:
        if int(value) <= MAX_SOLVED:
            return True
        else:
            print_input_err()
            return False
    except:
        print_input_err()
        return False


# Run Problem<solution_num>.py
def run_solution(solution_num):
    exec("from scripts import Problem{0}".format(solution_num))
    print("Problem{0}.py:".format(solution_num))
    start = perf_counter()
    exec("Problem{0}.run()".format(solution_num))
    print("")
    print("Total running time for Problem{0}.py is {1} seconds".format(solution_num, perf_counter() - start))


def run_if_file_exists(problem_index):
    if os.path.isfile("scripts/Problem{0}.py".format(problem_index)):
        run_solution(problem_index)
    else:
        print("Problem{0}.py does not exist!".format(problem_index))

# If input is invalid, default to highest solved problem
input_value = input("Evaluate Project Euler Problem #")
if input_value == "all":
    print(BORDER)
    for i in range(1, MAX_SOLVED + 1):
        run_if_file_exists(i)
        print(BORDER)
    exit(0)
if not isint(input_value):
    input_value = DEFAULT

print(BORDER)
# Check if file exists
run_if_file_exists(input_value)
print(BORDER)
