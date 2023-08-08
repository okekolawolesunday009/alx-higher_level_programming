#!/usr/bin/python3
for number in range(100):
    tens = number // 10
    units = number % 10
    if tens != 8 and units != 9:
        print("{:01}{:01}".format(tens, units), end=", ")
    else:
        print("{:01}{:01}".format(tens, units), end="") 
