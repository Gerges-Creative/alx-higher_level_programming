#!/usr/bin/python3
import sys
args = sys.argv
args_n = len(args) - 1
if __name__ == "__main__":
    if args_n == 0:
        print("0 arguments.")
    elif args_n == 1:
        print("1 argument:\n1: {0}".format(args[1]))
    elif args_n > 1:
        print("{0} arguments:".format(args_n))
        for i in range(1, args_n + 1):
            print("{0}: {1}".format(i, args[i]))
