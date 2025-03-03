#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

if argc == 0:
    print("Number of arguments: 0.")
elif argc == 1:
    print("Number of arguments: 1 argument:")
    print("1: {}".format(argv[0]))
else:
    print("Number of arguments: {} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))