#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 'a' <= i <= 'z':
            charUpper = chr(ord(i) - ord('a') + ord('A'))
            res += "{}".format(charUpper)
        else:
            res += "{}".format(i)
    return res
