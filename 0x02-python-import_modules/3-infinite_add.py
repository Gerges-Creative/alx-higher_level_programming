#!/usr/bin/python3
import sys
argv = sys.argv
argvn = len(argv) - 1
if __name__ == "__main__":
    i, add = 1, 0
    while i <= argvn:
        argv_t = int(argv[i])
        add += argv_t
        i += 1
    print("{}".format(add))
