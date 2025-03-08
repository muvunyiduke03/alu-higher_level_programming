#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=__import__('sys').stderr)
        return None
