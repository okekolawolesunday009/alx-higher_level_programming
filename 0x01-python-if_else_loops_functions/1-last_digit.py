#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last = abs(num) % 10
strn = "Last digit of"
if num < 0:
    last *= -1
if last > 5:
    print("{} {} is {} and is greater than 5".format(strn, num, last))
elif last == 0:
    print("{} {} is {} and is 0".format(strn, num, last))
else:
    print("{} {} is {} and is less than 6 and not 0".format(strn, num, last))
