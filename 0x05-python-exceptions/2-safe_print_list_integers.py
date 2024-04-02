#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            result = result + 1
        except (TypeError, ValueError):
            pass
    print("")
    return result
