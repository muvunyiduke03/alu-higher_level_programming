#!/usr/bin/python3
def fake_add(a,b):
    """Function that returns the result of substracting b from a."""
    return a - b
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    real_add_result = add(a, b)
    fake_add_result = fake_add(a, b)

    print("{} + {} = {}\nFake add: {} - {}".format(a, b, real_add_result, a, b, fake_add_result))