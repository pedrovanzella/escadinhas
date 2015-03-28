#!/usr/local/bin/python
import sys


def maxnum(base):
    return [base - i - 1 for i in range(0, base)]


def maiorDisponivel(disponiveis):
    for i in range(len(disponiveis) - 2, -1, -1):
        if disponiveis[i]:
            return i


def zeros(base):
    return [0 for x in range(0, base-1)]


def escadinha(base):
    i = base - 1
    count = 1
    disponiveis = [False for x in range(0, base)]
    num = maxnum(base)

    print num
    disponiveis[num[i]] = True

    while num[i] == 0:
        i -= 1
        disponiveis[num[i]] = True
    num[i] -= 1

    while num != zeros(base):
        print num
        while not disponiveis[num[i]]:
            print "While 1"
            while num[i] == 0:
                print "While 2"
                i -= 1
                disponiveis[num[i]] = True
            num[i] -= 1
        while abs(num[i] - num[i-1]) <= 2:
            print "While 3"
            disponiveis[num[i]] = False
            if i == base - 1:
                count += 1
                disponiveis[num[i]] = True
                while num[i] == 0:
                    print "While 4"
                    print "i = %d" % i
                    print "num[%r] = %r" % (i, num[i])
                    print "disp[%r] = %r" % (num[i], disponiveis[num[i]])
                    x = raw_input()
                    i -= 1
                    disponiveis[num[i]] = True
                num[i] -= 1
                break
            else:
                print "Incrementando i"
                i += 1
                print "i = %d" % i
                num[i] = maiorDisponivel(disponiveis)
                print "disponiveis = %r" % disponiveis
                print "Maior Disponivel = %d" % num[i]

    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
