#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse."""
    if isinstance(my_list, list):
        for index in range(-1, -1 * len(my_list) - 1, -1):
            print("{:d}".format(my_list[index]))
