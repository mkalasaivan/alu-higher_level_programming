#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in the file.

    Args:
        filename (str): The name of the file to be modified.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after each line containing the search_string.

    This function reads the contents of the file, modifies it as needed, and
    writes the changes back to the file. It does so by adding the new_string
    after every line containing the search_string.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)
    except FileNotFoundError:
        pass
