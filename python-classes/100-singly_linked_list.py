#!/usr/bin/python3
"""
Module to define a Node class for a singly linked list
and a SinglyLinkedList class to manage the list.
"""


class Node:
    """Class to define a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node or None): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node of the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the linked list.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class to define a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        current = self.__head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


# Example usage and tests
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
