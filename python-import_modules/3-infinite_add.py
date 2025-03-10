#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0

    # Iterate over the arguments starting from index 1
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert each argument to int and add it to total

    print(total)  # Print the final result
