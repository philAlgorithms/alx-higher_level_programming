#!/usr/bin/python3

def magic_calculation(a, b):
    """does exactly the same as the following Python bytecode:"""
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                res += a ** b / i
        except:
            res = b + a
            break
    return (res)
