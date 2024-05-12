#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_return = [None] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_return[i] = True
        else:
            list_return[i] = False
    return list_return
