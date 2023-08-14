#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def calc():
    num_args = len(sys.argv) - 1

    if num_args != 4:
        print("Usage: {} <num1> <operator> <num2>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    c = int(sys.argv[3])

    if operator == '+':
        result = add(a, c)
    elif operator == '-':
        result = sub(a, c)
    elif operator == '*':
        result = mul(a, c)
    elif operator == '/':
        if c == 0:
            print("Error: Division by zero.")
            sys.exit(1)
        result = div(a, c)
    else:
        print("Error: Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, c, result))


if __name__ == "__main__":
    calc()
