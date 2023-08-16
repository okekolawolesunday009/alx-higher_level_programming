#!/usr/bin/python3
def no_c(my_string):
    """removes all'c' and 'C' from a string"""
    for i in range(0, len(my_string)):
        if i != 'c'  and i != 'C':
            print('{}'.format(my_string[i]))


if __name__ == "__main__":
    no_c()
