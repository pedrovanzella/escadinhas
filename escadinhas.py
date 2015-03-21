#!/usr/local/bin/python

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

#def escadinha(base):
    #count = 0
    #num = []
    #for i in range(1, )


if __name__ == "__main__":
    num = [4, 5, 5]
    print incrementa(num, 6)
