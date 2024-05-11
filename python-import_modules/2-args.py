#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg))

    for i in range(arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
