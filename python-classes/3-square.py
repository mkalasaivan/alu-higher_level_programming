#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute

    def area(self):
        """Return the current square area."""
        return self.__size ** 2  # Area calculation
