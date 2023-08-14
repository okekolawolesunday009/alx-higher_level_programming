#!/usr/bin/python3

import sys


def argv_args():
    num_args = (len(sys.argv) - 1)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    if num_args > 0:
        i = 1
        for args in sys.argv[1:]:
            print("{}: {}".format(i, args))
            i += 1


if __name__ == "__main__":
    argv_args()
