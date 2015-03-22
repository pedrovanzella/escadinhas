#!/usr/local/bin/python

import sys


def incrementa(num, base):
    max = True
    for p in num:
        if p != base - 1:
            max = False
            break

    if max:
        num[0] = 1
        for i in range(1, len(num)):
            num[i] = 0
        num.append(0)
        return num

    if num[-1] < base - 1:
        num[-1] += 1
    else:
        num[-1] = 0
        for i in range(len(num) - 2, -1, -1):
            if num[i] < base - 1:
                num[i] += 1
                break
            else:
                num[i] = 0
    return num


def baseN_to_base_10(num, base):
    final = 0

    num.reverse()
    for idx, val in enumerate(num):
        final += val * pow(idx, base)

    return final


def unique(num):
    for idx, val in enumerate(num):
        for nidx, nval in enumerate(num):
            if val == nval:
                if idx == nidx:
                    continue
                # print "INVALIDO (unique) %s" % num
                return False
    return True


def valido(num, base):
    for idx, val in enumerate(num):
        if val >= base:
            # print "INVALIDO (base) %s" % num
            return False
        if abs(val - num[idx - 1]) > 2:
            # print "INVALIDO (modulus 2) %s" % num
            return False

        return unique(num)


def escadinha(base):
    count = 0
    num = [0]
    maxnum = []
    for i in range(0, base):
        maxnum.append(base - 1)

    while num != maxnum:
        num = incrementa(num, base)
        # print "TESTANDO %d", num
        if valido(num, base):
            count += 1
            # print "VALIDO %s" % num

    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
