#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """retrieves an element from a list like in C without modifying the original list"""
    copy_list = my_list[:]

    if idx < 0:
        return copy_list
    elif idx > len(copy_list) - 1:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
