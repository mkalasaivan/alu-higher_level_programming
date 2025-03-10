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


# Example usage and tests
if __name__ == "__main__":
    # Correct output - case: my_square = Square(3, (1, 1))
    my_square = Square(3, (1, 1))
    my_square.my_print()

    # Correct output - case: mysquare = Square(3, (1, 1))
    mysquare = Square(3, (1, 1))
    print("Size:", mysquare.size)          # Output: Size: 3
    print("Area:", mysquare.area())        # Output: Area: 9
    print("Position:", mysquare.position)   # Output: Position: (1, 1)

    # Correct output - case: my_square = Square(3, "Position")
    try:
        my_square = Square(3, "Position")  # Should raise TypeError
    except Exception as e:
        print(e)

    # Correct output - case: my_square = Square(3, (1,))
    try:
        my_square = Square(3, (1, ))  # Should raise TypeError
    except Exception as e:
        print(e)

    # Correct output - case: my_square = Square(3, (1, -3))
    try:
        my_square = Square(3, (1, -3))  # Should raise TypeError
    except Exception as e:
        print(e)

    # Correct output - case: my_square = Square(3, (1, "3"))
    try:
        my_square = Square(3, (1, "3"))  # Should raise TypeError
    except Exception as e:
        print(e)

    # Correct output - case: mysquare = Square(3)
    mysquare = Square(3)
    mysquare.my_print()  # Should print a 3x3 square

    # Correct output - case: mysquare = Square(3, (0, 0))
    mysquare = Square(3, (0, 0))
    mysquare.my_print()  # Should print a 3x3 square aligned to the left

    # Correct output - case: mysquare = Square(3, (1, 0))
    mysquare = Square(3, (1, 0))
    mysquare.my_print()  # Should print a 3x3 square with 1 space offset

    # Correct output - case: mysquare = Square(3, (0, 1))
    mysquare = Square(3, (0, 1))
    mysquare.my_print()  # Should print a 3x3 square with 1 empty line before

    # Correct output - case: mysquare = Square(3, (1, 1))
    mysquare = Square(3, (1, 1))
    mysquare.my_print()  # Should print a 3x3 square with offset

    # Correct output - case: mysquare = Square(5, (3, 2))
    mysquare = Square(5, (3, 2))
    mysquare.my_print()  # Should print a 5x5 square with offset

    # Correct output - case: mysquare = Square(0, (10, 3))
    mysquare = Square(0, (10, 3))
    mysquare.my_print()  # Should print an empty line
