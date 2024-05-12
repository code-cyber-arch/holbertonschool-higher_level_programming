#!/usr/bin/ptyhon3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary.keys())}
    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
