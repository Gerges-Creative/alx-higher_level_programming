#!/usr/bin/python3
import hidden_4
hidden = dir(hidden_4)
if __name__ == "__main__":
    for i in hidden:
        if i[0] != '_':
            print("{0}".format(i))
