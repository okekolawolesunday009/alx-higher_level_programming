#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
string = "Last digit of"
if l > 5:
    print("{} {} is {} and is greater than 5".format(string, number, l))
elif l == 0:
    print("{} {} is {} and is 0".format(string, number, l))
else:
    print("{} {} is {:d} and is less than 6 and not 0".format(string, number, l))
