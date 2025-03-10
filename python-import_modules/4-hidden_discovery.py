#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the hidden_4 module
    names = dir(hidden_4)

    # Filter names to exclude those starting with '__' and sort them
    filtered_names = sorted(
            name for name in names if not name.startswith('__')
            )

    # Print each name on a new line
    for name in filtered_names:
        print(name)
