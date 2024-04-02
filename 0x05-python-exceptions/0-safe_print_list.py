#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Arguments:
        my_list (list): The list to print elements from.
        x (integer) represents the number of elements to print

    Returns:
        the real number of elements printed
    """
    result = 0
    for index in range(length):
        try:
            print("{}".format(my_list[index]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return result
