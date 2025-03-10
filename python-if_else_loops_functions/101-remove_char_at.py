#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # Return the original string if n is out of bounds

    # Create a new string without the character at index n
    return string[:n] + string[n+1:]
