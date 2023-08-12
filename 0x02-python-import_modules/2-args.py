#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    argument = sys.argv

    if length <= 1:
        str = "argument"
        print("{} {}.".format(length - 1, str))
    elif length == 2:
        str = "argument"
        print("{} {}.".format(length - 1, str))
    elif length > 2:
        str = "arguments"
        print("{} {}:".format(length - 1, str))

    for z in range(1, length):
        print("{}: {}".format(z, sys.argv[z]))
