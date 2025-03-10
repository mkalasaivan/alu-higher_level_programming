#!/usr/bin/python3
"""
This module defines a LockedClass with restricted attribute setting.
"""


class LockedClass:
    """
    A class that only allows the 'first_name' attribute to be set dynamically.
    Attempting to set any other attribute raises an AttributeError.
    """
    __slots__ = ['first_name']
