#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigit = number % 10
string = "Last digit of"
if lastDigit > 5:
    print(f"{string} {number} is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"{string} {number} is {lastDigit} and is 0")
else:
    print(f"{string} {number} is {lastDigit} and is less than 6 and not 0")
