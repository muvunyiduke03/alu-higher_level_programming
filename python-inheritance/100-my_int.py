#!/usr/bin/python3
"""
Module: 100-my_int
Defines a class MyInt that inherits from int and inverts the behavior
of == and != operators.
"""


class MyInt(int):
    """
    A rebel integer class that inverts the behavior of == and != operators.
    """

    def __eq__(self, value):
        """
        Overrides the equality operator (==).

        Args:
            other: The value to compare against.

        Returns:
            bool: The opposite of the standard equality comparison.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=).

        Args:
            other: The value to compare against.

        Returns:
            bool: The opposite of the standard inequality comparison.
        """
        return super().__eq__(other)
