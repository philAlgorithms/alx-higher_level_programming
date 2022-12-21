#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, val):
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, val):
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = val


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, val):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            val (Node): The new Node to insert.
        """
        new = Node(val)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > val:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < val):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        vals = []
        tmp = self.__head
        while tmp is not None:
            vals.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(vals))
