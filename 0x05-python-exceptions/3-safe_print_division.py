#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result."""
    try:
        answer = a / b
    except (TypeError, ZeroDivisionError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return (answer)
