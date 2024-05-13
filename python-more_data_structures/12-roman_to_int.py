#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    for i in roman_string:
        if i not in roman:
            return 0
    return_num = roman[roman_string[-1]]
    for i in range(len(roman_string) - 2, -1, -1):
        if roman[roman_string[i]] >= roman[roman_string[i + 1]]:
            return_num += roman[roman_string[i]]
        else:
            return_num -= roman[roman_string[i]]
    return return_num
