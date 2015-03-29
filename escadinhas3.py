#!/usr/local/bin/python
import sys


def maxnum(base):
    return [base - i - 1 for i in range(0, base)]


def maiorDisponivel(disponiveis):
    for i in range(len(disponiveis) - 1, -1, -1):
        if disponiveis[i]:
            return i


def zeros(base):
    return [0 for x in range(0, base-1)]


def escadinha(base):
    i = base - 1
    b = 0
    count = 1
    disponiveis = [False for x in range(0, base)]
    num = maxnum(base)

    disponiveis[num[i]] = True

    while num[i] == 0:
        i -= 1
        disponiveis[num[i]] = True
    num[i] -= 1

    while num != zeros(base):
        print num
        while not disponiveis[num[i]]:
            while num[i] == 0:
                i -= 1
                disponiveis[num[i]] = True
            num[i] -= 1
            if i == b and num[i] == 0:
                b += 1
                disponiveis[num[i]] = True
                i += 1
                num[i] = maiorDisponivel(disponiveis)
        while i == b or abs(num[i] - num[i-1]) <= 2:
            disponiveis[num[i]] = False
            if i == base - 1:
                count += 1
                disponiveis[num[i]] = True
                while num[i] == 0:
                    i -= 1
                    disponiveis[num[i]] = True
                num[i] -= 1
                if i == b and num[i] == 0:
                    b += 1
                    disponiveis[num[i]] = True
                    i += 1
                    num[i] = maiorDisponivel(disponiveis)
                break
            else:
                i += 1
                num[i] = maiorDisponivel(disponiveis)
        while num[i] == 0:
            i -= 1
            disponiveis[num[i]] = True
        num[i] -= 1
        if i == b and num[i] == 0:
            b += 1
            disponiveis[num[i]] = True
            i += 1
            num[i] = maiorDisponivel(disponiveis)
    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
