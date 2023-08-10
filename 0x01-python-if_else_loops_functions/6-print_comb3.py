#!/usr/bin/python3
for tens in range(ord('0'), ord('9')):
    for units in range(ord('0') + 1, ord('9')):
        if tens != ord('8') or units != ord('9'):
            print("{:01}{:01}".format(chr(tens), chr(units)), end=", ")
        else:
            print("{:01}{:01}".format(chr(tens), chr(units)), end=" ")
