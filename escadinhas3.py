#!/usr/local/bin/python
import sys


def maxnum(base):
    maxnum = []
    for i in range(0, base):
        maxnum.append(base - i - 1)

    return maxnum


def escadinha(base):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
