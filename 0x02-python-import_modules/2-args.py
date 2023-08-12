#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    argument = sys.argv

    if length == 1:
        str = "argument"
        print("{} {}.".format(length - 1, str))
    elif length > 1:
        str = "argument"
        print("{} {}.".format(length, str))
    elif length > 1:
        str = "arguments"
        print("{} {} : \n".format(length, str))

    for z in range(1, length):
        if z <= 1:
            print("oops")
        print(sys.argv[z])
        print(z)
