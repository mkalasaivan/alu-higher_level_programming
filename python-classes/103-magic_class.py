#!/usr/bin/python3
"""
This module defines the MagicClass, a representation of a circle
with methods to calculate its area and circumference.
"""

import math


class MagicClass:
    """
    A class that represents a circle, with functionality to calculate
    its area and circumference based on a given radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.

        Args:
            radius (int or float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not an int or float.
        """
        self.__radius = 0  # Initial default value for radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius  # Set the radius if valid

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle, calculated as π * radius^2.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle, calculated as 2 * π * radius.
        """
        return 2 * math.pi * self.__radius
