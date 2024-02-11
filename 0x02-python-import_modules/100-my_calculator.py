#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
argv = sys.argv
args = len(argv)
if __name__ == "__main__":
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

    if argv[2] == '+':
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
