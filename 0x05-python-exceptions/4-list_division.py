#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the qisions.
    """
    ret_list = []
    for i in range(0, list_length):
        try:
            q = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            q = 0
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            ret_list.append(q)
    return (ret_list)
