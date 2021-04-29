#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv) - 1
    if argv == 0:
        print("0 arguments.")
    elif argv == 1:
        print("{} argument:".format(argv))
        print("{}: {}".format(argv, sys.argv[1]))
    else:
        print("{} arguments:".format(argv))
        for i in range(0, argv):
            i = i + 1
            print("{}: {}".format(i, sys.argv[i]))
