#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_values = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                roman_values[roman_string[i]] < 
                roman_values[roman_string[i + 1]]):
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]
    return total
