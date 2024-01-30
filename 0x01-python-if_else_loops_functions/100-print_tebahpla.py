#!/usr/bin/python3
n = 122
for i in range(27):
    if n % 2 == 0:
        c = chr(n)
    else:
        j = n
        j = j - 32
        c = chr(j)

    print('{0}'.format(c), end='')
    n -= 1
