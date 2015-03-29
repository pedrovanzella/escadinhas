#!/usr/local/bin/python
import sys


def esc(base, num, d, usad):
    count = 0
    if len(num) > base:
        return 1
    if num == [] or (abs(num[-1] - d) <= 2 and not usad[d]):
        num.append(d)
        print num
        usad[d] = True
        for i in range(0, base):
            count += 1 + esc(base, num, i, usad)
    return count


def escadinha(base):
    count = 0
    for i in range(1, base):
        count += esc(base, [], i, [False for x in range(0, base)])

    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
