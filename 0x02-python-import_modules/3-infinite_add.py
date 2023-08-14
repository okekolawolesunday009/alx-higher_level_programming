#!/usr/bin/python3

import sys

def argv_add():
    num_args = (len(sys.argv) - 1)
    add = 0

    if num_args == 0:
        print("{}".format(add))
    elif num_args == 1:
        print("{}".format(sys.argv[1]))
    else:
        if num_args > 0:
            for arg in sys.argv[1:]:
                add += int(arg)
        print("{}".format(add))

if __name__ == "__main__":
    argv_add()