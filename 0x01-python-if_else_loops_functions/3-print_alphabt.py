#!/usr/bin/python3
for char in range(ord('a'), ord('{')):
    if char != 113 and char != 101:
        print("{}".format(chr(char)), end="")
