#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return_num = 0
    for i in roman_string:
        if i in roman.keys():
            if return_num > roman[i]:
                return_num += roman[i]
            else:
                return_num -= roman[i]
                return_num = abs(return_num)
        else:
            break
    return return_num
