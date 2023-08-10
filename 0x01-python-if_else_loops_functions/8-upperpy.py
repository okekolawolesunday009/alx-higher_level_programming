#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            print(chr((ord(i) - ord('a') + ord('A'))), end="")
        else:
            print(i, end="")