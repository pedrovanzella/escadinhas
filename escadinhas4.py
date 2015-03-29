#!/usr/local/bin/python
import sys


def esc(base, num, d, usad):
    count = 0
    if num == [0] or len(num) > base:
        return 0
    if num == [] or abs(num[-1] - d) <= 2 and not usad[d]:
        num.append(d)
        usad[d] = True
        for i in range(0, base - 1):
            count += 1 + esc(base, num, i, usad)
    return count


def escadinha(base):
    count = 0
    for i in range(1, base - 1):
        count += esc(base, [], i, [False for x in range(0, base)])

    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
