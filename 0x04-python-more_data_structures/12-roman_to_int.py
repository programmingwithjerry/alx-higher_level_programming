#!/usr/bin/python3
def to_subtract(list_num):
    sub_from = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub_from += n

    return (max_list - sub_from)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_numerals.keys())

    num = 0
    last_roman = 0
    list_num = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if roman_numerals.get(char) <= last_roman:
                    num += to_subtract(list_num)
                    list_num = [roman_numerals.get(char)]
                else:
                    list_num.append(roman_numerals.get(char))

                last_roman = roman_numerals.get(char)

    num += to_subtract(list_num)

    return (num)
