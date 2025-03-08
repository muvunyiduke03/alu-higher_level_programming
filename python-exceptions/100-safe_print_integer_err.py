#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=__import__("sys").stderr)
        return False
