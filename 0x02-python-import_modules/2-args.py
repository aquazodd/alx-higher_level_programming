#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    argument = sys.argv

    if length <= 1:
        str = "argument"
        print("{} {}.".format(length - 1, str))
    elif length == 1:
        str = "argument"
        print("{} {}.".format(length - 1, str))
    elif length > 1:
        str = "arguments"
        print("{} {} : \n".format(length - 1, str))

    for z in range(1, length):
        print(sys.argv[z])
        print(z)
