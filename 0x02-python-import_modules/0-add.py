#!/usr/bin/python3

# Importing the add function from the add_0 module
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    # Printing the result of the addition
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
