#!/usr/bin/python3


def divisible_by_2(my_list):
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_3(my_list)

    i = 0
    while i < len(list_result):
        is_divisible = "is" if list_result[i] else "is not"
        print("{:d} {:s} divisible by 2".format(my_list[i], is_divisible))
        i += 1