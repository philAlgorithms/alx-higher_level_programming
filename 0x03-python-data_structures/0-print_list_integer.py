#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for index in range(list(my_list)):
        print("{:d}".format(my_list[index]))
