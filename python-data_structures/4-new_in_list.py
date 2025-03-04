#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Returns a new list with an element replaced at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list

    new_list = my_list[:]  # Create a copy of the original list
    new_list[idx] = element  # Modify the copy
    return new_list
