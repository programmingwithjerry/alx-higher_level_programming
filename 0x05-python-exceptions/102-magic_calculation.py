#!/usr/bin/python3
def magic_calculation(a, b):
    final_result = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception("Too far")
            final_result += (a ** b) / index
        except Exception:
            final_result = b + a
            break
    return final_result
