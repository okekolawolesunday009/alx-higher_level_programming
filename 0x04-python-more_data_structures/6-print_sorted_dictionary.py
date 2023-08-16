#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sort in sorted(a_dictionary):
        print("{}: {}".format(sort, a_dictionary[sort]))
