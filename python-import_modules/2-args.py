#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("Number of arguments: 0")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))