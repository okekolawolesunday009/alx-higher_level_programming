#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
string = "Last digit of"
if lastDigit > 5:
    print("{} {} is {} and is greater than 5".format(string, number, lastDigit))
elif lastDigit == 0:
    print("{} {} is {} and is 0".format(string, number, lastDigit))
else:
    print("{} {} is {} and is less than 6 and not 0".format(string, number, lastDigit))
