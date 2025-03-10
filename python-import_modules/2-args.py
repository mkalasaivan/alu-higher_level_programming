#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Exclude the script name itself

    if num_args == 0:
        print("0 arguments.")  # Updated this line
    else:
        arg_word = "argument" if num_args == 1 else "arguments"
        print(f"{num_args} {arg_word}:")

        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
