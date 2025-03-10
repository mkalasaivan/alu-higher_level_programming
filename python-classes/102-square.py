#!/usr/bin/python3
"""
This module defines a Square class with a size property,
an area method, and comparison operators based on square area.
"""

class Square:
    """
    Class Square that defines a square by:
    - private instance attribute size with property getter and setter
    - area method to calculate square area
    - comparison operators based on square area
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int or float): The size of a square's side.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        
        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The size of the square.
        
        Raises:
            TypeError: If the size is not an integer or float.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of self is less than the area of other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of self is less than or equal to the area of other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of self is greater than the area of other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of self is greater than or equal to the area of other."""
        return self.area() >= other.area()
 
