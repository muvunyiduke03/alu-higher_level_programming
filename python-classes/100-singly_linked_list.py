#!/usr/bin/python3
"""
This module defines classes for a singly linked list.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """Initializes a new singly linked list."""
        self.__head = None

    def __str__(self):
        """Printable representation of the linked list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The data to be inserted into the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
