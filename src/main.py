# Generic benchmarking code
# perf_counter() used for high precision
from time import perf_counter

# Constant Declarations
MAX_SOLVED = 5  # Max number of Euler problems solved
BORDER = "-----"  # Border string printed around execution output of Problem#.py
DEFAULT = str(MAX_SOLVED)  # Defaults to highest solved problem2


# Print error message for invalid inputs
def print_input_err():
    print("Please input an integer in the range 1-{0}".format(MAX_SOLVED))


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


input_value = DEFAULT

# Do-while emulation
while True:
    input_value = input("Evaluate Project Euler Problem #")
    if isint(input_value):
        break

# Imports
exec("from scripts import Problem{0}".format(input_value))

perf_counter()

print(BORDER)
exec("Problem{0}.run()".format(input_value))
print(BORDER)

print("Total running time for Problem{0}.py is {1} seconds".format(input_value, perf_counter()))
