#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    output = []
    for i in range(x):
        try:
            output.append(str(my_list[i]))
            count += 1
        except IndexError:
            break
    print("{}".format("".join(output)))
    return count
