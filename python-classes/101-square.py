#!/usr/bin/python3
"""
Module to define a Square class that represents a square with a given size
and position.
"""


class Square:
    """Class to define a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.size ** 2

    def my_print(self):
        """Print the square with the character # at the specified position."""
        if self.size == 0:
            print("")
            return

        # Print new lines for the vertical position
        for _ in range(self.position[1]):
            print("")

        # Print the square with the specified position
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Return the string representation of the square for print."""
        square_string = ""
        if self.size == 0:
            return square_string

        for _ in range(self.position[1]):
            square_string += "\n"
        for _ in range(self.size):
            square_string += " " * self.position[0] + "#" * self.size + "\n"

        return square_string.rstrip()  # Remove the trailing newline


# Example usage and tests
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
