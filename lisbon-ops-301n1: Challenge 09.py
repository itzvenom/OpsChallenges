#!/bin/python


#Script         Ops Challenge: Class 09 - Python Conditional Statements
#Purpose        Create a Python script that uses    conditional statements and logical conditionals.
#Why            Learn how to make use conditional statements and logical conditionals.

import random

# Function for new numbers
def newnumbers():
    global a
    global b
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"\nRandom numbers are: {a} and {b}\n")

# Assign random values to a and b
newnumbers()
# Check if a is greater than b
if a > b:
    print(f"{a} is greater than {b}")
# Check if a is less than or equal to b
elif a < b:
    print(f"{a} is less than {b}")
# If neither condition is met
else:
    print(f"{a} and {b} are the same number")

######################################################################

# Assign fresh random values to a and b
newnumbers()
# Check if a is equal to b
if a == b:
    print(f"{a} is equal to {b}")
# Check if a not equal to b
elif a != b:
    print(f"{a} is not equal to {b}")

######################################################################

# Assign fresh random values to a and b
newnumbers()
# Check if a greater or equal to b
if a >= b:
    print(f"{a} is greater or equal to {b}")
# Check if less than or equal to b
elif a <= b:
    print(f"{a} is less than or equal to {b}")

######################################################################

# Assign fresh random values to a and b
newnumbers()
# Check if a is greater than b and a is even
if a > b and a % 2 == 0:
    print(f"{a} is greater than {b} and even")
# Check if a is less than or equal to b or b is odd
elif a <= b or b % 2 != 0:
    print(f"{a} is less than or equal to {b} or {b} is odd")
# If neither condition is met
else:
    print("Neither condition is met")

######################################################################

# Assign fresh random values to a and b
newnumbers()
# Nested if statement
if a > b:
    print(f"{a} is greater than {b}")
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
else:
    print(f"{a} is not greater than {b}")

########################################################################

# If statement with pass to avoid errors
# Assign fresh random values to a and b
newnumbers()
if a == b:
    pass
else:
    print(f"{a} is not equal to {b}")