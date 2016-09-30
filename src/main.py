# Generic benchmarking code
# perf_counter() used for high precision
from time import perf_counter

# Constant Declarations
MAX_SOLVED = 11  # Max number of Euler problems solved
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


# If input is invalid, default to highest solved problem
input_value = input("Evaluate Project Euler Problem #")
if input_value == "all":
    print(BORDER)
    for i in range(1, MAX_SOLVED + 1):
        exec("from scripts import Problem{0}".format(i))

        perf_counter()

        print("Problem{0}.py:".format(i))
        exec("Problem{0}.run()".format(i))
        print("")
        print("Total running time for Problem{0}.py is {1} seconds".format(i, perf_counter()))
        print(BORDER)
    exit(0)
if not isint(input_value):
    input_value = DEFAULT

# Imports
exec("from scripts import Problem{0}".format(input_value))

perf_counter()

print(BORDER)
exec("Problem{0}.run()".format(input_value))
print("")
print("Total running time for Problem{0}.py is {1} seconds".format(input_value, perf_counter()))
print(BORDER)
