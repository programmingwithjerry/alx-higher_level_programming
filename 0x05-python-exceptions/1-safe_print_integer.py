#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        True if value has been correctly printed (it means the value is an integer)
        Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return True
    except BaseException:
        return False
