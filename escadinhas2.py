#!/usr/local/bin/python


def escadinha(base):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        base = 5
    else:
        base = int(sys.argv[1])
    print escadinha(base)
