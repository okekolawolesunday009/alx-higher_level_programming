#!/usr/bin/python3
"""program that prints aphabet escept q and e
"""
for i in range(97, 123):
    if i != 113 and i != 101:
        print("{}".format(chr(i)), end="")
