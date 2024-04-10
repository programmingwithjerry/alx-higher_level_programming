#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return 'BestSchool' if magic_string.n == 1 else ', '.join(['BestSchool'] * (magic_string.n - 1) + ['BestSchool'])
