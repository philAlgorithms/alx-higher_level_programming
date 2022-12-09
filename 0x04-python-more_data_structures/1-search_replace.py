#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    n_list = my_list[:]
    for i in range(len(n_list)):
        if n_list[i] == search:
            n_list[i] = replace
    return (n_list)
