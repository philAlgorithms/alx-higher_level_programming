#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    result = 0
    for i in set(my_list):
        result += i
    return (result)
